const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const { find } = require('../pesquisa.js');
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(require.resolve('../assets/pesquisa-dados.js'), 'utf8'), context);
const entries = context.window.BRINDES_SEARCH;
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
});
test('sublimação encontra a técnica e preserva o guia de equipamentos', () => {
  for (const query of ['sublimação', 'SUBLIMACAO']) {
    const urls = find(entries, query).map(entry => entry.url);
    assert.ok(urls.includes('tecnicas/tecnica-sublimacao.html'));
    assert.ok(urls.includes('industria/sublimacao.html'));
  }
});
