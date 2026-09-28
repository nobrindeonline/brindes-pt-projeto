"""Contactos das imagens realmente usadas na página, sem percorrer recursos globais."""
from pathlib import Path
from io import BytesIO
import sys
import pymupdf as fitz
from PIL import Image, ImageOps, ImageDraw
ROOT=Path(__file__).resolve().parents[1]
TMP=ROOT/'tmp/pdfs'
pdf=fitz.open(ROOT/'General Catalogue 2026 - Iberia Prices.pdf')
for n in map(int,sys.argv[1:]):
    tiles=[]
    for b in pdf[n-1].get_text('dict')['blocks']:
        if b['type']!=1 or max(b['width'],b['height'])<300:continue
        im=Image.open(BytesIO(b['image'])).convert('RGBA')
        if b.get('mask'):
            im.putalpha(Image.open(BytesIO(b['mask'])).convert('L'))
        bg=Image.new('RGBA',im.size,'white');bg.alpha_composite(im)
        image=bg.convert('RGB');image.thumbnail((230,230))
        tile=Image.new('RGB',(250,275),'#f4f6f9')
        tile.paste(image,((250-image.width)//2,5))
        ImageDraw.Draw(tile).text((8,242),f"block {b['number']} {b['width']}x{b['height']}",fill='black')
        tiles.append(tile)
        print(n,b['number'],b['width'],b['height'],tuple(round(x) for x in b['bbox']))
    sheet=Image.new('RGB',(1000,275*((len(tiles)+3)//4)),'white')
    for i,tile in enumerate(tiles):sheet.paste(tile,((i%4)*250,(i//4)*275))
    sheet.save(TMP/f'imagens-{n}.jpg')
