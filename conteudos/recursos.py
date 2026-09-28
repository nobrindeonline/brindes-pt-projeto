"""Fotografias e factos transcritos/conferidos visualmente no material recebido.
Páginas PDF contadas desde 1; impressa = número visível no catálogo.
Não incluir preços nem inferir o significado dos códigos de impressão.
"""
CATALOGO = 'General Catalogue 2026 - Iberia Prices'
FOTOS_TECNICAS = {
 'tampografia': {'titulo':'Máquina de tampografia','autor':'Swoolverton','licenca':'CC BY 3.0','licenca_url':'https://creativecommons.org/licenses/by/3.0/','fonte':'https://commons.wikimedia.org/wiki/File:Pad_printing_machine.JPG','width':1600,'height':1066,'alt':'Máquina de tampografia com tampão de silicone vermelho e suporte de fixação da peça.'},
 'serigrafia': {'titulo':'Demonstração de serigrafia','autor':'Ahmad Ali Karim','licenca':'CC0 1.0','licenca_url':'https://creativecommons.org/publicdomain/zero/1.0/','fonte':'https://commons.wikimedia.org/wiki/File:Screen_printing_demonstration_at_TEDxUTM.jpg','width':1600,'height':1067,'alt':'Pessoa a passar um rodo sobre uma tela durante uma demonstração de serigrafia.'},
 'gravacao-a-laser': {'titulo':'Máquina de gravação a laser','autor':'Rht bd','licenca':'CC BY-SA 4.0','licenca_url':'https://creativecommons.org/licenses/by-sa/4.0/','fonte':'https://commons.wikimedia.org/wiki/File:Laser_engraving_machine.jpg','width':1426,'height':1600,'alt':'Equipamento de gravação a laser com coluna, mesa de trabalho e computador de controlo.'},
 'impressao-uv': {'titulo':'Impressora UV Mimaki','autor':'Akaniji','licenca':'CC BY-SA 3.0','licenca_url':'https://creativecommons.org/licenses/by-sa/3.0/','fonte':'https://commons.wikimedia.org/wiki/File:UV_printer_MIMAKI_3042HG.JPG','width':1200,'height':1600,'alt':'Impressora UV Mimaki com a mesa de impressão e a zona de trabalho visíveis.'},
 'bordado': {'titulo':'Máquina de bordado','autor':'Srini297','licenca':'CC BY-SA 4.0','licenca_url':'https://creativecommons.org/licenses/by-sa/4.0/','fonte':'https://commons.wikimedia.org/wiki/File:Embroidery_machine.jpg','width':900,'height':1600,'alt':'Máquina de bordado industrial com várias cabeças sobre tecido rosa com motivos dourados.'},
}

