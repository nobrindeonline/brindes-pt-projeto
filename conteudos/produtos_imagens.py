"""Seleção visual local. Nomes de origem ficam na fonte e no registo privado.

Só o manifesto público derivado é usado pelo HTML e pelo JSON de Produtos.
Nenhum nome de ficheiro é usado para descrever materiais ou características.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def foto(pasta, original, nome_publico, alt, secao=None):
    return dict(original=f'assets/produtos/{pasta}/{original}', nome_publico=nome_publico,
                alt=alt, secao=secao)


IMAGENS = {
 'canetas-e-escrita': {
    'cartao': foto('CanetaseEscrita', 'ig_0_nb233802_SET-CANETA-E-LAPISEIRA-BAMBU.jpg',
        'canetas-cartao.jpg', 'Estojo aberto com dois instrumentos de escrita de corpo claro e detalhes prateados.'),
    'artigo': [foto('CanetaseEscrita', 'ig_0_nb235616_ESTOJO-DE-CANETAS-TRANSPARENTE-EXPOSITOR.jpg',
        'canetas-estojo.jpg', 'Estojo transparente comprido, com base e abertura superior.', 'usos')],
 },
 'garrafas-copos-e-canecas': {
    'cartao': foto('GarrafasCoposCanecas', 'ig_0_nb206769_CANECA-COLORIDA-P--SUBLIMACAO.jpg',
        'bebidas-cartao.jpg', 'Três canecas brancas com pegas e interiores nas cores azul, vermelho e preto.'),
    'artigo': [foto('GarrafasCoposCanecas', 'ig_0_nb213896_CONJUNTO-DE-VIDRO-DE-2-PECAS-BODA.jpg',
        'bebidas-copos.jpg', 'Dois copos transparentes, de formato baixo e sem pega.', 'tipos'),
      foto('GarrafasCoposCanecas', 'ig_0_nb319984_Caneca-De-Cha-Termica-De-500-Ml-Mepal-Ellipse.jpg',
        'bebidas-pega.jpg', 'Recipiente cilíndrico prateado com tampa rosa e pega superior.', 'zonas')],
 },
 'texteis': {
    'cartao': foto('Texteis', 'tooptshirth_1770893801_1.jpg', 'texteis-cartao.jpg',
        'Pessoa com t-shirt verde de manga curta e calções escuros.'),
    'artigo': [foto('Texteis', 'tooplegging_1770900493_1.jpg', 'texteis-corte.jpg',
        'Pessoa com calças justas e top com padrão em tons azuis e brancos.', 'criterios'),
      foto('Texteis', 'ig_0_nb316909_BONE-MAUI--100-POLIESTER-RECICLADO.jpg', 'texteis-bones.jpg',
        'Quatro bonés nas cores branca, preta, azul-escura e verde-escura.', 'zonas')],
 },
 'sacos-e-mochilas': {
    'cartao': foto('SacoseMochilas', 'ig_0_nb185624_SACO.jpg', 'sacos-cartao.jpg',
        'Três sacos de duas alças, nas cores clara, branca e preta.'),
    'artigo': [foto('SacoseMochilas', 'ig_0_nb184332_MOCHILA-DE-FALSO-TECIDO..jpg', 'sacos-cordoes.jpg',
        'Sacos de várias cores com cordões nas laterais e na abertura superior.', 'tipos'),
      foto('SacoseMochilas', 'ig_0_nb177487_PASTA-PARA-COMPUTADOR.jpg', 'sacos-pasta.jpg',
        'Pasta preta com duas pegas, alça comprida e bolsos com fecho.', 'zonas')],
 },
 'tecnologia': {
    'cartao': foto('Tecnologia', 'ig_0_nb222616_WIRELESS-POWERBANK-VIGOR-8000-mAh-TYPE-C.jpg',
        'tecnologia-cartao.jpg', 'Telemóvel preto sobre um objeto retangular escuro; outra vista do objeto aparece abaixo.'),
    'artigo': [foto('Tecnologia', 'ig_0_nb146380_ESTACAO-METEOROLOGICA.jpg', 'tecnologia-mostrador.jpg',
        'Dispositivo de mesa prateado com ecrã azul e botões na parte inferior.', 'materiais'),
      foto('Tecnologia', 'ig_0_nb171544_AQUECEDOR-CHAVENAS-MUG.jpg', 'tecnologia-base.jpg',
        'Base circular clara com cabo e ficha USB visíveis.', 'zonas')],
 },
 'artigos-de-escritorio': {
    'cartao': foto('Artigosdeescritorio', 'ig_0_nb168041_CALENDARIO-DE-MESA-PEQUENO-13-FOLHAS-PERSONALIZAVEL.jpg',
        'escritorio-cartao.jpg', 'Calendário de mesa com folhas presas por uma espiral na parte superior.'),
    'artigo': [foto('Artigosdeescritorio', 'ig_0_nb138417_REGUA-COM-LUPA-E-TRANSFERIDOR-LASTA.jpg',
        'escritorio-regua.jpg', 'Régua transparente graduada com uma zona circular junto a uma extremidade.', 'usos'),
      foto('Artigosdeescritorio', 'ig_0_nb137808_PORTA-ESFEROGRAFICAS.jpg', 'escritorio-suporte.jpg',
        'Suporte transparente com três instrumentos de escrita e um mostrador frontal.', 'materiais')],
 },
}


def fotos_publicas():
    return json.loads((ROOT/'assets/produtos/visuais/imagens.json').read_text(encoding='utf-8'))


CREDITOS = ('<section id="produtos-ilustrativos"><h2>Fotografias ilustrativas de Produtos</h2>'
    '<p>As fotografias são elementos visuais: não identificam modelos nem sustentam '
    'composição, desempenho ou compatibilidade de personalização.</p>'
    '<p>Autoria e licença de terceiros não identificadas nos registos disponíveis. '
    'Não se atribui uma licença aberta a estas imagens.</p></section>')
