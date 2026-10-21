"""Fonte semântica pública de Produtos; HTML, pesquisa e JSON derivam destes campos.
Os critérios e contextos são orientação editorial. Os factos têm referências
explícitas; nenhuma técnica está confirmada para um artigo específico.
"""
DATA_PRODUTOS = '2026-10-12'

def fonte(titulo, entidade, url, ambito):
    # A referência continua verificável pelo URL; a apresentação pública é neutra.
    titulos_neutros = {
        'Pilot Pen Australia': 'Rollerballs — perguntas frequentes',
        'Pilot Europe': 'Esferográficas — variantes',
        'Inkcups': 'Guia de tampografia',
        'Stanley 1913': 'Cuidados de recipientes de bebida',
        'Madeira': 'Bordado — suporte e estabilização',
        'Osprey': 'Cuidados de mochilas — âmbito específico',
        'Rocketbook Help Center': 'Sistema apagável — instruções de utilização',
        'Holmen Iggesund': 'Informação técnica sobre cartão',
        'CottonWorks / Cotton Incorporated': 'Estruturas de malha',
    }
    if entidade in titulos_neutros:
        titulo, entidade = titulos_neutros[entidade], 'Documentação técnica de referência'
    return dict(titulo=titulo, entidade=entidade, url=url, data_consulta=DATA_PRODUTOS, ambito=ambito)

FONTES_PRODUTOS = {
 'prodroller': fonte('Rollerball Pens — perguntas frequentes', 'Pilot Pen Australia', 'https://pilotpen.com.au/pens/categories/rollerball', 'Tinta aquosa ou de gel em rollerballs; não estabelece desempenho de todas as canetas.'),
 'prodball': fonte('Ballpoint pens', 'Pilot Europe', 'https://www.pilotpen.eu/our-products/ballpoint-pens/', 'Variantes com tinta de base oleosa e recarga; não generalizar a todos os instrumentos.'),
 'prodpad': fonte('Pad Printing 101 — The Ultimate Guide', 'Inkcups', 'https://www.inkcups.com/pad-printing-guide/', 'Transferência com tampão e aplicações em objetos; não confirma aplicação num artigo.'),
 'prodwash': fonte('How To Clean Your Stanley 1913 Products', 'Stanley 1913', 'https://ca.stanley1913.com/blogs/how-to-guides/how-to-properly-clean-your-stanley-products', 'Cuidados dos recipientes do fabricante e consulta das instruções antes de lavar à máquina.'),
 'prodknit': fonte('Knit Basics', 'CottonWorks / Cotton Incorporated', 'https://cottonworks.com/learning-hub/knitting/knit-basics/', 'Estrutura de malha e diferenças de construção; não comprova desempenho de uma peça.'),
 'prodmass': fonte('D3776 — Standard Test Methods for Mass Per Unit Area (Weight) of Fabric', 'ASTM International', 'https://store.astm.org/d3776-07.html', 'Título e resumo público do ensaio de massa por área; não foram usados procedimentos do texto integral.'),
 'prodcare': fonte('Care Labelling Symbols', 'GINETEX', 'https://www.ginetex.net/userfiles/files/gin_bro_gb_rz_brochure_web.pdf', 'Significado das instruções de cuidado; os símbolos não são reproduzidos.'),
 'prodemb': fonte('FAQ — tecido, estabilização e bordado', 'Madeira', 'https://www.madeira.com/en-in/service/support/faq', 'Influência do suporte, estabilizador, agulha e densidade de pontos.'),
 'prodpack': fonte('How to Clean Your Osprey Backpack', 'Osprey', 'https://www.osprey.com/gb/how-to-clean-your-osprey-backpack', 'Limpeza das mochilas abrangidas pelo guia; não estender a todos os sacos.'),
 'produsb': fonte('USB Type-C Language and Packaging Guidelines', 'USB Implementers Forum', 'https://www.usb.org/sites/default/files/usb_type-c_language_product_and_packaging_guidelines_20230320.pdf', 'Distinção entre conector USB Type-C, protocolos de dados e USB Power Delivery.'),
 'prodqi': fonte('Qi Certified Products', 'Wireless Power Consortium', 'https://www.wirelesspowerconsortium.com/knowledge-base/testing-and-certification/qi-certified-products/', 'Certificação e verificação de dispositivos Qi; não atribuir certificação sem consulta do artigo específico.'),
 'prodnotes': fonte('Rocketbook Core — instruções de utilização', 'Rocketbook Help Center', 'https://rocketbookhelp.zendesk.com/hc/en-us/articles/360004098373-Rocketbook-Core', 'Sistema específico com páginas sintéticas, caneta própria e limpeza húmida; não aplicável a todos os cadernos apagáveis.'),
 'prodboard': fonte('General Technical Information About Paperboard', 'Holmen Iggesund', 'https://www.iggesund.com/insights/paperboard-know-how/general-technical-information/', 'Diferenças entre gramagem, espessura e ensaios de rigidez do cartão.'),
}

