"""Copia sem transformação os visuais escolhidos e gera os dois manifestos."""
from pathlib import Path
import hashlib
import json
import shutil
import sys
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.produtos_imagens import IMAGENS

destino = ROOT/'assets/produtos/visuais'
destino.mkdir(parents=True, exist_ok=True)
publico = {}
registos = []


def preparar(foto, familia, uso):
    original = ROOT/foto['original']
    target = destino/foto['nome_publico']
    assert original.resolve().is_relative_to(ROOT/'assets/produtos')
    assert target.resolve().is_relative_to(destino.resolve())
    with Image.open(original) as image:
        width, height = image.size
        image.verify()
    digest = hashlib.sha256(original.read_bytes()).hexdigest()
    if not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest() != digest:
        shutil.copy2(original, target)
    assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
    dados = dict(url='assets/produtos/visuais/' + foto['nome_publico'], alt=foto['alt'],
                 width=width, height=height, funcao='ilustrativa', fonte_tecnica=False)
    if foto['secao']: dados['secao'] = foto['secao']
    registos.append(dict(familia=familia, uso=uso, original=foto['original'],
        publico=dados['url'], sha256=digest, width=width, height=height,
        autoria=None, licenca=None,
        utilizacao_local='Fotografias locais de Produtos selecionadas para os guias; revisão de 2026-10-21.',
        transformacoes='Nenhuma: cópia binária sob nome público neutro.'))
    return dados


for id, selecao in IMAGENS.items():
    publico[id] = dict(cartao=preparar(selecao['cartao'], id, 'cartao'),
        artigo=[preparar(foto, id, 'artigo') for foto in selecao['artigo']])
(destino/'imagens.json').write_text(json.dumps(publico, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(ROOT/'editorial/produtos-imagens.json').write_text(json.dumps(registos, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Preparadas {len(registos)} imagens ilustrativas, sem alteração dos originais.')

