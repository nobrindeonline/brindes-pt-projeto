"""Remove identidade da entidade mantenedora e registos internos da saída pública."""
import html
import re


def remover_creditos_imagens(documento):
    """Remove atribuições visíveis; conserva descrições e fontes de conteúdo."""
    documento = re.sub(r'<a\b[^>]*href=["\'][^"\']*creditos-imagens\.html[^"\']*["\'][^>]*>.*?</a\s*>', '', documento, flags=re.S | re.I)
    documento = re.sub(r'<(?P<credito_tag>span|strong)\b[^>]*>\s*(?:Fotografia:|Imagem provisória[^<]*origem).*?</(?P=credito_tag)\s*>', '', documento, flags=re.S | re.I)

    def legenda(m):
        conteudo = m[1]
        conteudo = re.sub(r'Fotografia:.*?(?=</figcaption>|$)', '', conteudo, flags=re.S | re.I)
        conteudo = re.sub(r'(?:Autoria|Autor e licença|Origem e licença)\b.*$', '', conteudo, flags=re.S | re.I)
        conteudo = re.sub(r'(?:\s|&nbsp;)*(?:[·—|]\s*)+$', '', conteudo)
        conteudo = re.sub(r'<(?:span|strong)\b[^>]*>\s*</(?:span|strong)>', '', conteudo)
        return '<figcaption>'+conteudo.strip()+'</figcaption>' if re.sub(r'<[^>]+>', '', conteudo).strip() else ''

    documento = re.sub(r'<figcaption\b[^>]*>(.*?)</figcaption>', legenda, documento, flags=re.S | re.I)
    documento = re.sub(r'<p\b[^>]*class="montagem-credits"[^>]*>.*?</p>', '', documento, flags=re.S)
    documento = re.sub(r'As fontes de contexto não são créditos fotográficos\.', '', documento)
    documento = re.sub(r'\s*Créditos (?:da imagem|das imagens|de imagens)', '', documento, flags=re.I)
    documento = re.sub(r'Nas quatro imagens locais, autoria fotográfica, licença e ligação ao registo original continuam por confirmar; os créditos distinguem essa lacuna das fontes históricas\.', '', documento)
    documento = re.sub(r'<(p|nav)\b[^>]*>\s*</\1>', '', documento, flags=re.S)
    return documento


def texto_publico(texto, permitir_empresa=False):
    partes = re.split(r'(?<=[.!?])\s+', texto)
    return ' '.join(p for p in partes if not re.search(
        ('' if permitir_empresa else r'nobrinde|') + r'revisão (?:editorial|documental)|auditoria interna|'
        r'(?:utilização|uso).*solicitad[oa].*utilizador|'
        r'(?:origem e autorização|autorização de publicação).*confirmar|'
        r'(?:ficheiro|imagens?).*(?:fornecid[oa]s? pela equipa|indicad[oa].*utilizador)|'
        r'referência interna|registo de aprovação|'
        r'utilizador.*autoriz|autoriz.*utilizador|'
        r'autoria.*(?:pendente|documentar)|documentação.*pendente|'
        r'(?:fornecid[oa]|indicad[oa]).*utilizador', p, re.I))


def corrigir_ligacoes(documento):
    # A remoção anterior dos exemplos deixou ligações órfãs. Os créditos
    # genéricos conservam os registos de licença sem expor fichas de produto.
    documento = re.sub(r'<a\b[^>]*href="#exemplos-catalogo"[^>]*>.*?</a>', '', documento, flags=re.S)
    documento = re.sub(r'(creditos-imagens\.html#catalogo)-[a-z0-9-]+', r'\1', documento)
    return remover_creditos_imagens(documento)


