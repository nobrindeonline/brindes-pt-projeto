"""Guia de bordado: texto, fontes primárias e âncoras estáveis da página existente."""
FONTES_BORDADO = {
    'bordlinhas': ('Madeira — Escolher linhas de viscose ou poliéster: aspeto, toque e cuidados', 'https://www.madeira.com/en-in/service/support/faq/when-to-use-rayon/viscose-and-when-to-use-polyester-threads'),
    'borddensidade': ('Madeira — Como evitar o enrugamento: desenho, tecido e montagem', 'https://www.madeira.com/en-in/service/support/embroidery-best-practice/how-to-avoid-puckering-during-embroidery'),
    'bordpontos': ('Wilcom — Embroidery Stitch Techniques: satin e tatami', 'https://wilcom.com/resources/blog/embroidery-stitch-techniques'),
    'bordprograma': ('Wilcom — Create fills with Auto-Digitizing: formas, preenchimentos e ponto corrido', 'https://docs.wilcom.com/embroiderystudio/28/en/OnlineHelp/Summary/summary_-_create/summary_-_create-75.htm'),
    'bordbrother': ('Brother — My Design Center: converter imagens em dados de bordado', 'https://prox.brother-usa.com/MyDesignCenter.aspx'),
    'bordmaquina': ('Tajima — SAI: agulhas, bastidores e acesso aos artigos', 'https://sai.tajima.com/en/function/'),
    'bordapoio': ('Madeira — Embroidery stabilisers: suporte e estabilização', 'https://www.madeira.com/hk-en/embroidery-supplies/embroidery-stabilisers'),
    'bordproblemas': ('Madeira — Perguntas técnicas: linhas, agulhas e problemas de bordado', 'https://www.madeira.com/en-in/service/support/faq'),
    'bordtecido': ('Madeira USA — Fabric Puckering & Looping Stitches', 'https://www.madeirausa.com/services/troubleshooting/fabric-puckering/'),
}
BORDADO = {
    'id': 'bordado', 'sec': 'tecnicas', 'tipo': 'tecnica', 'titulo': 'Bordado',
    'resumo': 'Como transformar um logótipo em pontos de linha: tipos de ponto, escolha do artigo, relevo, limitações e o que validar numa prova bordada.',
    'data_revisao': '2026-09-29', 'data_revisao_texto': '29 de setembro de 2026',
    'passos': ['Avaliar a peça e o logótipo à escala final', 'Preparar pontos, cores e sequência', 'Escolher bastidor, agulha e estabilização', 'Bordar e avaliar uma amostra'],
    # Conserva o significado dos oito destinos parte-0 a parte-7 já existentes.
    'ids_seccoes': ['parte-0', 'parte-1', 'ponto-satin', 'ponto-tatami', 'outros-pontos', 'parte-2', 'parte-3', 'parte-4', 'parte-6', 'parte-5', 'parte-7'],
    'seccoes': [
        ('O que é e como funciona', 'O bordado constrói uma imagem com pontos de linha no tecido. Antes de executar o desenho, faz-se a digitalização ou digitização para bordado: as formas são traduzidas em pontos, direções, cores e sequência de execução. Um JPEG, PNG ou desenho vetorial pode servir de referência, mas não é, por si só, um ficheiro de bordado pronto. Mesmo quando o programa ou a máquina converte uma imagem automaticamente, existe uma etapa de criação dos dados de bordado, cujo resultado deve ser revisto. Confirme o formato aceite pela máquina e a adequação ao tamanho e ao artigo. [bordprograma] [bordbrother]'),
        ('Máquina, agulhas, linhas e estabilização', 'As máquinas com várias agulhas podem ter diferentes linhas preparadas, selecionadas de acordo com a sequência do programa; isso não significa que todas bordem simultaneamente o mesmo desenho. O movimento do bastidor e a formação dos pontos têm de estar coordenados. O bastidor mantém a zona de trabalho posicionada; o estabilizador dá apoio ao tecido durante o bordado e, conforme o tipo, pode permanecer no avesso. Agulha, linha, bastidor e estabilizador são escolhidos em conjunto para a peça e para o desenho. A fotografia mostra um equipamento de terceiros, não o parque de máquinas da Nobrinde. [bordmaquina] [bordapoio]'),
        ('Ponto cheio ou satin', 'O satin preenche uma faixa com pontos que atravessam a sua largura. Pode criar uma superfície contínua e brilhante em letras, contornos e formas relativamente estreitas. A largura, as mudanças de direção e o comprimento dos pontos precisam de controlo: numa zona demasiado larga, pontos longos podem ficar instáveis ou prender-se. Não é uma solução universal para qualquer letra ou dimensão; pode ser necessário dividir a forma ou escolher outro preenchimento. [bordpontos]'),
        ('Ponto de preenchimento ou tatami', 'O tatami cobre uma área com filas de pontos mais curtos, distribuindo as entradas da agulha. É usado em fundos e formas mais amplas, com uma textura diferente do satin. Direção, espaçamento e sequência influenciam o aspeto e a cobertura. A possibilidade de preencher uma área grande não dispensa avaliar o tecido e a quantidade de pontos: cobrir uma superfície não é o mesmo que a tornar excessivamente densa. [bordpontos] [bordtecido]'),
        ('Ponto corrido, bases e outros preenchimentos', 'O ponto corrido acompanha um percurso e pode servir para contornos ou detalhes lineares, em vez de preencher toda uma superfície. Existem ainda preenchimentos com padrões e efeitos decorativos; a escolha depende da forma e da escala, não apenas do efeito no ecrã. As bases de pontos, também chamadas underlay, ajudam a preparar o apoio para os pontos visíveis. Não substituem o estabilizador colocado sob o tecido. Avalie a combinação numa amostra, sem transformar um desenho de pontos numa receita para qualquer peça. [bordprograma] [bordapoio]'),
        ('Materiais e artigos: avaliar a construção da peça', 'Vestuário, bonés, mochilas e casacos podem ser candidatos a bordado, mas a categoria não garante viabilidade. Registe composição, elasticidade e espessura. Em malhas elásticas, importa apoiar o tecido sem o deformar; em peças espessas, é necessário avaliar a fixação e o conjunto agulha/linha. Nos bonés, a curvatura, a pala, a estrutura frontal e as costuras condicionam o acesso e a posição. Em mochilas e casacos, forros, bolsos, acolchoamento, fechos e costuras podem limitar o bastidor ou prender camadas que deveriam ficar livres. Confirme a área numa peça real e a montagem adequada ao equipamento. [bordmaquina] [bordapoio]'),
        ('Resultado visual e tátil', 'O bordado acrescenta relevo e textura. A direção dos pontos e o brilho da linha alteram a forma como a luz é refletida; satin e tatami não têm necessariamente a mesma leitura visual. [bordpontos] Escolha as cores através de referências de linha e, quando necessário, de uma amostra física, sem prometer equivalência exata com o ecrã ou com uma impressão. Confirme também a cobertura, o toque do avesso e o conforto no local onde a peça será usada. Linha, suporte e acabamento precisam de aprovação no artigo concreto.'),
        ('Preparação do logótipo', 'Entregue o original mais nítido disponível, a dimensão final e a posição pretendida. Reveja a legibilidade das letras pequenas, os espaços estreitos, os contornos e as linhas finas à escala real. Um desenho legível ampliado no ecrã pode perder separação entre elementos quando é bordado. A preparação pode exigir simplificar pormenores, abrir espaços ou ajustar a espessura das formas; essas alterações à marca devem ser aprovadas. Não há uma medida mínima universal válida para todos os tipos de letra, linhas e tecidos. Peça uma prova bordada quando a legibilidade, a cor ou o toque forem decisivos.'),
        ('Limitações e problemas comuns', 'Fotografias e degradés não se reproduzem como numa impressão: são reinterpretados através de cores de linha e distribuição de pontos. Podem existir efeitos de mistura e preenchimentos especializados, mas isso não garante fidelidade fotográfica ou transições idênticas ao original. [bordpontos] Um bordado grande ou uma preparação inadequada pode tornar uma zona rígida ou deformar certos tecidos. Enrugamento, desalinhamento e quebras de linha têm várias causas possíveis; a observação do defeito, isoladamente, não substitui a análise da peça, do programa e da máquina. [bordtecido] [bordproblemas]'),
        ('O que confirmar antes de avançar', 'Identifique o artigo, a composição, a variante e a construção da zona escolhida. Acorde dimensão, posição, orientação, referências das cores de linha, tipos de ponto e estabilização prevista. Confirme as adaptações do logótipo, o formato do ficheiro e a prova necessária; registe qual é a amostra aprovada. Indique a utilização e peça os cuidados de lavagem do fabricante da peça e das linhas. Verifique se são compatíveis entre si: não atribua ao artigo completo a resistência de uma linha isolada. Esta lista ajuda a preparar a encomenda; não descreve capacidades ou procedimentos confirmados da Nobrinde.'),
        ('Comparar com outras técnicas', 'Compare com serigrafia quando o objetivo for uma imagem impressa e a textura do bordado não for a pretendida. Para imagens multicolores, pode também avaliar sublimação em tecidos compatíveis ou outros processos de transferência. O bordado, a impressão e a transferência têm condições diferentes de preparação, cor, toque e suporte. A escolha deve resultar do artigo, do desenho e da utilização, apoiada numa amostra quando necessário; nenhuma técnica é universalmente superior. Consulte os guias relacionados abaixo.'),
    ],
    'problemas': [
        ('Enrugamento ou distorção do tecido', 'Pode estar relacionado com tecido esticado no bastidor, apoio insuficiente ou programa demasiado denso para a peça. Peça revisão do bastidor, estabilizador e pontos; não conclua que basta aumentar a tensão ou acrescentar linha. [bordtecido]'),
        ('Contornos ou cores desalinhados', 'Peça avaliação da fixação, do movimento do tecido e da sequência de bordado. Compare com o ficheiro e a amostra aprovados. Uma fotografia do defeito não permite distinguir, por si só, um problema de preparação, montagem ou equipamento.'),
        ('Quebras de linha', 'Entre as possibilidades estão uma agulha inadequada ou danificada, problemas no percurso da linha, tensão desajustada e concentração excessiva de pontos. A verificação deve ser feita por quem opera o equipamento, observando quando ocorre a quebra. [bordproblemas]'),
        ('Letras fechadas ou detalhes perdidos', 'Reveja escala, desenho das letras, espaços e tipo de ponto com quem prepara o ficheiro. Aprove qualquer simplificação antes de repetir; reduzir ou ampliar um programa não garante o mesmo resultado em todas as dimensões.'),
    ],
    'fontes': list(FONTES_BORDADO),
    'relacionados': ['serigrafia', 'tecnica-sublimacao', 'como-escolher-a-tecnica', 'como-preparar-um-logotipo', 'como-avaliar-uma-maquete', 'materiais-texteis'],
    'ancoras': ['materiais/index.html#texteis', 'produtos/index.html#texteis', 'produtos/index.html#sacos'],
    'tags': 'bordado digitização digitalização ficheiro pontos satin ponto cheio tatami preenchimento ponto corrido underlay bastidor estabilizador bonés mochilas casacos vestuário linhas tensão enrugamento',
}

