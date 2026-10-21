"""Contrato público de Produtos: fonte única, rotas, citações e exportação."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.produtos import PRODUTOS, FONTES_PRODUTOS, textos_publicos
from conteudos.produtos_imagens import fotos_publicas, IMAGENS
from render_produtos import dados_publicos
from conteudos.produtos_areas import AREAS
from conteudos.catalogo import ARTIGOS


class Pagina(HTMLParser):
    def __init__(self, texto):
        super().__init__()
        self.cards = []
        self.ids = []
        self.links = []
        self.images = []
        self.visivel = []
        self.feed(texto)

    def handle_starttag(self, tag, atributos):
        a = dict(atributos)
        if 'id' in a: self.ids.append(a['id'])
        if 'href' in a: self.links.append(a['href'])
        if 'product-family-card' in a.get('class', '').split(): self.cards.append(a)
        if tag == 'img': self.images.append(a)

    def handle_data(self, data):
        self.visivel.append(data)


index = Pagina((ROOT/'produtos/index.html').read_text(encoding='utf-8'))
familias = [g for g in PRODUTOS if g['categoria'] == 'familia']
assert len(familias) == 11 and len(index.cards) == 10
assert len(AREAS) == 10
assert [c['id'] for c in index.cards] == [a['id'] for a in AREAS]
assert all(a['id'] in index.ids for a in AREAS)
assert {g['slug'] + '.html' for g in familias} <= set(index.links)
assert len(index.images) == 10
html_index = (ROOT/'produtos/index.html').read_text(encoding='utf-8')
blocos = re.findall(r'<article\b[^>]*class="idea-card product-family-card"[^>]*>(.*?)</article>', html_index, re.S)
assert len(blocos) == 10
for area, bloco in zip(AREAS, blocos):
    cartao = Pagina(bloco)
    assert len(cartao.images) == 1 and cartao.links
    assert re.search(r'<h2>\s*' + re.escape(area['titulo']) + r'\s*</h2>', bloco)
    assert '<p>' in bloco and 'idea-read-more' in bloco
    assert area['guias'] and all(id in {g['id'] for g in PRODUTOS} for id in area['guias'])
    assert area['guias'][0] + '.html' in cartao.links
    for img in cartao.images:
        assert img['alt'] and (ROOT/'produtos'/img['src']).is_file()
assert not re.search(r'<nav\b[^>]*aria-label="[Áá]reas de produtos"', html_index)
assert {'canetas', 'escritorio'} <= set(index.ids)
assert len(index.ids) == len(set(index.ids))
assert 'premium' in index.ids and 'brindes-premium.html' in index.links
entries = json.loads((ROOT/'assets/pesquisa-dados.js').read_text(encoding='utf-8').split('=', 1)[1].strip().removesuffix(';'))
by_url = {e['url']: e for e in entries}
by_id = {a['id']: a for a in ARTIGOS}
exportado = (ROOT/'assets/produtos-conteudos.json').read_text(encoding='utf-8')
assert exportado == dados_publicos(by_id), 'Exportação divergiu da fonte'
dados = json.loads(exportado)
novos = {'casa-decoracao-e-cuidados-pessoais', 'desporto-lazer-e-exterior',
         'eventos-identificacao-e-premios', 'mobilidade-ferramentas-e-seguranca',
         'embalagem-e-apresentacao'}
assert novos <= {id for g in PRODUTOS for id in g['relacionados']}
assert 'brindes-premium' not in {id for a in AREAS for id in a['guias']}
fotografias = fotos_publicas()
originais = [f['original'] for s in IMAGENS.values() for f in [s['cartao'], *s['artigo']]]
assert all(original not in exportado for original in originais)
assert len(dados['conteudos']) == 12 and dados['schema_version'] == '1.0'
proibidos = re.compile(r'nobrinde|catalogue|catálogo|\bSKU\b|PDF\s+p\.|disponível na nossa|revisão editorial|aprovação interna', re.I)
assert not proibidos.search(exportado)
assert not re.search(r'\[[a-z]+\]', exportado), 'Citações devem estar em campos estruturados'
def validar_citacoes(node, fontes):
    if isinstance(node, dict):
        for c in node.get('citacoes', []):
            assert c['campo'] in node and set(c['fontes']) <= fontes
            if 'indice' in c: assert 0 <= c['indice'] < len(node[c['campo']])
        for campo, value in node.items():
            if campo != 'citacoes': validar_citacoes(value, fontes)
    elif isinstance(node, list):
        for item in node: validar_citacoes(item, fontes)
for g in dados['conteudos']:
    validar_citacoes(g, {f['id'] for f in g['fontes']})
for g in PRODUTOS:
    path = ROOT/'produtos'/f'{g["id"]}.html'
    html = path.read_text(encoding='utf-8')
    page = Pagina(html)
    assert not proibidos.search(html), g['id']
    expected = fotografias.get(g['id'], {}).get('artigo', [])
    assert len(page.images) == len(expected)
    assert {i['src'] for i in page.images} == {'../' + f['url'] for f in expected}
    for img in page.images:
        assert img['alt'] and img['src'].startswith('../assets/produtos/visuais/')
    if expected: assert '../creditos-imagens.html#produtos-ilustrativos' in page.links
    assert all(k in page.ids for k in ['tipos', 'usos', 'criterios', 'materiais', 'zonas', 'tecnicas', 'limites', 'perguntas', 'faq', 'fontes'])
    assert g['data_revisao'] in html and 'Revisão documental' in html
    for texto in textos_publicos(g):
        for k in re.findall(r'\[([a-z]+)\]', texto):
            assert k in g['fontes'] and k in FONTES_PRODUTOS, (g['id'], k)
    for k in g['fontes']:
        assert 'fonte-' + k in page.ids
        assert FONTES_PRODUTOS[k]['url'] in page.links
    for componente in g['materiais_componentes']:
        assert componente['guia_id'] in by_id
    for t in g['tecnicas_relacionadas']:
        assert t['id'] in by_id and by_id[t['id']]['sec'] == 'tecnicas'
        assert t['estatuto'] == 'possibilidade_geral' and t['compatibilidade_confirmada'] is False
    assert all(id in by_id for id in g['relacionados'])
    entry = by_url['produtos/' + g['id'] + '.html']
    assert entry['summary'] == g['resumo']
    assert all(s in entry['text'] for s in g['sinonimos']), g['id']
    assert entry['text'] == ' '.join(textos_publicos(g)), 'Pesquisa divergiu da fonte semântica'
assert not Pagina((ROOT/'produtos/brindes-premium.html').read_text(encoding='utf-8')).images
assert dados['areas'] == json.loads(json.dumps(AREAS))
for area in AREAS:
    for destino, _ in area.get('links', []):
        assert (ROOT/destino).is_file(), destino
assert all(a['titulo'] in by_url['produtos/index.html']['text'] for a in AREAS)
print('OK: dez cartões completos e ordenados com imagem, título, descrição e destino; rotas, pesquisa e JSON consistentes.')
