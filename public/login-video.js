// Inject fan video on the login page, remove after login
(function () {
  function isLoginPage() {
    var form = document.querySelector('form');
    return form && form.querySelector('input[type="password"]');
  }

  function injectVideo() {
    if (!isLoginPage()) return;
    if (document.querySelector('.login-video-container')) return;

    var container = document.createElement('div');
    container.className = 'login-video-container';
    container.innerHTML =
      '<video autoplay muted loop playsinline>' +
      '<source src="/public/moving_fan_video.mp4" type="video/mp4">' +
      '</video>' +
      '<div class="login-video-overlay"></div>';

    document.body.appendChild(container);
  }

  function removeVideo() {
    var el = document.querySelector('.login-video-container');
    if (el) el.remove();
  }

  function sync() {
    if (isLoginPage()) {
      injectVideo();
    } else {
      removeVideo();
    }
  }

  // Initial check
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', sync);
  } else {
    sync();
  }

  // Watch for SPA route changes
  var observer = new MutationObserver(sync);
  observer.observe(document.body, { childList: true, subtree: true });
})();
