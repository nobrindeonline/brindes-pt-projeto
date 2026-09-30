# Termogravura — revisão documental de 29 de setembro de 2026

## Âmbito e implementação

O guia trata de estampagem a quente com folha (hot foil stamping). Não descreve
conformação metalúrgica a quente nem atribui à Nobrinde equipamentos ou serviços.

- Fonte editorial: `conteudos/termogravura.py`.
- Registo de artigo, fontes e relações: `conteudos/catalogo.py`.
- Geração: `gerar.py`, reutilizando cabeçalho, rodapé, índice, cartões, referências,
  esquema de processo e lista responsiva existentes.
- Página: `tecnicas/termogravura.html`.
- Listagem e etiqueta «Termogravura» no grupo «Gravação e relevo» passam a ter destino.
- Ligações de entrada nos guias de laser, UV, serigrafia, papel/cartão, pele/imitação,
  artigos de escritório, escolha da técnica, preparação do logótipo e revisão da maquete.
- Pesquisa gerada inclui sinónimos, lista de confirmação e problemas.

## Fontes consultadas diretamente

Todas as páginas e PDF abaixo foram abertos com sucesso nesta revisão; foram
consultados os trechos indicados, não apenas os resultados de pesquisa.

| Fonte | Trecho e utilização |
| --- | --- |
| [Foilco — Foil Academy](https://www.foilco.com/foil-academy/) | «What is stamping foil?», escolha do cunho, máquinas e glossário: definição, preparação e distinção de relevo. |
| [Foilco — Structure of Foil](https://www.foilco.com/structure-of-foil/) | Carrier, Release Coat e Adhesive or Size Coat: filme de transporte, libertação e fixação da decoração. |
| [Foilco — D4 Foil Grade Guide, edição 1](https://www.foilco.com/app/uploads/2019/05/Grade-Guide-Booklet_E_Doc.pdf) | Páginas impressas/PDF 5–6: acabamentos. Página 18: agendas, capas e pele revestida numa formulação específica. Página 24: imitação de pele e encadernação noutra formulação. As fichas ressalvam que as temperaturas orientativas dependem da velocidade da máquina. Não se reproduzem tabelas nem se generalizam compatibilidades. |
| [KURZ — Holograms](https://www.kurz-world.com/en/solutions/holograms/) | «Application and Integration: Cold Transfer and Hot Stamping»: confirmação dos efeitos holográficos por estampagem a quente. Não se importam promessas de segurança ou desempenho. |
| [Iggesund — Hot foil stamping in practice](https://www.iggesund.com/globalassets/iggesund/services/knowledge/iam/graphics-handbook/gh-pdf----en/hot_foil_stamping_in_practice.pdf) | Páginas impressas 62–63 (PDF 1–2): transferência, lisura, limpeza e superfície do cartão; distinção de embossing/debossing. |
| [Foilco — Fine Detail Foiling](https://www.foilco.com/fine-detail-foiling/) | «What is Fine Detail Foil?», «Fine detail foiling advice» e «Using typography?»: espaços negativos, letras e combinação de cheios com detalhe. Não se adota a medida exemplificada como mínimo universal. |
| [Foilco — Brass](https://www.foilco.com/brass/) | «Cons of Brass» e «Extra Info»: produção do cunho e diferenças de custo por material. Sem preços, prazos ou limiares de quantidade. |
| [Howard — Foil Application Guide](https://www.howardimprinting.com/myfiles/FOIL-APPLICATION-GUIDE.pdf) | Página 2, «Finding optimal release temperature»: interação entre temperatura e tempo de contacto, definição da impressão. Não se copiam valores operacionais do equipamento. |
| [Milford Astor / Ever Bright — Manual H-200B, H-250 e H-400](https://astor.com.au/content/products/H-200B%20H250%20H-400%20Operating%20Instructions.pdf) | Página 23, «Troubleshooting»: transferência incompleta, cunho desnivelado, folha e parâmetros. São causas possíveis documentadas para esses modelos, não diagnósticos nem instruções universais. |

Também consultada [Foilco — Magnesium](https://www.foilco.com/magnesium/) para
contexto da comparação de materiais do cunho; a página pública usa a referência
Brass, suficiente para a afirmação limitada sobre custo de fabrico.

As listas de aprovação, as perguntas comerciais e a comparação com os guias
locais são síntese editorial, sem promessas de compatibilidade ou de resistência.

## Imagens: inventário e decisão

A pasta real é `assets/tecnicas/Termogravura/` (maiúscula inicial). Os quatro
originais foram vistos e mantidos intactos. Não foram encontrados autoria,
fonte original ou direitos de utilização documentados no projeto. Nenhum dos
ficheiros é carregado ou ligado na página pública.

| Ficheiro | Observação | Decisão |
| --- | --- | --- |
| `unnamed (16).jpg` | Equipamento com alavanca e rolos laterais. | Reservado até documentar origem e autorização; não inferir modelo ou capacidades. |
| `unnamed (17).jpg` | Equipamento com folha de aspeto metálico e mãos junto à zona de trabalho. | Reservado até documentar origem e autorização; não usar como instrução de operação. |
| `unnamed (18).jpg` | Diapositivo Altair sobre conformação e tratamento térmico de metal. | Excluído por tratar de outro processo, além da falta de autorização. |
| `unnamed (19).jpg` | Esquema em inglês de camadas e transferência de folha. | Reservado até documentar origem e autorização. |

O artigo usa uma sequência original em HTML/CSS, sem reproduzir os desenhos das
imagens ou dos fabricantes. A autorização anterior para imagens de Bordado não
foi estendida a esta pasta.

## Verificações e pendências

- `python gerar.py`: 67 páginas geradas e formatadas.
- `python editorial/gerar_plano.py`: estado de Termogravura atualizado.
- `python verificar.py`: 67 páginas; 2476 ligações/recursos locais válidos.
- `node --test testes/pesquisa.test.cjs`: cinco testes aprovados.
- `python testes/verificar_materiais.py`: aprovado.
- `.venv/Scripts/python.exe testes/verificar_imagens.py`: 185 utilizações,
  32 ficheiros; dimensões, descodificação, textos alternativos e créditos aprovados.
- `npm.cmd run format:check`: aprovado.
- O CSS existente coloca artigo, índice e esquema numa coluna nos pontos de
  adaptação móvel; os novos parágrafos e lista não introduzem larguras fixas.
- Inspeção visual em telemóvel pendente: a ferramenta de interface devolveu
  inventários vazios de navegadores e aplicações. A revisão de HTML/CSS não
  substitui uma inspeção de renderização real.

Ainda a validar para qualquer trabalho concreto: artigo e revestimento, folha,
cunho, limites de detalhe, posição, parâmetros, prova e resistência ao uso;
preço do cunho/preparação, prazos e condições dependem do fornecedor. Para usar
as fotografias, documentar origem e direitos primeiro.

Alterações anteriores existentes no projeto foram preservadas. Sem push ou
publicação do site.
