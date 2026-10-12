"""Bibliografia privada gerada da fonte revista; não é uma cópia manual."""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.guias import FONTES_GUIAS_META, DATA_REVISAO_GUIAS

lines=['# Fontes dos Guias', '', 'Revisão efetiva do conteúdo: '+DATA_REVISAO_GUIAS+'.', '',
       'Registo gerado a partir de `conteudos/guias.py`. As páginas públicas mostram',
       'a bibliografia e as datas documentais, sem os registos internos de execução.', '']
for id,f in FONTES_GUIAS_META.items():
    lines += ['## '+id,'','- Título: '+f['titulo'],'- Entidade: '+f['entidade'],
              '- URL: '+f['url'],'- Consulta: '+f['data_consulta'],'- Âmbito: '+f['ambito'],'']
(ROOT/'editorial/fontes-guias.md').write_text('\n'.join(lines),encoding='utf-8')
print(f'Registadas {len(FONTES_GUIAS_META)} fontes públicas dos Guias.')
