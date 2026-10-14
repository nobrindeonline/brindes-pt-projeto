"""Regista factos, imagens e todos os destinos públicos onde foram utilizados."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from conteudos.recursos import PRODUTOS, CATALOGO, POR_ID
from conteudos.catalogo import ARTIGOS, SECCOES
from conteudos.ideias import IDEIAS

paths=[ROOT/'index.html',ROOT/'creditos-imagens.html']
paths += [ROOT/s['id']/'index.html' for s in SECCOES]
paths += [ROOT/a['sec']/(a['id']+'.html') for a in ARTIGOS]
manifest={p['id']:p for p in json.loads((ROOT/'assets/produtos/manifesto.json').read_text(encoding='utf-8'))}
lines=['# Fontes do catálogo','',f'Fonte: `{CATALOGO}.pdf`, recebido na raiz do projeto. 1238 páginas. A página PDF é contada desde 1, incluindo a capa; a numeração impressa é registada separadamente.','',
'As fichas selecionadas foram lidas e comparadas visualmente com a posição das fotografias. A ordem do texto extraído não foi usada como prova da correspondência entre produto e imagem. Os preços e os quadros comerciais não foram reproduzidos nem ligados nas páginas públicas.','',
'## Produtos, afirmações e fotografias','', '| Produto | Informação utilizada | PDF / impressa | Fotografia | Páginas do site |', '| --- | --- | --- | --- | --- |']
for p in PRODUTOS:
    used=[]
    for path in paths:
        html=path.read_text(encoding='utf-8')
        if p['ficheiro'] in html or 'catalogo-'+p['id'] in html:
            used.append('`'+path.relative_to(ROOT).as_posix()+'`')
    m=manifest[p['id']]
    facts=' '.join(p['factos'])
    if p['id']=='trombolix-22293':facts+=' A página assinala gravação a laser especial para esta referência.'
    lines.append(f"| {p['nome']} {p['ref']} | {facts} | {p['pdf']} / {p['impressa']} | `assets/produtos/{p['ficheiro']}`; bloco {p['bloco']}; {m['width']} × {m['height']} px | {'; '.join(used)} |")
lines += ['', '## Artigos e ideias', '', '| Artigo | Dados e imagens usados | Origem PDF |', '| --- | --- | --- |',
'| Garrafas reutilizáveis como brinde | Hetien 1364: alumínio/bambu, 800 ml, Ø 7,3 × 24,7 cm; fotografia no cartão e no artigo | 270 (impressa 268) |',
'| Sacos personalizados para eventos | Larsen 3322: algodão, 105 g/m²; Emphy 1818: algodão, 300 g/m²; ambos 37 × 41 cm. Fotografia Larsen no cartão e no artigo | 360 (impressa 358) |',
'| Kits de boas-vindas para equipas | Gratox 22075: 18 folhas, esferográfica apagável de tinta preta e pano; Hetien 1364: alumínio/bambu, 800 ml; Sulkan 6620: poliéster 600D, acolchoamento, ligação USB e compartimento de 17 polegadas. Três fotografias individuais no cartão e no artigo | 198 / 270 / 10 (impressas 196 / 268 / 8) |',
'', 'Os cartões usam os mesmos ficheiros WebP dos artigos. Não foi criada uma fotografia de um kit comercial: a disposição lado a lado é uma composição em HTML/CSS de produtos individuais. As combinações, listas de verificação e conselhos são propostas editoriais, não factos sobre vendas, notícias ou tendências comprovadas.',
'', '## Extração e qualidade', '',
'As 12 fotografias foram extraídas diretamente dos objetos de imagem do PDF, sem texto sobreposto, preços, capa ou páginas completas. A transparência foi composta em branco quando necessário. Conversão para WebP com qualidade 86, sem ampliação e sem recorte. Apenas Stiles foi reduzida, para um máximo de 1200 px. Total: '+str(sum(p['bytes'] for p in manifest.values()))+' bytes.',
'', 'O manifesto `assets/produtos/manifesto.json` regista bloco, caixa de posição na página, resolução original/final e SHA-256. Repetir a extração: `.venv/Scripts/python.exe editorial/extrair_produtos.py`.',
'', 'A folha de contacto foi inspecionada visualmente: 12 produtos identificáveis, sem preços nem legendas comerciais incorporadas. Nenhuma das 12 imagens selecionadas foi rejeitada. Miniaturas de variantes pequenas e imagens apenas decorativas não foram ampliadas para substituir fotografias principais. A seleção não cobre todas as imagens do catálogo.',
'', '## Limites e pendências', '',
'- O material da capa do Gratox não é identificado na ficha selecionada; não foi inventado.',
'- Não foram deduzidos isolamento, autonomia, carga de transporte, cuidados de lavagem ou certificações a partir dos materiais e capacidades.',
'- As alegações de material reciclado são identificações do catálogo, não certificações verificadas nem garantias ambientais.',
'- Os códigos de impressão não foram descodificados por suposição. Compatibilidade depende do artigo e da validação da produção, exceto indicações expressas atribuídas ao catálogo (Trombolix e Farnes).',
'- Autoria individual e licença das imagens do catálogo não estão identificadas no ficheiro recebido; ficam registadas como não identificadas na página de créditos. Confirmar estes dados para uma futura publicação.',
'- Faltam exemplos e fotografias de produção própria da Nobrinde. Nenhuma fotografia de terceiros é apresentada como produção própria.',
'- A verificação visual do site em navegador continua pendente: a ferramenta não dispõe de navegador ligado nesta sessão.',
'']
lines += ['## Indústria — imagens e menções textuais', '', '| Produto / informação | Página PDF | Utilização |', '| --- | --- | --- |',
 '| Gratox 22075: bloco, caneta apagável e pano incluídos | 198 | `industria/index.html`, `industria/montagem-e-acabamentos.html`; menção sem fotografia em `industria/encadernacao-e-argolagem.html`. O catálogo não identifica aqui fabrico por argolagem. |',
 '| Hetien 1364: alumínio, bambu e mosquetão | 270 | `industria/montagem-e-acabamentos.html`; conferência de componentes sugerida editorialmente. |',
 '| Trombolix 22293: aplicação especial de gravação a laser | 426 | `industria/maquinas-de-gravacao-laser.html` |',
 '| Larsen 3322: saco de algodão acabado, sem inferência de confeção local | 360 | `industria/costura-industrial.html` |',
 '| Farnes 22151: placa de bambu para sublimação | 610 | `industria/sublimacao.html` |',
 '', 'As fotografias são as extrações individuais já documentadas acima. Não foram extraídas imagens de máquinas nem usadas páginas inteiras. As operações de montagem são hipóteses editoriais, não serviços confirmados.', '']
lines += ['## Guias práticos — revisão de 25/09/2026', '',
 'Páginas 198, 242, 360, 414 e 610 conferidas visualmente no PDF nesta revisão. As fotografias são as extrações já documentadas. Sem preços, códigos de impressão interpretados ou capacidades de produção inferidas.', '',
 '| Guia | Exemplos e páginas PDF (impressas) |', '| --- | --- |']
for a in ARTIGOS:
    if a['sec']=='guias':
        refs='; '.join(f"{POR_ID[id]['nome']} {POR_ID[id]['ref']} — {POR_ID[id]['pdf']} ({POR_ID[id]['impressa']})" for id in a.get('produtos_guia',[])) or 'Sem afirmações novas do catálogo; esquema original e orientação editorial/técnica.'
        lines.append(f"| `guias/{a['id']}.html` | {refs} |")
lines += ['', 'Relação das fontes técnicas e pontos para validação: `editorial/fontes-guias.md`. Os esquemas são originais em HTML/CSS e não representam amostras de cor, áreas imprimíveis ou trabalhos da Nobrinde.', '']
(ROOT/'editorial/fontes-catalogo.md').write_text('\n'.join(lines),encoding='utf-8')
print('Registo de fontes atualizado:',len(PRODUTOS),'produtos e',len(IDEIAS),'artigos editoriais.')
