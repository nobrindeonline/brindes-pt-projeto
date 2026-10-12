"""Apresentação e exportação geradas da fonte semântica de Produtos."""
from html import escape
import json
import re
from conteudos.produtos import PRODUTOS, FONTES_PRODUTOS, exportacao_publica
from conteudos.produtos_imagens import fotos_publicas

POR_ID = {g['id']: g for g in PRODUTOS}


def media(foto, caption=False):
    imagem = ('<img src="../' + escape(foto['url'], quote=True) + '" alt="' +
        escape(foto['alt'], quote=True) + '" width="' + str(foto['width']) +
        '" height="' + str(foto['height']) + '" loading="lazy" decoding="async">')
    if not caption:
        return '<figure class="idea-media product-media"><div class="idea-images">' + imagem + '</div></figure>'
    return ('<figure class="product-illustration"><div class="product-illustration-frame">' + imagem +
        '</div><figcaption>Fotografia ilustrativa. <a href="../creditos-imagens.html#produtos-ilustrativos">'
        'Créditos da imagem</a></figcaption></figure>')


def referencias(texto):
    def substituir(m):
        k = m.group(1)
        f = FONTES_PRODUTOS[k]
        return f'<a class="source-ref" href="#fonte-{k}" aria-label="Fonte: {escape(f["entidade"])}">↗</a>'
    return re.sub(r'\[([a-z]+)\]', substituir, escape(texto))


def render_guia(g, artigos, shell, link, card):
    def lista(items):
        return '<ul>' + ''.join('<li>' + referencias(t) + '</li>' for t in items) + '</ul>'

    def destino(id):
        a = artigos[id]
        return link('../' + a['sec'] + '/' + id + '.html', a['titulo'])

    secoes = []
    tipos = ''.join('<div class="product-variant"><h3>' + escape(v['nome']) + '</h3><p>' +
        referencias(v['descricao']) + '</p><p><strong>Compare:</strong> ' + referencias(v['comparar']) +
        '</p><p><strong>Contexto possível:</strong> ' + referencias(v['contexto']) + '</p></div>' for v in g['tipos'])
    secoes.append(('tipos', 'Tipos e variantes' if g['categoria'] == 'familia' else 'Formas de compor a seleção', tipos))
    secoes.append(('usos', 'Usos e contextos', lista(g['usos_contextos'])))
    secoes.append(('criterios', 'O que comparar', lista(g['criterios_escolha'])))
    componentes = ''.join('<div class="product-component"><h3>' + escape(c['parte']) + '</h3><p>' +
        escape(' · '.join(c['materiais'])) + '</p><p>' + referencias(c['confirmar']) + '</p><p>' +
        destino(c['guia_id']) + '</p></div>' for c in g['materiais_componentes'])
    secoes.append(('materiais', 'Materiais e componentes', '<p>São possibilidades a identificar no artigo escolhido. Confirme a composição de cada parte; os materiais de uma variante não descrevem toda a família.</p>' + componentes))
    zonas = ''.join('<li><strong>' + escape(z['nome']) + ':</strong> ' + referencias(z['condicao']) + '</li>' for z in g['zonas_personalizacao'])
    secoes.append(('zonas', 'Zonas de personalização', '<ul>' + zonas + '</ul>'))
    tecnicas = '<p>Possibilidades gerais para comparar. A aplicação depende do artigo, da superfície, do desenho e das condições do processo; não está confirmada para um artigo específico.</p>'
    tecnicas += ''.join('<div class="product-method"><h3>' + destino(t['id']) + '</h3><p>' + referencias(t['condicoes']) + '</p></div>' for t in g['tecnicas_relacionadas'])
    secoes.append(('tecnicas', 'Técnicas e condições', tecnicas))
    secoes.append(('limites', 'Limitações e cuidados', lista(g['limitacoes']) + lista(g['cuidados'])))
    secoes.append(('perguntas', 'Antes de decidir', lista(g['perguntas_antes_de_decidir'])))
    perguntas = ''.join('<details class="product-faq"><summary>' + escape(f['pergunta']) + '</summary><p>' + referencias(f['resposta']) + '</p></details>' for f in g['perguntas_frequentes'])
    secoes.append(('faq', 'Perguntas frequentes', perguntas))
    fontes = '<p>As referências sustentam os factos identificados no texto. Os tipos, contextos e critérios de escolha são orientação editorial; as instruções de um fabricante aplicam-se ao seu próprio âmbito.</p><ul class="sources">'
    for k in g['fontes']:
        f = FONTES_PRODUTOS[k]
        fontes += '<li id="fonte-' + k + '">' + link(f['url'], f['titulo']) + '<br>' + escape(f['entidade']) + ' · Consulta: <time datetime="' + f['data_consulta'] + '">12 de outubro de 2026</time><p>' + escape(f['ambito']) + '</p></li>'
    secoes.append(('fontes', 'Fontes e âmbito', fontes + '</ul>'))
    toc = ''.join(link('#' + id, titulo) for id, titulo, _ in secoes)
    fotografias = fotos_publicas().get(g['id'], {}).get('artigo', [])
    corpo = ''.join('<section id="' + id + '"><h2>' + titulo + '</h2>' + texto +
        ''.join(media(f, True) for f in fotografias if f['secao'] == id) + '</section>' for id, titulo, texto in secoes)
    etiqueta = 'Família de produtos' if g['categoria'] == 'familia' else 'Coleção editorial · Várias famílias'
    intro = '<nav class="crumb" aria-label="Percurso">' + link('../index.html','Início') + ' / ' + link('index.html','Produtos') + ' / <span>' + escape(g['titulo']) + '</span></nav>'
    intro += '<div class="page-intro"><span class="eyebrow">' + etiqueta + '</span><h1>' + escape(g['titulo']) + '</h1><p>' + escape(g['resumo']) + '</p><p class="documentary-date">Revisão documental: <time datetime="' + g['data_revisao'] + '">12 de outubro de 2026</time></p></div>'
    relacionados = '<section><h2>Continue a explorar</h2><div class="article-grid">' + ''.join(card(artigos[id], '../') for id in g['relacionados']) + '</div></section>'
    conteudo = intro + '<div class="reading-layout"><aside class="contents"><strong>Neste guia</strong><nav aria-label="Índice do artigo">' + toc + '</nav></aside><article class="reading">' + corpo + '</article></div>' + relacionados + '<a class="back-to-ideas" href="index.html">← Voltar a Produtos</a>'
    return shell(g['titulo'], g['resumo'], conteudo, '../', 'produtos')


