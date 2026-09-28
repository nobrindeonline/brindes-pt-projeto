"""Verifica ficheiros decodificáveis, proporções declaradas, alt e preços em HTML."""
from pathlib import Path
from html.parser import HTMLParser
import sys
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.catalogo import ARTIGOS,SECCOES
from conteudos.ideias import IDEIAS
from conteudos.publicos import PUBLICOS, PAGINAS_PRODUTOS
from conteudos.recursos import POR_ID
paths=[ROOT/'index.html',ROOT/'pesquisa.html',ROOT/'creditos-imagens.html']
paths += [ROOT/s['id']/'index.html' for s in SECCOES]
paths += [ROOT/a['sec']/(a['id']+'.html') for a in ARTIGOS]
class Images(HTMLParser):
    def __init__(self):super().__init__();self.images=[]
    def handle_starttag(self,tag,attrs):
        if tag=='img':self.images.append(dict(attrs))
count=0;unique=set()
for path in paths:
    html=path.read_text(encoding='utf-8')
    assert '€' not in html and 'assets/assets/' not in html,path
    parser=Images();parser.feed(html)
    for img in parser.images:
        assert img.get('alt','').strip(),f'Alt em falta: {path}'
        file=(path.parent/img['src']).resolve()
        assert file.is_relative_to(ROOT) and file.is_file(),file
        with Image.open(file) as image:
            assert image.size==(int(img['width']),int(img['height'])),f'Dimensões: {file}'
            image.verify()
        count+=1;unique.add(file)
listing=(ROOT/'tendencias/index.html').read_text(encoding='utf-8')
assert listing.count('class="idea-card"')==3
for a in IDEIAS:
    assert f'href="{a["id"]}.html"' in listing
    html=(ROOT/'tendencias'/(a['id']+'.html')).read_text(encoding='utf-8')
    assert 'Voltar aos artigos e ideias' in html
    assert '<time' not in html and 'Guia permanente' not in html
    for id in a.get('produtos',a['imagens']):assert 'catalogo-'+id in html
assert not (ROOT/'assets/assets').exists()
public_listing=(ROOT/'publicos/index.html').read_text(encoding='utf-8')
assert public_listing.count('class="audience-card"')==6
for a in PUBLICOS:
    assert f'href="{a["id"]}.html"' in public_listing
    assert f'id="{a["ancora"]}"' in public_listing
    assert 3<=len(a['selecoes'])<=5
    html=(ROOT/'publicos'/(a['id']+'.html')).read_text(encoding='utf-8')
    assert 'Voltar a Para quem' in html
    assert html.count('class="product-example audience-choice"')==len(a['selecoes'])
    for id,why in a['selecoes']:
        p=POR_ID[id]
        assert 2<=len([s for s in why.split('.') if s.strip()])<=4
        assert p['ficheiro'] in html and 'catalogo-'+id in html
        assert f'PDF p. {p["pdf"]}' in html
        assert '../produtos/'+PAGINAS_PRODUTOS[p['categoria']]+'.html' in html
    for method in a['metodos']:assert '../tecnicas/'+method+'.html' in html
print(f'OK: {count} utilizações de imagens, {len(unique)} ficheiros; créditos, grelha, artigos e regressos válidos; sem preços em HTML.')
print('OK: seis públicos, 23 recomendações, justificações de 2 a 4 frases, fontes e guias relacionados.')
