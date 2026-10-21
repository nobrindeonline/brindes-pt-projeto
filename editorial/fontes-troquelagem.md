# Troquelagem — fontes e decisões editoriais

Consulta e revisão: 7 de outubro de 2026. Versão local; sem commit, push ou publicação.

## Implementação

- `conteudos/troquelagem.py`: artigo, fontes com título/URL, operações, passos, FAQ e metadados das imagens.
- `conteudos/catalogo.py`: registo e relações com Termogravura, Papel e cartão e o guia de Indústria.
- `scripts/gerar.py`: composição com os mesmos cabeçalho, rodapé, índice de leitura, referências, cartões, passos e imagens responsivas das técnicas existentes; pesquisa inclui também operações e FAQ.
- `conteudos/apresentacao_recursos.py`: créditos das duas imagens utilizadas.
- Rota: `tecnicas/tecnica-troquelagem.html`. O prefixo segue a solução existente em Sublimação e evita colisão no identificador global `troquelagem`, usado por `industria/troquelagem.html`. A rota anterior continua intacta e ambas estão ligadas.
- A listagem Técnicas passa a ligar o tema Troquelagem, além do cartão de guia disponível. Não existe mapa de rotas ou dados estruturados separado a atualizar.
- `testes/pesquisa.test.cjs`: regressão da pesquisa pelas duas rotas e pelas operações.

## Fontes efetivamente consultadas

As referências `[chave]` aparecem junto das afirmações e na lista final do artigo.
As instruções de preparação são recomendações editoriais para confirmação pelo fornecedor,
não tolerâncias ou parâmetros de produção.

