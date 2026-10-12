"""Guias: fonte de leitura, pesquisa e dados estruturados."""

DATA_REVISAO_GUIAS = '2026-10-12'
INTRO_GUIAS = 'Escolha o percurso que corresponde à sua dúvida: definir o artigo e a personalização, preparar a arte ou rever a proposta antes de produzir.'
RESUMO_GUIAS = 'Sete guias para escolher, preparar ficheiros e cor e rever antes de produzir.'

FONTES_GUIAS_META = {'adobevetor': {'titulo': 'Understand raster and vector files',
                'entidade': 'Adobe',
                'url': 'https://helpx.adobe.com/photoshop/desktop/create-open-import-images/import-files/use-raster-and-vector-files.html',
                'ambito': 'Vetor, raster e conteúdo misto em PDF; sem requisitos universais de resolução '
                          'para personalização.',
                'data_consulta': '2026-10-12'},
 'adobecor': {'titulo': 'About spot and process colors',
              'entidade': 'Adobe',
              'url': 'https://helpx.adobe.com/in/creative-cloud/apps/colors/spot-and-process-colors.html',
              'ambito': 'Cores diretas, CMYK, gamas e influência do suporte; não promete equivalência entre '
                        'processos.',
              'data_consulta': '2026-10-12'},
 'guiaprova': {'titulo': 'Proofing colors',
               'entidade': 'Adobe',
               'url': 'https://helpx.adobe.com/photoshop/using/proofing-colors.html',
               'ambito': 'Prova de ecrã e condições de visualização; não estabelece comportamento físico de '
                         'uma personalização.',
               'data_consulta': '2026-10-12'},
 'guiasuperficie': {'titulo': 'Features of Inks — teste no objeto real',
                    'entidade': 'Roland DG',
                    'url': 'https://downloadcenter.rolanddg.com/contents/manuals/BD-8_USE_EN/fxw1677454678109.html',
                    'ambito': 'Tratamentos de superfície e avaliação de aderência no sistema documentado; '
                              'não generalizar a outros equipamentos ou tintas.',
                    'data_consulta': '2026-10-12'},
 'guiabordado': {'titulo': 'FAQ — preparação e problemas de bordado',
                 'entidade': 'Madeira',
                 'url': 'https://www.madeira.com/en-in/service/support/faq',
                 'ambito': 'Desenho, estabilização, fixação e fatores de franzido; sem diagnóstico '
                           'automático de uma peça.',
                 'data_consulta': '2026-10-12'},
 'guiaserigrafia': {'titulo': 'A Guide to Screen Printing T-Shirts',
                    'entidade': 'ScreenPrinting.com',
                    'url': 'https://www.screenprinting.com/blogs/news/a-how-to-for-screen-printing-t-shirts',
                    'ambito': 'Registo e cura em serigrafia têxtil; as verificações descritas não são '
                              'universais para outros suportes.',
                    'data_consulta': '2026-10-12'},
 'guiaevento': {'titulo': 'Put crowd controls in place',
                'entidade': 'Health and Safety Executive',
                'url': 'https://www.hse.gov.uk/event-safety/crowd-management-controls.htm',
                'ambito': 'Chegada, circulação e saída de participantes; a seleção e distribuição de brindes '
                          'são recomendações editoriais, não um plano de segurança do evento.',
                'data_consulta': '2026-10-12'},
 'guiatampao': {'titulo': 'Pad Printing 101',
                'entidade': 'Inkcups',
                'url': 'https://www.inkcups.com/pad-printing-guide/',
                'ambito': 'Mecanismo de transferência por tampão e papel da geometria; não confirma '
                          'compatibilidade de um artigo.',
                'data_consulta': '2026-10-12'}}

FONTES_GUIAS = {k: (f['entidade'] + ' — ' + f['titulo'], f['url']) for k, f in FONTES_GUIAS_META.items()}

