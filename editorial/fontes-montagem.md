# Costura, Argolagem e Encadernação

Revisão: 7 de outubro de 2026. Implementação local; sem commit, push ou publicação.

## Estrutura e decisões

O projeto gera HTML com `gerar.py`, usa os dados de `conteudos/catalogo.py`
e formata com o Prettier local. As referências são chaves `[fonte]` no texto,
convertidas em ligações para a lista de fontes de cada página.

Criado `conteudos/montagem.py`: hub e três artigos com fontes junto das afirmações.
O hub está em Técnicas, com grupo próprio na listagem, três cartões com imagem
e ligações explícitas. Conserva cabeçalho, rodapé, cores e cartões existentes.
Os artigos usam o índice lateral e as classes de leitura de Troquelagem.
Costura usa o ID `tecnica-costura-industrial` para não colidir com o guia de
Indústria, pois os IDs do catálogo são globais. Mantidas as duas rotas antigas
de costura e encadernação/argolagem, com ligações para a nova entrada.

Argolagem é o termo do projeto para a família mecânica; o processo desenvolvido
é a espiral contínua. Não se confunde com pente plástico, argola dupla ou
mecanismo de dossier. A fotografia não comprova a composição da espiral.
Encadernação abrange adesiva, costurada e a ligação à modalidade mecânica.

## Fontes efetivamente abertas e consultadas

