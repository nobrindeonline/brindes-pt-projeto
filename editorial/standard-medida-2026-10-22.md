# Produto standard ou à medida? — 22 de outubro de 2026

## Integração

Fonte editorial em `conteudos/guia_standard.py`, integrada por `conteudos/guias.py`.
Página: `guias/produto-standard-ou-a-medida.html`. Cartão no percurso Escolher,
pesquisa e JSON gerados pelo sistema existente. URLs anteriores preservados.
Não houve publicação nem push.

O guia reutiliza tipografia, cartão com imagem integral, resposta breve, esquema,
índice, secções, erros, checklist, perguntas e fontes do renderizador existente.
As comparações são apresentadas por critério em texto, sem introduzir estilos novos.
Ligações para materiais, técnicas, produtos, maquete e Da ideia à entrega verificadas.

## Fontes e limites

- INPI / Justiça.gov.pt: pedido de registo e proteção da aparência. Não usado para
  concluir titularidade de ficheiros, propriedade de ferramentas ou condições contratuais.
- NIST: enquadramento de desenvolvimento, prototipagem e passagem ao fabrico.
- Universidade da Florida, Design Laboratory, DFMA Tips: relações entre desenho,
  materiais, fabrico, montagem e custos; sem transpor números para este guia.
- Conselho da União Europeia: dimensões de ecodesign, sem afirmar certificação,
  requisitos específicos de um produto ou superioridade ambiental.

URLs, datas e âmbito em `editorial/fontes-guias.md` e nos dados públicos.
As categorias, exemplos hipotéticos, sequência de trabalho e checklists são
orientações editoriais. Condições de cada projeto exigem confirmação específica.
O guia não determina direitos de um caso concreto nem oferece aconselhamento jurídico.

## Imagem fornecida

Original preservado: `assets/guias/MedidavsStandard/images.jpg` (335 × 597).
Cópia binária pública: `assets/guias/visuais/standard-medida-cartao.jpg`.
Representa dois sacos de dimensões diferentes; uso exclusivamente ilustrativo
no cartão, sem inferir materiais, processo ou desempenho. A proporção vertical
é mantida pelas regras existentes de contenção da imagem.
Texto alternativo e manifestos atualizados. Os créditos gerais indicam que
a autoria e a licença não estão identificadas; esses dados continuam por confirmar.

## Geração e verificações

- `.venv/Scripts/python.exe scripts/gerar.py --secao guias`
- `.venv/Scripts/python.exe editorial/gerar_fontes_guias.py`
- `.venv/Scripts/python.exe scripts/verificar_tudo.py`

Verificação integral aprovada: 123 páginas, 4873 ligações/recursos locais,
oito Guias consistentes com pesquisa e JSON, imagens e créditos válidos,
13 testes de pesquisa aprovados e formatação HTML conforme Prettier.
