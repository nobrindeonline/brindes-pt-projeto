"""Registo reproduzível das fontes e limites da secção indústria."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from conteudos.catalogo import FONTES
from conteudos.industria import INDUSTRIA

lines = ['# Fontes da secção indústria', '', 'Consulta e revisão: 24 de setembro de 2026.', '',
 '## Afirmações técnicas e históricas', '',
 'Cada guia apresenta as fontes publicamente. As explicações são sínteses; recomendações de confirmação são orientação editorial, não procedimentos internos da Nobrinde.',
 '', '| Página | Âmbito documentado | Fontes |', '| --- | --- | --- |']
for a in INDUSTRIA:
    sources = '; '.join(f'[{FONTES[k][0]}]({FONTES[k][1]})' for k in a['fontes'])
    lines.append(f"| `industria/{a['id']}.html` | {a['resumo']} | {sources or 'Catálogo: Gratox, PDF 198; Hetien, PDF 270. Operações propostas editorialmente.'} |")
lines += ['', '## Precisão histórica', '',
 '- Museu Bordalo Pinheiro, entrada 1881: Almanach Bijou ilustrado por Rafael e oferecido como publicidade pela Havaneza, no Chiado. Não se afirma uma primeira oferta portuguesa.',
 '- Cornell, coleção Susan H. Douglas, objeto 2214.BT0003b: emblemas de McKinley, data aproximada 1896. Trata-se de comunicação política, não de uma encomenda empresarial.',
 '- PPAI, artigo de Tina Berres Filipski publicado em 26/07/2016: reunião de fabricantes em Chicago em 1903. A página refere a reunião; não se transforma essa data em origem universal dos brindes.',
 '- Os guias atuais midocean sustentam a comparação entre tampografia e bordado, sem estabelecer uma cronologia de invenções.',
 '- O catálogo de 2026 não é usado como prova histórica.', '',
 '## Imagens e esquemas', '',
 '- Reutilizadas as cinco fotografias de técnicas já fornecidas. Autores, fontes, licenças e alterações mantidos em `creditos-imagens.html`. A fotografia de tampografia surge também na etapa de personalização do percurso.',
 '- Produtos reutilizados sem nova edição: Gratox (PDF 198), Hetien (270), Trombolix (426), Farnes (610) e Larsen (360). Ver o registo completo em `fontes-catalogo.md`.',
 '- Pesquisa de fotografias adicionais: Commons (DTF, Almanach Bijou e emblemas McKinley) e registo Cornell. Os pequenos recortes de emblemas encontrados não foram selecionados; o registo Cornell apresenta condições de reprodução que exigem esclarecimento para publicação. Não foi adotada uma imagem adicional com qualidade e licença verificadas.',
 '- Para as máquinas sem fotografia selecionada e para a história, foram criados esquemas HTML/CSS. Não representam instalações, procedimentos de segurança ou equipamento da Nobrinde.',
 '', '## Confirmações necessárias sobre a operação real', '',
 '- Equipamentos disponíveis e quais os processos executados internamente ou por parceiros.',
 '- Referências e superfícies aceites, ensaios e restrições de personalização.',
 '- Forma de aprovação, fornecimento de amostras e gestão de alterações.',
 '- Plano de inspeção, critérios de aceitação e tratamento de peças não conformes.',
 '- Operações de montagem, acessórios e embalagens efetivamente propostas.',
 '- Aquisição dos artigos, disponibilidade, condições e prazos acordáveis.',
 '- Expedição, transporte, acompanhamento, destinatários e modalidades de entrega.',
 '', 'O percurso é uma organização editorial em 11 etapas. Não se apresenta como procedimento confirmado da empresa.', '']
(ROOT/'editorial/fontes-industria.md').write_text('\n'.join(lines), encoding='utf-8')
print('Fontes da industria atualizadas.')
