# Crachás tipo pin/botão — fontes e revisão

Revisão documental: 7 de outubro de 2026. Versão local, sem commit, push ou publicação.

## Designação e âmbito

O pedido inicial usa «Crachás Automáticos». A designação pública escolhida é
**Crachás tipo pin/botão**, que delimita o produto montado numa prensa. A rota
`tecnicas/crachas-automaticos.html` e os termos de pesquisa conservam a expressão
inicial. O artigo distingue a automação da prensagem das operações de impressão,
corte, alimentação de componentes e inspeção. Não abrange cartões de identificação,
placas de nome ou emblemas bordados.

«Produção rápida e consistente» não é apresentada como garantia: depende da
preparação, do equipamento, do operador e dos componentes. Não se reproduzem
velocidades, capacidades, medidas ou condições comerciais dos fabricantes.
«Selagem» é esclarecida como montagem/fecho mecânico, sem promessa de estanquidade.

## Fontes consultadas

Todas as páginas abaixo foram abertas e lidas; os quatro URLs sugeridos estavam
disponíveis. As referências `[chave]` do projeto ligam as afirmações à lista de fontes.

| Chave | Entidade e título | Âmbito utilizado |
| --- | --- | --- |
| pinabm | [American Button Machines — How to Make a Button](https://www.americanbuttonmachines.com/pages/how-to-make-a-button) | Componentes, impressão, corte maior que a frente, montagem e aspetos a rever no grafismo, película e fecho. Sem instruções universais de afinação da máquina. |
| pingabarito | [American Button Machines — Frequently Asked Questions](https://www.americanbuttonmachines.com/pages/frequently-asked-questions) | Distinção entre linha de corte e área interior da imagem. Não se transferem medidas, papel recomendado ou compatibilidade de um sistema para outro. |
| pinbrildor | [BRILDOR — Automatic Electric Badge Making Machine](https://www.brildor.com/en/automatic-electric-badge-machine) | Descrição e instruções: modos de acionamento da prensa, colocação de componentes e deslocação da base pelo operador; imprimir/cortar antes; matrizes e testes prévios. |
| pinsecabo | [Secabo — Badge Making Machines for Custom Designs](https://www.secabo.com/en/button-production/badge-making-machines) | Matrizes para tamanho/forma, sistema de troca e aplicações publicitárias/criativas. |
| pinbuttonfly | [Buttonfly — Button badge machines](https://buttonfly.pl/en/our-offer/machines/button-badges/) | Modelos dedicados versus matrizes intercambiáveis, sequência de montagem e variantes de verso. Excluídas promessas comerciais de velocidade ou longevidade. |

As verificações propostas ao cliente são uma síntese editorial baseada nos pontos
de montagem e nos problemas descritos. Não são um protocolo de controlo de qualidade
da Nobrinde. As sugestões de campanha, grupo ou evento são exemplos gerais, identificados
como tal, e não trabalhos realizados pela empresa.

## Imagem local

Pasta real: `assets/tecnicas/Crachas/` (C maiúsculo).
Ficheiro: `pack-inicial-chapas-evolution-principal_1.jpg`, 360 × 360 píxeis.

A fotografia foi aberta antes da edição: prensa de bancada com alavanca de pega
laranja, matrizes metálicas e componentes circulares, incluindo diferentes versos.
Não foi atribuída uma função a cada componente apenas pela imagem, nem identificada
a máquina como automática. Foi colocada em **Equipamento, matrizes e formatos**.
Não retrata uma etapa de impressão, corte ou movimento da prensa.

Original preservado sem download de alternativas, edição, conversão ou recorte.
`pad-reference` usa largura automática, máximo de 100% e altura automática; a imagem
não é ampliada. Alt objetivo e legenda explicam o que é visível. Os créditos registam
a utilização local solicitada e a autoria/fonte original/licença ainda por documentar.

## Integração e ficheiros

- `conteudos/crachas.py`: conteúdo, fontes, passos, componentes, FAQ e imagem.
- `conteudos/catalogo.py`: registo global, tema do índice e ligação inversa de Indústria.
- `scripts/gerar.py`: mesma composição usada em Troquelagem; pesquisa inclui componentes, passos e FAQ.
- `conteudos/apresentacao_recursos.py`: créditos da imagem.
- `tecnicas/crachas-automaticos.html`, `tecnicas/index.html`, `industria/producao-de-crachas.html`, `creditos-imagens.html` e `assets/pesquisa-dados.js`: resultados gerados.
- `testes/pesquisa.test.cjs`: pesquisa pela designação inicial e termos do processo, preservando a rota de Indústria.
- `README.md` e `editorial/plano.md`: manutenção e estado do novo guia.

Não existe um mapa de rotas ou dados estruturados separado para as técnicas.
Cabeçalho, rodapé, índice do artigo, referências e estilos responsivos são partilhados;
não foram acrescentados CSS ou JavaScript de interface.

## Verificação

- Geração Python e Prettier concluídos.
- `python scripts/verificar.py`: 74 páginas e 2858 ligações/recursos locais válidos.
- `node --test testes/pesquisa.test.cjs`: oito testes aprovados.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 200 utilizações de imagens,
  40 ficheiros válidos; dimensões e alt verificados.
- `python testes/verificar_materiais.py`: aprovado.
- `npm.cmd run format:check`: aprovado.
- Nova rota com resposta HTTP 200 no servidor local.
- Imagem observada, caminho e capitalização preservados. CSS de leitura a uma coluna
  até 750 px e imagem contida no espaço disponível, sem altura fixa.
- **Limitação visual:** `cua.getState()` devolveu `apps: []`, `browsers: []` nesta tarefa.
  Não foi possível confirmar a renderização em ecrãs pequenos. Rever 360, 390, 768 e
  1440 px quando houver navegador: menu, índice, texto, imagem e ausência de overflow.

## Confirmações da equipa

- Sistema efetivamente utilizado e operações automatizadas; não inferidos da fotografia.
- Formatos, matrizes e referências compatíveis de frente, papel, película e verso.
- Gabarito, área visível, margem de montagem, papel e requisitos do ficheiro.
- Fixação, utilização, cuidados, amostra e critérios de aceitação.
- Condições reais de quantidade/prazo; sem mínimos ou velocidade inventados.
- Autoria, origem e direitos da imagem fornecida antes de eventual publicação.
