"""Contrato de integração e conteúdo público da secção de ocasiões."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys
import hashlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.catalogo import ARTIGOS, SECCOES
from conteudos.ocasioes import OCASIOES, FONTES_OCASIOES
from scripts.render_ocasioes import dados

class Pagina(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a': self.links.append(a.get('href', ''))
        if tag == 'img': self.images.append(a)

assert [a['id'] for a in OCASIOES] == ['natal','inverno','carnaval','verao']
assert len([s for s in SECCOES if s['id']=='ocasioes']) == 1
assert {a['id'] for a in ARTIGOS if a['sec']=='ocasioes'} == {a['id'] for a in OCASIOES}
index = (ROOT/'ocasioes/index.html').read_text(encoding='utf-8')
cards = re.findall(r'<article\b[^>]*class="idea-card occasion-card"[^>]*>(.*?)</article>', index, re.S)
assert len(cards)==4
for a, bloco in zip(OCASIOES,cards):
    p = Pagina(bloco)
    assert len(p.images)==1 and a['id']+'.html' in p.links
    assert '<h2>'+a['titulo']+'</h2>' in bloco and '<p>' in bloco
    assert a.get('imagem_cartao', a['imagem'])['alt'] == p.images[0]['alt']
    assert (ROOT/'ocasioes'/p.images[0]['src']).is_file()

proibido = re.compile(r'nobrinde|catálogo|catalogue|\bSKU\b|\bnb\d{3,}\b|€|quantidades mínimas',re.I)
all_ids = {a['id'] for a in ARTIGOS}
for a in OCASIOES:
    html = (ROOT/'ocasioes'/(a['id']+'.html')).read_text(encoding='utf-8')
    p = Pagina(html)
    assert not proibido.search(html)
    assert len(p.ids)==len(set(p.ids))
    assert all(s['id'] in p.ids for s in a['conteudo'])
    assert {'faq','relacionados','exemplos'} <= set(p.ids)
    assert 'fontes' not in p.ids and 'Fontes e âmbito' not in html
    assert '<figcaption' not in html
    assert not any(href.startswith('#fonte-') for href in p.links)
    assert len(p.images)==1+len(a['exemplos'])
    for e in a['exemplos']:
        assert e['id'] in p.ids and e['relacionado'] in all_ids
        assert e['imagem']['alt'] in html
        assert {'contexto','motivo','confirmar'} <= e.keys()
        assert e['imagem']['url'] in html
    assert 'index.html' in p.links
    nav = re.search(r'<nav\s+id="nav".*?</nav>',html,re.S)
    assert nav and re.search(r'href="../ocasioes/index.html"\s+aria-current="page"',nav[0])
    assert a['relacionados'] and set(a['relacionados']) <= all_ids
    citacoes = set(re.findall(r'\[([a-z]+)\]',json.dumps(a,ensure_ascii=False)))
    assert citacoes <= set(a['fontes']) <= FONTES_OCASIOES.keys()
    for chave in a['fontes']:
        assert FONTES_OCASIOES[chave]['url'] in p.links
    for outro in OCASIOES:
        if outro != a: assert outro['id']+'.html' in p.links

for path in [ROOT/'index.html']+[ROOT/a['sec']/(a['id']+'.html') for a in ARTIGOS]+[ROOT/s['id']/'index.html' for s in SECCOES]:
    html = path.read_text(encoding='utf-8')
    nav = re.search(r'<nav\s+id="nav".*?</nav>',html,re.S)
    assert nav and nav[0].count('ocasioes/index.html')==1, path
assert 'ocasioes/index.html' in (ROOT/'modelos/inicio.html').read_text(encoding='utf-8')
assert (ROOT/'assets/ocasioes-conteudos.json').read_text(encoding='utf-8')==dados()
registos = json.loads((ROOT/'editorial/ocasioes-exemplos-imagens.json').read_text(encoding='utf-8'))
assert len(registos)==12
for r in registos:
    original, copia = ROOT/r['original'], ROOT/r['publico']
    assert hashlib.sha256(original.read_bytes()).hexdigest()==r['sha256']
    assert original.read_bytes()==copia.read_bytes()
entries = json.loads((ROOT/'assets/pesquisa-dados.js').read_text(encoding='utf-8').split('=',1)[1].strip().removesuffix(';'))
assert {'ocasioes/index.html'} | {'ocasioes/'+a['id']+'.html' for a in OCASIOES} <= {e['url'] for e in entries}
print('OK: quatro ocasiões, cartões completos, navegação global, imagens, fontes, relações, pesquisa e JSON.')
