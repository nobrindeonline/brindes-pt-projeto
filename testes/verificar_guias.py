"""Contrato editorial dos sete Guias: fontes, identidade, rotas, pesquisa e dados."""
from pathlib import Path
from html.parser import HTMLParser
from datetime import date
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.guias import GUIAS, GRUPOS_GUIAS, FONTES_GUIAS_META, DATA_REVISAO_GUIAS
from conteudos.guias_imagens import IMAGENS_GUIAS, fotos_publicas_guias
from render_guias import dados_guias, texto_guia, data_pt

ids={g['id'] for g in GUIAS}
assert len(ids)==len(GUIAS)==7
assert len(GRUPOS_GUIAS)==3
assert {g['tema'] for g in GUIAS}=={theme for _,_,_,theme in GRUPOS_GUIAS}
forbidden=re.compile(r'nobrinde|catálogo|catalogue|produtos_guia|synex|gratox|chalmer|bastien|farnes|larsen|emphy|\bSKU\b|auditoria|procedimento interno',re.I)

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.cards=0;self.images=[];self.links=[];self.text=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if 'guide-card' in attrs.get('class','').split():self.cards+=1
        if tag=='img':self.images.append(attrs)
        if tag=='a':self.links.append(attrs.get('href'))
    def handle_data(self,data):self.text.append(data)

listing=(ROOT/'guias/index.html').read_text(encoding='utf-8')
index=Page(listing)
assert index.cards==7 and len(index.images)==7
assert all(g['id']+'.html' in index.links for g in GUIAS)
assert all(id in index.ids for id,_,_,_ in GRUPOS_GUIAS)
assert not forbidden.search(listing)
entries=json.loads((ROOT/'assets/pesquisa-dados.js').read_text(encoding='utf-8').split('=',1)[1].strip().removesuffix(';'))
search={e['url']:e for e in entries}
public=(ROOT/'assets/guias-conteudos.json').read_text(encoding='utf-8')
assert public==dados_guias(), 'Os dados devem derivar da fonte, sem cópia manual'
assert not forbidden.search(public)
assert not re.search(r'\[[a-z]+\]',public), 'As fontes devem estar em campos estruturados'
data=json.loads(public)
assert len(data['guias'])==7 and len(data['percursos'])==3
assert {g['id'] for g in data['guias']}==ids
for g in GUIAS:
    html=(ROOT/'guias'/(g['id']+'.html')).read_text(encoding='utf-8')
    page=Page(html)
    assert not forbidden.search(html),g['id']
    assert len(page.ids)==len(set(page.ids)),g['id']
    assert all(id in page.ids for id in ['resposta','problemas','confirmar','faq','fontes','guia-indice'])
    assert g['resposta_breve'] and g['confirmar'] and g['perguntas_frequentes']
    assert date.fromisoformat(g['data_revisao'])<=date.fromisoformat(DATA_REVISAO_GUIAS)
    assert data_pt(g['data_revisao']) in html
    assert f'datetime="{g["data_revisao"]}"' in html and '2026-09-25' not in html
    assert g['fontes'] and all(k in FONTES_GUIAS_META for k in g['fontes'])
    for key in re.findall(r'\[([a-z]+)\]',str(g)):
        assert key in g['fontes'],(g['id'],key)
        assert 'fonte-'+key in page.ids
    assert set(g['relacionados'])<=ids and g['id'] not in g['relacionados']
    assert len(g['relacionados'])==len(set(g['relacionados']))
    entry=search['guias/'+g['id']+'.html']
    assert entry['summary']==g['resumo'] and entry['text']==texto_guia(g)
    assert not forbidden.search(str(entry))
    for image in page.images:
        assert image.get('alt') and image['src'].startswith('../assets/guias/visuais/')
for id,selection in IMAGENS_GUIAS.items():
    original=[selection['cartao'],*selection['artigo']]
    prepared=[fotos_publicas_guias()[id]['cartao'],*fotos_publicas_guias()[id]['artigo']]
    for f,p in zip(original,prepared):
        assert hashlib.sha256((ROOT/f['original']).read_bytes()).digest()==hashlib.sha256((ROOT/p['url']).read_bytes()).digest()
        assert f['original'] not in public and p['fonte_tecnica'] is False
        path=Path(f['original'])
        assert all(part in [p.name for p in (ROOT/Path(*path.parts[:n])).iterdir()] for n,part in enumerate(path.parts[1:],1)),f['original']
credits=(ROOT/'creditos-imagens.html').read_text(encoding='utf-8')
assert credits.count('id="guias-ilustrativos"')==1
print('OK: sete guias, três percursos, fontes e datas, imagens, pesquisa e JSON consistentes; sem referências proibidas.')
