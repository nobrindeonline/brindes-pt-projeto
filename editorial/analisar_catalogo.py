"""Leitura local do PDF: texto por página e miniaturas para seleção editorial."""
from pathlib import Path
import json
import pymupdf as fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'tmp/pdfs'
TMP.mkdir(parents=True,exist_ok=True)
pdf=fitz.open(ROOT/'General Catalogue 2026 - Iberia Prices.pdf')
pages=[]
for n,page in enumerate(pdf,1):
    pages.append({'pagina_pdf':n,'rotulo':page.get_label(),'texto':page.get_text()})
(TMP/'paginas.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
print('PAGES',len(pdf),'METADATA',pdf.metadata)
for p in pages[:8]:
    print('PAGE',p['pagina_pdf'],p['texto'][:700].encode('ascii','backslashreplace').decode())
images=[]
for file in sorted((ROOT/'assets/tecnicas').glob('*.webp')):
    im=Image.open(file)
    print(file.name,im.size,file.stat().st_size)
    tile=Image.new('RGB',(420,330),'#f3f6f9')
    small=ImageOps.contain(im.convert('RGB'),(400,285))
    tile.paste(small,((420-small.width)//2,10))
    ImageDraw.Draw(tile).text((12,304),file.stem,fill='#12243a')
    images.append(tile)
sheet=Image.new('RGB',(1260,660),'white')
for n,im in enumerate(images):sheet.paste(im,((n%3)*420,(n//3)*330))
sheet.save(TMP/'techniques.jpg')
