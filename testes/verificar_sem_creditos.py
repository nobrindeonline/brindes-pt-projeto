"""Os créditos de imagem não integram a apresentação pública nem os modelos."""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.neutralidade import pagina_publica

assert not (ROOT/'creditos-imagens.html').exists()
checked=0
for path in ROOT.rglob('*.html'):
    if any(part in {'.git','.venv','node_modules','tmp','editorial','docs'} for part in path.relative_to(ROOT).parts):
        continue
    text=path.read_text(encoding='utf-8')
    assert not re.search(r'creditos-imagens\.html|créditos (?:de|da|das) image|Fotografia:',text,re.I),path
    checked+=1
sample='<figure><img src="objeto.jpg" alt="Objeto"><figcaption>Objeto sobre uma mesa. <span>Fotografia: Autor · CC BY</span> <a href="creditos-imagens.html">Créditos da imagem</a></figcaption></figure>'
clean=pagina_publica(sample)
assert 'Objeto sobre uma mesa.' in clean and 'alt="Objeto"' in clean
assert not re.search(r'Autor|CC BY|creditos-imagens|Créditos',clean)
assert pagina_publica(clean)==clean
assert 'Texto preservado' in pagina_publica('<a href="creditos-imagens.html">Créditos</a\n><p>Texto preservado</p>')
print(f'OK: {checked} páginas/modelos sem créditos públicos; descrições e imagens preservadas.')
