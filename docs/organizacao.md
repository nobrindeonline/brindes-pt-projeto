# Organização do projeto

Reorganização de 21 de outubro de 2026. Os URLs das páginas foram preservados.

| Local | Responsabilidade |
| --- | --- |
| Raiz | Entradas HTML, pesquisa, créditos, robots.txt e configurações |
| scripts/ | Geração, renderização e validação geral |
| conteudos/ | Dados editoriais de origem |
| modelos/ | Modelos HTML editáveis |
| assets/css/ | Estilos públicos |
| assets/js/ | JavaScript público |
| assets/ | Imagens e dados públicos gerados |
| docs/ | Brief, instruções e registos de apoio |
| editorial/ | Fontes, manifestos internos e ferramentas editoriais |
| testes/ | Verificadores específicos e testes da pesquisa |
| tmp/ | Inspeção e ficheiros temporários, excluídos da publicação |
| ../arquivo/referencias/ | PDFs locais, fora da pasta publicada |
| ../arquivo/backups/ | Arquivos ZIP, fora da pasta publicada |

## Comandos

Na raiz do projeto:

```powershell
npm.cmd run build
npm.cmd run check
```

Equivalentes: `python scripts/gerar.py` e
`python scripts/verificar_tudo.py`. A geração de uma única secção continua
disponível, por exemplo `python scripts/gerar.py --secao produtos`.
O verificador escolhe o Python da `.venv` existente se o Python corrente não
tiver Pillow. Node.js e o Prettier local continuam necessários.

As ferramentas Python importam os renderizadores através do pacote `scripts`.
O gerador resolve a raiz pelo caminho do próprio ficheiro, e não pela pasta de
trabalho do terminal. Os scripts de inspeção do PDF usam o novo caminho de arquivo.

## Publicação e preservação

`.assetsignore` exclui explicitamente scripts, docs, conteúdos, editorial,
testes e temporários. O PDF e os ZIPs ficam fora do diretório configurado no
Wrangler. A configuração de alojamento e o domínio não foram alterados.
Os comandos build/check não publicam, não fazem commit e não fazem push.

Foram movidos quinze ficheiros. A integridade de cada transferência foi
verificada por SHA-256 antes de atualizar o código e a documentação. As
imagens originais e os conteúdos de origem foram preservados. A geração
completa atualizou também cartões relacionados com os resumos e títulos de
Produtos que já estavam nos conteúdos Python; os corpos editoriais das outras
secções não foram reescritos.

## Verificações executadas

- Geração completa através de Python e do comando npm build.
- 114 páginas e 4389 ligações/recursos locais válidos.
- Nove verificadores específicos: estrutura, guias, imagens gerais, indústria,
  materiais, mercado, produtos, imagens de produtos e públicos.
- 226 utilizações de imagem, 128 ficheiros decodificados.
- Doze testes de pesquisa aprovados.
- Formatação HTML aprovada pelo Prettier.
- HTTP 200 para a entrada, artigo de Produtos e os quatro recursos CSS/JS movidos.

A conformidade verificada é técnica: estrutura, referências, geração, imagens,
pesquisa e exclusões de publicação. Não foi realizada revisão visual no navegador
nem publicação nesta execução.
