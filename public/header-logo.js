// Inject Envira-North logo into the chat header (top-left, beside sidebar)
(function () {
  function injectHeaderLogo() {
    if (document.getElementById('header-logo')) return;

    // Find the header element
    var header = document.querySelector('header');
    if (!header) return;

    var logo = document.createElement('img');
    logo.id = 'header-logo';
    logo.src = '/public/enviranorth_logo.png';
    logo.alt = 'Envira-North';
    logo.style.cssText = 'height:36px;margin-left:8px;margin-right:8px;object-fit:contain;';

    // Insert after the first child (sidebar toggle button)
    var firstChild = header.firstElementChild;
    if (firstChild && firstChild.nextElementSibling) {
      header.insertBefore(logo, firstChild.nextElementSibling);
    } else {
      header.appendChild(logo);
    }
  }

  function tryInject() {
    if (document.querySelector('header')) {
      injectHeaderLogo();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryInject);
  } else {
    tryInject();
  }

  // Re-check on DOM changes (SPA navigation)
  var observer = new MutationObserver(tryInject);
  observer.observe(document.body, { childList: true, subtree: true });
})();
