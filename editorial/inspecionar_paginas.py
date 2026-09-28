from pathlib import Path
import sys
import pymupdf as fitz
from PIL import Image, ImageOps, ImageDraw
ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'tmp/pdfs'
pdf=fitz.open(ROOT/'General Catalogue 2026 - Iberia Prices.pdf')
numbers=[int(x) for x in sys.argv[1:]]
tiles=[]
for number in numbers:
    page=pdf[number-1]
    pix=page.get_pixmap(matrix=fitz.Matrix(1.4,1.4))
    pix.save(TMP/f'pagina-{number}.png')
    image=Image.open(TMP/f'pagina-{number}.png')
    image.thumbnail((360,480))
    tile=Image.new('RGB',(380,520),'#e5eaf0')
    tile.paste(image,((380-image.width)//2,10))
    ImageDraw.Draw(tile).text((12,495),f'PDF {number}',fill='black')
    tiles.append(tile)
    print(number,'SIZE',page.rect)
sheet=Image.new('RGB',(380*min(4,len(tiles)),520*((len(tiles)+3)//4)),'white')
for i,tile in enumerate(tiles):sheet.paste(tile,((i%4)*380,(i//4)*520))
sheet.save(TMP/'seleccao.jpg')
