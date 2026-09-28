"""Valida as páginas geradas, recursos e destinos/âncoras de ligações internas."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
from conteudos.catalogo import ARTIGOS, SECCOES

ROOT=Path(__file__).resolve().parent
class Page(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.ids=[]; self.links=[]; self.h1=0; self.lang=None
        self.feed(file.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag=='h1': self.h1+=1
        if tag=='html': self.lang=attrs.get('lang')
        for key in ('href','src','action'):
            if key in attrs: self.links.append(attrs[key])

paths=[ROOT/'index.html',ROOT/'pesquisa.html',ROOT/'creditos-imagens.html']
paths += [ROOT/s['id']/'index.html' for s in SECCOES]
paths += [ROOT/a['sec']/(a['id']+'.html') for a in ARTIGOS]
pages={p:Page(p) for p in paths}
errors=[]; checked=0
for path,page in pages.items():
    if page.h1!=1: errors.append(f'{path}: número de H1 = {page.h1}')
    if page.lang!='pt-PT': errors.append(f'{path}: idioma incorreto')
    if any(n>1 for n in Counter(page.ids).values()): errors.append(f'{path}: IDs repetidos')
    for href in page.links:
        part=urlsplit(href)
        if part.scheme or part.netloc: continue
        target=(path.parent/unquote(part.path)).resolve() if part.path else path
        checked+=1
        if not target.is_relative_to(ROOT): errors.append(f'{path}: destino fora do projeto {href}')
        elif not target.is_file(): errors.append(f'{path}: ficheiro inexistente {href}')
        elif part.fragment and target in pages and unquote(part.fragment) not in pages[target].ids:
            errors.append(f'{path}: âncora inexistente {href}')
for article in ARTIGOS:
    for key in ('id','sec','tipo','titulo','resumo','seccoes'):
        if not article.get(key): errors.append(f'Artigo incompleto: {article.get("id")} / {key}')
    if any(not t or not p for t,p in article['seccoes']): errors.append(f'Texto vazio: {article["id"]}')
    if article['tipo']=='tecnica' and not article['fontes']: errors.append(f'Técnica sem fontes: {article["id"]}')
assert len({a['id'] for a in ARTIGOS})==len(ARTIGOS), 'IDs de artigos repetidos'
if errors:
    raise SystemExit('\n'.join(errors))
print(f'OK: {len(pages)} páginas; {checked} ligações/recursos locais; títulos, idioma e âncoras válidos.')
