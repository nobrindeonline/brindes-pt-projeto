// Índice de leitura: aberto em computador e expansível em ecrãs pequenos.
(() => {
  const index = document.querySelector('#guia-indice');
  if (!index) return;
  const smallScreen = window.matchMedia('(max-width: 850px)');
  const adjust = () => { index.open = !smallScreen.matches; };
  adjust();
  smallScreen.addEventListener('change', adjust);
  index.addEventListener('click', event => {
    if (smallScreen.matches && event.target.closest('a[href^="#"]')) index.open = false;
  });
})();