IMAGENS_BORDADO = {
    'parte-0': ('unnamed.jpg', 474, 474, 'Máquina de bordar branca com ecrã e tecido colocado num bastidor.', 'Exemplo de equipamento com bastidor.'),
    'parte-1': ('unnamed-2.jpg', 474, 357, 'Duas máquinas sobre fundo turquesa; a da esquerda tem vários cones de linha e posições de agulha.', 'Configurações diferentes de equipamento. A imagem não permite confirmar as capacidades de cada modelo.'),
    'parte-3': ('unnamed-3.jpg', 474, 474, 'Motivos florais em tons turquesa e laranja, com textura de fios e relevo sobre fundo claro.', 'Imagem ilustrativa de textura e relevo. Não comprova um tipo de ponto, execução à máquina ou resultado disponível para um logótipo.'),
}

# Complementos na fonte editorial; o gerador mantém os destinos anteriores.
COMPLEMENTOS = {
    'Máquina, agulhas, linhas e estabilização': '\n\nO apoio no avesso e uma película colocada sobre o tecido têm funções diferentes. Em superfícies com pelo ou laçadas, pode ser necessário um material de cobertura, ou topping, para ajudar a impedir que os pontos se afundem. O tipo de apoio, a sua remoção e a eventual utilização de água devem ser compatíveis com a peça; não se escolhem apenas pela facilidade de retirar o excedente. [bordapoio]',
    'Ponto de preenchimento ou tatami': ' Em pormenores muito pequenos, as filas podem não ter espaço para definir a forma; nesses casos, é necessário rever a escala ou a construção do desenho.',
    'Resultado visual e tátil': '\n\nA linha também faz parte da decisão: viscose e poliéster podem diferir no brilho, no toque e nos cuidados admitidos. A espessura da linha deve ser considerada com a agulha e o programa de pontos. Escolher uma linha mais fina, por si só, não resolve um logótipo demasiado pequeno. Registe a referência do fabricante e avalie a cor sobre o tecido escolhido. [bordlinhas]',
    'Preparação do logótipo': '\n\nUma maquete ajuda a rever posição, proporção e grafia; não demonstra o relevo, a cobertura nem o comportamento do tecido. Uma prova bordada no artigo, ou num suporte representativo acordado, permite avaliar esses aspetos. Se mudar a composição, a cor da peça, a posição ou a dimensão do desenho, confirme se a prova anterior continua a ser representativa.',
}
BORDADO['seccoes'] = [(titulo, texto + COMPLEMENTOS.get(titulo, '')) for titulo, texto in BORDADO['seccoes']]
BORDADO['confirmar_bordado'] = [
    ('Artigo e tecido', 'Referência, composição, elasticidade, espessura, forro e acesso à zona; avaliar costuras e camadas numa peça real.'),
    ('Dimensão e posição', 'Largura e altura finais, orientação e localização na peça; rever letras pequenas, espaços estreitos e adaptações da marca.'),
    ('Linhas e pontos', 'Fabricante e referências de cor, tipo e espessura da linha, satin, tatami ou outros pontos adequados a cada elemento.'),
    ('Montagem e estabilização', 'Bastidor, apoio no avesso e eventual cobertura; confirmar o toque e o acabamento das zonas em contacto com a pele.'),
    ('Ficheiro e prova', 'Formato aceite pelo equipamento, versão do desenho e amostra aprovada; distinguir a maquete visual da prova bordada.'),
    ('Utilização e lavagem', 'Uso previsto e cuidados indicados pelo fabricante do artigo e das linhas. Validar a peça já personalizada, sem transferir para o conjunto a resistência de um só componente. [bordlinhas]'),
]
BORDADO['seccoes'] = [
    (titulo, 'Antes de aprovar, registe as decisões abaixo com quem prepara e executa o bordado. Esta lista orienta a avaliação do artigo concreto; não descreve capacidades ou procedimentos confirmados da Nobrinde.' if titulo == 'O que confirmar antes de avançar' else texto)
    for titulo, texto in BORDADO['seccoes']
]
BORDADO['problemas'][0] = (
    'Enrugamento ou distorção do tecido',
    'Pode estar relacionado com tecido esticado no bastidor, apoio insuficiente ou programa demasiado denso para a peça. Peça revisão do bastidor, estabilizador e pontos; não conclua que basta aumentar a tensão ou acrescentar linha. [bordtecido] [borddensidade]',
)
