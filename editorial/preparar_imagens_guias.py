"""Prepara aliases binários neutros; conserva origem e utilização no registo privado."""
from pathlib import Path
import hashlib
import json
import shutil
import sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.guias_imagens import IMAGENS_GUIAS

folder = ROOT/'assets/guias/visuais'
folder.mkdir(parents=True,exist_ok=True)
records=[]
public={}

def preparar(f, guia, uso):
    source=ROOT/f['original'];target=folder/f['nome_publico']
    assert source.resolve().is_relative_to(ROOT/'assets/guias') and source.is_file()
    assert target.resolve().is_relative_to(folder.resolve())
    with Image.open(source) as im:
        width,height=im.size
        im.verify()
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest()!=digest: shutil.copy2(source,target)
    data=dict(url='assets/guias/visuais/'+f['nome_publico'],alt=f['alt'],width=width,height=height,
              funcao='ilustrativa',fonte_tecnica=False)
    if f['secao']: data.update(secao=f['secao'],legenda=f['legenda'])
    records.append(dict(guia=guia,uso=uso,original=f['original'],publico=data['url'],sha256=digest,
        autoria=None,licenca=None,transformacoes='Cópia binária, sem recorte ou conversão.',
        utilizacao_local='Seleção de imagens das pastas fornecidas para os Guias, solicitada em 2026-10-12.'))
    return data

for id,selection in IMAGENS_GUIAS.items():
    public[id]=dict(cartao=preparar(selection['cartao'],id,'cartao'),
        artigo=[preparar(f,id,'artigo') for f in selection['artigo']])
(folder/'imagens.json').write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'editorial/guias-imagens.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Preparadas {len(records)} imagens dos Guias, com originais preservados.')
