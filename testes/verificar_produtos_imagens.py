"""Fotografias por família: origem correta, cópia integral e metadados neutros."""
from pathlib import Path
import hashlib
import json
import sys
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.produtos_imagens import IMAGENS, fotos_publicas
from conteudos.produtos_areas import AREAS

expected_folders = dict(zip(
    ['canetas-e-escrita','garrafas-copos-e-canecas','texteis','sacos-e-mochilas','tecnologia','artigos-de-escritorio'],
    ['Papelaria, escritório e escrita','Bebidas, refeições e cozinha','Têxtil, vestuário e acessórios','Sacos, mochilas e viagem','Tecnologia e acessórios digitais','Papelaria, escritório e escrita']))
expected_folders.update({a['guias'][0]: a['titulo'] for a in AREAS
    if a['id'] in ['casa', 'desporto', 'eventos', 'mobilidade', 'embalagem']})
public=fotos_publicas()
used=[]
for id, selecao in IMAGENS.items():
    source=[selecao['cartao'],*selecao['artigo']]
    derived=[public[id]['cartao'],*public[id]['artigo']]
    assert len(source)==len(derived)
    for original,asset in zip(source,derived):
        assert original['original'].startswith('assets/produtos/'+expected_folders[id]+'/')
        a=ROOT/original['original']; b=ROOT/asset['url']
        assert a.is_file() and b.is_file()
        assert hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest()
        with Image.open(b) as image:
            assert image.size==(asset['width'],asset['height'])
            image.verify()
        assert asset['alt']==original['alt']
        assert asset['funcao']=='ilustrativa' and asset['fonte_tecnica'] is False
        assert not any(s in json.dumps(asset).lower() for s in ['nb2','nobrinde','mah','rpet','sku'])
        used.append(asset['url'])
assert len(used)==len(set(used))==29, 'Não repetir fotografias entre cartões e artigos'
records=json.loads((ROOT/'editorial/produtos-imagens.json').read_text(encoding='utf-8'))
assert len(records)==29 and all(r['autoria'] is None and r['licenca'] is None for r in records)
credits=(ROOT/'creditos-imagens.html').read_text(encoding='utf-8')
assert credits.count('id="produtos-ilustrativos"')==1
for area in AREAS:
    if 'visual' not in area:
        continue
    foto = area['visual']
    with Image.open(ROOT/foto['url']) as image:
        assert image.size == (foto['width'], foto['height'])
        image.verify()
print('OK: 29 fotografias das dez áreas, decodificadas e sem alteração dos originais; créditos e proporções documentados.')