def variante(nome, descricao, comparar, contexto):
    return dict(nome=nome, descricao=descricao, comparar=comparar, contexto=contexto)

def componente(parte, materiais, guia, confirmar):
    return dict(parte=parte, materiais=materiais, guia_id=guia, confirmar=confirmar)

def zona(nome, condicao):
    return dict(nome=nome, condicao=condicao)

def tecnica(id, condicoes):
    return dict(id=id, condicoes=condicoes, estatuto='possibilidade_geral', compatibilidade_confirmada=False)

def faq(pergunta, resposta):
    return dict(pergunta=pergunta, resposta=resposta)

def guia(id, ancora, titulo, resumo, sinonimos, tipos, usos, componentes, zonas, tecnicas,
         criterios, limitacoes, cuidados, perguntas, faq, fontes, relacionados, categoria='familia'):
    return dict(id=id, slug=id, ancora=ancora, titulo=titulo, categoria=categoria, resumo=resumo,
        sinonimos=sinonimos, nomes_alternativos=sinonimos, tipos=tipos, usos_contextos=usos,
        materiais_componentes=componentes, zonas_personalizacao=zonas, tecnicas_relacionadas=tecnicas,
        criterios_escolha=criterios, limitacoes=limitacoes, cuidados=cuidados,
        perguntas_antes_de_decidir=perguntas, perguntas_frequentes=faq, fontes=fontes,
        relacionados=relacionados, data_revisao=DATA_PRODUTOS)