GUIAS = [{'id': 'como-escolher-brindes-para-um-evento',
  'titulo': 'Como escolher brindes para um evento',
  'resumo': 'Ligue a escolha ao público, ao momento de entrega e ao uso depois do evento. Planeie também a '
            'distribuição.',
  'tema': 'Escolher',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('Antes: defina uma função para a oferta',
               'Escreva uma frase que explique a utilidade: transportar materiais, tomar notas durante uma '
               'sessão ou recordar uma participação. Distinguir estas funções ajuda a selecionar artigos sem '
               'depender apenas da aparência.'),
              ('1. Preparação: conheça destinatários e transporte',
               'Considere quem recebe, como chega e o que já transporta. Um artigo volumoso pode exigir '
               'outro modo de entrega. Se houver vários públicos, defina variantes justificadas e uma forma '
               'simples de as distribuir. Confirme adequação etária e requisitos de utilização quando '
               'relevantes.'),
              ('2. Preparação: experimente o conjunto real',
               'Reúna o conteúdo que pretende entregar e teste dimensões úteis, volume, fecho e forma de '
               'transporte. Observe se o conjunto cabe e se é confortável de levar. Não infira a carga '
               'admissível pela gramagem ou pelas dimensões exteriores: confirme esse requisito quando for '
               'essencial. Liste os componentes previstos e quem prepara cada etapa, sem presumir montagem '
               'ou embalagem incluídas.'),
              ('3. Entrega: organize variantes e distribuição',
               'Registe destinatários, quantidades por variante, identificação das caixas, local de '
               'distribuição e momento necessário de receção. Observe o percurso de chegada, circulação e '
               'saída descrito no planeamento de eventos da HSE; pense onde a entrega se encaixa nesse '
               'percurso. [guiaevento] Defina como localizar e entregar cada variante, incluindo uma '
               'alternativa para quem não recebe no momento previsto. Confirme as condições necessárias, sem '
               'presumir serviços ou um prazo padrão.'),
              ('4. Depois: pense no uso e na mensagem',
               'Decida se a data e o nome do evento devem dominar o desenho ou se uma mensagem mais '
               'duradoura serve melhor o uso posterior. Observe a marca na posição real de utilização. Não '
               'escolha uma dimensão de impressão antes de confirmar costuras, acessos e área disponível.')],
  'problemas': [('Escolher o saco sem experimentar o que vai levar',
                 'Valide o conjunto com os materiais reais e o transporte previsto.'),
                ('Aprovar o artigo e esquecer a distribuição',
                 'Defina responsáveis, variantes e condições de entrega antes de fechar o pedido.')],
  'confirmar': ['Função e destinatários definidos.',
                'Conteúdo, transporte e utilização avaliados.',
                'Quantidades e variantes organizadas.',
                'Receção, identificação das variantes e distribuição definidas.'],
  'relacionados': ['como-escolher-o-material', 'como-escolher-a-tecnica', 'como-avaliar-uma-maquete'],
  'fontes': ['guiaevento'],
  'esquema_guia': [('Antes', 'Escolha e preparação'),
                   ('Durante', 'Entrega e utilização'),
                   ('Depois', 'Utilidade que permanece')],
  'ancoras': [],
  'tags': 'Como escolher brindes para um evento Escolher checklist lista de verificação',
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Comece pela função para os destinatários e pelo percurso de entrega. Teste transporte e '
                    'distribuição, e escolha uma mensagem que continue útil no contexto de utilização '
                    'posterior.',
  'perguntas_frequentes': [{'pergunta': 'Como organizar vários destinatários sem complicar a entrega?',
                            'resposta': 'Use variantes justificadas, identifique-as de forma clara e teste o '
                                        'percurso de distribuição com o conjunto previsto.'},
                           {'pergunta': 'A data do evento deve aparecer em todos os artigos?',
                            'resposta': 'É uma decisão editorial. Compare o valor de recordar a ocasião com '
                                        'a utilidade e a leitura da mensagem depois do evento.'}],
  'casos': [],
  'links_contexto': [{'titulo': 'Conhecer os materiais', 'url': 'materiais/index.html'},
                     {'titulo': 'Serigrafia', 'url': 'tecnicas/serigrafia.html'}]},
 {'id': 'como-escolher-o-material',
  'titulo': 'Como escolher o material de um brinde',
  'resumo': 'Compare utilização, composição e acabamento. O nome do material não resolve sozinho a escolha '
            'da personalização.',
  'tema': 'Escolher',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('Comece pela utilização, não pela aparência',
               'Descreva o contacto, a limpeza, o transporte e a exposição previstos. Separe os requisitos '
               'essenciais das preferências de toque, peso ou aspeto. Um material adequado a um uso pode '
               'exigir cuidados diferentes noutro contexto. Não atribua resistência ou compatibilidade a uma '
               'família inteira de materiais.'),
              ('1. Identifique a peça completa',
               'Peça a composição do corpo e dos componentes que interessam à aplicação. Distinga material '
               'de base, pintura, verniz e outros revestimentos. Numa peça com várias superfícies, indique '
               'exatamente onde quer a marca. O nome comercial ou a aparência de madeira não substituem a '
               'ficha do artigo. A documentação Roland DG alerta que tratamentos de superfície podem não ser '
               'identificáveis pela aparência, recomendando uma prova no objeto concreto. [guiasuperficie]'),
              ('2. Compare uso, construção e cuidados',
               'Compare artigos que cumpram a mesma função e registe quais as diferenças relevantes: forma, '
               'peso completo, espessura, componentes e acesso para limpeza. Uma medida igual não demonstra '
               'construção ou desempenho equivalentes. Se resistência, contacto com líquidos ou exposição '
               'forem decisivos, peça documentação e instruções do artigo, incluindo o acabamento '
               'personalizado.'),
              ('3. Avalie superfície e processo em conjunto',
               'Assinale a zona acessível e a camada exterior que recebe a marca. A superfície pode ser '
               'diferente do material de base. Confirme o resultado pretendido e uma prova nessa combinação. '
               'Uma indicação de preparação para um processo aplica-se ao artigo e ao acabamento '
               'documentados; não se estende automaticamente a toda a família de materiais. '
               '[guiasuperficie]'),
              ('4. Peça fundamento para as alegações',
               'Se uma propriedade reciclada ou uma alegação ambiental pesar na decisão, peça identificação '
               'do componente, âmbito e documentação correspondente. A palavra «reciclado» não demonstra, '
               'por si só, o impacto global do artigo. Compare também a utilidade prevista e as instruções '
               'de conservação, sem inventar vantagens ambientais.')],
  'problemas': [('Confundir o revestimento com o material de base',
                 'Registe ambos e confirme em qual deles ficará a marca.'),
                ('Escolher por uma propriedade isolada',
                 'Compare a peça completa, o uso e os cuidados, não apenas capacidade ou composição.')],
  'confirmar': ['Composição e revestimento identificados.',
                'Zona de personalização e acabamento definidos.',
                'Cuidados e resistência necessários confirmados.',
                'Alegações relevantes sustentadas por documentação.'],
  'relacionados': ['como-escolher-a-tecnica',
                   'pantone-cmyk-e-cor-final',
                   'problemas-comuns-na-personalizacao'],
  'fontes': ['guiasuperficie'],
  'esquema_guia': [('Material', 'De que é feito'),
                   ('Superfície', 'Onde se aplica a marca'),
                   ('Uso', 'O que terá de suportar')],
  'ancoras': [],
  'tags': 'Como escolher o material de um brinde Escolher checklist lista de verificação',
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Escolha pelo uso previsto e identifique separadamente material de base, revestimento e '
                    'acabamento. Compare a peça completa e confirme os cuidados e a superfície a '
                    'personalizar.',
  'perguntas_frequentes': [{'pergunta': 'A aparência permite identificar a composição?',
                            'resposta': 'Não é suficiente. Peça a identificação do material, dos '
                                        'revestimentos e dos componentes relevantes.'},
                           {'pergunta': 'Uma alegação de material reciclado resolve a escolha?',
                            'resposta': 'Não. Confirme o componente, o âmbito e a documentação da alegação, '
                                        'juntamente com uso e cuidados. Este guia não classifica o impacto '
                                        'ambiental de artigos.'}],
  'casos': [],
  'links_contexto': [{'titulo': 'Conhecer os materiais', 'url': 'materiais/index.html'},
                     {'titulo': 'Gravação a laser', 'url': 'tecnicas/gravacao-a-laser.html'},
                     {'titulo': 'Impressão digital UV', 'url': 'tecnicas/impressao-uv.html'}]},
 {'id': 'como-escolher-a-tecnica',
  'titulo': 'Como escolher a técnica',
  'resumo': 'Relacione o efeito pretendido com a superfície, o desenho, a quantidade e o uso do artigo.',
  'tema': 'Escolher',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('1. Defina o resultado e a utilização',
               'Indique se pretende uma imagem a cores, uma marca sem tinta, relevo ou outro efeito. '
               'Descreva contacto, limpeza e utilização esperados. Separe preferências visuais de requisitos '
               'que precisam de documentação ou ensaio; uma simulação não confirma resistência.'),
              ('2. Identifique a superfície e a área útil',
               'Registe material de base, pintura, verniz e outros revestimentos. Assinale a face, '
               'curvatura, acessos e componentes próximos da marca. A Roland DG recomenda ensaiar a '
               'aderência no objeto real porque o tratamento da superfície nem sempre é identificável '
               'visualmente. Esta recomendação pertence ao sistema documentado e não certifica outros '
               'processos. [guiasuperficie]'),
              ('3. Observe a arte à escala final',
               'Indique cores, fotografias, degradês, linhas, espaços e texto mais pequeno. Reveja as '
               'medidas no suporte antes de escolher o processo. Para pormenores que precisem de adaptação, '
               'defina qual a versão que será avaliada; não altere proporções ou elementos da marca sem '
               'validar a alteração.'),
              ('4. Compare possibilidades e condições',
               'Consulte os guias das técnicas para conhecer os seus mecanismos e limites. A tampografia '
               'transfere a imagem através de um tampão; geometria, tinta e superfície precisam de avaliação '
               'conjunta. [guiatampao] No bordado, desenho, tecido e estabilização influenciam o resultado. '
               '[guiabordado] Estes princípios não atribuem compatibilidade a uma família inteira de '
               'artigos.'),
              ('5. Organize quantidade e variantes',
               'Indique número de peças, tamanhos ou cores do suporte e quantas versões da arte existem. '
               'Esclareça se a personalização muda entre peças. Peça avaliação dessa combinação: não escolha '
               'uma técnica por um limiar universal de quantidade nem presuma preparação ou condições iguais '
               'entre variantes.'),
              ('6. Confirme com uma prova relevante',
               'Identifique o que a prova deverá esclarecer: leitura, posição, cor, toque ou comportamento '
               'em uso. Escolha uma amostra ou verificação adequada ao requisito, com critérios explícitos. '
               'Conserve a versão da arte, a identificação do suporte e as condições avaliadas antes de '
               'repetir a aplicação.')],
  'problemas': [('Escolher pela fotografia de outro trabalho',
                 'Use a fotografia apenas como referência visual e peça avaliação da combinação de artigo, '
                 'arte e processo.'),
                ('Tomar o material como garantia de compatibilidade',
                 'Identifique a camada exterior e confirme a área, o acesso e a prova relevante.'),
                ('Deixar variantes para depois da escolha',
                 'Inclua alterações de suporte, cor, tamanho e arte na informação a avaliar.')],
  'confirmar': ['Resultado visual e requisitos de uso separados.',
                'Superfície, área e acessos identificados.',
                'Arte à escala final e variantes reunidas.',
                'Quantidade, prova e critério de aceitação definidos.'],
  'relacionados': ['como-escolher-o-material', 'como-preparar-um-logotipo', 'como-avaliar-uma-maquete'],
  'fontes': ['guiasuperficie', 'guiatampao', 'guiabordado'],
  'esquema_guia': [('Resultado', 'Qual o efeito e a utilização?'),
                   ('Combinação', 'Qual a superfície, arte e quantidade?'),
                   ('Prova', 'O que precisa de ser confirmado?')],
  'ancoras': [],
  'tags': 'técnica personalização efeito superfície quantidade variantes prova Escolher checklist lista de '
          'verificação',
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Escolha a técnica depois de relacionar o efeito desejado com a superfície real, a arte '
                    'à escala final, as variantes e o uso. A escolha só fica confirmada para a combinação '
                    'que foi avaliada.',
  'perguntas_frequentes': [{'pergunta': 'Posso repetir a técnica quando muda apenas a cor do suporte?',
                            'resposta': 'Reveja os pontos afetados: contraste, cobertura e acabamento podem '
                                        'ser diferentes. A avaliação anterior deve identificar as variantes '
                                        'abrangidas.'},
                           {'pergunta': 'A quantidade decide por si só a técnica?',
                            'resposta': 'Não. Inclua também resultado, superfície, desenho, variantes e '
                                        'condições do processo; não existe aqui um limiar universal de '
                                        'escolha.'}],
  'casos': [],
  'links_contexto': [{'titulo': 'Conhecer os materiais', 'url': 'materiais/index.html'},
                     {'titulo': 'Tampografia', 'url': 'tecnicas/tampografia.html'},
                     {'titulo': 'Gravação a laser', 'url': 'tecnicas/gravacao-a-laser.html'},
                     {'titulo': 'Bordado', 'url': 'tecnicas/bordado.html'},
                     {'titulo': 'Impressão digital UV', 'url': 'tecnicas/impressao-uv.html'}]},
 {'id': 'como-preparar-um-logotipo',
  'titulo': 'Como preparar um logótipo para personalização',
  'resumo': 'Do ficheiro original à arte aprovada: prepare o logótipo para o artigo e a dimensão escolhidos.',
  'tema': 'Preparar ficheiros e cor',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('Comece pelo original',
               'Reúna o ficheiro da identidade visual, a versão correta do logótipo e as referências de cor. '
               'Evite partir de uma captura de ecrã ou de uma imagem copiada de uma assinatura de email. Se '
               'só tiver essa versão, envie-a para avaliação e explique a limitação antes de aprovar '
               'qualquer reconstrução.'),
              ('1. Distinga vetor e imagem',
               'Um vetor descreve formas; uma imagem raster é composta por píxeis. O vetor adapta-se à '
               'escala sem a mesma dependência da resolução. [adobevetor] A extensão não basta: um PDF pode '
               'conter apenas uma imagem. Mudar o nome de JPG para PDF não reconstrói o desenho. Peça '
               'inspeção do conteúdo do ficheiro.'),
              ('2. Verifique a arte à dimensão final',
               'Indique o artigo, a face e as dimensões pretendidas. Observe letras pequenas, linhas e '
               'espaços vazios à escala final. Um desenho legível numa área larga pode deixar de o ser numa '
               'área estreita. Não confunda as dimensões totais do artigo com a área utilizável: peça a '
               'identificação desta área antes de adaptar a arte.'),
              ('3. Adapte sem alterar a marca por acidente',
               'Se os detalhes não forem viáveis, proponha uma versão simplificada ou outra posição. Não '
               'elimine o slogan nem altere proporções sem aprovação. Para bordado, é necessária uma '
               'preparação própria dos pontos e estabilização do suporte. [guiabordado] Para impressão, '
               'podem ser necessárias separações de cor. Confirme quem faz essa adaptação e qual a prova a '
               'rever.'),
              ('4. Entregue um conjunto inequívoco',
               'Envie o original editável disponível, uma pré-visualização e uma nota com versão, dimensões, '
               'posição e cores. Pergunte se é necessário incorporar imagens ligadas ou converter texto em '
               'contornos, conservando uma cópia editável. Formatos aceites, resolução e detalhe mínimo '
               'dependem do processo: não aplique um valor universal de DPI a todos os trabalhos.')],
  'problemas': [('Enviar várias versões sem identificar a final',
                 'Nomeie a versão aprovada e retire as alternativas do conjunto destinado à produção.'),
                ('Aumentar uma imagem pequena para a tornar nítida',
                 'Peça o original ou uma reconstrução validada; aumentar as dimensões não recupera o detalhe '
                 'que falta.')],
  'confirmar': ['Artigo, face e dimensão final identificados.',
                'Versão e grafia aprovadas.',
                'Formato e tratamento de letras/imagens confirmados.',
                'Simplificações e cores aprovadas antes da produção.'],
  'relacionados': ['pantone-cmyk-e-cor-final', 'como-avaliar-uma-maquete'],
  'fontes': ['adobevetor', 'guiabordado'],
  'esquema_guia': [('Original', 'Identificar a versão'),
                   ('Escala final', 'Avaliar o pormenor'),
                   ('Prova', 'Aprovar a adaptação')],
  'ancoras': [],
  'tags': 'Como preparar um logótipo para personalização Preparar ficheiros e cor checklist lista de '
          'verificação',
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Reúna a versão correta da marca, confirme o conteúdo do ficheiro e avalie a arte à '
                    'dimensão de aplicação. Entregue uma versão identificada com medidas, posição e cores, '
                    'sujeita às condições do processo.',
  'perguntas_frequentes': [{'pergunta': 'Um PDF é sempre vetorial?',
                            'resposta': 'Não. Pode conter vetor, imagem raster ou ambos. Inspecione o '
                                        'conteúdo; a extensão não basta. [adobevetor]'},
                           {'pergunta': 'Existe um valor de resolução adequado a todos os processos?',
                            'resposta': 'Não aplique um número universal. Relacione conteúdo e dimensão '
                                        'final e confirme os requisitos do processo; preserve o original '
                                        'disponível.'}],
  'casos': [],
  'links_contexto': [{'titulo': 'Tampografia', 'url': 'tecnicas/tampografia.html'},
                     {'titulo': 'Serigrafia', 'url': 'tecnicas/serigrafia.html'},
                     {'titulo': 'Bordado', 'url': 'tecnicas/bordado.html'}]},
 {'id': 'pantone-cmyk-e-cor-final',
  'titulo': 'Pantone, CMYK e a cor final do brinde',
  'resumo': 'Perceba o que uma referência de cor define e o que só uma prova no artigo permite avaliar.',
  'tema': 'Preparar ficheiros e cor',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('Defina o que precisa de comparar',
               'Use o ecrã para discutir o desenho e identifique o que é prioritário: referência de cor, '
               'contraste ou consistência entre superfícies. Uma prova de ecrã simula a reprodução, com '
               'limitações do monitor e das condições de observação. Não substitui a avaliação física quando '
               'esta for decisiva. [guiaprova]'),
              ('1. Separe referência e método de reprodução',
               'Uma referência Pantone identifica uma cor num sistema de referência; não determina, por si '
               'só, a técnica. Uma cor direta usa uma tinta preparada, enquanto CMYK combina ciano, magenta, '
               'amarelo e preto. As cores diretas podem estar fora da gama reproduzível por CMYK. [adobecor] '
               'Pergunte como a referência será interpretada no processo proposto.'),
              ('2. Identifique suporte e configuração',
               'A aparência final depende também do suporte e da tinta, como explica a Adobe para as cores '
               'diretas. [adobecor] Identifique cor de fundo, textura, pintura e revestimento. Se forem '
               'propostas bases brancas ou acabamentos adicionais, confirme se fazem parte da configuração '
               'avaliada. Não estenda a aprovação a outra superfície sem rever as condições alteradas.'),
              ('3. Compare uma prova relevante',
               'Forneça a referência completa disponível e combine uma prova no suporte escolhido quando a '
               'cor for decisiva. Compare as amostras em condições de luz consistentes e registe qual serve '
               'de referência. Defina o critério de aceitação para cada suporte; não presuma uma tolerância '
               'numérica ou igualdade entre técnicas.'),
              ('4. Aprove cada variante necessária',
               'Num conjunto com caneta e saco, confirme separadamente a aparência em cada superfície. A '
               'coerência visual do conjunto pode exigir ajustes próprios. Uma alteração de tinta, artigo ou '
               'acabamento pode justificar nova avaliação, mesmo que o ficheiro seja o mesmo. Guarde a '
               'identificação da prova e a versão aprovada.')],
  'problemas': [('Tomar uma fotografia como amostra de cor',
                 'Use a fotografia para discutir composição; para avaliar a cor final, recorra à referência '
                 'física e às condições de comparação acordadas.'),
                ('Converter uma referência para CMYK e prometer igualdade',
                 'Peça avaliação da reprodução e aprove o resultado no suporte.')],
  'confirmar': ['Referência de cor e variante do artigo registadas.',
                'Técnica e configuração de tinta confirmadas.',
                'Prova e condições de comparação acordadas.',
                'Critério de aceitação definido para cada suporte.'],
  'relacionados': ['como-preparar-um-logotipo',
                   'como-avaliar-uma-maquete',
                   'problemas-comuns-na-personalizacao'],
  'fontes': ['adobecor', 'guiaprova'],
  'esquema_guia': [('Referência', 'A intenção de cor'),
                   ('Processo', 'Como a cor é reproduzida'),
                   ('Suporte', 'Onde a cor é vista')],
  'ancoras': [],
  'tags': 'Pantone, CMYK e a cor final do brinde Preparar ficheiros e cor checklist lista de verificação',
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Use Pantone como referência de cor e CMYK como método de reprodução, sem prometer '
                    'equivalência exata. Quando a cor final for decisiva, avalie uma prova relevante no '
                    'suporte escolhido.',
  'perguntas_frequentes': [{'pergunta': 'Converter uma referência para CMYK garante igualdade?',
                            'resposta': 'Não. As gamas de reprodução diferem e a conversão depende das '
                                        'condições do documento e do processo. [adobecor]'},
                           {'pergunta': 'A mesma aprovação de cor serve para vários suportes?',
                            'resposta': 'Identifique quais foram avaliados. Se muda superfície, fundo, tinta '
                                        'ou acabamento, reveja a necessidade de uma nova prova.'}],
  'casos': [],
  'links_contexto': [{'titulo': 'Impressão digital UV', 'url': 'tecnicas/impressao-uv.html'},
                     {'titulo': 'Serigrafia', 'url': 'tecnicas/serigrafia.html'},
                     {'titulo': 'Tampografia', 'url': 'tecnicas/tampografia.html'}]},
 {'id': 'como-avaliar-uma-maquete',
  'titulo': 'Como avaliar uma maquete antes da produção',
  'resumo': 'Reveja versão, texto, posição e escala. Distinga o que a maquete confirma do que exige uma '
            'amostra.',
  'tema': 'Rever antes de produzir',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('Identifique o alcance da maquete',
               'A maquete representa a composição proposta: texto, posicionamento e proporções. Comece por '
               'identificar artigo, variante e versão da arte. Se a representação for genérica, confirme as '
               'medidas que a relacionam com o artigo escolhido. Para cor, uma simulação depende das '
               'condições de visualização; para aderência, é necessário avaliar o suporte real. [guiaprova] '
               '[guiasuperficie]'),
              ('1. Confira os dados, não apenas o aspeto',
               'Leia nomes, contactos, datas e acentos sem depender da memória. Compare com o texto de '
               'origem e confirme se todos os elementos pertencem à versão final. Num trabalho com nomes '
               'individuais, valide também a lista e a correspondência de cada nome ao artigo; uma maquete '
               'geral não valida todas as variantes.'),
              ('2. Localize a marca com referências claras',
               'Confirme face, orientação, distância a elementos da peça e dimensão. Uma indicação como '
               '«centrado» pode referir-se ao artigo inteiro ou apenas à zona disponível. Peça que a área '
               'aprovada fique distinguida de costuras, clips, tampas e outras zonas que condicionam a '
               'aplicação. Não deduza medidas pelo tamanho da imagem no ecrã.'),
              ('3. Separe composição e resultado físico',
               'Reveja a posição numa representação com medidas explícitas, quando aplicável. Para cor, '
               'cobertura, relevo ou toque decisivos, defina a amostra necessária. Numa peça com componentes '
               'distintos, assinale a face e o componente a que a maquete corresponde. Uma imagem do '
               'conjunto não esclarece, sozinha, qual a superfície que será personalizada.'),
              ('4. Feche a revisão por escrito',
               'Concentre as correções numa lista e peça uma nova versão que as incorpore. Registe o '
               'identificador aprovado, os artigos e variantes abrangidos e as condições ainda pendentes. '
               'Uma resposta como «parece bem» pode deixar dúvidas sobre o alcance da aprovação.')],
  'problemas': [('Aprovar a imagem anterior após uma correção',
                 'Confira o número ou nome da versão e compare os pontos alterados.'),
                ('Confundir simulação com prova de resistência',
                 'Acorde um ensaio adequado ao uso antes de validar esse requisito.')],
  'confirmar': ['Artigo, variante e componentes certos.',
                'Texto, nomes e versão final conferidos.',
                'Posição, orientação e medidas explícitas.',
                'Âmbito da aprovação e amostras pendentes registados.'],
  'relacionados': ['como-preparar-um-logotipo',
                   'pantone-cmyk-e-cor-final',
                   'problemas-comuns-na-personalizacao'],
  'fontes': ['guiaprova', 'guiasuperficie'],
  'esquema_guia': [('Conteúdo', 'O que vai ser reproduzido'),
                   ('Composição', 'Onde e com que dimensão'),
                   ('Amostra', 'Como fica no artigo')],
  'ancoras': [],
  'tags': 'Como avaliar uma maquete antes da produção Rever antes de produzir checklist lista de verificação',
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Confirme texto, versão, face, orientação e medidas na maquete. Separe essa revisão da '
                    'avaliação física de cor, toque, aderência ou comportamento em uso.',
  'perguntas_frequentes': [{'pergunta': 'Uma maquete confirma resistência à lavagem?',
                            'resposta': 'Não. A simulação revê composição; esse requisito exige documentação '
                                        'ou verificação adequada à combinação real.'},
                           {'pergunta': 'O que faço depois de pedir uma correção?',
                            'resposta': 'Reveja uma nova versão identificada e confirme os pontos alterados. '
                                        'A aprovação deve referir-se a essa versão e às variantes '
                                        'abrangidas.'}],
  'casos': [],
  'links_contexto': [{'titulo': 'Conhecer os materiais', 'url': 'materiais/index.html'},
                     {'titulo': 'Comparar técnicas', 'url': 'tecnicas/index.html'}]},
 {'id': 'problemas-comuns-na-personalizacao',
  'titulo': 'Problemas comuns na personalização e como os prevenir',
  'resumo': 'Identifique o sinal, reúna evidência e escolha a verificação adequada antes de repetir a '
            'produção.',
  'tema': 'Rever antes de produzir',
  'sec': 'guias',
  'tipo': 'guia',
  'seccoes': [('Descreva o problema antes de procurar a causa',
               'Registe referência, variante, versão da arte, técnica e momento em que o problema apareceu. '
               'Fotografe o conjunto e o pormenor em condições comparáveis. Guarde uma peça afetada e a '
               'referência aprovada. A mesma aparência pode resultar de causas distintas; este guia orienta '
               'perguntas, não substitui o diagnóstico da produção.'),
              ('5. Feche o ciclo de prevenção',
               'Registe o que foi observado, a verificação realizada e a alteração aprovada. Peça uma prova '
               'que avalie o problema concreto e conserve-a como referência. Se o artigo, o revestimento ou '
               'a arte mudar, reveja os pontos afetados. Evite repetir a produção com base apenas na '
               'hipótese de que a causa foi encontrada.')],
  'problemas': [('Atribuir uma falha a uma causa única pela fotografia',
                 'Junte contexto e uma amostra; peça diagnóstico do processo.'),
                ('Repetir sem prova da correção',
                 'Defina o critério de aceitação e confirme-o numa nova avaliação.')],
  'confirmar': ['Sinal, momento e artigos afetados registados.',
                'Prova aprovada e amostra disponíveis.',
                'Causa avaliada pela produção.',
                'Correção e verificação acordadas antes da repetição.'],
  'relacionados': ['como-escolher-a-tecnica', 'pantone-cmyk-e-cor-final', 'como-avaliar-uma-maquete'],
  'fontes': ['guiaserigrafia', 'adobecor', 'guiabordado'],
  'esquema_guia': [('Observar', 'Descrever o sinal'),
                   ('Verificar', 'Investigar com contexto'),
                   ('Validar', 'Confirmar a correção')],
  'ancoras': [],
  'tags': 'Problemas comuns na personalização e como os prevenir Rever antes de produzir checklist lista de '
          'verificação',
  'ids_seccoes': ['parte-0', 'parte-5'],
  'casos': [{'id': 'parte-1',
             'titulo': 'Letras fechadas ou detalhes pouco legíveis',
             'sinal': 'Os espaços entre letras ou linhas desaparecem, ou o texto perde leitura na dimensão '
                      'de utilização.',
             'verificar': 'Compare o ficheiro e a aplicação à escala final. Distinga um desenho já pouco '
                          'legível de um pormenor perdido na reprodução. Peça avaliação da arte para o '
                          'processo escolhido antes de simplificar ou alterar a posição.',
             'evidencia': 'Ficheiro final, medidas da marca, maquete e fotografia do conjunto e do pormenor, '
                          'acompanhadas de uma peça afetada quando disponível.'},
            {'id': 'parte-2',
             'titulo': 'Cores ou contornos desalinhados',
             'sinal': 'Os contornos de várias cores não coincidem, ou a marca inteira aparece fora da '
                      'posição prevista.',
             'verificar': 'Distinga desalinhamento entre cores de deslocamento da composição inteira. Em '
                          'serigrafia, a posição das telas e da peça faz parte do registo. [guiaserigrafia] '
                          'Compare com a posição indicada na maquete; não atribua a causa apenas pela '
                          'fotografia.',
             'evidencia': 'Representação com medidas, versão aprovada e imagens comparáveis de várias peças, '
                          'indicando se o desvio se repete na mesma direção.'},
            {'id': 'parte-3',
             'titulo': 'Tinta que se solta ou se altera em uso',
             'sinal': 'A marca apresenta perda de tinta, alteração do aspeto ou desprendimento após '
                      'utilização ou limpeza.',
             'verificar': 'Reúna os cuidados efetivamente aplicados e peça revisão de superfície, '
                          'preparação, tinta e condições do processo. A documentação de serigrafia têxtil '
                          'relaciona a cura com a conservação da impressão e descreve verificações próprias '
                          'desse processo. [guiaserigrafia] Não aplique um teste ou detergente universal aos '
                          'restantes suportes.',
             'evidencia': 'Peça afetada, instruções de cuidado, momento em que apareceu o sinal, condições '
                          'de uso e amostra de referência; combine um ensaio específico para o requisito.'},
            {'id': 'parte-4',
             'titulo': 'Cor, posição ou variante diferentes da aprovação',
             'sinal': 'A cor percebida, a face, a orientação ou o artigo recebido diferem da referência '
                      'acordada.',
             'verificar': 'Compare a mesma variante e a versão final. Para cor, use a referência e as '
                          'condições de observação acordadas, não apenas o ecrã ou uma fotografia. '
                          '[adobecor] Para posição, confira medidas e orientação; para variantes, reveja a '
                          'identificação dos ficheiros e das peças.',
             'evidencia': 'Aprovação identificada, referência física quando aplicável, lista de variantes e '
                          'medições da posição observada.'},
            {'id': 'bordado',
             'titulo': 'Tecido franzido ou bordado pouco definido',
             'sinal': 'A superfície junto ao bordado apresenta franzido, ou letras e contornos ficam pouco '
                      'definidos.',
             'verificar': 'A Madeira descreve vários fatores possíveis, incluindo estabilização, tensão, '
                          'fixação e preparação dos pontos. [guiabordado] Peça avaliação conjunta do tecido '
                          'e do desenho; o aspeto não demonstra sozinho qual o fator responsável.',
             'evidencia': 'Amostra, desenho e dimensão final, composição documentada da peça e indicação de '
                          'quando o sinal foi observado.'}],
  'data_revisao': '2026-10-12',
  'resposta_breve': 'Descreva o sinal e reúna contexto, ficheiro aprovado e uma peça afetada antes de '
                    'procurar a causa. Compare hipóteses e confirme a correção com uma verificação adequada, '
                    'em vez de diagnosticar apenas pela fotografia.',
  'perguntas_frequentes': [{'pergunta': 'Uma fotografia basta para encontrar a causa?',
                            'resposta': 'Não. Ajuda a descrever o sinal; junte contexto, condições de uso e '
                                        'uma amostra quando necessária.'},
                           {'pergunta': 'Devo repetir imediatamente depois de corrigir o ficheiro?',
                            'resposta': 'Confirme primeiro se a alteração trata o problema observado e se a '
                                        'nova prova cumpre o critério de aceitação acordado.'}],
  'links_contexto': [{'titulo': 'Serigrafia', 'url': 'tecnicas/serigrafia.html'},
                     {'titulo': 'Impressão digital UV', 'url': 'tecnicas/impressao-uv.html'},
                     {'titulo': 'Bordado', 'url': 'tecnicas/bordado.html'}]}]

GRUPOS_GUIAS = [('escolher', 'Escolher', 'Uso e destinatários primeiro; material e técnica depois.', 'Escolher'),
 ('cor',
  'Preparar ficheiros e cor',
  'Do original à dimensão final e à referência de cor.',
  'Preparar ficheiros e cor'),
 ('qualidade',
  'Rever antes de produzir',
  'Da composição proposta à verificação do resultado.',
  'Rever antes de produzir')]
