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
    'cartao': foto('Papelaria, escritório e escrita', 'ig_0_nb233802_SET-CANETA-E-LAPISEIRA-BAMBU.jpg',
        'canetas-cartao.jpg', 'Estojo aberto com dois instrumentos de escrita de corpo claro e detalhes prateados.'),
    'artigo': [foto('Papelaria, escritório e escrita', 'ig_0_nb235616_ESTOJO-DE-CANETAS-TRANSPARENTE-EXPOSITOR.jpg',
        'canetas-estojo.jpg', 'Estojo transparente comprido, com base e abertura superior.', 'usos')],
 },
 'garrafas-copos-e-canecas': {
    'cartao': foto('Bebidas, refeições e cozinha', 'ig_0_nb206769_CANECA-COLORIDA-P--SUBLIMACAO.jpg',
        'bebidas-cartao.jpg', 'Três canecas brancas com pegas e interiores nas cores azul, vermelho e preto.'),
    'artigo': [foto('Bebidas, refeições e cozinha', 'ig_0_nb213896_CONJUNTO-DE-VIDRO-DE-2-PECAS-BODA.jpg',
        'bebidas-copos.jpg', 'Dois copos transparentes, de formato baixo e sem pega.', 'tipos'),
      foto('Bebidas, refeições e cozinha', 'ig_0_nb319984_Caneca-De-Cha-Termica-De-500-Ml-Mepal-Ellipse.jpg',
        'bebidas-pega.jpg', 'Recipiente cilíndrico prateado com tampa rosa e pega superior.', 'zonas')],
 },
 'texteis': {
    'cartao': foto('Têxtil, vestuário e acessórios', 'tooptshirth_1770893801_1.jpg', 'texteis-cartao.jpg',
        'Pessoa com t-shirt verde de manga curta e calções escuros.'),
    'artigo': [foto('Têxtil, vestuário e acessórios', 'tooplegging_1770900493_1.jpg', 'texteis-corte.jpg',
        'Pessoa com calças justas e top com padrão em tons azuis e brancos.', 'criterios'),
      foto('Têxtil, vestuário e acessórios', 'ig_0_nb316909_BONE-MAUI--100-POLIESTER-RECICLADO.jpg', 'texteis-bones.jpg',
        'Quatro bonés nas cores branca, preta, azul-escura e verde-escura.', 'zonas')],
 },
 'sacos-e-mochilas': {
    'cartao': foto('Sacos, mochilas e viagem', 'ig_0_nb185624_SACO.jpg', 'sacos-cartao.jpg',
        'Três sacos de duas alças, nas cores clara, branca e preta.'),
    'artigo': [foto('Sacos, mochilas e viagem', 'ig_0_nb184332_MOCHILA-DE-FALSO-TECIDO..jpg', 'sacos-cordoes.jpg',
        'Sacos de várias cores com cordões nas laterais e na abertura superior.', 'tipos'),
      foto('Sacos, mochilas e viagem', 'ig_0_nb177487_PASTA-PARA-COMPUTADOR.jpg', 'sacos-pasta.jpg',
        'Pasta preta com duas pegas, alça comprida e bolsos com fecho.', 'zonas')],
 },
 'tecnologia': {
    'cartao': foto('Tecnologia e acessórios digitais', 'ig_0_nb222616_WIRELESS-POWERBANK-VIGOR-8000-mAh-TYPE-C.jpg',
        'tecnologia-cartao.jpg', 'Telemóvel preto sobre um objeto retangular escuro; outra vista do objeto aparece abaixo.'),
    'artigo': [foto('Tecnologia e acessórios digitais', 'ig_0_nb146380_ESTACAO-METEOROLOGICA.jpg', 'tecnologia-mostrador.jpg',
        'Dispositivo de mesa prateado com ecrã azul e botões na parte inferior.', 'materiais'),
      foto('Tecnologia e acessórios digitais', 'ig_0_nb171544_AQUECEDOR-CHAVENAS-MUG.jpg', 'tecnologia-base.jpg',
        'Base circular clara com cabo e ficha USB visíveis.', 'zonas')],
 },
 'artigos-de-escritorio': {
    'cartao': foto('Papelaria, escritório e escrita', 'ig_0_nb168041_CALENDARIO-DE-MESA-PEQUENO-13-FOLHAS-PERSONALIZAVEL.jpg',
        'escritorio-cartao.jpg', 'Calendário de mesa com folhas presas por uma espiral na parte superior.'),
    'artigo': [foto('Papelaria, escritório e escrita', 'ig_0_nb138417_REGUA-COM-LUPA-E-TRANSFERIDOR-LASTA.jpg',
        'escritorio-regua.jpg', 'Régua transparente graduada com uma zona circular junto a uma extremidade.', 'usos'),
      foto('Papelaria, escritório e escrita', 'ig_0_nb137808_PORTA-ESFEROGRAFICAS.jpg', 'escritorio-suporte.jpg',
        'Suporte transparente com três instrumentos de escrita e um mostrador frontal.', 'materiais')],
 },
}


