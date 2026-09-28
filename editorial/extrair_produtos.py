"""Extrai só as fotografias selecionadas, sem texto, preços ou páginas completas."""
from pathlib import Path
from io import BytesIO
import sys,json,hashlib
import pymupdf as fitz
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.recursos import PRODUTOS
OUT=ROOT/'assets/produtos';OUT.mkdir(parents=True,exist_ok=True)
pdf=fitz.open(ROOT/'General Catalogue 2026 - Iberia Prices.pdf')
manifest=[];tiles=[]
for p in PRODUTOS:
    blocks=pdf[p['pdf']-1].get_text('dict')['blocks']
    b=next(b for b in blocks if b['number']==p['bloco'] and b['type']==1)
    im=Image.open(BytesIO(b['image'])).convert('RGBA')
    if b.get('mask'):im.putalpha(Image.open(BytesIO(b['mask'])).convert('L'))
    # Mantém o objeto inteiro; apenas compõe transparência em branco.
    bg=Image.new('RGBA',im.size,'white');bg.alpha_composite(im)
    im=bg.convert('RGB')
    im.thumbnail((1200,1200),Image.Resampling.LANCZOS) # nunca ampliar
    target=OUT/p['ficheiro'];im.save(target,'WEBP',quality=86,method=6)
    manifest.append({'id':p['id'],'ficheiro':'assets/produtos/'+p['ficheiro'],'pdf':p['pdf'],'impressa':p['impressa'],'bloco':p['bloco'],'bbox':b['bbox'],'original':[b['width'],b['height']],'width':im.width,'height':im.height,'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()})
    tile=Image.new('RGB',(260,310),'#f3f6fa');small=ImageOps.contain(im,(240,260))
    tile.paste(small,((260-small.width)//2,6))
    ImageDraw.Draw(tile).text((10,275),p['id'],fill='black');tiles.append(tile)
(ROOT/'assets/produtos/manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
sheet=Image.new('RGB',(1040,310*((len(tiles)+3)//4)),'white')
for i,tile in enumerate(tiles):sheet.paste(tile,((i%4)*260,(i//4)*310))
tmp=ROOT/'tmp/pdfs';tmp.mkdir(parents=True,exist_ok=True)
sheet.save(tmp/'produtos-extraidos.jpg')
print(len(manifest),'imagens;',sum(x['bytes'] for x in manifest),'bytes')
