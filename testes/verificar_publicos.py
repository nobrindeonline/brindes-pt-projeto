"""Valida estrutura, fontes, imagens, ligações e neutralidade dos guias públicos."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.publicos import PUBLICOS


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.context_figures = 0
        self.scenario_paragraphs = 0
        self.tabular_fact_lists = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag == 'img':
            self.images.append(attrs)
        if tag == 'figure' and 'audience-context-image' in attrs.get('class', '').split():
            self.context_figures += 1
        if tag == 'p' and 'audience-scenario' in attrs.get('class', '').split():
            self.scenario_paragraphs += 1
        if tag == 'dl' and 'audience-facts' in attrs.get('class', '').split():
            self.tabular_fact_lists += 1


forbidden = re.compile(
    r'nobrinde|catálogo|catalogue|general catalogue|\bSKU\b|\bnb\d{3,}\b|'
    r'gratox|sulkan|larsen|synex|hetien|trombolix|chalmer|bastien|stiles|'
    r'emphy|farnes|fabrica',
    re.I,
)

listing_path = ROOT / 'publicos' / 'index.html'
listing = listing_path.read_text(encoding='utf-8')
listing_page = Page(listing)
assert listing.count('class="audience-card"') == len(PUBLICOS) == 8
assert len(listing_page.images) == 8

structured = json.loads((ROOT / 'assets' / 'para-quem-conteudos.json').read_text(encoding='utf-8'))
search_text = (ROOT / 'assets' / 'pesquisa-dados.js').read_text(encoding='utf-8')
search = json.loads(search_text.split('=', 1)[1].strip().removesuffix(';'))
search_by_url = {entry['url']: entry for entry in search}
source_text = (ROOT / 'conteudos' / 'publicos.py').read_text(encoding='utf-8')

required = {'destinatário', 'ocasiões', 'famílias_de_artigos', 'critérios', 'fontes', 'etiquetas'}
assert len(structured['destinos']) == 8
assert {item['id'] for item in structured['destinos']} == {item['id'] for item in PUBLICOS}

for audience in PUBLICOS:
    path = ROOT / 'publicos' / (audience['id'] + '.html')
    text = path.read_text(encoding='utf-8')
    page = Page(text)
    record = next(item for item in structured['destinos'] if item['id'] == audience['id'])
    assert required <= record.keys()
    assert record['data_revisao'] == '2026-10-14'
    assert any(image['alt'] == audience['imagem']['alt'] for image in listing_page.images)
    image_path = ROOT / audience['imagem']['url']
    assert image_path.is_file()
    assert audience['imagem']['url'] in listing
    assert all(anchor in page.ids for anchor in (
        'destinatarios', 'ocasioes', 'familias', 'distribuicao',
        'criterios', 'faq', 'relacionados',
    ))
    assert 'fontes' not in page.ids
    assert 'Fontes, âmbito e revisão' not in text
    assert 'documentary-date' not in text
    assert not forbidden.search(text), audience['id']
    assert not forbidden.search(json.dumps(record, ensure_ascii=False)), audience['id']
    assert not forbidden.search(json.dumps(search_by_url['publicos/' + audience['id'] + '.html'], ensure_ascii=False))
    families_section = re.search(
        r'<section id="familias">(.*?)</section>',
        text,
        re.S,
    )
    assert families_section, audience['id']
    assert families_section.group(1).count('class="audience-family"') == len(record['famílias_de_artigos'])
    assert 'class="audience-context"' not in families_section.group(1)
    assert families_section.group(1).count('<strong>Objetivo</strong>') == len(record['famílias_de_artigos'])
    assert families_section.group(1).count('<strong>Famílias a avaliar</strong>') == len(record['famílias_de_artigos'])
    assert page.scenario_paragraphs == len(record['ocasiões'])
    assert page.tabular_fact_lists == 0
    assert page.context_figures == len(record['imagens_contexto'])
    for image in record['imagens_contexto']:
        assert image['alt'] in text
        assert ''.join(image['legenda'].split()) in ''.join(text.split())
        assert (ROOT / image['url']).is_file()
    for occasion in record['ocasiões']:
        assert {'destinatário', 'ocasião', 'local', 'época', 'objetivo'} <= occasion.keys()
        assert occasion['texto_editorial']
    for reference in record['fontes']:
        assert reference['data_consulta'] == '2026-10-14'
        if f'[{reference["id"]}]' in json.dumps(record, ensure_ascii=False):
            assert reference['url'] in text
    for href in page.links:
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        assert target.is_relative_to(ROOT) and target.is_file(), (path, href)
        if parsed.fragment and target == path:
            assert unquote(parsed.fragment) in page.ids, (path, href)

assert not forbidden.search(listing)
assert not forbidden.search(json.dumps(structured, ensure_ascii=False))
assert not forbidden.search(source_text)
assert not forbidden.search(json.dumps(search_by_url['publicos/index.html'], ensure_ascii=False))
print('OK: oito guias, estrutura consultável, fontes datadas, imagens, ligações e pesquisa sem dados comerciais.')
