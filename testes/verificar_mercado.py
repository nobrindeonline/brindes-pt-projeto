"""Valida a navegação em três níveis, perfis canónicos e recursos de Mercado."""
import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.mercado import AREAS, PERFIS, MERCADO
from conteudos.mercado_areas import ASSOCIACOES
from conteudos.mercado_empresas import LOGOS
from conteudos.mercado import FONTES_MERCADO
from conteudos.mercado_modelos import MODELOS, CLASSIFICACOES, DESTAQUES

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links=[]; self.images=[]; self.meta={}; self.ids=[]
        self.market_cards=[]; self.company_cards=[]; self.current=None; self.model_cards=[]
        self.text=path.read_text(encoding='utf-8')
        self.feed(self.text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='a' and 'market-card' in a.get('class','').split():self.market_cards.append(a)
        if tag=='article' and 'market-model-card' in a.get('class','').split():self.model_cards.append(a)
        if tag=='article' and a.get('class')=='market-company':self.current=dict(links=[],images=[])
        if self.current is not None and tag=='a':self.current['links'].append(a.get('href',''))
        if self.current is not None and tag=='img':self.current['images'].append(a)
        if tag=='img': self.images.append(a)
        if tag=='meta': self.meta[a.get('name')]=a.get('content')
        if 'id' in a: self.ids.append(a['id'])
    def handle_endtag(self,tag):
        if tag=='article' and self.current is not None:
            self.company_cards.append(self.current);self.current=None

assert len(AREAS)==6
selected=set(id for members in ASSOCIACOES.values() for id in members)
assert len(selected)==14
assert len({a['id'] for a in PERFIS})==len(PERFIS)==17
assert selected <= {a['id'] for a in PERFIS}
home=Page(ROOT/'mercado/index.html')
assert len(home.model_cards)==4 and not home.market_cards
assert len(home.company_cards)==len(DESTAQUES)==7
assert set(CLASSIFICACOES)=={a['id'] for a in PERFIS}
for id,c in CLASSIFICACOES.items():
    assert c['principal'] in c['funcoes'] or (c['principal']=='mista' and len(c['funcoes'])>=2)
    assert c['funcoes'] and c['limite'] and c['texto'] and c['especialidades']
    assert all(keys and set(keys)<=FONTES_MERCADO.keys() for keys in c['funcoes'].values()),id
    assert id+'.html' in home.links
for modelo in MODELOS:
    assert modelo['id']+'.html' in home.links
    page=Page(ROOT/'mercado'/(modelo['id']+'.html'))
    assert len(page.company_cards)==len(modelo['empresas'])
    for id in modelo['empresas']:
        cards=[c for c in page.company_cards if id+'.html' in c['links']]
        assert len(cards)==1,(modelo['id'],id)
        if modelo['funcao']=='mista': assert len(CLASSIFICACOES[id]['funcoes'])>=2
        else: assert modelo['funcao'] in CLASSIFICACOES[id]['funcoes']
        assert all(FONTES_MERCADO[k][1] in page.links for refs in CLASSIFICACOES[id]['funcoes'].values() for k in refs)
    assert {'empresas','fontes','parte-1','parte-2','parte-3'}<=set(page.ids)
    assert all('../'+s+'/index.html' in page.links for s in ['produtos','materiais','tecnicas'])
for area in AREAS:
    assert area['id']+'.html' in home.links
    page=Page(ROOT/'mercado'/f"{area['id']}.html")
    cards=page.company_cards
    assert len(cards)==len(ASSOCIACOES[area['id']])==(3 if area['id']=='textil-e-vestuario' else 4)
    for id in ASSOCIACOES[area['id']]:
        found=[card for card in cards if f'{id}.html' in card['links']]
        assert len(found)==1,(area['id'],id)
        if id in LOGOS:
            assert any(unquote(LOGOS[id][0]) in unquote(im['src']) for im in found[0]['images']),(area['id'],id)
        else:
            assert not found[0]['images'],(area['id'],id,'logotipo indevido')
    assert '2026-10-14' in page.text and 'id="fontes"' in page.text

entries=json.loads((ROOT/'assets/pesquisa-dados.js').read_text(encoding='utf-8').split('=',1)[1].strip().removesuffix(';'))
urls=[e['url'] for e in entries]
assert len(urls)==len(set(urls))
descriptions=set()
for a in MERCADO:
    path=ROOT/'mercado'/f"{a['id']}.html"
    page=Page(path)
    assert page.meta['robots']=='index, follow'
    assert page.meta['description'] not in descriptions,path
    descriptions.add(page.meta['description'])
    assert len(page.ids)==len(set(page.ids)),path
    assert a['id']=='nobrinde' or not re.search(r'compras internas|clientes internos|catálogo|catálogos',unescape(page.text),re.I),path
    for href in page.links:
        if urlsplit(href).netloc:
            assert href==FONTES_MERCADO['nobrinde_tecnicas'][1] or not re.search(r'/(?:catalogue|catalogues|catalogo|catalogues-overview|catalogsearch)(?:/|$)',urlsplit(href).path,re.I),href
    for im in page.images:
        target=(path.parent/unquote(im['src'])).resolve()
        assert target.is_file() and im.get('alt') and im.get('width') and im.get('height'),target
    entry=next(e for e in entries if e['url']==f"mercado/{a['id']}.html")
    assert entry['summary']==a['resumo']
    if a.get('ficha'):
        assert 'market-profile-summary' in page.text
        for section_id in a['ids_seccoes']:assert section_id in page.ids
        for title,_ in a['seccoes']:assert title in entry['text'],(a['id'],title)
assert not (ROOT/'mercado/mukua.html').exists()
assert 'jhk' not in LOGOS
assert DESTAQUES[-1]=='nobrinde'
assert CLASSIFICACOES['nobrinde']['principal']=='mista'
assert all('nobrinde' in modelo['empresas'] for modelo in MODELOS)
profile=Page(ROOT/'mercado/nobrinde.html')
assert '2026-10-22' in profile.text and 'Logótipo da Nobrinde' in profile.text
assert any(im['src']=='../assets/mercado/Empresas/Nobrinde/images.jpg' for im in profile.images)
from scripts.neutralidade import pagina_publica, texto_publico
sample='<p>Nobrinde combina funções.</p><img src="Nobrinde/images.jpg" alt="Logótipo da Nobrinde">'
assert 'Nobrinde' not in pagina_publica(sample)
assert pagina_publica(sample,permitir_empresa=True)==sample
assert texto_publico('Nobrinde combina funções.',permitir_empresa=True)=='Nobrinde combina funções.'
print('OK: quatro modelos, sete destaques, 17 perfis preservados, funções documentadas, seis áreas anteriores, logos e pesquisa válidos.')