| Fonte | Utilização e limites |
| --- | --- |
| [SCHMETZ — Sewing Focus: Luggage, Bags, Travel and Leather Accessories](https://www.schmetz.com/mm/media/en/web/7_tochtergesellschaften/bilder_18/schmetz/pdfs_4/sewing_focus/SewingFocus_23_3075-26_Gepaeck_D.pdf) | Seleção de agulha, linha, material e camadas; aplicações em sacos e acessórios; falhas de ponto e danos. Não transpostos valores de agulha, velocidade, densidade ou resistência. |
| [Coats — Basic Stitch Types](https://www.coats.com/en-us/info-hub/Basic-stitch-types/) | Agulha, formação da laçada e mecanismos de formação do ponto. |
| [Coats — Seam Types](https://www.coats.com/en-us/info-hub/seam-types/) | União estrutural, distinção entre ponto e construção, sobreposição e remate dos bordos. |
| [MyBinding — How to Use a Coil Binding Machine](https://www.mybinding.com/a/knowledge-base/coil-binding/how-to-use-a-coil-binding-machine) | Organização, perfuração, inserção, acabamento das pontas e revisão. Não adotados parâmetros numéricos nem promessas de produtividade. |
| [Sappi — The Standard 6: Binding](https://cdn-s3.sappi.com/s3fs-public/sappietc/sappi_standard06.pdf) | Família de métodos; espiral contínua e Wire-O; costura em cadernos; distinção entre capa e fixação. |
| [HEIDELBERG — C.P. Bourg Perfect Binder](https://www.heidelberg.com/global/en/print_and_packaging/products/digital_printing/postpress_for_digital_printing/cp_bourg_perfect_binder.jsp) | Exemplo industrial de adesiva: preparação de lombada, adesivo, capa, módulos e aplicações. Não identifica equipamento Nobrinde. |

Todas as quatro fontes sugeridas estavam acessíveis. As perguntas de encomenda,
listas de revisão e exemplos de utilização são orientação editorial; não são
especificações de produção ou garantias técnicas.

## Inventário e seleção das imagens

Pasta real: `assets/tecnicas/Costura_Argolagem_Encardenacao/`.
Preservados `tecnicas`, `Encardenacao`, nomes, espaços e extensões. Os dez
ficheiros foram inspecionados numa folha de contacto; os três selecionados
foram também abertos individualmente na dimensão original.

| Ficheiro relativo | Dimensões | Observação / decisão |
| --- | --- | --- |
| `Costura_Industrial/unnamed (35).jpg` | 474 × 474 | Máquina de costura de bancada; não utilizada. |
| `Costura_Industrial/unnamed (36).jpg` | 474 × 266 | Tecido guiado na zona da agulha; menos nítida que a seleção. |
| `Costura_Industrial/unnamed (37).jpg` | 474 × 266 | Selecionada: pormenor de agulha, calcador e tecido. Sem afirmação sobre composição ou carga. |
| `Costura_Industrial/unnamed (38).jpg` | 474 × 315 | Máquina sobre mesa; não acrescenta informação à seleção. |
| `Argolagem/unnamed (40).jpg` | 474 × 511 | Equipamento e pentes de plástico; excluída para não ilustrar espiral com outro sistema. |
| `Argolagem/unnamed (41).jpg` | 474 × 487 | Selecionada: equipamento, espirais contínuas e alicate. Composição não inferida. |
| `Encardenacao/unnamed (42).jpg` | 474 × 474 | Equipamento e pentes de plástico; não ilustra adesiva. |
| `Encardenacao/unnamed (43).jpg` | 474 × 474 | Equipamento com folhas em suporte; processo exato não confirmado, excluída. |
| `Encardenacao/unnamed (44).jpg` | 474 × 298 | Esquema com texto demasiado pequeno para leitura no site, excluído. |
| `Encardenacao/unnamed (45).jpg` | 474 × 474 | Selecionada: trabalho manual com linha em cadernos de papel. Não é imagem de colagem industrial. |

Cada imagem selecionada aparece no cartão e no artigo respetivo, sem recorte,
conversão ou ampliação, com proporção natural e alt descritivo. Créditos em
`creditos-imagens.html#montagem-fornecidas`. Utilização local solicitada pelo
utilizador; autor, fonte original e licença de terceiros por documentar.
Não foram descarregadas imagens externas.

## Ficheiros de implementação

- Novo: `conteudos/montagem.py`.
- Integração: `conteudos/catalogo.py`, `gerar.py`, `styles.css`,
  `conteudos/apresentacao_recursos.py`.
- Documentação: este dossier, `README.md`, `editorial/plano.md`.
- Pesquisa: `testes/pesquisa.test.cjs` e dados regenerados em `assets/pesquisa-dados.js`.
- Quatro páginas novas em `tecnicas/`; atualizados o índice de Técnicas,
  créditos e ligações dos três guias de Indústria relacionados.
- Alterações anteriores a Crachás preservadas.

## Verificações executadas

- `python gerar.py`: 78 páginas, com formatação automática.
- `python verificar.py`: 3024 ligações e recursos locais válidos nas 78 páginas.
- `node --test testes/pesquisa.test.cjs`: nove testes aprovados, incluindo
  pesquisas com e sem acentos e preservação dos guias de Indústria.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 210 utilizações de
  imagens, 43 ficheiros; dimensões, descodificação e textos alternativos válidos.
- `python testes/verificar_materiais.py`: regressões de Materiais aprovadas.
- `npm.cmd run format:check` e `git diff --check`: aprovados.
- Chrome sem janela, com Playwright disponível no ambiente: quatro páginas
  em 360, 390, 768 e 1440 píxeis. HTTP 200, imagens carregadas, sem excesso
  horizontal, três cartões com destinos corretos e menu móvel funcional.
  Capturas em `tmp/montagem-qa/` (ficheiros locais ignorados pelo Git).
  Inspeção visual das capturas do hub em computador e telemóvel e dos artigos.

## Revalidação — 12 de outubro de 2026

O pedido recebido corresponde à implementação já existente. Não foi necessário
alterar os conteúdos, rotas, imagens ou gerador, nem regenerar HTML idêntico.
As seis fontes acima foram novamente abertas; confirmados os trechos sobre
formação do ponto, construção da costura, acessórios, espiral, Wire-O e
preparação da lombada na encadernação adesiva. Reabertas as três fotografias
selecionadas e confirmada a correspondência entre conteúdo, alt e legenda.

Executadas novamente: `python verificar.py` (78 páginas, 3024 ligações/recursos),
`node --test testes/pesquisa.test.cjs` (nove testes),
`.venv/Scripts/python.exe testes/verificar_imagens.py`,
`python testes/verificar_materiais.py`, `npm.cmd run format:check` e
`git diff --check`; todas aprovadas.

Executado `node tmp/montagem-qa/verificar.cjs`: as quatro páginas responderam
HTTP 200 em 360, 390, 768 e 1440 px, sem imagens quebradas nem excesso
horizontal. Confirmados os três cartões, os destinos e o menu móvel.
Capturas completas atualizadas em `tmp/montagem-qa/`; revista visualmente
a captura de 390 px do hub e a apresentação de computador já arquivada.
Nesta revisão, apenas este registo editorial foi alterado. Sem commit, push
ou publicação.

## Confirmações internas

Confirmar processos realmente disponíveis e eventuais parceiros de produção;
materiais, componentes, formatos e equipamentos aceites; consumíveis e gabaritos;
construção das costuras e requisitos de utilização; método de encadernação,
papel, capa e abertura; tolerâncias, provas e ensaios. Não foram inventados
preços, prazos, quantidades mínimas ou capacidades. Documentar a origem e os
direitos das fotografias fornecidas antes de uma eventual publicação.