IMAGENS.update({
 'casa-decoracao-e-cuidados-pessoais': {
    'cartao': foto('Casa, decoração e cuidados pessoais', 'z_0_nb181155_MANTA-COM-PELUCHE.jpg',
        'casa-cartao.jpg', 'Manta clara enrolada com uma figura de peluche castanha à volta.'),
    'artigo': [foto('Casa, decoração e cuidados pessoais', 'ig_0_nb150658_PEGA-PIPER.jpg',
        'casa-pega.jpg', 'Três luvas de cozinha acolchoadas, nas cores vermelha, azul e branca.', 'tipos')],
 },
 'desporto-lazer-e-exterior': {
    'cartao': foto('Desporto, lazer e exterior', 'ig_0_nb223045_CADEIRA-FLENTUL.jpg',
        'desporto-cartao.jpg', 'Cadeira dobrável azul com estrutura escura e exemplos em outras cores.'),
    'artigo': [foto('Desporto, lazer e exterior', 'ig_0_nb294142_SACO-DE-DESPORTO.jpg',
        'desporto-saco.jpg', 'Saco preto e cinzento com duas pegas, alça comprida e bolso lateral.', 'usos')],
 },
 'eventos-identificacao-e-premios': {
    'cartao': foto('Eventos, identificação e prémios', 'ig_0_nb180414_CRACHA-HORIZONTAL-SIMPLES.jpg',
        'eventos-cartao.jpg', 'Porta-cartões horizontal transparente suspenso numa fita escura por uma mola.'),
    'artigo': [foto('Eventos, identificação e prémios', 'ig_0_nb216919_MEDALHA-DE-METAL.jpg',
        'eventos-medalhas.jpg', 'Três medalhas redondas com superfícies lisas em tons prateado, dourado e acobreado.', 'tipos'),
      foto('Eventos, identificação e prémios', 'ig_0_nb219910_TROFEU-FORMA-REDONDA.jpg',
        'eventos-trofeu.jpg', 'Placa redonda transparente apoiada numa base retangular transparente.', 'zonas')],
 },
 'mobilidade-ferramentas-e-seguranca': {
    'cartao': foto('Mobilidade, ferramentas e segurança', 'ig_0_nb138170_CANIVETE-COM-13-FUNCOES.jpg',
        'mobilidade-cartao.jpg', 'Ferramenta dobrável com várias peças abertas em torno de um corpo cinzento.'),
    'artigo': [foto('Mobilidade, ferramentas e segurança', 'ig_0_nb184237_FLEXOMETRO-HOMOLOGADO-DE-3-M-COMCLIP-DE-METAL-E-FRENO..jpg',
        'mobilidade-fita.jpg', 'Fita graduada parcialmente estendida de uma caixa preta e clara.', 'criterios'),
      foto('Mobilidade, ferramentas e segurança', 'ig_0_nb232636_COLETE-DE-SEGURANCA-COM-GANCHO-E-LACO-PARA-CRIANCAS-DE.jpg',
        'mobilidade-colete.jpg', 'Peça sem mangas amarela com duas faixas cinzentas horizontais e abertura frontal.', 'limites')],
 },
 'embalagem-e-apresentacao': {
    'cartao': foto('Embalagem e apresentação', 'ig_0_nb296700_ESTOJO-APRESENTACAO-DORKUS.jpg',
        'embalagem-cartao.jpg', 'Caixa retangular clara com padrão de veios e pega superior.'),
    'artigo': [foto('Embalagem e apresentação', 'ig_0_nb233041_CAIXA-DE-CARTAO-LUXE-2-PCS.jpg',
        'embalagem-transporte.jpg', 'Embalagem alta escura com duas pegas e duas aberturas na parte inferior.', 'tipos')],
 },
})


def fotos_publicas():
    return json.loads((ROOT/'assets/produtos/visuais/imagens.json').read_text(encoding='utf-8'))


CREDITOS = ('<section id="produtos-ilustrativos"><h2>Fotografias ilustrativas de Produtos</h2>'
    '<p>As fotografias são elementos visuais: não identificam modelos nem sustentam '
    'composição, desempenho ou compatibilidade de personalização. Os visuais abrangem '
    'as dez áreas: escrita e escritório, tecnologia, bebidas e cozinha, sacos e viagem, '
    'têxteis, casa, desporto, eventos, mobilidade e embalagem. Imagens de utensílios, '
    'peças vestíveis ou ferramentas não comprovam proteção ou certificação.</p>'
    '<p>Autoria e licença de terceiros não identificadas nos registos disponíveis. '
    'Não se atribui uma licença aberta a estas imagens.</p></section>')
