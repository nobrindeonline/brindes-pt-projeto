# Bordado — revisão de 29 de setembro de 2026

## Fonte e geração

O artigo é definido em `conteudos/bordado.py`, importado por `conteudos/catalogo.py`.
`python gerar.py` produz `tecnicas/bordado.html`, os cartões relacionados e
`assets/pesquisa-dados.js`. O gerador preserva as âncoras `parte-0` a `parte-7`
e as três âncoras de tipos de ponto. A lista de confirmação e os problemas
também entram na pesquisa. O esquema de processo é HTML/CSS original do site.

## Referências consultadas

- [Wilcom — tipos de ponto](https://wilcom.com/resources/blog/embroidery-stitch-techniques): satin, tatami, dimensões das formas e efeitos de preenchimento. Não se adotaram medidas ou parâmetros universais.
- [Wilcom — Auto-Digitizing](https://docs.wilcom.com/embroiderystudio/28/en/OnlineHelp/Summary/summary_-_create/summary_-_create-75.htm): conversão de formas em pontos e contornos em ponto corrido.
- [Brother — My Design Center](https://prox.brother-usa.com/MyDesignCenter.aspx): distingue importar/digitalizar a imagem de a converter em dados de bordado. Exemplo de um sistema específico.
- [Tajima — SAI](https://sai.tajima.com/en/function/): máquina com várias agulhas e diferentes bastidores; as dimensões e capacidades desse modelo não são atribuídas à Nobrinde.
- [Madeira — estabilizadores](https://www.madeira.com/hk-en/embroidery-supplies/embroidery-stabilisers): apoio no avesso, cobertura superior e adequação ao tecido.
- [Madeira — FAQ](https://www.madeira.com/en-in/service/support/faq): causas possíveis de quebras de linha e escolha de agulha.
- [Madeira USA — enrugamento](https://www.madeirausa.com/services/troubleshooting/fabric-puckering/): montagem, estabilizador e agulha.
- [Madeira — evitar enrugamento](https://www.madeira.com/en-in/service/support/embroidery-best-practice/how-to-avoid-puckering-during-embroidery): densidade, preparação e teste no tecido.
- [Madeira — viscose e poliéster](https://www.madeira.com/en-in/service/support/faq/when-to-use-rayon/viscose-and-when-to-use-polyester-threads): escolha de linha, brilho, toque e cuidados. As condições de uma linha não são condições de lavagem da peça completa.

Todas as nove referências abriram na consulta documental e estão identificadas
na própria página. As recomendações de aprovação são orientações editoriais;
não representam processos internos confirmados da Nobrinde.

## Imagens e pendências

`assets/Bordado/` não existe nesta cópia. Foram encontrados
`assets/tecnicas/Bordado/unnamed.jpg`, `unnamed-2.jpg` e `unnamed-3.jpg`.
O utilizador autorizou expressamente a utilização dos três ficheiros em 29 de
setembro de 2026. Foram inspecionados e incorporados nas secções de funcionamento,
equipamento e resultado visual, com legendas factuais e ligação aos créditos.
Os originais não foram alterados. Autoria e fonte original continuam por identificar;
a autorização não é apresentada como licença aberta. A imagem floral é apenas
ilustrativa: não comprova execução à máquina nem um tipo de ponto específico.

Mantida `assets/tecnicas/bordado.webp`, com autoria de Srini297, origem Wikimedia
Commons e licença CC BY-SA 4.0 documentadas em `assets/LEIA-ME-creditos.md`,
`conteudos/recursos.py` e na página pública de créditos. Mantidos caminho relativo,
dimensões, texto alternativo factual e identificação como equipamento de terceiros.

Continuam a depender de avaliação concreta: acesso ao painel, compatibilidade
da peça, dimensão e legibilidade, cores de linha, estabilização, prova e cuidados.

## Verificação

- `python gerar.py`: 66 páginas geradas e formatadas.
- `python verificar.py`: páginas, ligações e recursos locais aprovados após inserir as três imagens autorizadas.
- `node --test testes/pesquisa.test.cjs`: 5 testes aprovados.
- `python testes/verificar_materiais.py`: aprovado.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: imagens, créditos e percursos aprovados após inserir as três imagens autorizadas. O Python global não tem Pillow.
- `npm.cmd run format:check`: aprovado; usado o executável CMD porque a política
  do PowerShell impede executar `npm.ps1`.
- Revisão do CSS: abaixo de 750 px, artigo numa coluna; abaixo de 590 px,
  índice e esquema numa coluna. Lista de confirmação sem largura fixa.
- Inspeção visual em telemóvel pendente: a ferramenta de navegador devolveu
  «No browser is available». A revisão do código não substitui essa inspeção.

Sem push e sem publicação do site.
