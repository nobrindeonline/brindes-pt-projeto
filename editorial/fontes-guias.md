# Guias práticos — fontes e validação

Revisão: 25/09/2026. Versão local, sem publicação na Internet.

## Fontes e âmbito

- Catálogo `General Catalogue 2026 - Iberia Prices.pdf`: páginas PDF 198 (impressa 196), 242 (240), 360 (358), 414 (412), 610 (608). Conferência visual das cinco páginas; factos e fotografias reutilizados de `conteudos/recursos.py`. Relação por artigo em `fontes-catalogo.md`.
- [Adobe — Raster e vetor](https://www.adobe.com/creativecloud/file-types/image/comparison/raster-vs-vector.html): distinção entre píxeis e formas vetoriais, para o guia de logótipo. Não impõe formatos aceites pela Nobrinde.
- [Adobe — Cores diretas e de processo](https://helpx.adobe.com/in/creative-cloud/apps/colors/spot-and-process-colors.html): princípios de cor direta e CMYK e limites de reprodução. Não garante correspondência sobre brindes.
- [ScreenPrinting.com — Impressão de t-shirts](https://help.screenprinting.com/en-US/how-to-screen-print-t-shirts-114141): registo de telas e verificação da cura em serigrafia têxtil, para prevenção de problemas. Não extrapolado para todos os suportes.
- Guias técnicos locais de tampografia, serigrafia, UV, laser e bordado, com as suas fontes identificadas: midocean, Inkcups, Marabu, Roland DG, Trotec e Madeira. Ligações de contexto, sem transformar especificações de fabricantes em capacidades da Nobrinde.

Escolha de evento, organização da aprovação, listas de confirmação e comparações de utilização são propostas editoriais. Não são procedimentos internos confirmados. Os esquemas HTML/CSS são originais; o esquema CMYK não é prova de cor. Não se acrescentaram imagens de máquinas nem imagens técnicas provisórias aos guias.

## Confirmar com a Nobrinde

- Formatos de ficheiro aceites, preparação de letras/imagens e responsabilidade pela adaptação da arte para cada processo.
- Área de aplicação, pormenor viável, tinta, preparação e compatibilidade para a referência e variante escolhidas.
- Processo de aprovação de maquetes e amostras, identificação de versões e responsáveis.
- Critérios de aceitação de cor, posição e acabamento; ensaios de aderência, lavagem ou desgaste conforme o uso.
- Disponibilidade, quantidades, calendário, embalagem e entrega para cada pedido. Nenhuma condição comercial foi presumida.
- Autoria e licença das fotografias do catálogo antes de futura publicação. A origem está documentada; a autorização não é inferida.

## Manutenção e verificação

Conteúdo: `conteudos/guias.py`, complemento do guia original em `conteudos/catalogo.py`.
Geração: `python gerar.py`; fontes: `python editorial/gerar_fontes_catalogo.py`.
As primeiras sete secções e as âncoras do guia de técnica foram conservadas.
As âncoras `escolher`, `cor` e `qualidade` da entrada continuam disponíveis.

A ferramenta de navegador não disponibilizou aplicações ou browsers nesta sessão.
Foi revista a estrutura responsiva (cartões em coluna até 750 px, esquemas em
coluna até 590 px, imagens proporcionais e índice móvel), mas a inspeção visual
real a 360, 390, 768 e 1440 px continua pendente. Não confundir verificações
estáticas com aprovação visual em telemóvel.

Resultados: `verificar.py` aprovou 54 páginas e 1842 ligações/recursos;
`testes/verificar_imagens.py` aprovou 110 utilizações de 24 imagens;
os quatro testes JavaScript de pesquisa passaram. Conferência adicional:
sete cartões com artigos existentes, cabeçalho/rodapé partilhados, secções de
erros, confirmação e fontes em todos os guias e preservação das sete âncoras
originais do guia de técnica. Registo do catálogo e plano editorial regenerados.