PRODUTOS = [
 guia('canetas-e-escrita','canetas','Canetas e escrita',
  'Compare o tipo de escrita, o mecanismo, a recarga e o espaço livre no corpo antes de escolher a marca.',
  ['esferográfica','esferografica','rollerball','caneta de gel','lapiseira','lápis','instrumentos de escrita'],
  [variante('Esferográficas','Instrumentos de ponta esférica; a documentação descreve variantes com tinta de base oleosa. Identifique o tipo de tinta na documentação. [prodball]', 'Botão, rotação ou tampa; traço, pega e recarga.', 'Anotações rápidas, receção e uso diário.'),
   variante('Rollerballs e canetas de gel','A documentação descreve rollerballs com tinta aquosa ou de gel. O nome do tipo não basta para deduzir o tempo de secagem. [prodroller]', 'Tinta, traço no papel habitual, tampa e recarga.', 'Escrita prolongada, apontamentos e oferta individual.'),
   variante('Lápis e lapiseiras','Compare um lápis que se afia com uma lapiseira que recebe minas; os consumíveis e a preparação para escrever diferem.', 'Dureza e diâmetro da mina, avanço e borracha.', 'Desenho, formação e tarefas em que apagar seja útil.')],
  ['Numa distribuição ampla, teste escrita e leitura da mensagem sem depender da embalagem.', 'Num conjunto individual, compare instrumento, recarga e estojo; confirme o que está incluído.'],
  [componente('Corpo e tampa',['plásticos'],'plasticos','Identificar polímero, pintura e revestimento.'),
   componente('Corpo, clip e ponteira',['metais'],'metais','Distinguir metal de base e acabamento; verificar cada componente.')],
  [zona('Corpo','Medir espaço livre, curvatura e orientação em relação ao clip.'),zona('Clip ou tampa','Confirmar dimensão, mobilidade e acesso.')],
  [tecnica('tampografia','A referência descreve aplicações em canetas; tinta, tampão e acabamento exigem avaliação do artigo. [prodpad]'),
   tecnica('gravacao-a-laser','Avaliar superfície e efeito numa amostra; metal pintado não equivale a metal sem revestimento.'),
   tecnica('impressao-uv','Confirmar acesso, aderência, curvatura e legibilidade à dimensão final.')],
  ['Teste o traço no papel habitual e observe falhas, manchas e conforto.', 'Acione o mecanismo e verifique se o clip interfere com a marca.', 'Compare a recarga compatível e a forma de substituição; cargas semelhantes não são necessariamente intercambiáveis.'],
  ['Não atribua comprimento de escrita, resistência da tinta ou vida útil sem documentação.', 'Uma maquete ampliada pode ocultar texto ilegível; reveja a marca à escala real.'],
  ['Siga as instruções de fecho, armazenamento e substituição de consumíveis. A referência identifica variantes recarregáveis, não toda a família. [prodball]'],
  ['Que papel e duração de escrita são habituais?','O mecanismo e a pega são confortáveis?','Qual é a recarga compatível?','A marca cabe na área medida?'],
  [faq('Uma caneta metálica pode sempre ser gravada?','Não. Metal de base, revestimento e efeito pretendido devem ser avaliados na superfície concreta.'),
   faq('O diâmetro da ponta é igual à largura do traço?','Não use os valores como equivalentes sem confirmação. Compare o traço indicado e teste no papel habitual.'),
   faq('Uma caneta recarregável aceita qualquer carga?','Não. Confirme identificação, encaixe e instruções da carga compatível.')],
  ['prodball','prodroller','prodpad'], ['como-escolher-a-tecnica','como-preparar-um-logotipo','artigos-de-escritorio']),

 guia('garrafas-copos-e-canecas','bebidas','Garrafas, copos e canecas',
  'Distinga transporte e consumo à mesa; compare formato, abertura, tampa, limpeza e zonas de personalização.',
  ['recipientes de bebida','garrafa','copo','caneca','térmico','termo','tumbler'],
  [variante('Garrafas','Compare gargalo, abertura, fecho e forma de agarrar; a presença de uma tampa não demonstra estanquidade.', 'Altura, diâmetro, capacidade e acesso para limpeza.', 'Deslocações, secretária e transporte de bebida.'),
   variante('Copos com ou sem tampa','Copo aberto, tampa com abertura e fecho para transporte respondem a necessidades diferentes.', 'Bocal, palhinha se existir, base e instruções de transporte.', 'Consumo à mesa ou em movimento, conforme o fecho documentado.'),
   variante('Canecas','A pega e o formato de consumo fazem parte da escolha; compare a posição da mensagem com ambas as mãos.', 'Pega, base, peso e acesso ao interior.', 'Bebidas à mesa e pausas no trabalho.')],
  ['Para transporte dentro de um saco, confirme fecho e estanquidade.', 'Para consumo à mesa, compare conforto de pega, estabilidade e limpeza.'],
  [componente('Corpo',['aço inoxidável','alumínio'],'metais','Confirmar construção, revestimento interior e uso previsto.'),
   componente('Tampa, bocal e acessórios',['plásticos'],'plasticos','Identificar peças desmontáveis e juntas; o corpo não descreve a tampa.'),
   componente('Corpo ou recipiente interior',['vidro','cerâmica'],'vidro-e-ceramica','Confirmar acabamento e instruções do artigo completo.')],
  [zona('Parede exterior','Medir altura útil, curvatura e mudanças de diâmetro; excluir zonas de contacto com a bebida.'),zona('Pega ou tampa','Avaliar cada componente sem dificultar abertura ou limpeza.')],
  [tecnica('gravacao-a-laser','Confirmar material, acabamento, fixação e efeito; aparência metálica não prova compatibilidade.'),
   tecnica('serigrafia','Confirmar geometria, área livre, tinta e lavagem prevista.'),
   tecnica('tecnica-sublimacao','Exige suporte e revestimento adequados; não se presume que qualquer caneca de cerâmica aceite o processo.')],
  ['Compare capacidade com dimensões e peso; verifique o encaixe no local de uso.', 'Peça instruções sobre bebidas quentes, temperatura, fecho e transporte.', 'Observe desmontagem e acesso ao bocal, juntas e palhinha.'],
  ['“Térmico” não quantifica duração de conservação da temperatura; procure ensaio e condições do artigo.', 'Não atribua estanquidade, resistência a quedas ou uso em micro-ondas pelo material.'],
  ['A referência de cuidados recomenda consultar as instruções antes de lavar à máquina e separar componentes quando essa lavagem é permitida. Isto não confirma os cuidados de outros artigos. [prodwash]', 'Confirme também os cuidados do acabamento personalizado.'],
  ['Vai ser transportado ou usado à mesa?','Que bebida e temperatura estão previstas?','Como se desmonta a tampa?','Que cuidados exigem corpo e marca?'],
  [faq('Uma tampa torna o copo estanque?','Não. Pode haver abertura para beber; confirme estanquidade e posição permitida no transporte.'),
   faq('Pode ir à máquina de lavar loiça?','Só quando as instruções do artigo e da personalização o permitirem; confirme todas as peças.'),
   faq('Parede dupla garante um resultado térmico específico?','Não atribua horas de conservação sem documentação e condições de ensaio.')],
  ['prodwash'], ['como-escolher-o-material','como-escolher-a-tecnica','sacos-e-mochilas']),

 guia('texteis','texteis','Têxteis',
  'Compare composição, estrutura, gramagem, corte, medidas e cuidados antes de definir a posição do desenho.',
  ['t-shirt','tshirt','camisola','polo','sweatshirt','casaco','vestuário','roupa','tamanhos'],
  [variante('T-shirts e polos','Compare corte, gola, mangas e superfície. Malha é uma construção com laçadas, não o nome de uma fibra. [prodknit]', 'Composição, estrutura, gramagem, transparência e medidas.', 'Eventos, equipas e uso diário.'),
   variante('Sweatshirts e casacos','Compare camadas, forro, punhos e fechos; uma face não descreve o conjunto.', 'Espessura, ajuste com outras peças e acesso à zona da marca.', 'Sobreposição e contextos com necessidades de abrigo.'),
   variante('Bonés e acessórios','Observe painéis, costuras e ajuste; o desenho deve caber numa zona acessível.', 'Forma dos painéis, ajuste e posição das costuras.', 'Identificação de equipas e uso recorrente.')],
  ['Para grupos, recolha medidas e escolha o corte antes dos tamanhos; as letras não substituem a tabela da peça.', 'Para uso repetido, considere lavagem, conforto e manutenção da marca.'],
  [componente('Tecido exterior',['algodão','poliéster','misturas de fibras'],'materiais-texteis','Separar composição, estrutura e acabamento; confirmar percentagens da variante.'),
   componente('Forro, punhos e painéis',['materiais têxteis'],'materiais-texteis','Identificar cada parte; a composição do exterior não descreve todos os acessórios.')],
  [zona('Peito, costas ou manga','Medir no tamanho escolhido; verificar bolsos, costuras e proporção nos diferentes tamanhos.'),zona('Painel de boné','Confirmar curvatura, costuras e acesso ao verso.')],
  [tecnica('serigrafia','Avaliar fibras, acabamento, cor, tinta e cura.'),
   tecnica('bordado','A referência de bordado relaciona o resultado com tecido, estabilização e densidade de pontos; confirmar desenho e suporte. [prodemb]'),
   tecnica('transfers','Escolher a modalidade após conhecer composição, acabamento, aplicação de calor e cuidados.')],
  ['Gramagem é massa por área, habitualmente expressa em g/m², e difere de espessura. O âmbito do ensaio ASTM D3776 é a massa por unidade de área do tecido. [prodmass]', 'Compare peito, comprimento e manga na tabela da peça; observe o corte numa amostra.', 'Examine costuras e remates, e o comportamento após o cuidado previsto quando este for decisivo.'],
  ['Mais gramagem não prova, por si só, conforto ou durabilidade superiores.', 'Não deduza encolhimento, resistência da cor ou proteção contra intempéries sem documentação ou ensaio.'],
  ['A GINETEX explica os tratamentos de lavagem, secagem, passagem a ferro e cuidado profissional indicados na etiqueta. Siga os cuidados da peça e da personalização. [prodcare]'],
  ['Que uso e lavagem estão previstos?','Qual é a composição de cada parte?','Que tabela de medidas corresponde ao corte?','A arte foi medida nos tamanhos relevantes?'],
  [faq('Algodão e malha são a mesma coisa?','Não. Algodão é uma fibra; malha descreve uma construção do tecido. Identifique ambos.'),
   faq('Mais gramagem significa sempre melhor peça?','Não. Compare construção, corte, conforto, acabamento e adequação ao uso.'),
   faq('O mesmo desenho serve para todos os tamanhos?','A presença visual e a área podem mudar. Reveja posição e dimensões nos tamanhos usados.')],
  ['prodknit','prodmass','prodemb','prodcare'], ['como-escolher-a-tecnica','como-avaliar-uma-maquete','sacos-e-mochilas']),

 guia('sacos-e-mochilas','sacos','Sacos e mochilas',
  'Compare abertura, construção, compartimentos, alças e área livre de personalização com o conteúdo a transportar.',
  ['saco','mochila','tote','saco de cordões','saco a tiracolo','transporte','alças','compartimentos'],
  [variante('Sacos de duas alças','Observe fundo, abertura e união das alças ao corpo; compare o interior com o conteúdo habitual.', 'Alças, profundidade, costuras e eventual fecho.', 'Eventos, compras e transporte conforme a carga documentada.'),
   variante('Sacos de cordões e a tiracolo','Fecho por cordões e alça de ombro são soluções distintas; avalie acesso e transporte com o conteúdo real.', 'Abertura, ajuste e pontos de união.', 'Atividades pontuais e acesso rápido.'),
   variante('Mochilas','Compare organização interior e ajuste em vez de escolher apenas pela dimensão exterior.', 'Compartimentos, acolchoamento, alças e fechos.', 'Deslocações diárias e transporte de equipamento.')],
  ['Para entregar documentos ou artigos, teste o encaixe do conteúdo previsto.', 'Para equipamento, compare as medidas internas úteis e a proteção documentada, não apenas a diagonal nominal.'],
  [componente('Corpo e painéis',['algodão','poliéster','tecidos e não tecidos'],'materiais-texteis','Confirmar fibra, construção, gramagem quando indicada e revestimento de cada painel.'),
   componente('Fechos, fivelas e acessórios',['plásticos'],'plasticos','Identificar peças e forma de substituição; testar funcionamento.'),
   componente('Argolas e ferragens',['metais'],'metais','Observar acabamento e fixação; não deduzir resistência da aparência.')],
  [zona('Painel frontal ou traseiro','Medir zona sem costuras e acesso ao verso; bolsos e forros podem dificultar a aplicação.'),zona('Bolso exterior','Confirmar área e fixação sem afetar o fecho.')],
  [tecnica('serigrafia','Confirmar superfície, acabamento, acesso e separação de camadas.'),
   tecnica('bordado','Avaliar agulha, estabilização e acesso; a referência de bordado identifica a influência do tecido e da densidade de pontos. [prodemb]'),
   tecnica('transfers','Verificar revestimentos, sensibilidade ao calor e área plana para a modalidade escolhida.')],
  ['Teste abertura e conforto das alças com o conteúdo esperado.', 'Observe uniões das alças, fundo, remates, forro e fechos.', 'Peça documentação ou ensaio se carga ou proteção contra água forem decisivas.'],
  ['Gramagem, volume e densidade do fio não equivalem a carga máxima.', 'Um bolso para equipamento não demonstra proteção contra quedas nem impermeabilidade.', 'Uma passagem ou cabo USB não prova que exista bateria incluída.'],
  ['A referência de cuidados desaconselha lavagem à máquina para as mochilas abrangidas pelo seu guia; não é uma regra para todos os sacos. Consulte os cuidados do artigo escolhido. [prodpack]', 'Confirme limpeza do forro, fechos e personalização e a forma de secar antes de guardar.'],
  ['O que vai ser transportado e com que medidas?','As alças e fechos funcionam com esse conteúdo?','Que carga e proteção estão documentadas?','O painel está acessível?'],
  [faq('Um saco mais pesado suporta mais carga?','Não necessariamente. Avalie construção, uniões e componentes; peça dados de carga quando necessários.'),
   faq('O tamanho exterior garante que o portátil cabe?','Não. Confirme medidas úteis do compartimento e teste o equipamento ou as suas dimensões.'),
   faq('Um saco revestido é impermeável?','Não conclua impermeabilidade do artigo completo pelo revestimento; costuras e fechos também precisam de documentação.')],
  ['prodemb','prodpack'], ['texteis','como-escolher-o-material','como-escolher-a-tecnica']),

 guia('tecnologia','tecnologia','Tecnologia',
  'Escolha pela função e pelos dispositivos envolvidos; compare ligações, componentes e superfície separadamente.',
  ['acessórios tecnológicos','eletrónica','power bank','bateria externa','carregador','USB-C','altifalante','suporte de telemóvel'],
  [variante('Cabos, carregadores e baterias externas','USB Type-C não é sinónimo de USB Power Delivery nem de uma versão de transferência de dados. Separe conector de capacidades. [produsb]', 'Entrada, saída, protocolo, cabo necessário e dispositivos suportados.', 'Carregamento ou dados conforme a função documentada.'),
   variante('Altifalantes e áudio','O nome da ligação não descreve sozinho controlos, autonomia ou experiência de audição.', 'Ligação, alimentação, controlos e emparelhamento.', 'Escuta individual ou partilha de som em ambiente adequado.'),
   variante('Suportes sem eletrónica','Podem resolver posicionamento sem carregar nem comunicar com o dispositivo.', 'Encaixe, estabilidade, ajuste e uso com capa.', 'Secretária, videochamadas e organização.')],
  ['Identifique os dispositivos e a tarefa: carregar, comunicar, ouvir ou apoiar.', 'Peça documentação e teste a combinação real se depender de uma função específica.'],
  [componente('Carcaça e botões',['plásticos'],'plasticos','Separar invólucro e eletrónica; confirmar textura, revestimento e peças móveis.'),
   componente('Invólucro ou placa exterior',['metais'],'metais','Identificar acabamento e área livre; não inferir dissipação térmica pela aparência.'),
   componente('Painel decorativo',['madeira','bambu'],'madeira-e-bambu','Avaliar o painel; a decoração não descreve os circuitos interiores.')],
  [zona('Face exterior livre','Excluir portas, botões, grelhas, informação de segurança e área de carregamento.'),zona('Painel decorativo','Confirmar acesso sem abrir ou alterar componentes eletrónicos.')],
  [tecnica('tampografia','Avaliar material da carcaça, tinta, acesso e aderência; evitar controlos e aberturas.'),
   tecnica('impressao-uv','Confirmar acabamento, aderência e fixação; uma face lisa não prova compatibilidade.'),
   tecnica('gravacao-a-laser','Avaliar superfície, acabamento e proximidade de componentes sensíveis; metal exterior não basta.')],
  ['Porta, cabo e dispositivo devem suportar a função pretendida em ambas as extremidades.', 'Para carregamento sem fios, verifique a identificação e certificação no registo público do Wireless Power Consortium; não atribua certificação por uma fotografia. [prodqi]', 'Separe autonomia documentada de capacidade nominal da bateria e registe as condições declaradas.'],
  ['Não prometa autonomia ou velocidade sem dados e condições do dispositivo concreto.', 'Não deduza potência pelo conector nem proteção contra água pela forma da carcaça.'],
  ['Siga instruções do dispositivo e alimentação; confirme limites de uso, armazenamento e limpeza.', 'Mantenha legíveis as informações técnicas e de utilização; a marca não deve tapá-las.'],
  ['Que dispositivos e funções são necessários?','Que cabo e alimentação são exigidos?','Que dados estão documentados e em que condições?','Que face está livre de controlos?'],
  [faq('USB-C garante carregamento rápido?','Não. Confirme protocolo, potência e capacidades de carregador, cabo e dispositivo. O conector não basta. [produsb]'),
   faq('Mais capacidade da bateria garante mais horas?','Não compare autonomia só pela capacidade; procure condições e resultados declarados para o uso pretendido.'),
   faq('Um suporte de telemóvel também carrega?','Só se essa função estiver documentada e for compatível com o dispositivo.')],
  ['produsb','prodqi'], ['como-escolher-a-tecnica','como-avaliar-uma-maquete','artigos-de-escritorio']),

 guia('artigos-de-escritorio','escritorio','Artigos de escritório',
  'Compare formato, páginas, encadernação, acessórios e consumíveis com a rotina de escrita e organização.',
  ['caderno','bloco de notas','agenda','pasta','organizador','secretária','papelaria','caderno apagável'],
  [variante('Cadernos, blocos e agendas','Distinga folhas destacáveis, encadernação permanente e organização por datas; confirme o período de uma agenda datada.', 'Formato útil, pauta, folhas ou páginas, abertura e encadernação.', 'Apontamentos, planeamento e formação.'),
   variante('Pastas e organizadores','Compare o conteúdo a guardar e o acesso; não deduza acessórios incluídos da apresentação.', 'Compartimentos, fecho e dimensões internas.', 'Reuniões e organização de documentos.'),
   variante('Sistemas apagáveis','A referência documenta um sistema com páginas sintéticas, caneta específica e limpeza húmida; não generalize esse método a todos os cadernos apagáveis. [prodnotes]', 'Consumível compatível, apagamento e conservação dos registos.', 'Notas temporárias com método de manutenção próprio.')],
  ['Teste o papel com o instrumento habitual e observe a leitura no verso.', 'Num conjunto de reunião, confirme acessórios e encaixe da documentação.'],
  [componente('Folhas e capa de papel ou cartão',['papel','cartão'],'papel-e-cartao','A referência distingue gramagem, espessura e rigidez como propriedades e ensaios diferentes. [prodboard]'),
   componente('Capa revestida',['pele','imitação de pele'],'pele-e-imitacao-de-pele','Identificar suporte, revestimento e acabamento.'),
   componente('Espiral, ferragens e fechos',['metais'],'metais','Verificar abertura, saliências e proximidade da marca.')],
  [zona('Capa','Medir espaço livre de elástico, espiral, fechos e acessórios; identificar a camada exterior.'),zona('Folhas ou separadores','Confirmar possibilidade e processo de impressão e montagem.')],
  [tecnica('impressao-uv','Avaliar acabamento, aderência e acesso à capa.'),
   tecnica('termogravura','Confirmar material e resposta a calor e pressão numa amostra; aparência de pele não basta.'),
   tecnica('serigrafia','Verificar tinta, revestimento, área plana e uso da capa.')],
  ['Confirme se a contagem é de folhas ou páginas e quais são utilizáveis.', 'Teste abertura e passagem de página com os acessórios.', 'Identifique canetas, recargas, folhas de reposição ou panos incluídos e a sua substituição.'],
  ['Não atribua compatibilidade de escrita ou apagamento sem instruções do sistema.', 'O material das folhas não identifica o da capa; rigidez não demonstra resistência à água.'],
  ['Limpeza húmida só se aplica a sistemas que a documentem; siga as instruções do suporte e consumíveis. [prodnotes]', 'Para notas permanentes, escolha suporte e conservação adequados à informação.'],
  ['O uso é temporário, permanente ou datado?','Qual é o formato e a contagem de folhas?','Que acessórios estão incluídos?','Qual é o acabamento exterior?'],
  [faq('Folhas e páginas são a mesma contagem?','Não. Uma folha tem duas faces; confirme se a contagem inclui faces em branco ou outros elementos.'),
   faq('Qualquer caneta serve num caderno apagável?','Não. Use o consumível indicado nas instruções do sistema.'),
   faq('Gramagem revela a espessura da capa?','Não. Mede massa por área; confirme também espessura, construção e rigidez. [prodboard]')],
  ['prodnotes','prodboard'], ['canetas-e-escrita','como-escolher-o-material','como-escolher-a-tecnica','encadernacao']),

 guia('brindes-premium','premium','Premium: seleção transversal',
  'Uma coleção editorial para comparar utilidade, acabamento, apresentação e contexto entre diferentes famílias.',
  ['brindes premium','oferta individual','coleção editorial','colecção','apresentação','conjunto de oferta'],
  [variante('Um artigo de uso frequente','Selecione em qualquer família pela rotina do destinatário; a designação editorial não comprova qualidade superior.', 'Utilidade, conforto e manutenção.', 'Reconhecimento individual e relações de longa duração.'),
   variante('Um conjunto coerente','Combine funções complementares e identifique cada componente; uma caixa não demonstra acessórios incluídos.', 'Conteúdo e reposição de consumíveis.', 'Acolhimento, reuniões e oferta com um tema definido.'),
   variante('Apresentação cuidada','Observe mensagem, acabamento e experiência de abrir e guardar.', 'Proteção, legibilidade e destino da embalagem.', 'Ocasiões em que a forma de entrega tenha significado.')],
  ['Defina destinatário, ocasião e função antes da apresentação.', 'Use critérios verificáveis numa amostra: abertura, encaixe, toque e legibilidade.'],
  [componente('Artigo principal',['materiais da família escolhida'],'como-escolher-o-material','Identificar materiais de cada parte e usar o guia da família.'),
   componente('Caixa e separadores',['papel','cartão'],'papel-e-cartao','Avaliar encaixe e proteção; a referência distingue gramagem, espessura e rigidez. [prodboard]')],
  [zona('Artigo principal','Usar áreas e condições do guia da família.'),zona('Embalagem e cartão','Confirmar área, contraste e relação com a marca; manter instruções legíveis.')],
  [tecnica('gravacao-a-laser','Considerar apenas para superfície identificada e avaliada.'),tecnica('termogravura','Avaliar suporte e efeito; não é um indicador automático de qualidade.'),tecnica('impressao-uv','Confirmar acesso e aderência em cada componente.')],
  ['Compare utilidade e facilidade de manutenção para o destinatário.', 'Observe consistência visual, remates, encaixe e leitura numa amostra.', 'Identifique componentes, instruções e consumíveis.'],
  ['“Premium” é uma designação editorial transversal, não uma família técnica nem garantia de qualidade, durabilidade ou impacto ambiental.', 'Não atribua vantagem ambiental por aparência ou material sem documentação com âmbito claro.'],
  ['Conserve as instruções de cada componente e avalie proteção após abrir.', 'O estatuto editorial não altera os cuidados da respetiva família.'],
  ['Que função terá para o destinatário?','Que componentes estão incluídos?','Que acabamento consigo avaliar?','A embalagem protege sem dificultar o uso?'],
  [faq('Premium significa melhor qualidade?','Não. Compare critérios concretos e documentados; a designação não substitui a avaliação.'),
   faq('Uma embalagem transforma qualquer artigo em premium?','É um critério de apresentação a comparar com utilidade, acabamento e contexto.'),
   faq('A coleção tem técnicas ou materiais exclusivos?','Não. Abrange várias famílias; cada componente mantém as suas condições de personalização.')],
  ['prodboard'], ['canetas-e-escrita','garrafas-copos-e-canecas','texteis','sacos-e-mochilas','tecnologia','artigos-de-escritorio','como-avaliar-uma-maquete'], categoria='colecao_editorial'),
]

