"""Seleção visual dos Guias, sem usar nomes de origem nos dados públicos."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def foto(pasta, ficheiro, nome_publico, alt, secao=None, legenda=None):
    return dict(original=f'assets/guias/{pasta}/{ficheiro}', nome_publico=nome_publico,
                alt=alt, secao=secao, legenda=legenda)

IMAGENS_GUIAS = {
 'como-escolher-a-tecnica': dict(cartao=foto('ComoEscolheraTecnica','images.jpg','tecnica-cartao.jpg',
     'Três t-shirts, cinzenta, escura e branca, penduradas em cabides com desenhos na frente.'), artigo=[]),
 'como-escolher-brindes-para-um-evento': dict(cartao=foto('ComoEscolherBrindesEvento','brindes-para-feiras.jpg','evento-cartao.jpg',
     'Duas pessoas seguram um instrumento de escrita junto a uma mesa com cestos e cadernos.'), artigo=[]),
 'como-escolher-o-material': dict(cartao=foto('ComoEscolheroMaterialdeUmBrinde','images.jpg','material-cartao.jpg',
     'Conjunto de recipientes, cadernos, pastas e estojos sobre um fundo cinzento.'), artigo=[]),
 'como-avaliar-uma-maquete': dict(cartao=foto('Como avaliarumamaqueteantesdaprodução','melhores-empresas-brindes-em-portugal.jpg','maquete-cartao.jpg',
     'Saco, garrafa, caneca, caderno, lápis e porta-chaves dispostos sobre um fundo claro, com marcações genéricas.'),
     artigo=[foto('Como avaliarumamaqueteantesdaprodução','images.jpg','maquete-composicao.jpg',
         'Composição com recipientes, estojos, sacos e outros objetos com textos e marcas genéricas.', 'parte-3',
         'Composição ilustrativa: a representação de vários objetos não comprova materiais, funções ou resultados físicos.')]),
 'pantone-cmyk-e-cor-final': dict(cartao=foto('PantoneCMYKeacorfinaldobrinde','gp6102b-pantone-graphics-color-bridge-coated-uncoated-guides-product-2-1_2-sk5dvkob7f.webp','cor-cartao.webp',
     'Dois leques de amostras de cor abertos sobre um fundo claro.'),
     artigo=[foto('PantoneCMYKeacorfinaldobrinde','pantone-brindes-promocionais-1024x569.jpg','cor-suporte.jpg',
         'Recipiente verde sobre leques e folhas com amostras coloridas.', 'parte-2',
         'Fotografia ilustrativa de um suporte junto a amostras. A imagem de ecrã não constitui uma referência física de cor.')]),
}

def fotos_publicas_guias():
    return json.loads((ROOT/'assets/guias/visuais/imagens.json').read_text(encoding='utf-8'))

CREDITOS_GUIAS = ('<section id="guias-ilustrativos"><h2>Imagens ilustrativas dos Guias</h2>'
    '<p>As imagens ilustram composição, entrega e comparação visual. Não identificam '
    'artigos comerciais nem comprovam materiais, funções, compatibilidade ou resultados técnicos.</p>'
    '<p>Autoria e licença de terceiros não identificadas nos registos disponíveis. '
    'Não se atribui uma licença aberta a estas imagens. Os esquemas de decisão e '
    'as ilustrações de conceitos são originais do brindes.pt.</p></section>')
