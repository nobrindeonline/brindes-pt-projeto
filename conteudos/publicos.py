"""Seleções editoriais por público; factos e fotografias em recursos.py."""
def publico(id,titulo,resumo,contexto,selecoes,confirmar,metodos,ancora=None):
    return dict(id=id,sec='publicos',tipo='publico',titulo=titulo,resumo=resumo,
        seccoes=[('Necessidades e critérios',contexto),('Antes de escolher',confirmar)],
        selecoes=selecoes,metodos=metodos,ancora=ancora or id,
        problemas=[],fontes=[],relacionados=['como-escolher-a-tecnica'],ancoras=[],tags=' '.join([titulo]+[x[0] for x in selecoes]))

PUBLICOS=[
 publico('empresas','Empresas',
 'Artigos para acolher colaboradores, apoiar reuniões e acompanhar as deslocações da equipa.',
 'Diferencie a oferta de acolhimento, o material de trabalho e a lembrança para clientes. Considere a rotina dos destinatários, a forma de entrega e o equipamento que já utilizam; um conjunto só faz sentido quando cada componente acrescenta utilidade.',[
 ('gratox-22075','Para sessões de integração ou reuniões, o Gratox pode ser uma opção centrada em apontamentos. O catálogo descreve 18 folhas apagáveis e inclui a esferográfica apropriada e o pano de limpeza. Confirme as instruções de utilização antes de o incorporar numa rotina de trabalho.'),
 ('hetien-1364','A Hetien permite explorar uma oferta para acompanhar o dia de trabalho, com os 800 ml indicados na ficha. A combinação de alumínio e bambu exige identificar a zona que receberá a marca. Confirme cuidados e facilidade de transporte, sem pressupor isolamento térmico.'),
 ('sulkan-6620','Para colaboradores que transportam um portátil, a Sulkan oferece um ponto de partida com acolchoamento e compartimento indicado para 17 polegadas. Experimente o equipamento concreto numa amostra antes de decidir. A ligação USB documentada não demonstra a inclusão de bateria ou do telemóvel da fotografia.'),
 ('trombolix-22293','Para reuniões com clientes ou uma oferta individual de escrita, a Trombolix permite considerar um acabamento aborrachado em alumínio reciclado. O catálogo assinala gravação a laser especial para esta referência. Peça confirmação do efeito e da área antes de aprovar a marca.')],
 'Defina destinatários e momento de entrega, confirme os componentes e peça uma amostra. Se combinar produtos, trate a montagem e a embalagem como decisões próprias: não se apresenta um kit comercial documentado.',
 ['gravacao-a-laser','tampografia']),
 publico('camaras-municipais','Câmaras municipais',
 'Opções para ações culturais, encontros locais e reconhecimento de participantes, com escolhas ajustadas a cada iniciativa.',
 'Uma iniciativa cultural, uma sessão informativa e uma homenagem têm destinatários e necessidades diferentes. Defina o objetivo da ação, a utilidade da oferta e a legibilidade da identificação institucional antes de escolher o artigo.',[
 ('larsen-3322','Numa ação cultural ou sessão com documentação, o Larsen pode reunir os materiais entregues ao participante. A ficha indica algodão de 105 g/m² e 37 × 41 cm. Teste o conteúdo previsto no saco, sem transformar a gramagem numa garantia de carga.'),
 ('synex-20673','A Synex pode acompanhar sessões de participação em que seja necessário escrever. A ficha identifica uma esferográfica em ABS reciclado, permitindo preparar a avaliação do suporte. Confirme a posição e a leitura do nome da iniciativa na área realmente disponível.'),
 ('farnes-22151','Para uma homenagem ou reconhecimento local, a Farnes permite estudar uma placa com uma mensagem própria. O catálogo identifica esta referência de bambu como placa para sublimação. Essa indicação não se estende a todos os artigos de bambu; confirme a arte e o resultado pretendido.'),
 ('stiles-21840','A Stiles de adulto pode ser considerada para identificar a equipa de apoio de uma iniciativa. O catálogo documenta algodão de 170 g/m² e uma gama de tamanhos para esta referência. Recolha os tamanhos necessários e valide a identificação visual, sem presumir existência de stock.')],
 'Reveja a identidade institucional, os destinatários, a montagem e o local de distribuição. Este guia ajuda a comparar artigos; não avalia nem afirma conformidade com regras de contratação pública.',
 ['serigrafia','bordado'],'municipios'),
 publico('escolas','Escolas',
 'Escolhas para docentes, equipas escolares e iniciativas educativas, com avaliação específica dos destinatários.',
 'Separe materiais para docentes e serviços dos artigos destinados a alunos. A idade, a utilização supervisionada e as instruções do fabricante devem fazer parte da escolha; estar num catálogo de brindes não torna um artigo adequado a crianças de todas as idades.',[
 ('gratox-22075','Para docentes ou equipas administrativas, o Gratox pode apoiar apontamentos em reuniões e preparação de atividades. A ficha documenta 18 folhas apagáveis, esferográfica apagável e pano. A utilização por alunos exige uma avaliação própria, incluindo os acessórios e as instruções do artigo.'),
 ('larsen-3322','O Larsen pode organizar documentação entregue a docentes ou encarregados de educação numa sessão escolar. As dimensões de 37 × 41 cm ajudam a preparar uma montagem de teste. Não se apresenta como mochila escolar nem se deduz capacidade de transporte pela gramagem.'),
 ('stiles-21840','A Stiles 21840 pode ser avaliada para identificar docentes ou equipas adultas de apoio em atividades. Trata-se da referência de adulto em algodão de 170 g/m² documentada no catálogo. Não a apresente como uma gama infantil: confirme medidas e adequação aos destinatários concretos.')],
 'Antes de entregar qualquer artigo a alunos, confirme a faixa etária e as instruções com o fornecedor e a escola. Não se presume conformidade específica para uso infantil, nem se transferem as características de uma referência de adulto para uma infantil.',
 ['serigrafia','bordado']),
 publico('clubes-desportivos','Clubes desportivos',
 'Artigos para equipas de apoio, adeptos e momentos de reconhecimento, escolhidos segundo a utilização.',
 'Diferencie o material de treino da identificação de voluntários, das ofertas a adeptos e das lembranças de participação. Defina também se a marca deve privilegiar o emblema do clube, o nome do evento ou uma mensagem de reconhecimento.',[
 ('stiles-21840','Para voluntários ou adeptos adultos, a Stiles pode servir de base a uma identificação visual comum. O catálogo descreve uma t-shirt de algodão de 170 g/m². Essa descrição não prova desempenho técnico para competição, pelo que não se apresenta como equipamento desportivo especializado.'),
 ('hetien-1364','A Hetien pode ser considerada como oferta individual a membros adultos ou equipas de apoio. A capacidade de 800 ml é um dado útil para comparar o formato com a utilização prevista. Confirme a tampa, as instruções de cuidado e as condições de transporte antes de a propor para uma atividade.'),
 ('emphy-1818','O Emphy permite estudar um saco para entregar artigos a adeptos ou participantes. A ficha indica algodão de 300 g/m² e 37 × 41 cm. Experimente o conjunto a transportar, sem equiparar maior gramagem a resistência ou carga garantidas.'),
 ('farnes-22151','A Farnes pode ilustrar uma proposta de reconhecimento de participantes ou colaboradores do clube. É uma placa de bambu que o catálogo identifica para sublimação. O motivo desportivo da fotografia pertence ao catálogo e não demonstra um trabalho realizado para o clube ou pela Nobrinde.')],
 'Confirme destinatários, tamanhos e versões do emblema, incluindo nomes e datas quando existirem. Para menores, é necessária uma avaliação própria de adequação; as escolhas apresentadas não a substituem.',
 ['bordado','serigrafia'],'clubes'),
 publico('revendedores','Revendedores',
 'Exemplos para construir comparações claras entre referências e preparar propostas sem extrapolar as fichas.',
 'Organize cada proposta por utilização, material, referência e ponto a confirmar. Uma comparação útil mostra diferenças documentadas e separa as características do artigo das condições comerciais, de disponibilidade e de personalização.',[
 ('synex-20673','A Synex é um exemplo de escrita em ABS reciclado para apresentar ao lado de outras construções. Use a referência e a composição como dados objetivos da proposta. Não deduza custos, mínimos de encomenda ou técnicas de impressão a partir do material.'),
 ('trombolix-22293','A Trombolix permite comparar com a Synex um corpo em alumínio reciclado com acabamento aborrachado. A indicação expressa de gravação a laser no catálogo pode orientar uma consulta técnica para esta referência. Confirme a área e o efeito sem prometer resultados idênticos em todos os artigos metálicos.'),
 ('chalmer-21986','O Chalmer pode integrar uma comparação de recipientes de 900 ml, documentando o aço inoxidável reciclado. Compare dimensões, construção e utilização em vez de usar apenas a capacidade como critério. A ficha não justifica promessas próprias de lavagem ou desempenho térmico.'),
 ('bastien-22361','O Bastien tem igualmente 900 ml indicados, mas a ficha identifica PP. Esta diferença permite explicar ao cliente por que razão igual capacidade não equivale ao mesmo produto. A seleção e a personalização devem ser confirmadas para a referência concreta.')],
 'Registe as fontes e a versão da arte em cada proposta. Confirme separadamente condições comerciais, prazos, disponibilidade e requisitos de produção; este guia não define descontos, margens, exclusividades ou quantidades mínimas.',
 ['gravacao-a-laser','impressao-uv']),
 publico('eventos','Eventos',
 'Escolhas para a receção, a participação e a identificação da equipa, considerando como cada artigo será entregue.',
 'Comece pelo percurso do participante: chegada, atividades e saída. Defina o que precisa de transportar, quando recebe a oferta e como a equipa de apoio será reconhecida, antes de montar um conjunto de artigos.',[
 ('larsen-3322','O Larsen pode reunir programa e documentação na receção dos participantes. Os 37 × 41 cm indicados ajudam a testar a montagem com os materiais reais do evento. A facilidade de distribuição deve ser avaliada com o conjunto completo, não apenas com o saco vazio.'),
 ('synex-20673','A Synex pode acompanhar uma sessão com exercícios escritos ou tomada de notas. É uma esferográfica em ABS reciclado, segundo a ficha. Confirme a identificação do evento na área de personalização disponível e evite texto demasiado extenso.'),
 ('stiles-21840','A Stiles de adulto pode apoiar a identificação de organizadores e voluntários. A ficha apresenta algodão de 170 g/m² e tamanhos de XS a 3XL. Prepare a distribuição por tamanho e confirme a produção das marcas, sem assumir disponibilidade de todas as variantes.'),
 ('hetien-1364','A Hetien pode ser estudada como oferta individual para participantes adultos, quando uma garrafa fizer sentido no contexto. O catálogo indica alumínio e bambu e capacidade de 800 ml. Avalie transporte, entrega e instruções de uso, sem atribuir um benefício ambiental comprovado apenas à escolha do material.')],
 'Faça uma montagem de teste e reveja versões de marca, listas de tamanhos e modo de entrega. Se houver embalagem ou combinação de artigos, confirme esses elementos à parte; as referências do catálogo não constituem um kit montado.',
 ['serigrafia','tampografia']),
]

PAGINAS_PRODUTOS={'canetas':'canetas-e-escrita','bebidas':'garrafas-copos-e-canecas','sacos':'sacos-e-mochilas','texteis':'texteis','tecnologia':'tecnologia','escritorio':'artigos-de-escritorio','premium':'brindes-premium'}