| Chave | Fonte | Âmbito utilizado |
| --- | --- | --- |
| troqessencial | [BOBST — The essentials of carton converting](https://www.bobst.com/na/en/news/1768493402-the-essentials-of-carton-converting) | Forma versus impressão; cartão; diferentes configurações, custo de preparação e contexto de séries curtas. |
| troqplaca | [BOBST — The importance of the cutting plate in the folding carton die-cutting process](https://www.bobst.com/eu/en/news/1689880801-the-importance-of-the-cutting-plate-in-the-folding-carton-die-cutting-process) | Superfície de apoio, estado da placa e problemas possíveis. Não se transcrevem durezas, espessuras ou números de ciclos. |
| troqoperacoes | [Esko — Processing Steps: Groups and Types](https://docs.esko.com/docs/en-us/automationengine/24.07/userguide/en-us/common/ae/concept/co_ae_PDFplus_ProcessingSteps.html) | Corte, corte parcial, vincagem e identificação dos dados estruturais separados do grafismo. |
| troqmaquinas | [HEIDELBERG — Die-cutting & embossing](https://www.heidelberg.com/global/en/print_and_packaging/finishing/die_cutting/die_cutting___overview.jsp) | Existência de sistemas planos e rotativos; não representa equipamento da Nobrinde. |
| troqferramenta | [Rollem — Insignia](https://www.rollemusa.com/wp-content/uploads/2022/06/Insignia-Brochure-2021-email.pdf) | PDF, pp. 2–5: ferramentas, cilindros, kiss-cut até à base, aplicações e separação de peças. Sem transferir parâmetros dos modelos para uma regra universal. |
| troqpvc | [Rollem — Success Stories](https://www.rollemusa.com/success-stories/) | Secção Shuffled Ink: PVC entre as aplicações Insignia. Exemplo de fabricante, não promessa de serviço. |
| troqpele | [ATOM — Leather Cutting Machines](https://atom.it/en/industrial-sector/leather-cutting-machines/) | Prensas de troquelagem entre as soluções para couro; não confundir com todos os sistemas digitais também apresentados. |
| troqmanual | [Sizzix — New to Die Cutting](https://www.sizzix.com/pages/new-to-die-cutting) | Equipamento manual de bancada. Não identifica a marca das imagens fornecidas. |
| troqauto | [BOBST — 85 years of Autoplaten innovation](https://www.bobst.com/ru/en/news/1762165202-engineering-the-future-bobst-celebrates-85-years-of-autoplaten-innovation) | Processos manuais/semiautomáticos e automação de alimentação e alinhamento. Sem cronologia ou velocidade comercial no artigo. |
| troqdigital | [Zünd — Packaging](https://www.zund.com/en/applications/packaging) | Corte digital sem troquel para protótipos e séries curtas. Comparação não garante menor custo total. |
| troqperfurar | [Duplo — Print finishing](https://www.duplointernational.com/uk/article/how-duplo-print-finishing-can-boost-your-holiday-business) | Perfuração como sequência de aberturas para destacar partes. |

O primeiro URL sugerido em `media.bobst.com` devolveu timeout. O artigo foi encontrado
e consultado na página oficial BOBST indicada acima; o URL que falhou não foi apresentado
como fonte consultada. As imagens não foram usadas como prova técnica.

## Inspeção e seleção das três imagens locais

Todas abertas e observadas antes da edição. Caminhos e originais preservados.

| Ficheiro em `assets/tecnicas/Troquelagem/` | Dimensões | Observação e decisão |
| --- | --- | --- |
| `unnamed (31).jpg` | 474 × 474 | Máquina branca com manivela turquesa, placas e acessórios. Não utilizada: redundante com a fotografia selecionada. |
| `unnamed (32).jpg` | 474 × 474 | Máquina azul-clara com manivela, ferramenta/placas e recortes decorativos. Destaque após a introdução. |
| `unnamed (33).jpg` | 474 × 206 | Esquema de ferramenta sobre folha e placa de apoio. Junto dos passos do processo. Não implica que todas as operações estejam representadas. |

Utilização dos ficheiros locais pedida expressamente pelo utilizador. Autoria, fonte original
e licença de terceiros permanecem por documentar. Estado registado nos créditos existentes;
nenhuma licença aberta inventada. Não houve download, conversão, recorte ou ampliação.
`pad-reference` conserva proporção natural, largura automática, máximo de 100% e altura automática.

## Confirmações pela equipa

- Material e composição, espessura, camadas/base a preservar, formato e finalidade.
- Máquina e ferramenta adequadas, operações e alinhamento com impressão.
- Prova de corte, destaque, vinco e montagem conforme o trabalho.
- Custo/preparação e eventual reutilização do troquel; dimensão da série e condições comerciais.
- Autoria, origem e direitos das imagens locais antes de eventual publicação.

Não são atribuídos à Nobrinde equipamentos, materiais aceites, tolerâncias,
quantidades mínimas, preços ou prazos.

## Verificação

- `python scripts/gerar.py`: geração com Prettier concluída.
- `python scripts/verificar.py`: 73 páginas, 2795 ligações/recursos locais válidos.
- `node --test testes/pesquisa.test.cjs`: sete testes aprovados, incluindo Troquelagem.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 198 utilizações de imagens,
  39 ficheiros válidos; dimensões e texto alternativo verificados.
- `python testes/verificar_materiais.py`: aprovado.
- `npm.cmd run format:check`: aprovado.
- HTTP local: nova página com resposta 200.
- Rota nova, índice e rota anterior preservada; fontes, âncoras e imagens validadas.
- Limitação de inspeção renderizada: Computer Use devolveu `native pipe is unavailable`
  e o inventário de navegador devolveu `apps: []`, `browsers: []`.
  CSS responsivo partilhado revisto, mas não foi possível confirmar visualmente em
  computador/telemóvel. Rever 360, 390, 768 e 1440 px quando houver navegador ligado.

O gerador também reproduziu duas divergências pré-existentes entre os modelos e
os ficheiros entregues: uma linha na página inicial e omissões de subguias de
Transfers no plano editorial. Conservou-se o estado anterior desses trechos para
manter esta alteração limitada a Troquelagem.
