(function (root) {
  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('pt-PT');
  function find(entries, query) {
    const terms = normalize(query).trim().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    return entries.map(entry => {
      const title = normalize(entry.title);
      const body = normalize(`${entry.title} ${entry.summary} ${entry.text}`);
      if (!terms.every(term => body.includes(term))) return null;
      return { entry, score: terms.reduce((score, term) => score + (title.includes(term) ? 10 : 1), 0) };
    }).filter(Boolean).sort((a, b) => b.score - a.score).map(item => item.entry);
  }
  if (typeof module !== 'undefined') module.exports = { normalize, find };
  if (typeof document === 'undefined') return;
  const form = document.querySelector('form[role="search"]');
  const input = form.querySelector('input');
  const results = document.querySelector('#search-results');
  const status = document.querySelector('#search-status');
  function render() {
    input.value = (new URLSearchParams(location.search).get('q') || '').slice(0, 160);
    results.replaceChildren();
    if (!input.value.trim()) {
      status.textContent = 'Escreva um assunto para começar, por exemplo «laser» ou «canetas».';
      return;
    }
    const matches = find(root.BRINDES_SEARCH || [], input.value);
    status.textContent = matches.length ? `${matches.length} resultado${matches.length === 1 ? '' : 's'} para «${input.value}».` : `Não encontrámos resultados para «${input.value}». Experimente menos palavras ou explore as secções abaixo.`;
    for (const entry of matches) {
      const card = document.createElement('a');
      card.className = 'topic content-card';
      card.href = entry.url;
      for (const [tag, text, className] of [['span', entry.category, 'eyebrow'], ['h2', entry.title, ''], ['p', entry.summary, ''], ['span', 'Ler →', 'arrow']]) {
        const el = document.createElement(tag);
        el.textContent = text;
        el.className = className;
        card.append(el);
      }
      results.append(card);
    }
  }
  form.addEventListener('submit', event => {
    // file:// também funciona: a submissão normal evita restrições de History API.
    if (location.protocol === 'file:') return;
    event.preventDefault();
    history.pushState({}, '', `${location.pathname}?q=${encodeURIComponent(input.value.trim())}`);
    render();
  });
  window.addEventListener('popstate', render);
  render();
})(typeof window === 'undefined' ? globalThis : window);