PRODUTOS = [
 {'id':'synex-20673','nome':'Synex','ref':'20673','categoria':'canetas','pdf':414,'impressa':412,'bloco':25,'ficheiro':'esferografica-synex-20673-abs-reciclado.webp','alt':'Esferográfica Synex vermelha, com clip branco e botão prateado.',
  'factos':['Esferográfica em ABS reciclado.','Dimensões indicadas: Ø 1 × 14,5 cm.'],
  'leitura':'Um exemplo de corpo em plástico. A identificação do ABS ajuda a preparar a avaliação, mas não confirma por si só uma tinta ou técnica.'},
 {'id':'trombolix-22293','nome':'Trombolix','ref':'22293','categoria':'canetas','pdf':426,'impressa':424,'bloco':12,'ficheiro':'esferografica-trombolix-22293-aluminio.webp','alt':'Esferográfica Trombolix verde, com clip e ponta no mesmo tom.',
  'factos':['Alumínio reciclado, acabamento aborrachado e carga jumbo.','Dimensões indicadas: Ø 1 × 13,7 cm.'],
  'leitura':'O catálogo assinala uma aplicação especial de gravação a laser para este modelo. A área, o efeito e as condições de produção continuam a precisar de confirmação para o artigo escolhido.'},
 {'id':'chalmer-21986','nome':'Chalmer','ref':'21986','categoria':'bebidas','pdf':242,'impressa':240,'bloco':12,'ficheiro':'copo-chalmer-21986-inox-900ml.webp','alt':'Copo térmico Chalmer azul-escuro, com tampa preta, pega e palhinha.',
  'factos':['Copo térmico em aço inoxidável reciclado.','Capacidade indicada: 900 ml; Ø 10,5 × 24,8 cm.'],
  'leitura':'Compare o material, o formato e a tampa, além da capacidade. A ficha não dispensa a confirmação dos cuidados de lavagem.'},
 {'id':'bastien-22361','nome':'Bastien','ref':'22361','categoria':'bebidas','pdf':242,'impressa':240,'bloco':4,'ficheiro':'copo-bastien-22361-pp-900ml.webp','alt':'Copo Bastien preto com tampa, pega superior e faixa prateada.',
  'factos':['Copo descrito no catálogo como térmico, em PP.','Capacidade indicada: 900 ml; Ø 9,1 × 25 cm.'],
  'leitura':'Tem a mesma capacidade indicada para o Chalmer, mas outro material. Não se deve transferir automaticamente a solução de personalização entre os dois.'},
 {'id':'hetien-1364','nome':'Hetien','ref':'1364','categoria':'bebidas','pdf':270,'impressa':268,'bloco':8,'ficheiro':'garrafa-hetien-1364-aluminio-bambu-800ml.webp','alt':'Garrafa Hetien prateada com tampa de bambu e mosquetão.',
  'factos':['Garrafa em alumínio e bambu.','Capacidade indicada: 800 ml; Ø 7,3 × 24,7 cm.'],
  'leitura':'Num artigo com materiais diferentes, identifique primeiro a zona onde ficará o logótipo. O corpo e a tampa não devem ser avaliados como uma única superfície.'},
 {'id':'larsen-3322','nome':'Larsen','ref':'3322','categoria':'sacos','pdf':360,'impressa':358,'bloco':1,'ficheiro':'saco-larsen-3322-algodao-105g.webp','alt':'Saco Larsen em algodão de cor natural, com duas alças compridas.',
  'factos':['Saco de algodão com gramagem de 105 g/m².','Dimensões indicadas: 37 × 41 cm.'],
  'leitura':'Compare com o Emphy: a dimensão é igual, mas a gramagem é diferente. A gramagem não deve ser apresentada como uma carga máxima de transporte.'},
 {'id':'emphy-1818','nome':'Emphy','ref':'1818','categoria':'sacos','pdf':360,'impressa':358,'bloco':5,'ficheiro':'saco-emphy-1818-algodao-300g.webp','alt':'Saco Emphy em algodão de cor natural, com duas alças compridas.',
  'factos':['Saco de algodão com gramagem de 300 g/m².','Dimensões indicadas: 37 × 41 cm.'],
  'leitura':'Uma alternativa para comparar ao toque e na construção. Confirme numa amostra o comportamento do tecido e a área a personalizar.'},
 {'id':'sulkan-6620','nome':'Sulkan','ref':'6620','categoria':'sacos','pdf':10,'impressa':8,'bloco':0,'ficheiro':'mochila-sulkan-6620-poliester-600d.webp','alt':'Mochila Sulkan cinzenta com bolsos frontais; a imagem do catálogo inclui um telemóvel ao lado.',
  'factos':['Mochila em poliéster 600D, acolchoada, com ligação USB e bolso acolchoado para portátil.','Dimensões indicadas: 32 × 46 × 20 cm; compartimento para portátil de 17 polegadas.'],
  'leitura':'Bolsos, costuras e acesso ao painel condicionam a escolha da zona de personalização. O telemóvel mostrado é um acessório ilustrativo; a ficha não o indica como incluído.'},
 {'id':'stiles-21840','nome':'Stiles','ref':'21840','categoria':'texteis','pdf':1000,'impressa':996,'bloco':1,'ficheiro':'tshirt-stiles-21840-algodao-170g.webp','alt':'Modelo a vestir uma t-shirt Stiles amarela, de manga curta e gola redonda.',
  'factos':['T-shirt de adulto de cor: 100% algodão ring spun, single jersey de 170 g/m².','A ficha indica tamanhos XS, S, M, L, XL, XXL e 3XL.'],
  'leitura':'Escolha a referência e a cor antes de validar a arte. Os tamanhos indicados pertencem à edição do catálogo e não representam disponibilidade atual.'},
 {'id':'nalow-1146','nome':'Nalow','ref':'1146','categoria':'tecnologia','pdf':88,'impressa':86,'bloco':7,'ficheiro':'altifalante-nalow-1146-abs-bambu.webp','alt':'Altifalante Nalow com difusor branco e base de bambu.',
  'factos':['Altifalante em ABS e bambu, com ligação Bluetooth e potência sonora indicada de 3 W.','Bateria indicada de 1200 mAh; três modos de luz e intensidade regulável.'],
  'leitura':'A potência e a capacidade da bateria não permitem concluir a autonomia. Distinga a zona de luz da base ao definir a posição da marca.'},
 {'id':'gratox-22075','nome':'Gratox','ref':'22075','categoria':'escritorio','pdf':198,'impressa':196,'bloco':0,'ficheiro':'caderno-gratox-22075-apagavel.webp','alt':'Caderno Gratox preto com encadernação em espiral, esferográfica e pano de limpeza.',
  'factos':['Caderno apagável com 18 folhas pautadas.','Inclui esferográfica apagável de tinta preta e pano de limpeza; 16 × 21,5 × 1,7 cm.'],
  'leitura':'O sistema de escrita e os acessórios fazem parte da escolha. A ficha não identifica o material da capa, pelo que não se presume a sua compatibilidade com uma técnica.'},
 {'id':'farnes-22151','nome':'Farnes','ref':'22151','categoria':'premium','pdf':610,'impressa':608,'bloco':0,'ficheiro':'placa-farnes-22151-bambu-sublimacao.webp','alt':'Placa Farnes circular com base de bambu e imagem desportiva ilustrativa do catálogo.',
  'factos':['Placa de bambu identificada expressamente como placa para sublimação.','Dimensões indicadas: 9,5 × 12,5 × 4,5 cm.'],
  'leitura':'A indicação de sublimação é específica desta referência; não prova que qualquer artigo de bambu aceite o processo. O desenho mostrado pertence à apresentação do catálogo.'},
]

