/* Massonelec Sàrl — site behaviour */
(function () {
  'use strict';
  var CFG = {
    phone: '+41793505519',
    phoneHuman: '079 350 55 19',
    wa: '41793505519',
    email: 'picpus_ch@hotmail.com'
  };
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- header shadow ---------- */
  var hdr = $('.hdr');
  function onScroll() { if (hdr) hdr.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* ---------- mega menu ---------- */
  $$('.nav > li.has-mega').forEach(function (li) {
    var btn = $('.nav-link', li), t, at = 0;
    function open() { clearTimeout(t); if (!li.classList.contains('open')) at = Date.now(); li.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); }
    function close() { t = setTimeout(function () { li.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }, 120); }
    li.addEventListener('mouseenter', open);
    li.addEventListener('mouseleave', close);
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      if (li.classList.contains('open') && Date.now() - at > 450) { li.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); } else open();
    });
    li.addEventListener('focusout', function (e) { if (!li.contains(e.relatedTarget)) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && li.classList.contains('open')) { li.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus(); } });
  });

  /* ---------- mobile drawer ---------- */
  var drawer = $('#drawer');
  $$('[data-drawer-open]').forEach(function (b) { b.addEventListener('click', function () { drawer.classList.add('open'); drawer.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; var f = $('a,button', drawer); if (f) f.focus(); }); });
  $$('[data-drawer-close]').forEach(function (b) { b.addEventListener('click', closeDrawer); });
  function closeDrawer() { if (!drawer) return; drawer.classList.remove('open'); drawer.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; }
  if (drawer) $$('a', drawer).forEach(function (a) { a.addEventListener('click', closeDrawer); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDrawer(); });

  /* ---------- live opening status (Europe/Zurich) ---------- */
  function zurichNow() {
    try {
      var parts = new Intl.DateTimeFormat('fr-CH', { timeZone: 'Europe/Zurich', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
      var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
      var days = { 'lun.': 1, 'mar.': 2, 'mer.': 3, 'jeu.': 4, 'ven.': 5, 'sam.': 6, 'dim.': 0 };
      return { d: days[o.weekday] !== undefined ? days[o.weekday] : new Date().getDay(), m: parseInt(o.hour, 10) * 60 + parseInt(o.minute, 10) };
    } catch (e) { var n = new Date(); return { d: n.getDay(), m: n.getHours() * 60 + n.getMinutes() }; }
  }
  var now = zurichNow();
  var slots = { 1: [[450, 720], [810, 1020]], 2: [[450, 720], [810, 1020]], 3: [[450, 720], [810, 1020]], 4: [[450, 720], [810, 1020]], 5: [[450, 720], [810, 960]] };
  var isOpen = (slots[now.d] || []).some(function (s) { return now.m >= s[0] && now.m < s[1]; });
  $$('[data-open-status]').forEach(function (el) {
    el.textContent = isOpen ? 'Bureau ouvert' : 'Bureau fermé · dépannage 24/7';
  });
  $$('.dot-live').forEach(function (d) { if (!isOpen) d.classList.add('closed'); });
  $$('.hours tr[data-day]').forEach(function (tr) { if (tr.getAttribute('data-day').split(',').indexOf(String(now.d)) > -1) tr.classList.add('today'); });

  /* ---------- forms: WhatsApp / e-mail hand-off ---------- */
  function collect(form) {
    var lines = [], fd = new FormData(form), seen = {};
    $$('[data-label]', form).forEach(function (el) {
      var name = el.name; if (!name || seen[name]) return; seen[name] = 1;
      var vals = fd.getAll(name).filter(function (v) { return String(v).trim(); });
      if (vals.length) lines.push(el.getAttribute('data-label') + ' : ' + vals.join(', '));
    });
    return lines;
  }
  function validate(form) {
    var ok = true;
    $$('[required]', form).forEach(function (el) {
      var f = el.closest('.f'); var bad = !String(el.value).trim() || (el.type === 'email' && el.value && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
      if (f) f.classList.toggle('err', bad);
      if (bad && ok) { el.focus(); ok = false; }
    });
    return ok;
  }
  function send(form, via) {
    if (!validate(form)) return;
    var subject = form.getAttribute('data-subject') || 'Demande depuis le site';
    var body = [subject, '—'].concat(collect(form)).join('\n');
    if (via === 'mail') {
      location.href = 'mailto:' + CFG.email + '?subject=' + encodeURIComponent(subject + ' – Massonelec') + '&body=' + encodeURIComponent(body);
    } else {
      window.open('https://wa.me/' + CFG.wa + '?text=' + encodeURIComponent(body), '_blank', 'noopener');
    }
    form.classList.add('sent');
  }
  $$('form.js-form').forEach(function (form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) { e.preventDefault(); send(form, (e.submitter && e.submitter.value) || 'wa'); });
    $$('input,select,textarea', form).forEach(function (el) { el.addEventListener('input', function () { var f = el.closest('.f'); if (f) f.classList.remove('err'); }); });
  });

  /* ---------- quote wizard ---------- */
  var wz = $('#wizard');
  if (wz) {
    var steps = $$('.wz-step', wz), bars = $$('.wz-progress i', wz), cur = 0;
    function go(i) {
      cur = i; steps.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      bars.forEach(function (b, k) { b.classList.toggle('on', k <= i); });
      if (i === steps.length - 1) { var r = $('.wz-recap', wz); if (r) r.textContent = collect(wz).join('\n'); }
      var top = wz.getBoundingClientRect().top + window.scrollY - 120; if (window.scrollY > top) window.scrollTo({ top: top, behavior: reduce ? 'auto' : 'smooth' });
    }
    $$('[data-next]', wz).forEach(function (b) { b.addEventListener('click', function () {
      var st = steps[cur], need = $$('[data-need]', st);
      for (var k = 0; k < need.length; k++) { var grp = need[k]; if (!$('input:checked', grp)) { grp.classList.add('shake'); var m = $('.wz-miss', st); if (m) m.hidden = false; return; } }
      var req = $$('[required]', st), ok = true;
      req.forEach(function (el) { var f = el.closest('.f'); var bad = !String(el.value).trim(); if (f) f.classList.toggle('err', bad); if (bad && ok) { el.focus(); ok = false; } });
      if (!ok) return; go(cur + 1);
    }); });
    $$('[data-prev]', wz).forEach(function (b) { b.addEventListener('click', function () { go(Math.max(0, cur - 1)); }); });
    $$('input', wz).forEach(function (i) { i.addEventListener('change', function () { $$('.wz-miss', wz).forEach(function (m) { m.hidden = true; }); }); });
    // prefill from ?service=
    var q = new URLSearchParams(location.search).get('service');
    if (q) $$('input[name="prestations"]', wz).forEach(function (i) { if (i.value === q) i.checked = true; });
    go(0);
  }
  // prefill service selects from data attribute
  $$('select[data-preselect]').forEach(function (s) { var v = s.getAttribute('data-preselect'); $$('option', s).forEach(function (o) { if (o.value === v) o.selected = true; }); });

  /* ---------- WhatsApp widget ---------- */
  var fab = $('.wa-fab'), panel = $('.wa-panel');
  function togglePanel(open) { if (!panel) return; panel.classList.toggle('open', open); panel.setAttribute('aria-hidden', open ? 'false' : 'true'); if (fab) fab.setAttribute('aria-expanded', open ? 'true' : 'false'); var b = fab && $('.badge', fab); if (b) b.remove(); }
  if (fab) fab.addEventListener('click', function () { togglePanel(!panel.classList.contains('open')); });
  $$('[data-wa-open]').forEach(function (a) { a.addEventListener('click', function (e) { if (window.innerWidth > 720) { e.preventDefault(); togglePanel(true); } }); });
  $$('.wa-panel .x').forEach(function (x) { x.addEventListener('click', function () { togglePanel(false); }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') togglePanel(false); });
  $$('.wa-time').forEach(function (t) { var d = new Date(); t.textContent = ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2); });

  /* ---------- gallery filters + lightbox ---------- */
  var filters = $$('.filters button');
  filters.forEach(function (b) { b.addEventListener('click', function () {
    filters.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    var f = b.getAttribute('data-filter');
    $$('.gal-item').forEach(function (it) { it.hidden = !(f === 'all' || (it.getAttribute('data-cat') || '').split(' ').indexOf(f) > -1); });
    if (window.ScrollTrigger) window.ScrollTrigger.refresh();
  }); });
  var lb = $('#lightbox');
  if (lb) {
    var items = [], idx = 0, fig = $('figure', lb);
    function render() {
      var it = items[idx]; var src = it.getAttribute('data-full'), cap = it.getAttribute('data-caption') || '';
      var media = it.getAttribute('data-video') ? '<video src="' + it.getAttribute('data-video') + '" controls autoplay playsinline poster="' + src + '"></video>' : '<img src="' + src + '" alt="">';
      fig.innerHTML = media + '<figcaption>' + cap + '</figcaption>';
      var im = $('img', fig); if (im) im.alt = cap;
    }
    function openLb(el) { items = $$('.gal-item:not([hidden]), [data-lb]').filter(function (x) { return x.offsetParent !== null; }); idx = Math.max(0, items.indexOf(el)); render(); lb.classList.add('open'); document.body.style.overflow = 'hidden'; $('.lb-x', lb).focus(); }
    function closeLb() { lb.classList.remove('open'); fig.innerHTML = ''; document.body.style.overflow = ''; }
    $$('.gal-item, [data-lb]').forEach(function (el) { el.addEventListener('click', function (e) { e.preventDefault(); openLb(el); }); });
    $('.lb-x', lb).addEventListener('click', closeLb);
    $('.lb-p', lb).addEventListener('click', function () { idx = (idx - 1 + items.length) % items.length; render(); });
    $('.lb-n', lb).addEventListener('click', function () { idx = (idx + 1) % items.length; render(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener('keydown', function (e) { if (!lb.classList.contains('open')) return; if (e.key === 'Escape') closeLb(); if (e.key === 'ArrowLeft') $('.lb-p', lb).click(); if (e.key === 'ArrowRight') $('.lb-n', lb).click(); });
  }

  /* ---------- map click-to-load ---------- */
  $$('[data-map]').forEach(function (b) { b.addEventListener('click', function () {
    var box = b.closest('.map'); box.innerHTML = '<iframe title="Plan d\'accès Massonelec Sàrl" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Massonelec%20S%C3%A0rl%2C%20Chemin%20de%20la%20Perrolaz%202%2C%201860%20Aigle&z=15&output=embed"></iframe>';
  }); });

  /* ---------- videos: pause off-screen / reduced motion ---------- */
  $$('video[data-autoplay]').forEach(function (v) {
    v.muted = true;
    if (reduce) { v.removeAttribute('autoplay'); v.pause(); return; }
    var p = v.play(); if (p && p.catch) p.catch(function () {});
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { var pp = v.play(); if (pp && pp.catch) pp.catch(function () {}); } else v.pause(); }); }, { threshold: 0.05 }).observe(v);
  });
  $$('[data-unmute]').forEach(function (b) { b.addEventListener('click', function () {
    var v = $(b.getAttribute('data-unmute')); if (!v) return;
    v.muted = !v.muted; if (!v.muted) { v.currentTime = 0; v.play(); }
    b.querySelector('span').textContent = v.muted ? 'Activer le son' : 'Couper le son';
  }); });

  /* ---------- subtle 3D tilt ---------- */
  if (!reduce && window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    $$('[data-tilt]').forEach(function (el) {
      var raf;
      el.addEventListener('mousemove', function (e) {
        var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        cancelAnimationFrame(raf); raf = requestAnimationFrame(function () { el.style.transform = 'perspective(900px) rotateX(' + (-y * 6).toFixed(2) + 'deg) rotateY(' + (x * 7).toFixed(2) + 'deg) translateY(-4px)'; });
      });
      el.addEventListener('mouseleave', function () { cancelAnimationFrame(raf); el.style.transition = 'transform .5s cubic-bezier(.2,.7,.2,1), box-shadow .3s, border-color .3s'; el.style.transform = ''; setTimeout(function () { el.style.transition = ''; }, 500); });
    });
  }

  /* ---------- scroll reveals (GSAP, only for elements below the fold) ---------- */
  if (!reduce && window.gsap && window.ScrollTrigger && location.search.indexOf('static') < 0) {
    gsap.registerPlugin(ScrollTrigger);
    var vh = window.innerHeight;
    var els = $$('[data-reveal]').filter(function (el) { return el.getBoundingClientRect().top > vh * 0.92; });
    gsap.set(els, { autoAlpha: 0, y: 28 });
    ScrollTrigger.batch(els, { start: 'top 90%', once: true, onEnter: function (b) { gsap.to(b, { autoAlpha: 1, y: 0, duration: .8, ease: 'power3.out', stagger: .08, overwrite: true }); } });
    // counters
    $$('[data-count]').forEach(function (el) {
      var end = parseFloat(el.getAttribute('data-count')), o = { v: 0 }, dec = (el.getAttribute('data-count').split('.')[1] || '').length;
      ScrollTrigger.create({ trigger: el, start: 'top 92%', once: true, onEnter: function () { gsap.to(o, { v: end, duration: 1.6, ease: 'power2.out', onUpdate: function () { el.textContent = o.v.toFixed(dec).replace('.', ','); } }); } });
    });
    window.addEventListener('load', function () { ScrollTrigger.refresh(); });
  }

  /* ---------- 3D zone map: load when near ---------- */
  var zc = $('#zone3d');
  if (zc) {
    var loaded = false;
    var loadZone = function () { if (loaded) return; loaded = true; var s = document.createElement('script'); s.type = 'module'; s.src = zc.getAttribute('data-src'); document.body.appendChild(s); };
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es, ob) { es.forEach(function (e) { if (e.isIntersecting) { loadZone(); ob.disconnect(); } }); }, { rootMargin: '400px' }).observe(zc);
    else loadZone();
  }

  $$('[data-year]').forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();
