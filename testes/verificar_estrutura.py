"""Protege a organização e a separação entre publicação e ferramentas internas."""
from pathlib import Path
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.catalogo import ARTIGOS, SECCOES

for name in ['gerar.py', 'verificar.py', 'neutralidade.py', 'render_guias.py',
             'render_produtos.py', 'render_mercado.py']:
    assert (ROOT/'scripts'/name).is_file()
    assert not (ROOT/name).exists()
for name in ['script.js', 'pesquisa.js', 'guias.js']:
    assert (ROOT/'assets/js'/name).is_file() and not (ROOT/name).exists()
assert (ROOT/'assets/css/styles.css').is_file() and not (ROOT/'styles.css').exists()
assert not list(ROOT.glob('*.pdf')) and not list(ROOT.glob('*.zip'))
ignore = (ROOT/'.assetsignore').read_text(encoding='utf-8').splitlines()
assert all(name in ignore for name in ['scripts/', 'docs/', 'conteudos/', 'editorial/', 'testes/', 'tmp/'])

class Recursos(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.resources = []
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'script' and 'src' in a: self.resources.append(a['src'])
        if tag == 'link' and a.get('rel') == 'stylesheet': self.resources.append(a['href'])

pages = ['index.html', 'pesquisa.html', 'creditos-imagens.html']
pages += [s['id'] + '/index.html' for s in SECCOES]
pages += [a['sec'] + '/' + a['id'] + '.html' for a in ARTIGOS]
for name in pages:
    resources = Recursos(ROOT/name).resources
    assert any(r.endswith('assets/css/styles.css') for r in resources), name
    assert any(r.endswith('assets/js/script.js') for r in resources), name
    assert not any(r in ['styles.css', '../styles.css', 'script.js', '../script.js',
                         'pesquisa.js', '../guias.js'] for r in resources), name
print('OK: estrutura organizada, recursos públicos e exclusões de publicação coerentes.')