def render_entrada(shell, link):
    familias = [g for g in PRODUTOS if g['categoria'] == 'familia']
    fotografias = fotos_publicas()
    cards = ''.join('<article class="idea-card product-family-card" id="' + g['ancora'] + '">' +
        media(fotografias[g['id']]['cartao']) + '<div class="idea-card-copy"><span class="eyebrow">Guia de família</span><h2>' +
        escape(g['titulo']) + '</h2><p>' + escape(g['resumo']) + '</p><a class="link idea-read-more" href="' +
        g['slug'] + '.html" aria-label="Explorar o guia: ' + escape(g['titulo'], quote=True) +
        '">Explorar o guia <span aria-hidden="true">→</span></a></div></article>' for g in familias)
    intro = '<nav class="crumb" aria-label="Percurso">' + link('../index.html','Início') + ' / Produtos</nav><div class="page-intro"><span class="eyebrow">Compreender e comparar</span><h1>Produtos</h1><p>Explore famílias de brindes pela utilização, construção e personalização. Cada guia ajuda a comparar variantes e a preparar as perguntas sobre o artigo escolhido.</p></div>'
    grelha = '<section class="product-family-list" aria-label="Guias das famílias"><div class="ideas-grid products-grid">' + cards + '</div></section>'
    ajuda = '<section class="note"><h2>Ainda não sabe por onde começar?</h2><p>Defina a utilização e quem vai receber o artigo. Depois compare materiais e a área onde pretende a mensagem.</p><div class="context-links">' + link('../guias/como-escolher-brindes-para-um-evento.html','Escolher pelo uso num evento') + link('../publicos/index.html','Pensar no destinatário') + link('../guias/como-escolher-o-material.html','Comparar materiais') + link('../guias/como-escolher-a-tecnica.html','Escolher a personalização') + '</div></section>'
    premium = POR_ID['brindes-premium']
    colecao = '<section id="premium" class="product-collection"><span class="eyebrow">Seleção transversal</span><h2>Premium: utilidade e apresentação</h2><p>' + escape(premium['resumo']) + ' A designação não garante qualidade superior.</p>' + link('brindes-premium.html','Explorar a coleção editorial →') + '</section>'
    return shell('Produtos', 'Guias para compreender e comparar seis famílias de brindes e uma seleção editorial transversal.', intro + grelha + ajuda + colecao, '../', 'produtos')


def dados_publicos(artigos):
    dados = exportacao_publica()
    fotografias = fotos_publicas()
    def destino(id):
        a = artigos[id]
        return dict(id=id, titulo=a['titulo'], url=a['sec'] + '/' + id + '.html')
    for g in dados['conteudos']:
        if g['id'] in fotografias: g['imagens'] = fotografias[g['id']]
        g['relacionados'] = [destino(id) for id in g['relacionados']]
        for c in g['materiais_componentes']:
            c['guia'] = destino(c.pop('guia_id'))
        for t in g['tecnicas_relacionadas']:
            t.update(destino(t['id']))
    def resolver_citacoes(node):
        if isinstance(node, list):
            for item in node: resolver_citacoes(item)
        elif isinstance(node, dict):
            citacoes = []
            for campo, valor in list(node.items()):
                if isinstance(valor, str):
                    keys = list(dict.fromkeys(re.findall(r'\[([a-z]+)\]', valor)))
                    if keys:
                        node[campo] = re.sub(r'\s*\[([a-z]+)\]', '', valor)
                        citacoes.append(dict(campo=campo, fontes=keys))
                elif isinstance(valor, list):
                    for indice, item in enumerate(valor):
                        if isinstance(item, str):
                            keys = list(dict.fromkeys(re.findall(r'\[([a-z]+)\]', item)))
                            if keys:
                                valor[indice] = re.sub(r'\s*\[([a-z]+)\]', '', item)
                                citacoes.append(dict(campo=campo, indice=indice, fontes=keys))
                        else:
                            resolver_citacoes(item)
                else:
                    resolver_citacoes(valor)
            if citacoes: node['citacoes'] = citacoes
    resolver_citacoes(dados)
    return json.dumps(dados, ensure_ascii=False, indent=2) + '\n'
