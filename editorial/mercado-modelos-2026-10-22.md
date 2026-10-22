# Mercado — reformulação por modelos de atividade

## Estrutura e ficheiros

A entrada `mercado/index.html` passa a apresentar a cadeia de fornecimento,
quatro modelos de atividade, seis destaques, acesso aos 16 perfis, critérios,
percursos anteriores e ligações para Produtos, Materiais e Técnicas.

Os cartões representam funções empresariais, com esquemas HTML/CSS, cores de
apoio, títulos separados e ligações explícitas. Não foram criadas imagens externas.
Os destaques reutilizam os logótipos existentes e apresentam atividade principal,
etiquetas secundárias, especialidades, descrição factual e fontes expansíveis.

- `conteudos/mercado_modelos.py`: quatro modelos, classificação dos 16 perfis,
  evidência por função, limitações, destaques e etapas da cadeia.
- `scripts/render_mercado_modelos.py`: nova entrada e páginas de modelos.
- `conteudos/mercado.py` e `scripts/render_mercado.py`: integração no gerador.
- `conteudos/catalogo.py`: descrição e grupos de Mercado derivados dos modelos.
- `assets/css/styles.css`: esquemas, cartões, cadeia, etiquetas e adaptação
  a computador, tablet e telemóvel.
- `mercado/*.html` e `assets/pesquisa-dados.js`: saídas geradas e pesquisa.
- `testes/verificar_mercado.py` e `testes/pesquisa.test.cjs`: navegação, funções
  documentadas, preservação dos perfis, imagens e pesquisa.

Mantidos os URLs `distribuicao-e-importacao.html` e
`personalizacao-impressao-acabamento.html`, agora como páginas de modelos.
Preservadas as suas âncoras `parte-1`, `parte-2`, `parte-3`, `empresas` e `fontes`.
Criadas apenas `fabricantes-e-produtores.html` e
`empresas-de-atividade-mista.html`. As seis áreas de oferta anteriores e os
outros guias de Mercado continuam acessíveis como documentação complementar.

## Classificação e fontes

O registo completo de empresas e fontes está em
`editorial/mercado-classificacao-2026-10-22.md`.

- Distribuição inclui fornecedores de artigos e, explicitamente, os fornecedores
  de materiais/equipamentos Dimatur e Eurovinil. Estes não são classificados
  como fabricantes do brinde ou executantes de impressão por venderem máquinas.
- BIC Graphic: fabrico limitado aos instrumentos de escrita assinalados pela
  oferta oficial como fabricados e impressos em fábricas BIC.
- Velilla Group: declaração institucional de desenho, fabrico e distribuição de
  vestuário; não se presume confeção interna ou origem espanhola de todas as peças.
- PF Concept: a apresentação institucional identifica PF Manufactured no Reino
  Unido, além de distribuição e impressão na Polónia. A atribuição de fabrico
  fica limitada a essa operação, não à totalidade dos artigos ou componentes.
- Tela: impressão e personalização documentadas em Sintra, sem converter produção
  gráfica em fabrico de todos os suportes. Stricker, Solo midocean, Giving Europe,
  TejoBrinde, Goya, Plural, XD Connects e AODACi têm funções adicionais de
  personalização documentadas, com os limites de execução indicados em cada cartão.
- TH Clothes e Roly são apresentadas como fornecimento/distribuição e desenvolvimento;
  o desenho e a marca não são usados como prova de confeção própria.

As páginas oficiais de TejoBrinde, Goya, Giving Europe, Solo midocean, Stricker,
Tela, TH Clothes, Gor Factory, Dimatur, Eurovinil e Plural foram consultadas.
Para BIC foi consultada a informação pública indexada da oferta oficial.
O site da Velilla devolveu erro de acesso; foi consultada a apresentação
institucional publicada pela própria empresa no LinkedIn. A página PF Concept
em inglês devolveu erro; a versão oficial acessível em `/ru_ru/about-pf`
apresenta o texto institucional em inglês com o âmbito PF Manufactured.
A página institucional da AODACi no LinkedIn documenta atividade grossista e
personalização; a abertura do site principal foi recusada.

Na XD Connects, a abertura direta devolve uma página dependente de JavaScript.
Mantém-se a descrição já documentada no projeto, com consulta de 14 de outubro
de 2026 explicitamente identificada. Não foi apresentada como verificação nova
de execução própria. Não se atribuiu país aos produtos pela sede e foram omitidas
localizações não confirmadas nos dados usados, como as de Goya e AODACi.

Não foram publicadas comparações de dimensão, volumes, capacidade, exclusividade
ou eficácia comercial. As funções são descrições atribuídas, não uma auditoria.

## Geração e verificações

```powershell
.venv/Scripts/python.exe scripts/gerar.py --secao mercado
.venv/Scripts/python.exe testes/verificar_mercado.py
.venv/Scripts/python.exe testes/verificar_sem_creditos.py
node --test testes/pesquisa.test.cjs
node node_modules/prettier/bin/prettier.cjs --check "mercado/*.html"
```

Resultados: quatro cartões de modelos, seis destaques e 16 perfis preservados;
31 páginas de Mercado e 1 340 ligações/recursos locais verificados; imagens,
dimensões e unicidade de âncoras verificadas; 16 testes de pesquisa aprovados;
formatação aprovada; ausência de créditos públicos confirmada.

Foi confirmada por hashes a preservação byte a byte do HTML fora de Mercado.
A verificação global continua a falhar apenas nas referências a fontes sem
destino em `guias/produto-standard-ou-a-medida.html`, anteriores a esta tarefa.

Foram definidos pontos de adaptação para tablet e telemóvel, mas não foi possível
fazer inspeção visual renderizada: o inventário de navegadores disponível está
vazio. Não se declara revisão por capturas de ecrã.

Sem commit, push ou publicação.
