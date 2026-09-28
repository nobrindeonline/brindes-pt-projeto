"""Guias de categorias, apoiados pelos exemplos documentados em recursos.py."""
def produto(id,titulo,resumo,seccoes,relacionados,ancoras,tags):
    return dict(id=id,sec='produtos',tipo='produto',titulo=titulo,resumo=resumo,seccoes=seccoes,problemas=[],fontes=[],relacionados=relacionados,ancoras=ancoras,tags=tags)

NOVOS_ARTIGOS=[
 produto('garrafas-copos-e-canecas','Garrafas, copos e canecas',
 'Compare a capacidade, os materiais e a construção antes de escolher onde ficará a marca.',[
 ('Capacidade e formato','O volume não descreve sozinho o artigo. Nos exemplos do catálogo abaixo, Chalmer e Bastien têm ambos 900 ml, mas apresentam materiais e dimensões diferentes. Compare também a tampa, a pega e a forma de transportar.'),
 ('Materiais do corpo e da tampa','A Hetien combina alumínio e bambu. Identifique o componente a personalizar antes de escolher uma técnica; não estenda uma conclusão sobre o corpo à tampa.'),
 ('Personalização e utilização','Defina posição, orientação e dimensão da marca. A possibilidade de aplicar tinta ou laser depende da referência, do acabamento e da avaliação da produção. A capacidade da garrafa não determina a área de personalização.'),
 ('O que confirmar','Peça as instruções de lavagem e utilização do modelo concreto. Os exemplos não estabelecem resistência à máquina de lavar, estanquidade ou desempenho térmico. Confirme estes pontos quando forem decisivos.')],
 ['como-escolher-a-tecnica','gravacao-a-laser','impressao-uv'],['materiais/index.html#metais','materiais/index.html#plasticos'],'garrafa copo caneca tampa capacidade ml alumínio inox PP'),
 produto('texteis','Têxteis',
 'Composição, gramagem, tamanho e posição da arte ajudam a preparar uma escolha adequada à peça.',[
 ('Escolher uma referência concreta','Uma t-shirt deve ser identificada pela referência e pela variante. A Stiles 21840 é a versão de cor documentada nos exemplos; não se devem generalizar as suas características a toda a coleção.'),
 ('Composição e gramagem','A ficha da Stiles indica algodão ring spun e gramagem de 170 g/m². Use estes dados para comparar peças, sem tratar a gramagem como prova isolada de durabilidade ou conforto.'),
 ('Tamanhos e arte','Defina quantidades por tamanho e confirme a posição do desenho. Peça uma maquete com medidas e uma avaliação do pormenor mais pequeno; a mesma largura de marca pode ter uma presença diferente em tamanhos distintos.'),
 ('Comparar técnicas','Os guias de serigrafia e bordado explicam processos possíveis em têxteis. Não confirmam a sua aplicação a esta referência: a peça, a arte e as condições de produção precisam de validação.'),
 ('Antes de aprovar','Confirme composição da variante escolhida, tabela de medidas, instruções de lavagem e amostra. A gama apresentada no catálogo não garante disponibilidade atual.')],
 ['serigrafia','bordado','como-escolher-a-tecnica','sacos-e-mochilas'],['materiais/index.html#texteis'],'tshirt algodão ring spun gramagem tecido tamanho vestuário'),
 produto('sacos-e-mochilas','Sacos e mochilas',
 'Observe o tecido, a construção e o acesso à zona de personalização, para além das dimensões exteriores.',[
 ('Duas gramagens, a mesma dimensão','Larsen e Emphy são sacos de algodão de 37 × 41 cm, mas as fichas indicam 105 e 300 g/m², respetivamente. Compare-os numa amostra; estes valores não representam o peso máximo que podem transportar.'),
 ('Uma mochila tem vários componentes','A Sulkan acrescenta compartimentos, acolchoamento e ligação USB. Confirme o que será transportado e a dimensão do equipamento a guardar. Não deduza a existência de bateria a partir da ligação USB.'),
 ('Escolher a zona da marca','Assinale o painel e verifique bolsos, fechos e costuras. A dimensão exterior do saco ou mochila não corresponde automaticamente à área imprimível.'),
 ('Técnicas e confirmação','Compare os guias de serigrafia e bordado para perceber as diferenças de processo. A seleção final depende do artigo, do acesso à zona de trabalho e da validação da produção.'),
 ('Uso e apresentação','Defina o conteúdo a transportar, a forma de distribuição e a apresentação final. Se resistência ou carga forem critérios essenciais, peça documentação ou ensaio específico em vez de inferir a partir da gramagem.')],
 ['serigrafia','bordado','texteis','como-escolher-a-tecnica'],['materiais/index.html#texteis'],'saco mochila algodão poliéster 600D portátil gramagem'),
 produto('tecnologia','Tecnologia',
 'Separe as características eletrónicas da avaliação da superfície que vai receber a marca.',[
 ('Escolher pela função','Comece pela utilização esperada e pelos dispositivos envolvidos. O Nalow, documentado abaixo, combina som e luz; a potência sonora indicada não permite comparar sozinha toda a experiência de utilização.'),
 ('Ler a ficha sem extrapolar','O catálogo indica a capacidade da bateria, mas esse valor não permite calcular uma autonomia garantida. Confirme os dados relevantes para a utilização pretendida na documentação do modelo.'),
 ('Identificar a superfície','Num artigo em ABS e bambu, assinale onde pretende a marca. A zona de luz e a base têm funções e superfícies diferentes.'),
 ('Confirmar a personalização','Os guias de tampografia e UV explicam alternativas de processo. A sua presença nesta categoria não comprova compatibilidade com todos os dispositivos. Confirme o artigo, a zona, a tinta e o ensaio com a produção.')],
 ['tampografia','impressao-uv','como-escolher-a-tecnica'],['materiais/index.html#plasticos','materiais/index.html#naturais'],'tecnologia altifalante bluetooth bateria luz ABS bambu'),
 produto('artigos-de-escritorio','Artigos de escritório',
 'Considere a forma de utilização, os consumíveis e os acessórios que acompanham cada artigo.',[
 ('Olhar para o conjunto','Um caderno pode fazer parte de um sistema de escrita. No Gratox, o catálogo identifica folhas apagáveis, uma esferográfica e um pano; os elementos incluídos ajudam a compreender a utilização.'),
 ('Distinguir interior e capa','O número e o tipo de folhas não identificam o material exterior. A ficha selecionada não especifica o material da capa, pelo que não se atribui automaticamente uma técnica de personalização.'),
 ('Organizar a informação para a produção','Forneça a referência, a versão do logótipo, a posição e as dimensões pretendidas. Em artigos com espiral, elásticos ou acessórios, confirme a área livre e o acesso ao suporte.'),
 ('O que confirmar','Reveja o conteúdo do conjunto e as instruções de utilização. Antes de repetir uma encomenda, confirme a referência e a versão da arte que foram aprovadas.')],
 ['canetas-e-escrita','como-escolher-a-tecnica','impressao-uv'],['materiais/index.html'],'escritório caderno bloco notas apagável folhas Gratox'),
 produto('brindes-premium','Brindes premium',
 'Defina o efeito pretendido e avalie material, apresentação e personalização como um conjunto.',[
 ('O significado de premium','Use critérios concretos para a escolha: aspeto, utilidade, contexto da oferta e apresentação. A classificação de uma categoria no catálogo não substitui a avaliação de uma amostra.'),
 ('Uma referência preparada para um processo','A placa Farnes é identificada no catálogo como placa de bambu para sublimação. Esta indicação pertence à referência 22151 e não deve ser generalizada a outras peças de bambu.'),
 ('Imagem e mensagem','Verifique legibilidade, proporção do desenho e equilíbrio entre texto e imagem. As fotografias do catálogo ilustram a apresentação do fornecedor; não são exemplos de trabalhos da Nobrinde.'),
 ('Antes de escolher','Confirme acabamento, estabilidade, apresentação, embalagem e condições de aplicação da arte. Não presuma que uma caixa de oferta ou qualquer acessório não descrito está incluído.')],
 ['como-escolher-a-tecnica','artigos-de-escritorio'],['materiais/index.html#naturais'],'premium placa bambu sublimação Farnes oferta troféu'),
]
