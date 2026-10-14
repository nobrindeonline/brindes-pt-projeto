brindes.pt — biblioteca informativa
Projeto de um site estático, em português de Portugal, com conteúdos educativos sobre brindes, materiais, técnicas de personalização, produtos, públicos e processos de produção.
Estado do projeto
- O site é composto por páginas HTML, CSS e JavaScript estáticos.
- Não inclui loja, base de dados, chatbot nem recolha de pesquisas dos visitantes.
- A versão de trabalho é local e ainda precisa de validação antes de qualquer publicação.
- O objetivo editorial é disponibilizar conteúdos públicos, anónimos e úteis para leitores e sistemas de pesquisa. Antes de publicar, confirmar o domínio, o sitemap, as regras de rastreio e a ausência de bloqueios noindex nas páginas públicas.
- A pasta editorial/ e os materiais temporários são documentação de trabalho; não devem ser publicados sem revisão.
Conteúdos
O site reúne páginas de entrada e artigos nas secções Técnicas, Materiais, Produtos, Guias, Para quem, Tendências e Indústria, além da página inicial e da pesquisa.
Indústria
A página industria/index.html organiza a secção em cartões com ligações para:
- História dos brindes;
- Da ideia à entrega;
- Máquinas e processos;
- Montagem e acabamentos.
Cada tema tem uma página própria. A história aborda a evolução dos brindes e da personalização; o percurso da ideia à entrega descreve as etapas possíveis de um trabalho; máquinas e processos apresenta uma visão geral e encaminha para as técnicas detalhadas; montagem e acabamentos explica as operações finais, incluindo, quando aplicável, embalagem e preparação para expedição.
As páginas específicas de equipamentos e processos são acessíveis a partir da secção. As imagens disponíveis estão organizadas em pastas dentro de assets/industria/; cada imagem deve ser usada apenas quando corresponde ao tema e acrescenta contexto.
Técnicas, materiais e guias
As técnicas incluem guias de personalização como tampografia, serigrafia, gravação a laser, impressão UV, bordado, transfers, sublimação, termogravura e troquelagem, além de outros conteúdos existentes no projeto. A secção Materiais contém artigos sobre diferentes famílias de materiais. Os Guias ajudam a comparar opções e a tomar decisões informadas.
As páginas Para quem apresentam conteúdos organizados por públicos e contextos de utilização. A secção Tendências reúne artigos editoriais e temas em desenvolvimento. Consulta as páginas de entrada do site para ver a lista atualizada de conteúdos.
Abrir o site localmente
Abre index.html num navegador ou inicia um servidor local na pasta do projeto:
python -m http.server 8765 --bind 127.0.0.1
Depois, abre http://127.0.0.1:8765. Termina o servidor com Ctrl+C. Este servidor só permite rever o site no computador local; não publica o projeto na Internet.
Gerar e verificar
Edita os conteúdos e modelos de origem, e não apenas o HTML gerado, porque a geração pode substituir alterações feitas diretamente nas páginas.
python gerar.py
python editorial/gerar_plano.py
python verificar.py
node --test testes/pesquisa.test.cjs
Na primeira utilização, instala as dependências de formatação:
npm ci
python gerar.py atualiza as páginas e os dados usados pela pesquisa. Quando necessário, gera também os registos editoriais específicos indicados nas secções de editorial/. Para verificar a formatação sem alterar ficheiros:
npm run format:check
Python 3 é usado para gerar e verificar o site. Node.js é necessário para os testes JavaScript e para a formatação automática com Prettier. O site gerado continua estático e pode ser navegado sem estas ferramentas.
Estrutura principal
index.html                   Página inicial gerada
tecnicas/, materiais/,       Secções e artigos HTML gerados
produtos/, guias/,
publicos/, tendencias/,
industria/
assets/                      Imagens, estilos e dados da pesquisa
conteudos/                   Conteúdos de origem em Python
modelos/                     Modelos HTML editáveis
gerar.py                     Geração das páginas e apresentação comum
verificar.py                 Verificação de páginas, recursos e âncoras
testes/                      Testes automatizados
editorial/                   Fontes, planeamento e validações internas
Alterar ou acrescentar conteúdos
1. Identifica o ficheiro de origem em conteudos/ ou modelos/ e verifica as instruções específicas em editorial/.
2. Usa um identificador estável para artigos e páginas existentes; não alteres URLs sem preparar uma alternativa.
3. Regista fontes fiáveis e pontos por confirmar. Não apresentes informação incerta como facto.
4. Se usares imagens, confirma que pertencem ao tema, preserva os originais e acrescenta texto alternativo e créditos quando a origem exigir.
5. Gera novamente o site e executa as verificações relevantes.
Para artigos mantidos no catálogo, os conteúdos, relações e fontes estão em conteudos/catalogo.py; os modelos reutilizáveis estão em conteudos/modelos.py. Vários temas têm módulos próprios em conteudos/, como materiais, guias, públicos, transfers, troquelagem e crachás. Consulta o ficheiro específico antes de editar.
Fontes e qualidade editorial
Usa fontes públicas fiáveis, dando preferência a documentação técnica, instituições e associações reconhecidas. Regista título, entidade ou autor, URL e data de consulta nos ficheiros editoriais apropriados. Não inventes datas, compatibilidades, parâmetros de produção, capacidades ou garantias. Quando um resultado depender do equipamento, material ou consumível, explica essa dependência.
Mantém o conteúdo independente e anónimo. Não incluas nomes de empresas, clientes, contactos, referências comerciais, SKUs ou texto copiado de catálogos. Escreve para informar, sem repetir palavras-chave artificialmente.
Publicação
Antes de publicar, revê visualmente as páginas em computador e telemóvel, confirma ligações e imagens e verifica o HTML gerado. Confirma também que as páginas destinadas ao público podem ser rastreadas, que os canonicals usam o domínio real e que o sitemap contém apenas URLs públicas válidas. A permissão de rastreio não garante indexação ou posicionamento nos resultados.
Não publiques documentação editorial, ficheiros temporários ou materiais de revisão que não se destinem aos visitantes.