def pagina_publica(documento, permitir_empresa=False):
    documento = corrigir_ligacoes(documento)
    documento = re.sub(r'<section\b[^>]*class="(?:catalogue-examples|audience-selection)"[^>]*>.*?</section>', '', documento, flags=re.S)
    documento = re.sub(r'<p\b[^>]*class="catalogue-intro"[^>]*>.*?</p>', '', documento, flags=re.S)
    documento = re.sub(r'<li\b[^>]*>[^<]*General Catalogue.*?</li>', '', documento, flags=re.S)
    documento = re.sub(r'<figcaption\b[^>]*>\s*Fotografias do catálogo\..*?</figcaption>',
        '<figcaption>Fotografias ilustrativas. <a href="../creditos-imagens.html#catalogo">Créditos das imagens</a></figcaption>', documento, flags=re.S)
    documento = re.sub(r'<section\b[^>]*id="catalogo"[^>]*>.*?</section>',
        '<section id="catalogo"><h2>Fotografias ilustrativas de artigos</h2>'
        '<p>Autoria individual e licença de reutilização não identificadas. '
        'Não se atribui uma licença aberta a estas fotografias.</p></section>', documento, flags=re.S)
    documento = re.sub(r'<footer\b[^>]*>.*?</footer>',
        '<footer class="footer"><div class="wrap foot-inner">'
        '<div class="footer-library"><p>brindes.pt — Biblioteca informativa independente. '
        'Informação para compreender, comparar e escolher.</p></div>'
        '<nav class="footer-links" aria-label="Informação do site">'
        '<a href="' + ('../' if 'href="../assets/css/styles.css"' in documento else '') +
        'creditos-imagens.html">Créditos de imagens</a></nav></div></footer>',
        documento, flags=re.S | re.I)
    documento = re.sub(r'<div\b[^>]*class="review"[^>]*>.*?</div>', '', documento, flags=re.S)
    if not permitir_empresa:
        documento = re.sub(r'<img\b[^>]*nobrinde[^>]*>', '', documento, flags=re.S | re.I)
    documento = re.sub(r'<div class="print">nobrinde</div>', '<div class="print">brindes.pt</div>', documento, flags=re.I)

    def limpar_bloco(m):
        original = m.group('body')
        simples = html.unescape(re.sub(r'<[^>]+>', '', original))
        simples = re.sub(r'\s+', ' ', simples).strip()
        if not re.search(('' if permitir_empresa else r'nobrinde|') + r'origem e autorização|autorização de publicação|'
                         r'solicitad[oa].*utilizador|indicad[oa].*utilizador|'
                         r'fornecid[oa]s? pela equipa|referência interna|'
                         r'utilizador|autoria.*(?:pendente|documentar)|documentação.*pendente', simples, re.I):
            return m.group(0)
        limpo = texto_publico(simples, permitir_empresa=permitir_empresa)
        # Preserva ligações de atribuição, sem expor a tramitação editorial.
        creditos = re.findall(r'<a\b[^>]*href="[^"]*creditos-imagens[^>]*>.*?</a>', original, re.S)
        if creditos:
            limpo += ' ' + ' '.join(re.sub(r'>.*?</a>', '>Créditos da imagem</a>', a, flags=re.S) for a in creditos)
        return m.group('open') + (limpo if creditos else html.escape(limpo)) + m.group('close')

    documento = re.sub(r'(?P<open><(?P<tag>p|figcaption|span|li)\b[^>]*>)(?P<body>.*?)(?P<close></(?P=tag)>)', limpar_bloco, documento, flags=re.S)
    if not permitir_empresa:
        documento = re.sub(r'(<meta\b[^>]*content=")[^"]*Nobrinde[^"]*(")', r'\1Biblioteca informativa independente sobre brindes, materiais e técnicas de personalização.\2', documento, flags=re.I | re.S)
    documento = documento.replace('Origem e autorização de utilização', 'Créditos das imagens')
    documento = documento.replace('Estado dos créditos', 'Créditos das imagens')
    documento = re.sub(r'Estas licenças aplicam-se.*?site completo\.',
        'Estas licenças aplicam-se apenas às respetivas fotografias.', documento, flags=re.S)
    documento = re.sub(r'<strong>Imagem provisória:.*?</strong>', '', documento, flags=re.S)
    return remover_creditos_imagens(documento)
