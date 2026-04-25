// === Login page fan video ===
(function () {
  function isLoginPage() {
    var form = document.querySelector('form');
    // Check for password OR text input (password field toggles type on show/hide)
    return form && (form.querySelector('input[type="password"]') || form.querySelector('input[name="password"]') || form.querySelector('input[autocomplete="current-password"]'));
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

    // Hide Chainlit's default login page decoration (large avatar on right half)
    hideLoginDecoration();
  }

  function hideLoginDecoration() {
    // Chainlit renders a large logo/avatar on the right side of the login page
    // Target common patterns: large images or SVGs outside the form
    var form = document.querySelector('form');
    if (!form) return;
    var formParent = form.parentElement;
    if (!formParent) return;

    // Walk up to find the login page root container
    var loginRoot = formParent;
    while (loginRoot.parentElement && loginRoot.parentElement !== document.body) {
      loginRoot = loginRoot.parentElement;
    }

    // Find all direct children or large visual elements that aren't the form side
    var children = loginRoot.querySelectorAll(':scope > div, :scope > section');
    for (var i = 0; i < children.length; i++) {
      var child = children[i];
      // Skip the div that contains the form
      if (child.contains(form)) continue;
      // Hide the other half (the decoration)
      child.style.display = 'none';
    }
  }

  function removeVideo() {
    var el = document.querySelector('.login-video-container');
    if (el) el.remove();
  }

  function syncVideo() {
    if (isLoginPage()) {
      injectVideo();
    } else {
      removeVideo();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncVideo);
  } else {
    syncVideo();
  }

  var videoObserver = new MutationObserver(syncVideo);
  videoObserver.observe(document.body, { childList: true, subtree: true });
})();


// === Header logo (persistent top-left) ===
(function () {
  function injectHeaderLogo() {
    if (document.getElementById('header-logo')) return;

    // Try multiple selectors for Chainlit's header
    var header = document.getElementById('header')
      || document.querySelector('header')
      || document.querySelector('[class*="header"]')
      || document.querySelector('nav');

    if (!header) return;

    var logo = document.createElement('img');
    logo.id = 'header-logo';
    logo.src = '/public/enviranorth_logo.png';
    logo.alt = 'Envira-North';
    logo.style.cssText = 'height:36px;margin-left:4px;margin-right:12px;object-fit:contain;cursor:pointer;flex-shrink:0;position:relative;z-index:10;';

    // Insert right after the sidebar trigger button so logo sits
    // visually adjacent to the sidebar panel
    var sidebarTrigger = header.querySelector('[data-sidebar="trigger"]')
      || header.querySelector('#sidebar-trigger-button')
      || header.firstElementChild;
    if (sidebarTrigger) {
      sidebarTrigger.after(logo);
    } else {
      header.prepend(logo);
    }
  }

  function tryInject() {
    if (!document.getElementById('header-logo')) {
      injectHeaderLogo();
    }
  }

  // Run periodically for the first 10 seconds to catch late-rendering headers
  var attempts = 0;
  var interval = setInterval(function () {
    tryInject();
    attempts++;
    if (attempts > 20 || document.getElementById('header-logo')) {
      clearInterval(interval);
    }
  }, 500);

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryInject);
  } else {
    tryInject();
  }

  var logoObserver = new MutationObserver(tryInject);
  logoObserver.observe(document.body, { childList: true, subtree: true });
})();


// === Tame aggressive auto-scroll ===
(function () {
  // Override scrollIntoView to use smooth behavior and keep context
  var origScroll = Element.prototype.scrollIntoView;
  Element.prototype.scrollIntoView = function (opts) {
    if (typeof opts === 'boolean') {
      opts = { block: opts ? 'start' : 'end', behavior: 'smooth' };
    } else if (!opts) {
      opts = {};
    }
    opts.behavior = 'smooth';
    opts.block = opts.block || 'end';
    return origScroll.call(this, opts);
  };
})();

// === Shimmer effect + avatar spin on "Searching Knowledge Base..." ===
(function () {
  function applyEffects() {
    // Use TreeWalker to find any text node containing "Searching Knowledge Base"
    var walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function (node) {
          return node.textContent.indexOf('Searching Knowledge Base') !== -1
            ? NodeFilter.FILTER_ACCEPT
            : NodeFilter.FILTER_REJECT;
        }
      }
    );

    var searchingFound = new Set();
    var node;
    while ((node = walker.nextNode())) {
      var parent = node.parentElement;
      if (!parent) continue;

      // Wrap the text in a shimmer span if not already wrapped
      if (!parent.classList.contains('searching-shimmer')) {
        // If the parent is a simple inline element (em, span, p), add class directly
        if (['EM', 'SPAN', 'P', 'DIV', 'STRONG', 'I'].indexOf(parent.tagName) !== -1) {
          parent.classList.add('searching-shimmer');
        } else {
          // Wrap in a span
          var span = document.createElement('span');
          span.className = 'searching-shimmer';
          span.textContent = node.textContent;
          node.parentElement.replaceChild(span, node);
          parent = span;
        }
      }

      // Find the closest message container and spin its avatar
      var msgContainer = parent.closest('[class*="message"], [class*="step"], [class*="Message"]');
      if (msgContainer) {
        searchingFound.add(msgContainer);
        var avatar = msgContainer.querySelector('[class*="avatar"], [class*="Avatar"], img[alt*="avatar"]');
        if (!avatar) {
          var prev = msgContainer.previousElementSibling;
          if (prev && (prev.className || '').match(/avatar/i)) {
            avatar = prev;
          }
        }
        if (avatar && !avatar.classList.contains('avatar-spinning')) {
          avatar.classList.add('avatar-spinning');
        }
      }
    }

    // Remove shimmer from elements whose text no longer says "Searching..."
    var shimmering = document.querySelectorAll('.searching-shimmer');
    for (var i = 0; i < shimmering.length; i++) {
      if (shimmering[i].textContent.indexOf('Searching Knowledge Base') === -1) {
        shimmering[i].classList.remove('searching-shimmer');
      }
    }

    // Remove spin from avatars whose messages no longer show "Searching..."
    var spinning = document.querySelectorAll('.avatar-spinning');
    for (var j = 0; j < spinning.length; j++) {
      var el = spinning[j];
      var parentMsg = el.closest('[class*="message"], [class*="step"], [class*="Message"]');
      if (!parentMsg || !searchingFound.has(parentMsg)) {
        el.classList.remove('avatar-spinning');
      }
    }
  }

  var shimmerObserver = new MutationObserver(applyEffects);
  shimmerObserver.observe(document.body, { childList: true, subtree: true });
})();
