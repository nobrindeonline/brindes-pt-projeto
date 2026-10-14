# Verificação da reorganização de Mercado

Data: 14 de outubro de 2026. Trabalho local; não houve publicação remota.

- `python gerar.py --secao mercado`: 30 páginas geradas e formatadas, incluindo a entrada, seis áreas, seis guias complementares e dezassete perfis. Pesquisa atualizada apenas para Mercado.
- `python verificar.py`: **110 páginas; 4 185 ligações/recursos locais**. Títulos, idioma, recursos e âncoras válidos.
- `python testes/verificar_mercado.py`: **seis áreas, 24 associações, quinze perfis selecionados e dois complementares**. Cada cartão liga ao perfil canónico; MUKUA não tem perfil duplicado; JHK não usa o logótipo Velilla.
- `node --test testes/pesquisa.test.cjs`: **12 testes aprovados**, sem falhas.
- `npm.cmd run format:check`: todos os HTML conformes.
- `python -m py_compile`: módulos de conteúdo, apresentação e geração compilados sem erro.
- Verificação adicional com Pillow: dimensões efetivas dos logótipos e imagens correspondem aos atributos HTML. As cópias de imagens são byte a byte iguais aos originais, que não foram movidos nem editados.
- Comparação SHA-256 com o estado anterior ao trabalho: todos os HTML fora de Mercado, incluindo pesquisa e entrada geral do site, permanecem intactos.
- O índice local insere as dezasseis rotas novas (seis áreas e dez perfis), sem duplicar URLs; perfis e área principal têm os textos atuais.
- As verificações específicas confirmam metadados únicos, `index, follow`, fontes datadas, imagens com texto alternativo e ausência de referências comerciais extensas ou dados internos no HTML de Mercado.
- `git diff --check`: sem erros de espaços; apenas avisos habituais de conversão LF/CRLF do repositório.

## Limitações que não são ocultadas

- O navegador ligado não está disponível: a consulta à ferramenta devolveu `apps: []` e `browsers: []`. A revisão visual de desktop e telemóvel permanece pendente. Foram reutilizadas as grelhas, tipografia e regras responsivas; imagens e logótipos foram inspecionados em folhas de contacto.
- Logótipo JHK ausente. A pasta com vários nomes contém apenas Velilla; o cartão e o perfil JHK usam identificação textual. O ficheiro não foi atribuído a outra empresa.
- O logótipo Velilla identifica o grupo no cartão conjunto Velilla Group / MUKUA. Não foi apresentado como logótipo independente de MUKUA.
- Algumas fontes oficiais falharam na abertura direta ou dependem de JavaScript. O conteúdo público indexado e as limitações de acesso estão identificados no dossier e junto das fontes do site. Não se declara que todos os endpoints responderam com sucesso.
- Não foram verificados certificados para todos os produtos nem indicadores quantitativos sem entidade e período claros. As lacunas estão declaradas nos perfis.
- Não existe sitemap no projeto e o domínio canónico não foi confirmado. Não foi criado um sitemap com domínio presumido.

## Entrega e manutenção

As seis áreas têm quatro empresas cada, na ordem editorial proposta. As repetições apontam sempre para o mesmo perfil. Nenhuma das quinze entradas da shortlist foi excluída. Os perfis de Dimatur e Eurovinil e os guias da organização anterior foram preservados como conteúdo complementar.

Fontes, mapeamento por área, papéis atribuídos e inventário dos logótipos: [fontes-mercado.md](fontes-mercado.md).

Regenerar com `python gerar.py --secao mercado` e `python editorial/gerar_fontes_mercado.py`. O inventário editorial tem suporte em `editorial/gerar_plano.py`; nesta revisão, foi atualizado apenas o bloco Mercado de `editorial/plano.md`.
