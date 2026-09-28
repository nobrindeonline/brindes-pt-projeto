# Integração de Tendências — 28 de setembro de 2026

## Âmbito

Integração local dos quatro artigos Markdown fornecidos em `TesteTendenciasv1`.
Os documentos foram tratados como conteúdos e propostas editoriais, não como
instruções para publicar, contactar fornecedores ou alterar aplicações externas.
Não houve publicação, commit ou push.

A listagem conserva as três ideias anteriores e acrescenta quatro cartões com
páginas completas. O cabeçalho, rodapé, fontes tipográficas, cores e componentes
partilhados são os existentes. Os novos painéis tipográficos identificam fornecedor
e referência; não representam fotografias ou características visuais dos produtos.

## Classificação e fontes

- SMART collection: **Coleção em destaque**. O pacote recebido afirma que é um
  lançamento de 2026. A página `https://www.pfconcept.com/en_nl/end-of-year-2026`
  e a página principal não puderam ser reconfirmadas: erro de acesso na pesquisa
  e ciclo de redirecionamentos na consulta direta. O texto atribui a informação
  ao dossier e assinala a reconfirmação pendente; não apresenta novidade confirmada.
- Clerk MO2845: **Novidade confirmada**, identificada na apresentação pública
  Novelties 2026 da midocean (página numerada 12; resultado indexado também em
  versões neerlandesa, romena e alemã). O relatório EMC original foi consultado:
  modelo, data e normas correspondem ao dossier; os resultados respeitam à amostra.
- Taier MO2932: **Novidade confirmada**, identificada na apresentação pública
  Novelties 2026 da midocean (página numerada 53 da versão francesa, indexada).
  O relatório original identifica a amostra e o ensaio IEC 62471:2006 como PASS.
- Trigo 1514191: **Novidade confirmada**. Surge explicitamente na listagem
  `https://www.givingeurope.com/global/en/all-products/specials/featured/novelties-2026`
  e a ficha pública confirma as características descritas no artigo.

A página inicial Iberia da midocean já destaca outras referências; retirou-se a
formulação transitória “apresenta atualmente” dos artigos. A classificação assenta
na apresentação Novelties 2026, não na posição atual na homepage. O PDF francês
é demasiado grande para leitura integral pela ferramenta web e a transferência
direta expirou; a confirmação utilizou os excertos indexados e os relatórios
originais acessíveis. As ligações originais do dossier foram preservadas.

As datas visíveis são datas editoriais, não datas exatas de lançamento.
Sugestões de utilização não são apresentadas como procura comprovada. A existência
de uma referência no fornecedor não demonstra oferta ou disponibilidade na Nobrinde.

## Ficheiros criados ou alterados

- `conteudos/novidades.py`: quatro artigos, fontes, categorias, data e pendentes.
- `conteudos/catalogo.py`: registo dos quatro artigos para geração e pesquisa.
- `gerar.py`: renderização de artigos com parágrafos, listas, destaque, fontes,
  índice interno, data, nota editorial e ligações; novos cartões na listagem.
- `styles.css`: apresentação dos painéis tipográficos e ajustes responsivos locais.
- `tendencias/index.html`: sete cartões e explicação das categorias editoriais.
- `tendencias/smart-collection-pf-concept.html`.
- `tendencias/calculadora-lcd-mo2845.html`.
- `tendencias/lanterna-magnetica-mo2932.html`.
- `tendencias/carregador-trigo-3-em-1.html`.
- `assets/pesquisa-dados.js`: quatro artigos incluídos no índice.
- `README.md`: manutenção dos novos artigos e ligação a este registo.
- `editorial/integracao-tendencias.md`: este registo.

A geração integral revelou um desfasamento anterior entre `modelos/inicio.html`
e `index.html`: o modelo acrescenta uma legenda junto ao logótipo. Essa alteração
incidental foi retirada de `index.html`, preservando a página inicial desta tarefa.
Uma futura geração integral voltará a reproduzir a legenda prevista no modelo.

## Verificações realizadas

- Geração pelo gerador Python existente e formatação pelo Prettier fixado no projeto.
- `python3 verificar.py`: 65 páginas e 2297 ligações/recursos locais válidos;
  um H1 por página, idioma pt-PT, destinos internos e âncoras verificados.
- `python3 testes/verificar_materiais.py`: passou.
- `node --test testes/pesquisa.test.cjs`: quatro testes passaram.
- Chromium/Playwright, ficheiros locais: listagem e quatro artigos nas larguras
  360, 390, 768 e 1440 px (20 combinações). Sem deslocamento horizontal;
  grelha com 1/2/3 colunas conforme a largura; cabeçalho e rodapé presentes.
- Menu abre e fecha por Escape nas larguras de telemóvel; datas, fontes,
  confirmações e ligações dos quatro cartões presentes.
- Pesquisa no navegador por MO2845, MO2932, Trigo e SMART encontra os artigos;
  nenhum erro JavaScript observado.
- Capturas em `tmp/tendencias-*-390.png` e `tmp/tendencias-*-1440.png`;
  resultados automáticos em `tmp/tendencias-browser.json`. A pasta é ignorada pelo Git.
- Inspeção visual das capturas da listagem e de artigo em telemóvel.

Node.js e Playwright foram usados a partir de instalações temporárias; o projeto
mantém apenas o Prettier como dependência de desenvolvimento.

## Validações pendentes

- Reconfirmar o lançamento SMART collection na página original da PF Concept.
- Aprovação editorial final pela Nobrinde e confirmação das correspondências com
  referências próprias, disponibilidade em Portugal, stock, quantidades mínimas,
  preços, prazos, técnicas e áreas de personalização.
- Resolver as questões específicas de cada artigo, visíveis em “Antes de uma
  proposta comercial”: composição da SMART collection; alimentação e códigos
  DL/DO1 do Clerk; lúmens e classificações de resistência da Taier;
  compatibilidade, potências por zona, adaptador e composição reciclada do Trigo.
- Teste num telemóvel físico e em Safari/iOS: as verificações responsivas realizadas
  usaram Chromium em larguras simuladas e não substituem esses testes.
- Se forem pretendidas fotografias, obter imagens próprias ou autorização de uso.
  A integração atual está completa com painéis tipográficos.
