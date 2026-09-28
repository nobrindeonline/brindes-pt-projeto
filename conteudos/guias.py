"""Guias práticos: decisões editoriais, fontes técnicas e exemplos documentados."""

FONTES_GUIAS = {
 'adobevetor': ('Adobe — Imagens raster e vetoriais', 'https://www.adobe.com/creativecloud/file-types/image/comparison/raster-vs-vector.html'),
 'adobecor': ('Adobe — Cores diretas e cores de processo', 'https://helpx.adobe.com/in/creative-cloud/apps/colors/spot-and-process-colors.html'),
}

def guia(id, titulo, resumo, tema, seccoes, erros, confirmar, relacionados, fontes, produtos, esquema):
    return dict(id=id, titulo=titulo, resumo=resumo, tema=tema, sec='guias', tipo='guia',
                seccoes=seccoes, problemas=erros, confirmar=confirmar, relacionados=relacionados,
                fontes=fontes, produtos_guia=produtos, esquema_guia=esquema,
                ancoras=['materiais/index.html','produtos/index.html'], tags=titulo+' '+tema)

GUIAS = [
 guia('como-preparar-um-logotipo', 'Como preparar um logótipo para personalização',
 'Do ficheiro original à arte aprovada: prepare o logótipo para o artigo e a dimensão escolhidos.', 'Preparar a arte', [
 ('Comece pelo original', 'Reúna o ficheiro da identidade visual, a versão correta do logótipo e as referências de cor. Evite partir de uma captura de ecrã ou de uma imagem copiada de uma assinatura de email. Se só tiver essa versão, envie-a para avaliação e explique a limitação antes de aprovar qualquer reconstrução.'),
 ('1. Distinga vetor e imagem', 'Um vetor descreve formas; uma imagem raster é composta por píxeis. O vetor adapta-se à escala sem a mesma dependência da resolução. [adobevetor] A extensão não basta: um PDF pode conter apenas uma imagem. Mudar o nome de JPG para PDF não reconstrói o desenho. Peça inspeção do conteúdo do ficheiro.'),
 ('2. Trabalhe à dimensão final', 'Indique a referência do artigo, a face e as dimensões pretendidas. Observe letras pequenas, linhas e espaços vazios à escala final. Uma assinatura legível num saco pode deixar de o ser no corpo de uma caneta. Na Synex 20673, o catálogo documenta o corpo em ABS reciclado; a área de marcação continua por confirmar. Não confunda as dimensões totais da caneta com a área imprimível.'),
 ('3. Adapte sem alterar a marca por acidente', 'Se os detalhes não forem viáveis, proponha uma versão simplificada ou outra posição. Não elimine o slogan nem altere proporções sem aprovação. Para bordado, é necessária uma preparação própria dos pontos; para impressão, podem ser necessárias separações de cor. Confirme quem faz essa adaptação e qual a prova a rever.'),
 ('4. Entregue um conjunto inequívoco', 'Envie o original editável disponível, uma pré-visualização e uma nota com versão, dimensões, posição e cores. Pergunte se é necessário incorporar imagens ligadas ou converter texto em contornos, conservando uma cópia editável. Formatos aceites, resolução e detalhe mínimo dependem do processo: não aplique um valor universal de DPI a todos os trabalhos.')],
 [('Enviar várias versões sem identificar a final','Nomeie a versão aprovada e retire as alternativas do conjunto destinado à produção.'),('Aumentar uma imagem pequena para a tornar nítida','Peça o original ou uma reconstrução validada; aumentar as dimensões não recupera o detalhe que falta.')],
 ['Artigo, face e dimensão final identificados.','Versão e grafia aprovadas.','Formato e tratamento de letras/imagens confirmados.','Simplificações e cores aprovadas antes da produção.'],
 ['tampografia','bordado','serigrafia','como-avaliar-uma-maquete'], ['adobevetor'], ['synex-20673'],
 [('Original','Identificar a versão'),('Escala final','Avaliar o pormenor'),('Prova','Aprovar a adaptação')]),
 guia('pantone-cmyk-e-cor-final', 'Pantone, CMYK e a cor final do brinde',
 'Perceba o que uma referência de cor define e o que só uma prova no artigo permite avaliar.', 'Preparar a arte', [
 ('Porque não basta escolher uma cor no ecrã?', 'O ecrã apresenta luz; o artigo apresenta uma superfície com tinta, textura e acabamento. Use a pré-visualização para discutir o desenho, mas não como amostra física de cor. Identifique o que é prioritário: proximidade à identidade visual, contraste ou consistência entre artigos diferentes.'),
 ('1. Separe referência e método de reprodução', 'Uma referência Pantone identifica uma cor num sistema de referência; não determina, por si só, a técnica. Uma cor direta usa uma tinta preparada, enquanto CMYK combina ciano, magenta, amarelo e preto. Nem todas as cores diretas têm equivalente exato em cores de processo. [adobecor] Pergunte como a referência será interpretada no processo proposto.'),
 ('2. Considere o fundo e o acabamento', 'A cor do artigo e a cobertura da tinta podem alterar a leitura da marca. Um fundo escuro pode exigir uma solução diferente de um fundo branco. Em impressão UV, branco e verniz dependem da configuração disponível. Não transponha automaticamente a aprovação de um artigo para outro material, cor ou revestimento.'),
 ('3. Compare uma prova relevante', 'Forneça a referência completa disponível e combine uma prova no suporte escolhido quando a cor for decisiva. Compare as amostras em condições de luz consistentes e registe qual serve de referência. Defina com o fornecedor o critério de aceitação; não presuma uma tolerância numérica ou igualdade entre técnicas.'),
 ('4. Aprove cada variante necessária', 'Num conjunto com caneta e saco, confirme separadamente a aparência em cada superfície. A coerência visual do conjunto pode exigir ajustes próprios. Uma alteração de tinta, artigo ou acabamento pode justificar nova avaliação, mesmo que o ficheiro seja o mesmo. Guarde a identificação da prova e a versão aprovada.')],
 [('Usar a fotografia do catálogo como amostra de cor','A fotografia ajuda a identificar a variante, mas não substitui uma amostra física.'),('Converter uma referência para CMYK e prometer igualdade','Peça avaliação da reprodução e aprove o resultado no suporte.')],
 ['Referência de cor e variante do artigo registadas.','Técnica e configuração de tinta confirmadas.','Prova e condições de comparação acordadas.','Critério de aceitação definido para cada suporte.'],
 ['impressao-uv','serigrafia','tampografia','como-avaliar-uma-maquete'], ['adobecor'], [],
 [('Referência','A intenção de cor'),('Processo','Como a cor é reproduzida'),('Suporte','Onde a cor é vista')]),
 guia('como-avaliar-uma-maquete', 'Como avaliar uma maquete antes da produção',
 'Reveja versão, texto, posição e escala. Distinga o que a maquete confirma do que exige uma amostra.', 'Verificar e aprovar', [
 ('O que está realmente a aprovar?', 'A maquete representa a composição proposta. Pode ajudar a confirmar conteúdo e posicionamento, mas não demonstra aderência, textura ou resistência. Comece por identificar o artigo, a variante e a versão da arte. Se a imagem representar um produto genérico, peça confirmação de que as proporções correspondem ao modelo escolhido.'),
 ('1. Confira os dados, não apenas o aspeto', 'Leia nomes, contactos, datas e acentos sem depender da memória. Compare com o texto de origem e confirme se todos os elementos pertencem à versão final. Num trabalho com nomes individuais, valide também a lista e a correspondência de cada nome ao artigo; uma maquete geral não valida todas as variantes.'),
 ('2. Localize a marca com referências claras', 'Confirme face, orientação, distância a elementos da peça e dimensão. Uma indicação como «centrado» pode referir-se ao artigo inteiro ou apenas à zona disponível. Peça que a área aprovada fique distinguida de costuras, clips, tampas e outras zonas que condicionam a aplicação. Não deduza medidas pelo tamanho da imagem no ecrã.'),
 ('3. Separe composição e resultado físico', 'Aprove a posição com base numa representação cotada, quando aplicável. Para cor, cobertura, relevo ou toque decisivos, combine a amostra necessária. No Gratox 22075, a ficha documenta caderno, caneta apagável e pano: confirme a que componente corresponde a maquete. O material da capa não está identificado nessa ficha.'),
 ('4. Feche a revisão por escrito', 'Concentre as correções numa lista e peça uma nova versão que as incorpore. Registe o identificador aprovado, os artigos e variantes abrangidos e as condições ainda pendentes. Uma resposta como «parece bem» pode deixar dúvidas sobre o alcance da aprovação. Este método é uma proposta de organização, não um procedimento interno confirmado da Nobrinde.')],
 [('Aprovar a imagem anterior após uma correção','Confira o número ou nome da versão e compare os pontos alterados.'),('Confundir simulação com prova de resistência','Acorde um ensaio adequado ao uso antes de validar esse requisito.')],
 ['Referência, cor e componentes certos.','Texto, nomes e versão final conferidos.','Posição, orientação e medidas explícitas.','Âmbito da aprovação e amostras pendentes registados.'],
 ['como-preparar-um-logotipo','pantone-cmyk-e-cor-final','artigos-de-escritorio','como-escolher-a-tecnica'], [], ['gratox-22075'],
 [('Conteúdo','O que vai ser reproduzido'),('Composição','Onde e com que dimensão'),('Amostra','Como fica no artigo')]),
 guia('como-escolher-brindes-para-um-evento', 'Como escolher brindes para um evento',
 'Ligue a escolha ao público, ao momento de entrega e ao uso depois do evento. Planeie também a distribuição.', 'Escolher o brinde', [
 ('Defina uma função para a oferta', 'Escreva uma frase que explique a utilidade: transportar materiais, tomar notas durante uma sessão ou recordar uma participação. Distinguir estas funções ajuda a selecionar artigos sem depender apenas da aparência. As sugestões deste guia são critérios editoriais, não previsões de retorno comercial.'),
 ('1. Conheça o destinatário e o percurso', 'Considere quem recebe, como chega e o que já transporta. Um artigo volumoso pode exigir outro modo de entrega. Se houver vários públicos, defina variantes justificadas e uma forma simples de as distribuir. Confirme adequação etária e requisitos de utilização quando relevantes.'),
 ('2. Experimente o conteúdo real', 'Para um saco, reúna o que pretende colocar no interior e avalie dimensões, volume e transporte. Larsen 3322 e Emphy 1818 medem 37 × 41 cm no catálogo, mas têm gramagens distintas: 105 e 300 g/m². Estes dados não estabelecem uma carga máxima nem provam qual será mais adequado. Peça avaliação com o conteúdo previsto.'),
 ('3. Pense na mensagem depois do evento', 'Decida se a data e o nome do evento devem dominar o desenho ou se uma mensagem mais duradoura serve melhor o uso posterior. Observe a marca na posição real de utilização. Não escolha uma dimensão de impressão antes de confirmar costuras, acessos e área disponível.'),
 ('4. Planeie a entrega antes de fechar a escolha', 'Registe destinatários, quantidades por variante, embalagens, local e data necessária de receção. Peça confirmação de disponibilidade e calendário com quem vai fornecer. Combine montagem de conjuntos, identificação das caixas e receção; não presuma esses serviços nem um prazo padrão. Uma amostra montada ajuda a detetar componentes esquecidos.')],
 [('Escolher o saco sem experimentar o que vai levar','Valide o conjunto com os materiais reais e o transporte previsto.'),('Aprovar o artigo e esquecer a distribuição','Defina responsáveis, variantes e condições de entrega antes de fechar o pedido.')],
 ['Função e destinatários definidos.','Conteúdo, transporte e utilização avaliados.','Quantidades e variantes organizadas.','Disponibilidade, entrega e embalagem confirmadas.'],
 ['sacos-e-mochilas','eventos','serigrafia','como-escolher-o-material'], [], ['larsen-3322','emphy-1818'],
 [('Antes','Escolha e preparação'),('Durante','Entrega e utilização'),('Depois','Utilidade que permanece')]),
 guia('como-escolher-o-material', 'Como escolher o material de um brinde',
 'Compare utilização, composição e acabamento. O nome do material não resolve sozinho a escolha da personalização.', 'Escolher o brinde', [
 ('Comece pela utilização, não pela aparência', 'Descreva o contacto, a limpeza, o transporte e a exposição previstos. Separe os requisitos essenciais das preferências de toque, peso ou aspeto. Um material adequado a um uso pode exigir cuidados diferentes noutro contexto. Não atribua resistência ou compatibilidade a uma família inteira de materiais.'),
 ('1. Identifique a peça completa', 'Peça a composição do corpo e dos componentes que interessam à aplicação. Distinga material de base, pintura, verniz e outros revestimentos. Numa peça com várias superfícies, indique exatamente onde quer a marca. O nome comercial ou a aparência de madeira não substituem a ficha do artigo.'),
 ('2. Compare referências equivalentes com cuidado', 'Chalmer 21986 e Bastien 22361 têm capacidade indicada de 900 ml. O primeiro é de aço inoxidável reciclado; o segundo é de PP. Esta comparação mostra por que a capacidade não determina o material nem a personalização. Não permite concluir qual conserva melhor a temperatura ou aceita a mesma tinta: esses requisitos precisam de confirmação.'),
 ('3. Avalie superfície e processo em conjunto', 'Confirme a zona acessível, o revestimento e o resultado pretendido. A indicação de sublimação para Farnes 22151 é específica dessa placa; não se aplica automaticamente a todo o bambu. Uma prova no modelo certo é mais útil do que escolher uma técnica apenas pelo nome do material.'),
 ('4. Peça fundamento para as alegações', 'Se uma propriedade reciclada ou uma alegação ambiental pesar na decisão, peça identificação do componente, âmbito e documentação correspondente. A palavra «reciclado» não demonstra, por si só, o impacto global do artigo. Compare também a utilidade prevista e as instruções de conservação, sem inventar vantagens ambientais.')],
 [('Confundir o revestimento com o material de base','Registe ambos e confirme em qual deles ficará a marca.'),('Escolher por uma propriedade isolada','Compare a peça completa, o uso e os cuidados, não apenas capacidade ou composição.')],
 ['Composição e revestimento identificados.','Zona de personalização e acabamento definidos.','Cuidados e resistência necessários confirmados.','Alegações relevantes sustentadas por documentação.'],
 ['garrafas-copos-e-canecas','brindes-premium','gravacao-a-laser','como-escolher-a-tecnica'], [], ['chalmer-21986','bastien-22361','farnes-22151'],
 [('Material','De que é feito'),('Superfície','Onde se aplica a marca'),('Uso','O que terá de suportar')]),
 guia('problemas-comuns-na-personalizacao', 'Problemas comuns na personalização e como os prevenir',
 'Identifique o sinal, reúna evidência e escolha a verificação adequada antes de repetir a produção.', 'Verificar e aprovar', [
 ('Descreva o problema antes de procurar a causa', 'Registe referência, variante, versão da arte, técnica e momento em que o problema apareceu. Fotografe o conjunto e o pormenor em condições comparáveis. Guarde uma peça afetada e a referência aprovada. A mesma aparência pode resultar de causas distintas; este guia orienta perguntas, não substitui o diagnóstico da produção.'),
 ('1. Letras fechadas ou detalhes pouco legíveis', 'Compare o ficheiro e a marca à dimensão final. Verifique se o pormenor já era pouco legível na maquete ou se se perdeu na aplicação. Peça avaliação das linhas e espaços para a técnica escolhida. Antes de repetir, aprove qualquer simplificação, aumento ou mudança de posição.'),
 ('2. Cores ou contornos desalinhados', 'Na serigrafia, várias telas exigem registo entre as cores. [screenhelp] Confira também se a peça se manteve na posição prevista. Distinguir deslocamento da marca inteira e desalinhamento entre cores ajuda a explicar o sinal. Uma nova prova deve confirmar a correção antes de avançar.'),
 ('3. Tinta que se solta ou perde resistência', 'Peça revisão da superfície, preparação, sistema de tinta e condições de cura. Em serigrafia têxtil, a aparência inicial não demonstra uma cura correta; a verificação pode incluir ensaios de lavagem adequados. [screenhelp] Nos restantes artigos, combine o ensaio com a utilização prevista e as instruções aplicáveis. Não aplique um teste ou produto de limpeza universal.'),
 ('4. Cor, posição ou variante incorretas', 'Compare o artigo com a aprovação identificada, incluindo a cor do suporte, face e orientação. Se a diferença for de cor, recorra à referência física acordada; uma fotografia de telemóvel não é uma medição. Para variantes trocadas, reveja a correspondência entre ficheiros, artigos e identificação do lote.'),
 ('5. Feche o ciclo de prevenção', 'Registe o que foi observado, a verificação realizada e a alteração aprovada. Peça uma prova que avalie o problema concreto e conserve-a como referência. Se o modelo, o revestimento ou a arte mudar, reveja os pontos afetados. Evite repetir a produção com base apenas na hipótese de que a causa foi encontrada.')],
 [('Atribuir uma falha a uma causa única pela fotografia','Junte contexto e uma amostra; peça diagnóstico do processo.'),('Repetir sem prova da correção','Defina o critério de aceitação e confirme-o numa nova avaliação.')],
 ['Sinal, momento e artigos afetados registados.','Prova aprovada e amostra disponíveis.','Causa avaliada pela produção.','Correção e verificação acordadas antes da repetição.'],
 ['serigrafia','impressao-uv','bordado','pantone-cmyk-e-cor-final','como-avaliar-uma-maquete'], ['screenhelp'], [],
 [('Observar','Descrever o sinal'),('Verificar','Investigar com contexto'),('Validar','Confirmar a correção')]),
]

TECNICA_EXTRA = dict(tema='Escolher o brinde',
 confirmar=['Referência, material e acabamento identificados.','Arte e zona de aplicação avaliadas.','Uso e resistência necessários definidos.','Prova, quantidade e condições de produção confirmadas.'],
 problemas=[('Escolher só pela fotografia de outro trabalho','Peça avaliação no artigo e variante que pretende encomendar.'),('Confundir o material com uma garantia de compatibilidade','Confirme superfície, tinta ou processo e resultado numa amostra.')],
 esquema_guia=[('Artigo','Forma e superfície'),('Desenho','Cor, detalhe e área'),('Validação','Prova para o uso previsto')],
 produtos_guia=['chalmer-21986','bastien-22361','farnes-22151'])

GRUPOS_GUIAS = [
 ('escolher','Escolher o brinde','Parta da utilização para decidir o artigo, o material e a técnica.','Escolher o brinde'),
 ('cor','Preparar a arte','Prepare o original e saiba o que a referência de cor permite confirmar.','Preparar a arte'),
 ('qualidade','Verificar e aprovar','Reveja a proposta e previna falhas antes de avançar.','Verificar e aprovar')]