POR_ID={p['id']:p for p in PRODUTOS}
ARTIGO_PRODUTOS={
 'canetas-e-escrita':['synex-20673','trombolix-22293'],
 'garrafas-copos-e-canecas':['chalmer-21986','bastien-22361','hetien-1364'],
 'texteis':['stiles-21840'], 'sacos-e-mochilas':['larsen-3322','emphy-1818','sulkan-6620'],
 'tecnologia':['nalow-1146'], 'artigos-de-escritorio':['gratox-22075'], 'brindes-premium':['farnes-22151'],
 'como-escolher-a-tecnica':['chalmer-21986','bastien-22361','farnes-22151'],
 'gravacao-a-laser':['trombolix-22293'],
}
GRUPO_PRODUTOS={
 ('produtos','canetas'):['synex-20673'], ('produtos','bebidas'):['hetien-1364'],
 ('produtos','texteis'):['stiles-21840'], ('produtos','sacos'):['sulkan-6620'],
 ('produtos','tecnologia'):['nalow-1146'], ('produtos','escritorio'):['gratox-22075'],
 ('produtos','premium'):['farnes-22151'],
 ('materiais','plasticos'):['synex-20673','bastien-22361'], ('materiais','metais'):['trombolix-22293','chalmer-21986'],
 ('materiais','naturais'):['hetien-1364','farnes-22151'], ('materiais','texteis'):['larsen-3322','emphy-1818'],
}

ARTIGO_PRODUTOS.update({"maquinas-de-gravacao-laser":["trombolix-22293"], "sublimacao":["farnes-22151"], "montagem-e-acabamentos":["gratox-22075","hetien-1364"], "costura-industrial":["larsen-3322"]})
