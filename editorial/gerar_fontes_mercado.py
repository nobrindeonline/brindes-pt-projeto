"""Regenera o inventário editorial, associações e fontes públicas de Mercado."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.mercado import DATA, PERFIS, TEMAS, AREAS, FONTES_MERCADO
from conteudos.mercado_areas import ASSOCIACOES, NOTAS_FONTES
from conteudos.mercado_empresas import EMPRESAS, LOGOS
from conteudos.mercado_imagens import IMAGENS, destino

shortlist = list(dict.fromkeys(id for members in ASSOCIACOES.values() for id in members))
lines = ['# Mercado — áreas de produto, empresas e fontes', '',
         f'Consulta: {DATA}. Gerado com `python editorial/gerar_fontes_mercado.py`.', '',
         '## Estrutura e âmbito', '',
         f'- Seis áreas de produto; {len(shortlist)} entradas únicas da shortlist e {len(PERFIS)} perfis no total.',
         '- A lista recebida contém catorze entradas ao tratar Velilla Group / MUKUA como uma relação empresa–marca.',
         '- Sete perfis anteriores revistos; nove perfis acrescentados. Dimatur e Eurovinil conservam as rotas e o enquadramento nos guias complementares.',
         '- Preservaram-se os seis guias de cadeia e todas as suas rotas. A entrada apresenta seis cartões de produto; os guias anteriores ficam em navegação complementar.',
         '- As categorias são editoriais e podem sobrepor-se. A ordem segue a organização proposta, sem classificação de dimensão ou desempenho.',
         '- Não foram usados ficheiros de contactos, dados de contas, compras ou classificações privadas. A pesquisa usou fontes públicas.', '',
         '## Áreas, cartões e prova da associação', '']
for area in AREAS:
    lines += ['### '+area['titulo'], '', '`mercado/'+area['id']+'.html`', '',
              'Imagem: `'+destino(area['id'],'cartao')+'` — '+IMAGENS[area['id']]['cartao'][3], '']
    for id,(reason,keys) in ASSOCIACOES[area['id']].items():
        lines += ['- **'+EMPRESAS[id]['nome']+'** — '+reason+' Perfil canónico: `mercado/'+id+'.html`. Fontes: '+', '.join(keys)+'.']
    lines += ['']
lines += ['## Perfis, funções e fontes por secção', '']
for a in PERFIS:
    lines += ['### '+a['titulo'], '', '`mercado/'+a['id']+'.html`', '', a['resumo'], '',
              'Papel resumido: '+EMPRESAS[a['id']]['papel']+'.', '']
    for n,(title,text) in enumerate(a['seccoes']):
        keys = a['fontes_seccoes'][n]
        lines += ['- **'+title+'** — '+(', '.join(keys) if keys else 'Delimitação editorial da informação disponível')+'.']
    lines += ['', '**Limites publicados:** '+a['seccoes'][-1][1], '']
lines += ['## Fontes públicas consultadas', '']
used = list(dict.fromkeys([key for a in PERFIS for key in a['fontes']] +
                         [key for members in ASSOCIACOES.values() for _,keys in members.values() for key in keys] +
                         [key for a in TEMAS for key in a['fontes']]))
for key in used:
    title,url = FONTES_MERCADO[key]
    lines += ['- `'+key+'` — ['+title+']('+url+') — consulta '+DATA+'. '+NOTAS_FONTES.get(key,'Conteúdo público consultado; a data de consulta não é uma garantia futura de disponibilidade do endereço.')]
lines += ['', '## Limites da pesquisa e critérios de publicação', '',
          '- Nenhuma das catorze entradas foi excluída: a atividade e a associação temática encontram apoio nas fontes listadas. As candidatas de pesquisas antigas que não pertencem à seleção não foram acrescentadas.',
          '- Algumas aberturas diretas de PF Concept e Velilla devolveram erros temporários; XD Connects requer JavaScript e o relatório XD não abriu diretamente. Usaram-se os conteúdos oficiais indexados publicamente, com a limitação identificada junto da fonte. Não se usaram ambientes dev/uat.',
          '- A abertura direta do site AODACi devolveu 403; o relatório institucional 2024, publicado em setembro de 2025, foi consultado e a apresentação pública institucional suporta as famílias de produto. O relatório é um documento ESG, não um documento comercial de produtos, apesar do subdomínio que o aloja.',
          '- A associação sazonal da Stricker foi confirmada na página de técnicas: guarda-chuvas, bonés e mantas. Não se ligou documentação comercial extensa.',
          '- MUKUA é marca da Velilla. A aquisição em 2020 é corroborada pelo Cinco Días.',
          '- Giving Europe: o certificado disponibilizado tem titular FL B.V.; não se altera o titular para Giving Europe B.V. nem se presume cobertura de cada produto. A validade indicada no PDF não foi reconfirmada no registo FSC.',
          '- Políticas, selos ou materiais não são extrapolados para toda a empresa. Metas ambientais não são tratadas como realizações. Brindes Ecológicos não é um selo nem ranking.',
          '- Mantiveram-se apenas indicadores já documentados com entidade e período, como a faturação Gor Factory de 2025 atribuída pela Modaes. Não se acrescentaram estimativas de importação, emprego ou produção a partir de resultados incompletos.',
          '- Os limites são declarados individualmente; não se infere um ano de constituição a partir de expressões de antiguidade.', '',
          '## Logótipos e imagens', '']
for id in shortlist:
    if id in LOGOS:
        file,w,h,alt = LOGOS[id]
        lines += ['- '+EMPRESAS[id]['nome']+' — `assets/mercado/Empresas/'+file+'` ('+str(w)+' × '+str(h)+'). Texto alternativo: '+alt+'.']
    else:
        lines += ['- '+EMPRESAS[id]['nome']+' — **logótipo local em falta**. O ficheiro da pasta “Velilla Group  MUKUA, JHK” mostra apenas Velilla; não foi atribuído a JHK.']
lines += ['',
          '- Os logótipos foram inspecionados; não se moveram, redesenharam ou substituíram originais. O logótipo Roly disponível identifica agora a marca, distinguindo-a da sociedade Gor Factory.',
          '- Os seis cartões de área reutilizam imagens locais inspecionadas, em cópias byte a byte com nomes neutros. Os bonés ilustram sazonalidade; a imagem de escrita na área ambiental é de contexto, sem comprovar composição ou impacto.',
          '- Não se associaram fotografias genéricas de instalações a fornecedores. O utilizador autorizou o uso dos logótipos; não se inventou autoria ou licença externa.', '',
          '## Geração e verificações', '',
          '- Conteúdos: `conteudos/mercado_areas.py`, `conteudos/mercado_novos_perfis.py`, `conteudos/perfis_mercado.py` e `conteudos/mercado.py`. Apresentação: `render_mercado.py` e estilos existentes.',
          '- `python gerar.py --secao mercado`: entrada e 29 páginas individuais; pesquisa insere novas entradas e atualiza apenas Mercado. Outras entradas e HTML fora da secção são preservados.',
          '- Resultados finais em `editorial/verificacao-mercado-areas.md`: verificação geral, pesquisa, formatação, seis cartões, 24 associações, perfis canónicos, imagens e privacidade.',
          '- Não existe sitemap nem domínio canónico confirmado. As novas rotas integram pesquisa e inventário; não se inventou um sitemap absoluto sem domínio.',
          '- Mantêm-se `index, follow`, as regras de robots existentes e conteúdo principal em HTML, sem dependência de JavaScript.',
          '- Revisão visual de navegador pendente: não havia navegador ligado nas verificações anteriores. Os recursos foram inspecionados e os componentes responsivos reutilizados.', '']
(ROOT/'editorial/fontes-mercado.md').write_text('\n'.join(lines),encoding='utf-8')
print('Dossier de Mercado atualizado.')
