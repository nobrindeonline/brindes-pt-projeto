"""Registo privado das fontes consultadas; usa a bibliografia única de Produtos."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.produtos import FONTES_PRODUTOS

linhas = ['# Fontes de Produtos — atualização de 21 de outubro de 2026', '',
          'Registo gerado da bibliografia em `conteudos/produtos.py`. As páginas públicas',
          'apresentam apenas as fontes técnicas, o seu âmbito e as datas documentais.', '',
          'As páginas HTML, os documentos USB-IF e GINETEX e as instruções dos fabricantes',
          'foram consultados publicamente. Para ASTM D3776 foi consultado apenas o título',
          'e o resumo indexado público; o acesso direto não devolveu o conteúdo integral.',
          'Não se usaram métodos, limites ou resultados do texto integral dessa norma.', '']
for id, fonte in FONTES_PRODUTOS.items():
    linhas += [f'## {id}', '', f'- Título: {fonte["titulo"]}',
               f'- Entidade: {fonte["entidade"]}', f'- URL: {fonte["url"]}',
               f'- Consulta: {fonte["data_consulta"]}', f'- Âmbito: {fonte["ambito"]}', '']
(ROOT/'editorial/fontes-produtos.md').write_text('\n'.join(linhas), encoding='utf-8')
print(f'Registadas {len(FONTES_PRODUTOS)} fontes públicas de Produtos.')
