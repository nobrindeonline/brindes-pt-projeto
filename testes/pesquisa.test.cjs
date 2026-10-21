const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const { find } = require('../pesquisa.js');
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(require.resolve('../assets/pesquisa-dados.js'), 'utf8'), context);
const entries = context.window.BRINDES_SEARCH;

test('Guias indexa perguntas, critérios e evidência sem exemplos comerciais', () => {
  for (const [query, slug] of [
    ['PDF vetorial', 'como-preparar-um-logotipo'],
    ['quantidade variantes', 'como-escolher-a-tecnica'],
    ['distribuição transporte', 'como-escolher-brindes-para-um-evento'],
    ['revestimento cuidados', 'como-escolher-o-material'],
    ['CMYK referência', 'pantone-cmyk-e-cor-final'],
    ['maquete orientação', 'como-avaliar-uma-maquete'],
    ['bordado franzido', 'problemas-comuns-na-personalizacao'],
  ]) assert.ok(find(entries, query).some(e => e.url === `guias/${slug}.html`), query);
  for (const e of entries.filter(e => e.url.startsWith('guias/'))) {
    assert.ok(!/nobrinde|catálogo|catalogue|synex|gratox|chalmer|farnes|larsen/i.test(JSON.stringify(e)));
  }
});

test('Produtos encontra sinónimos e critérios específicos das famílias', () => {
  for (const [query, slug] of [
    ['esferografica', 'canetas-e-escrita'],
    ['rollerball', 'canetas-e-escrita'],
    ['tumbler', 'garrafas-copos-e-canecas'],
    ['tshirt', 'texteis'],
    ['saco a tiracolo', 'sacos-e-mochilas'],
    ['power bank', 'tecnologia'],
    ['USB-C', 'tecnologia'],
    ['papelaria', 'artigos-de-escritorio'],
    ['coleccao', 'brindes-premium'],
    ['velas manta', 'casa-decoracao-e-cuidados-pessoais'],
    ['cadeira piquenique', 'desporto-lazer-e-exterior'],
    ['pulseiras medalhas', 'eventos-identificacao-e-premios'],
    ['lanternas ferramentas', 'mobilidade-ferramentas-e-seguranca'],
    ['separadores encaixe', 'embalagem-e-apresentacao'],
    ['lancheiras utensílios', 'garrafas-copos-e-canecas'],
    ['dobráveis viagem', 'sacos-e-mochilas'],
  ]) {
    assert.ok(find(entries, query).some(e => e.url === `produtos/${slug}.html`), query);
  }
});
test('pesquisa sem acentos ou distinção de maiúsculas', () => {
  assert.equal(find(entries, 'GRAVACAO')[0].title, 'Gravação a laser');
  assert.equal(find(entries, 'serigrafia')[0].title, 'Serigrafia');
});
test('todos os termos têm de ocorrer; títulos têm prioridade', () => {
  assert.equal(find(entries, 'digital uv')[0].title, 'Impressão digital UV');
  assert.equal(find(entries, 'canetas')[0].title, 'Canetas e escrita');
  assert.equal(find(entries, 'laser inexistente123').length, 0);
});
test('pesquisa vazia, desconhecida e texto de HTML são seguros', () => {
  for (const q of ['', '   ', 'xyz987654', '<script>alert(1)</script>']) assert.equal(find(entries, q).length, 0);
});
test('DTF conduz ao guia publicado de processos', () => {
  const found = find(entries, 'DTF');
  assert.ok(found.length > 0);
  assert.ok(found.some(e => e.url === 'industria/dtf-e-prensas-termicas.html'));
  assert.ok(found.some(e => e.url === 'tecnicas/dtf.html'));
});

test('as designações dos transfers encontram os respetivos guias', () => {
  for (const [query, slug] of [
    ['transfers', 'transfers'],
    ['transfer serigrafico', 'transfer-serigrafico'],
    ['transfer digital', 'transfer-digital'],
    ['transfer digital com base', 'transfer-digital-com-base'],
    ['base branca', 'transfer-digital-com-base'],
  ]) {
    assert.ok(find(entries, query).some(e => e.url === `tecnicas/${slug}.html`), query);
  }
});
test('sublimação encontra a técnica e preserva o guia de equipamentos', () => {
  for (const query of ['sublimação', 'SUBLIMACAO']) {
    const urls = find(entries, query).map(entry => entry.url);
    assert.ok(urls.includes('tecnicas/tecnica-sublimacao.html'));
    assert.ok(urls.includes('industria/sublimacao.html'));
  }
});

test('Para quem encontra os oito guias por destinatário e contexto', () => {
  for (const [query, slug] of [
    ['integração colaboradores', 'empresas'],
    ['feiras locais voluntários', 'camaras-municipais'],
    ['alunos idade calendário', 'escolas'],
    ['atletas voluntários equipamento', 'clubes-desportivos'],
    ['comparação destinatários material', 'revendedores'],
    ['expositores inscrição participantes', 'eventos'],
    ['hóspedes visitas guiadas', 'turismo-alojamento'],
    ['voluntários sensibilização comunidade', 'associacoes-organizacoes-comunitarias'],
  ]) {
    assert.ok(find(entries, query).some(entry => entry.url === `publicos/${slug}.html`), query);
  }
  for (const entry of entries.filter(item => item.url.startsWith('publicos/'))) {
    assert.ok(!/nobrinde|catálogo|catalogue|\bSKU\b|gratox|sulkan|larsen|synex/i.test(JSON.stringify(entry)));
  }
});

test('troquelagem encontra a técnica, operações e o guia de indústria existente', () => {
  const urls = find(entries, 'TROQUELAGEM').map(entry => entry.url);
  assert.ok(urls.includes('tecnicas/tecnica-troquelagem.html'));
  assert.ok(urls.includes('industria/troquelagem.html'));
  for (const query of ['kiss-cut', 'vincagem', 'perfuração', 'etiqueta base', 'amostra troquel']) {
    assert.ok(find(entries, query).some(entry => entry.url === 'tecnicas/tecnica-troquelagem.html'), query);
  }
});

test('crachás automáticos encontra o guia delimitado a pin/botão e preserva Indústria', () => {
  for (const query of ['crachas automaticos', 'CRACHÁS', 'pin', 'gabarito', 'selagem']) {
    assert.ok(find(entries, query).some(entry => entry.url === 'tecnicas/crachas-automaticos.html'), query);
  }
  assert.ok(find(entries, 'crachas').some(entry => entry.url === 'industria/producao-de-crachas.html'));
});

test('montagem encontra o hub e distingue os guias novos dos artigos de Indústria', () => {
  for (const [query, slug] of [
    ['costura argolagem encadernacao', 'costura-argolagem-e-encadernacao'],
    ['COSTURA INDUSTRIAL', 'tecnica-costura-industrial'],
    ['argolagem', 'argolagem'],
    ['encadernacao', 'encadernacao'],
    ['espiral', 'argolagem'],
    ['lombada', 'encadernacao'],
  ]) {
    assert.ok(find(entries, query).some(e => e.url === `tecnicas/${slug}.html`), query);
  }
  assert.ok(find(entries, 'costura').some(e => e.url === 'industria/costura-industrial.html'));
  assert.ok(find(entries, 'argolagem').some(e => e.url === 'industria/encadernacao-e-argolagem.html'));
});
