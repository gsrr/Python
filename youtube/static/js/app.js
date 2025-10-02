(function () {
  // ===== Overlay =====
  function showOverlay() {
    var el = document.getElementById('overlay');
    if (el) el.style.display = 'block';
  }
  window.showOverlay = showOverlay;

  function bindOverlayToForms() {
    var forms = document.querySelectorAll('form[data-overlay]');
    forms.forEach(function (f) {
      f.addEventListener('submit', function () {
        showOverlay();
      });
    });
  }

  // ===== Saved Songs 選取 + 鍵盤上下移動 =====
  function initSavedSongsSelection() {
    var list = document.getElementById('saved-songs');
    if (!list) return;

    var items = Array.from(list.querySelectorAll('li[data-url]'));
    if (items.length === 0) return;

    var preview = document.getElementById('preview');
    var playUrlInput = document.getElementById('play-url');
    var nowUrl = document.body.dataset.nowUrl; // 後端傳的當前播放 URL

    function updatePreview(li) {
      var title = li.dataset.title || '';
      var thumb = li.dataset.thumbnail || '';
      var url = li.dataset.url || '';
      preview.innerHTML =
        (thumb ? '<img src="' + thumb + '" class="thumbnail">' : '') +
        '<h2>' + title + '</h2>';
      if (playUrlInput) playUrlInput.value = url;
    }

    // 根據後端 nowUrl 決定 activeIndex
    var activeIndex = -1;
    if (nowUrl) {
      activeIndex = items.findIndex(function (li) { return li.dataset.url === nowUrl; });
    }
    if (activeIndex < 0) activeIndex = 0;

    items.forEach(function (x) { x.classList.remove('active'); });
    items[activeIndex].classList.add('active');
    updatePreview(items[activeIndex]);
    items[activeIndex].scrollIntoView({ block: 'nearest', inline: 'nearest' });

    function setActive(idx) {
      if (items.length === 0) return;
      idx = (idx % items.length + items.length) % items.length;
      items.forEach(function (x) { x.classList.remove('active'); });
      items[idx].classList.add('active');
      activeIndex = idx;
      updatePreview(items[idx]);
      items[idx].scrollIntoView({ block: 'nearest', inline: 'nearest' });
    }

    // 滑鼠點擊
    items.forEach(function (li, idx) {
      li.addEventListener('click', function () { setActive(idx); });
    });

    // 鍵盤上下移動
    document.addEventListener('keydown', function (e) {
      var ae = document.activeElement;
      var tag = ae && ae.tagName;
      var isEditing = ae && (ae.isContentEditable ||
        tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT');
      if (isEditing) return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        setActive(activeIndex + 1);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setActive(activeIndex - 1);
      }
    });
  }

  // ===== Boot =====
  function boot() {
    bindOverlayToForms();
    initSavedSongsSelection();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();

