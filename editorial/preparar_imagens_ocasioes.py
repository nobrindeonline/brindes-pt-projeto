"""Cópias integrais com nomes neutros para exemplos de Ocasiões."""
from pathlib import Path
import sys
import json
import hashlib
import shutil
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.ocasioes_exemplos import ORIGINAIS
base = ROOT/'assets/ocasioes'
destino = base/'visuais'
destino.mkdir(exist_ok=True)
registos = []
for id, ficheiro in ORIGINAIS.items():
    origem, alvo = base/ficheiro, destino/(id+'.jpg')
    assert origem.resolve().is_relative_to(base) and alvo.resolve().is_relative_to(destino)
    with Image.open(origem) as image:
        width, height = image.size
        image.verify()
    digest = hashlib.sha256(origem.read_bytes()).hexdigest()
    if not alvo.exists() or hashlib.sha256(alvo.read_bytes()).hexdigest()!=digest:
        shutil.copy2(origem, alvo)
    registos.append(dict(id=id, original=origem.relative_to(ROOT).as_posix(),
        publico=alvo.relative_to(ROOT).as_posix(), width=width, height=height,
        sha256=digest, autoria=None, licenca=None, transformacoes='Nenhuma: cópia integral.'))
(ROOT/'editorial/ocasioes-exemplos-imagens.json').write_text(
    json.dumps(registos,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Preparadas {len(registos)} imagens locais de exemplos, sem alterar os originais.')
