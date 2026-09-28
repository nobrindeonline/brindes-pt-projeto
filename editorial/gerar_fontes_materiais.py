"""Reproduz o registo de fontes e fotografias dos sete guias de materiais."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.materiais import MATERIAIS
from conteudos.catalogo import FONTES
from conteudos.recursos import POR_ID

lines = ['# Fontes de Materiais', '', 'Revisão documental: 28 de setembro de 2026.', '',
         'Conteúdo mantido em `conteudos/materiais.py`; referências `[chave]` junto das afirmações e lista de fontes em cada guia, segundo o modelo do projeto.', '',
         'As fontes de fabricantes sustentam propriedades gerais ou os seus próprios produtos/processos. Não certificam referências da Nobrinde. As fontes de conservação explicam vulnerabilidades; não se transferem tratamentos museológicos para brindes novos. Critérios de comparação e perguntas de confirmação são propostas editoriais.', '',
         'As técnicas remetem também para os guias existentes e respetivas fontes. Nenhuma ligação confirma compatibilidade universal.', '']
for a in MATERIAIS:
    lines += [f'## {a["titulo"]}', '', f'Página: `materiais/{a["id"]}.html`', '', '| Tema | Fontes |', '| --- | --- |']
    for title, paragraph in a['seccoes']:
        keys = re.findall(r'\[([a-z]+)\]', paragraph)
        refs = '; '.join(f'[{FONTES[k][0]}]({FONTES[k][1]})' for k in keys)
        lines.append(f'| {title} | {refs or "Orientação editorial; confirmar a referência e consultar os guias técnicos relacionados."} |')
    if a['imagem']:
        product_id, description = a['imagem']
        p = POR_ID[product_id]
        lines += ['', f'Fotografia: `assets/produtos/{p["ficheiro"]}`; {p["nome"]} {p["ref"]}. Origem interna: PDF p. {p["pdf"]}, página impressa {p["impressa"]}. Composição registada em `conteudos/recursos.py`: {" ".join(p["factos"])}', '',
                  f'Legenda/alt públicos: «{description}»', '', 'Reutilizada no cartão e no artigo, sem referências bibliográficas visíveis junto da imagem. Registo de origem e direitos já existente em `creditos-imagens.html` e `editorial/fontes-catalogo.md`. A fotografia ilustra o produto; não comprova composição, certificação ou benefício ambiental.']
    else:
        lines += ['', 'Sem fotografia: os recursos existentes não oferecem uma imagem com composição documentada adequada à família. Não foram usadas fotografias externas nem imagens provisórias.']
    lines.append('')
lines += ['## Confirmações pela Nobrinde', '',
          '- Composição por componente: polímero/liga/fibra, misturas, revestimentos, membranas, colagens e tratamento de pele.',
          '- Referências disponíveis, dimensões, peso completo, resistência e critérios de ensaio.',
          '- Uso alimentar, temperaturas e cuidados do artigo já personalizado: lavagem, detergentes, secagem e equipamentos permitidos.',
          '- Área, técnica, tinta, preparação e resultado numa amostra do acabamento escolhido.',
          '- Documentação de percentagem reciclada, origem, certificações e âmbito de qualquer alegação ambiental.', '',
          'Não foram inventados valores ou capacidades para suprir estes dados. Estes pontos não deixam os guias incompletos: são decisões próprias de cada artigo.', '']
(ROOT/'editorial/fontes-materiais.md').write_text('\n'.join(lines), encoding='utf-8')
print('Fontes de Materiais atualizadas: sete guias e quatro fotografias existentes.')