from conteudos.produtos_complementos import completar
completar(PRODUTOS, FONTES_PRODUTOS, guia=guia, variante=variante, componente=componente,
          zona=zona, tecnica=tecnica, faq=faq)


def textos_publicos(valor):
    if isinstance(valor,str):
        yield valor
    elif isinstance(valor,list):
        for item in valor: yield from textos_publicos(item)
    elif isinstance(valor,dict):
        for chave,item in valor.items():
            if chave not in ('id','slug','guia_id','estatuto','data_revisao'):
                yield from textos_publicos(item)

def artigo_legado(g):
    return dict(id=g['id'],sec='produtos',tipo='produto',titulo=g['titulo'],resumo=g['resumo'],
        seccoes=[('Tipos e variantes',' '.join(t['descricao'] for t in g['tipos']))],problemas=[],
        fontes=list(g['fontes']),relacionados=list(g['relacionados']),ancoras=[],
        tags=' '.join(g['sinonimos']),data_revisao=g['data_revisao'])

NOVOS_ARTIGOS = [artigo_legado(g) for g in PRODUTOS]

def exportacao_publica():
    import copy
    conteudos=copy.deepcopy(PRODUTOS)
    for g in conteudos:
        g['url']='produtos/'+g['slug']+'.html'
        g['fontes']=[dict(id=k,**FONTES_PRODUTOS[k]) for k in g['fontes']]
    return dict(schema_version='1.0',idioma='pt-PT',site='brindes.pt',data_revisao=max(g['data_revisao'] for g in PRODUTOS),conteudos=conteudos)
