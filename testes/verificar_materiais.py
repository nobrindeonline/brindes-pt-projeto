"""Requisitos editoriais de Materiais: destinos, fontes, pesquisa e texto público."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.materiais import MATERIAIS
from conteudos.catalogo import ARTIGOS, FONTES

class PublicText(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.text = []
        self.cards = []
        self.feed(html)

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'img':
            assert attrs.get('alt', '').strip(), 'Imagem sem descrição'
            self.text.append(attrs['alt'])
        if tag == 'article' and 'material-card' in attrs.get('class', '').split():
            self.cards.append(attrs['id'])

listing = (ROOT/'materiais/index.html').read_text(encoding='utf-8')
assert len(PublicText(listing).cards) == 7
entries = json.loads((ROOT/'assets/pesquisa-dados.js').read_text(encoding='utf-8').split(' = ', 1)[1].strip().removesuffix(';'))
by_id = {a['id']: a for a in ARTIGOS}
for a in MATERIAIS:
    assert f'href="{a["id"]}.html"' in listing
    assert f'id="{a["ancora"]}"' in listing
    assert any(e['url'] == f'materiais/{a["id"]}.html' for e in entries)
    assert a['fontes'] and all(k in FONTES for k in a['fontes'])
    assert all(k in a['fontes'] for _, p in a['seccoes'] for k in re.findall(r'\[([a-z]+)\]', p))
    assert any(by_id[k]['sec'] == 'produtos' for k in a['relacionados'])
    assert any(by_id[k]['sec'] == 'tecnicas' for k in a['relacionados'])
    html = (ROOT/'materiais'/f'{a["id"]}.html').read_text(encoding='utf-8')
    assert 'Voltar aos materiais' in html
    for text in (listing, html):
        visible = ' '.join(PublicText(text).text)
        assert not re.search(r'catálogo|catalogue|PDF|página\s+\d|\bp\.\s*\d', visible, re.I), a['id']
print('OK: sete cartões, sete artigos na pesquisa, fontes, produtos e técnicas; sem referências públicas ao catálogo em Materiais.')
