/* Massonelec Sàrl — interaction & motion */
(function () {
  'use strict';
  var CFG = { wa: '41793505519', email: 'picpus_ch@hotmail.com' };
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  var G = window.gsap, ST = window.ScrollTrigger;
  var motion = !!(G && ST) && !reduce && location.search.indexOf('static') < 0;
  var lenis = null;
  window.__mx = { ready: false };

  /* ================= live clock & opening status (Europe/Zurich) ================= */
  function zurich() {
    try {
      var p = {}; new Intl.DateTimeFormat('fr-CH', { timeZone: 'Europe/Zurich', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
      var d = { 'lun.': 1, 'mar.': 2, 'mer.': 3, 'jeu.': 4, 'ven.': 5, 'sam.': 6, 'dim.': 0 }[p.weekday];
      return { d: d === undefined ? new Date().getDay() : d, h: p.hour, mi: p.minute, m: (+p.hour) * 60 + (+p.minute) };
    } catch (e) { var n = new Date(); return { d: n.getDay(), h: ('0' + n.getHours()).slice(-2), mi: ('0' + n.getMinutes()).slice(-2), m: n.getHours() * 60 + n.getMinutes() }; }
  }
  var SL = { 1: [[450, 720], [810, 1020]], 2: [[450, 720], [810, 1020]], 3: [[450, 720], [810, 1020]], 4: [[450, 720], [810, 1020]], 5: [[450, 720], [810, 960]] };
  function tick() {
    var z = zurich(), open = (SL[z.d] || []).some(function (s) { return z.m >= s[0] && z.m < s[1]; });
    $$('[data-clock]').forEach(function (e) { e.textContent = 'Aigle ' + z.h + ':' + z.mi; });
    $$('[data-open]').forEach(function (e) { e.textContent = open ? 'Bureau ouvert' : 'Fermé · urgences 24/7'; });
    $$('.dot').forEach(function (d) { d.classList.toggle('off', !open); });
    $$('.hours tr[data-day]').forEach(function (tr) { tr.classList.toggle('today', tr.getAttribute('data-day').split(',').indexOf(String(z.d)) > -1); });
  }
  tick(); setInterval(tick, 30000);

  /* ================= header ================= */
  var hdr = $('.hdr'), lastY = 0, mbar = $('.mbar'), darks = $$('[data-dark]');
  function onScroll(y) {
    if (!hdr) return;
    var dy = y - lastY;
    hdr.classList.toggle('solid', y > 40);
    if (y > 300 && dy > 4 && !document.body.classList.contains('menu-open')) hdr.classList.add('hide');
    else if (dy < -4 || y < 300) hdr.classList.remove('hide');
    if (mbar) { if (dy > 6 && y > 400) mbar.classList.add('away'); else if (dy < -6) mbar.classList.remove('away'); }
    var dark = false;
    darks.forEach(function (s) { var r = s.getBoundingClientRect(); if (r.top <= 36 && r.bottom >= 36) dark = true; });
    hdr.classList.toggle('on-dark', dark);
    lastY = y;
  }
  window.addEventListener('scroll', function () { if (!lenis) onScroll(window.scrollY); }, { passive: true });
  onScroll(window.scrollY);

  /* ================= full-screen menu ================= */
  var menu = $('#menu');
  function openMenu() {
    if (!menu) return;
    document.body.classList.add('menu-open'); menu.classList.add('open'); menu.setAttribute('aria-hidden', 'false');
    if (lenis) lenis.stop();
    if (G && !reduce) {
      G.fromTo(menu, { clipPath: 'inset(0% 0% 100% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: .9, ease: 'expo.inOut' });
      G.fromTo($$('.menu-list a', menu), { yPercent: 105 }, { yPercent: 0, duration: 1, stagger: .045, ease: 'expo.out', delay: .35 });
      G.fromTo($$('.menu-side > *', menu), { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, duration: .8, stagger: .08, delay: .55, ease: 'power3.out' });
    } else menu.style.clipPath = 'none';
    var c = $('.menu-close', menu); if (c) c.focus();
  }
  function closeMenu() {
    if (!menu || !menu.classList.contains('open')) return;
    var done = function () { menu.classList.remove('open'); menu.setAttribute('aria-hidden', 'true'); document.body.classList.remove('menu-open'); if (lenis) lenis.start(); };
    if (G && !reduce) G.fromTo(menu, { clipPath: 'inset(0% 0% 0% 0%)' }, { clipPath: 'inset(100% 0% 0% 0%)', duration: .7, ease: 'expo.inOut', onComplete: done }); else done();
  }
  $$('[data-menu]').forEach(function (b) { b.addEventListener('click', openMenu); });
  $$('.menu-close').forEach(function (b) { b.addEventListener('click', closeMenu); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  if (menu) {
    var mimgs = $$('.menu-img img', menu);
    $$('.menu-list a', menu).forEach(function (a, i) {
      a.addEventListener('mouseenter', function () { mimgs.forEach(function (im, k) { im.classList.toggle('on', k === i); }); });
    });
  }

  /* ================= forms → WhatsApp / e-mail ================= */
  function collect(form) {
    var lines = [], fd = new FormData(form), seen = {};
    $$('[data-label]', form).forEach(function (el) {
      var n = el.name; if (!n || seen[n]) return; seen[n] = 1;
      var v = fd.getAll(n).filter(function (x) { return String(x).trim(); });
      if (v.length) lines.push(el.getAttribute('data-label') + ' : ' + v.join(', '));
    });
    return lines;
  }
  function validate(scope) {
    var ok = true;
    $$('[required]', scope).forEach(function (el) {
      var f = el.closest('.fld'), bad = !String(el.value).trim() || (el.type === 'email' && el.value && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(el.value));
      if (f) f.classList.toggle('err', bad);
      if (bad && ok) { el.focus(); ok = false; }
    });
    return ok;
  }
  function send(form, via) {
    if (!validate(form)) return;
    var subj = form.getAttribute('data-subject') || 'Demande depuis le site';
    var body = [subj, '—'].concat(collect(form)).join('\n');
    if (via === 'mail') location.href = 'mailto:' + CFG.email + '?subject=' + encodeURIComponent(subj + ' – Massonelec') + '&body=' + encodeURIComponent(body);
    else window.open('https://wa.me/' + CFG.wa + '?text=' + encodeURIComponent(body), '_blank', 'noopener');
    form.classList.add('sent');
  }
  $$('form.js-form').forEach(function (form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('submit', function (e) { e.preventDefault(); send(form, (e.submitter && e.submitter.value) || 'wa'); });
    $$('input,select,textarea', form).forEach(function (el) { el.addEventListener('input', function () { var f = el.closest('.fld'); if (f) f.classList.remove('err'); }); });
  });

  /* ================= quote wizard ================= */
  var wz = $('#wizard');
  if (wz) {
    var steps = $$('.wz-step', wz), navs = $$('.wz-nav li'), cur = 0;
    var go = function (i) {
      cur = i;
      steps.forEach(function (s, k) { s.classList.toggle('on', k === i); });
      navs.forEach(function (n, k) { n.classList.toggle('on', k === i); n.classList.toggle('done', k < i); });
      if (i === steps.length - 1) { var r = $('.wz-recap', wz); if (r) r.textContent = collect(wz).join('\n'); }
      if (G && !reduce) G.fromTo(steps[i], { autoAlpha: 0, y: 24 }, { autoAlpha: 1, y: 0, duration: .7, ease: 'power3.out' });
      var top = wz.getBoundingClientRect().top + window.scrollY - 110;
      if (window.scrollY > top) { if (lenis) lenis.scrollTo(top); else window.scrollTo(0, top); }
    };
    $$('[data-next]', wz).forEach(function (b) { b.addEventListener('click', function () {
      var st = steps[cur], need = $$('[data-need]', st);
      for (var k = 0; k < need.length; k++) if (!$('input:checked', need[k])) { need[k].classList.remove('shake'); void need[k].offsetWidth; need[k].classList.add('shake'); var m = $('.wz-miss', st); if (m) m.hidden = false; return; }
      if (!validate(st)) return;
      go(cur + 1);
    }); });
    $$('[data-prev]', wz).forEach(function (b) { b.addEventListener('click', function () { go(Math.max(0, cur - 1)); }); });
    $$('input', wz).forEach(function (i) { i.addEventListener('change', function () { $$('.wz-miss', wz).forEach(function (m) { m.hidden = true; }); }); });
    var q = new URLSearchParams(location.search).get('service');
    if (q) $$('input[name="prestations"]', wz).forEach(function (i) { if (i.value === q) i.checked = true; });
  }

  /* ================= WhatsApp widget ================= */
  var fab = $('.wa-fab'), panel = $('.wa-panel');
  function wa(open) { if (!panel) return; panel.classList.toggle('open', open); panel.setAttribute('aria-hidden', open ? 'false' : 'true'); if (fab) fab.setAttribute('aria-expanded', String(open)); }
  if (fab) fab.addEventListener('click', function () { wa(!panel.classList.contains('open')); });
  $$('.wa-panel .x').forEach(function (x) { x.addEventListener('click', function () { wa(false); }); });
  $$('[data-wa]').forEach(function (a) { a.addEventListener('click', function (e) { if (window.innerWidth > 640 && panel) { e.preventDefault(); wa(true); } }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') wa(false); });

  /* ================= gallery filters + lightbox ================= */
  var fbtn = $$('.filters button');
  fbtn.forEach(function (b) { b.addEventListener('click', function () {
    fbtn.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    var f = b.getAttribute('data-filter');
    $$('.gi').forEach(function (it) { it.hidden = !(f === 'all' || (it.getAttribute('data-cat') || '').split(' ').indexOf(f) > -1); });
    if (ST) ST.refresh();
  }); });
  var lb = $('#lightbox');
  if (lb) {
    var items = [], idx = 0, fig = $('figure', lb);
    var render = function () {
      var it = items[idx], src = it.getAttribute('data-full'), cap = it.getAttribute('data-caption') || '', v = it.getAttribute('data-video');
      fig.innerHTML = (v ? '<video src="' + v + '" controls autoplay playsinline poster="' + src + '"></video>' : '<img src="' + src + '" alt="">') + '<figcaption></figcaption>';
      $('figcaption', fig).textContent = cap; var im = $('img', fig); if (im) im.alt = cap;
    };
    var openLb = function (el) { items = $$('[data-lb]').filter(function (x) { return !x.hidden; }); idx = Math.max(0, items.indexOf(el)); render(); lb.classList.add('open'); if (lenis) lenis.stop(); $('.x', lb).focus(); };
    var closeLb = function () { lb.classList.remove('open'); fig.innerHTML = ''; if (lenis) lenis.start(); };
    $$('[data-lb]').forEach(function (el) { el.addEventListener('click', function (e) { e.preventDefault(); openLb(el); }); });
    $('.x', lb).addEventListener('click', closeLb);
    $('.p', lb).addEventListener('click', function () { idx = (idx - 1 + items.length) % items.length; render(); });
    $('.n', lb).addEventListener('click', function () { idx = (idx + 1) % items.length; render(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener('keydown', function (e) { if (!lb.classList.contains('open')) return; if (e.key === 'Escape') closeLb(); if (e.key === 'ArrowLeft') $('.p', lb).click(); if (e.key === 'ArrowRight') $('.n', lb).click(); });
  }

  /* ================= map click-to-load ================= */
  $$('[data-map]').forEach(function (b) { b.addEventListener('click', function () {
    b.closest('.map').innerHTML = '<iframe title="Plan d\'accès Massonelec Sàrl" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://maps.google.com/maps?q=Massonelec%20S%C3%A0rl%2C%20Chemin%20de%20la%20Perrolaz%202%2C%201860%20Aigle&z=15&output=embed"></iframe>';
  }); });

  /* ================= videos ================= */
  $$('video[data-auto]').forEach(function (v) {
    v.muted = true;
    if (reduce) { v.pause(); return; }
    var p = v.play(); if (p && p.catch) p.catch(function () {});
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { var pp = v.play(); if (pp && pp.catch) pp.catch(function () {}); } else v.pause(); }); }).observe(v);
  });
  $$('[data-sound]').forEach(function (b) { b.addEventListener('click', function () {
    var v = $(b.getAttribute('data-sound')); if (!v) return;
    var full = v.getAttribute('data-full');
    if (full && !v.__full) { v.__full = true; var t = v.currentTime; v.src = full; v.currentTime = 0; }
    v.muted = !v.muted; var p = v.play(); if (p && p.catch) p.catch(function () {});
    b.querySelector('span').textContent = v.muted ? 'Activer le son' : 'Couper le son';
  }); });

  /* ================= service index floating image ================= */
  var fl = $('.idx-float');
  if (fl && fine) {
    var fimg = $('img', fl), qx = null, qy = null;
    if (G) { qx = G.quickTo(fl, 'x', { duration: .7, ease: 'power3' }); qy = G.quickTo(fl, 'y', { duration: .7, ease: 'power3' }); }
    $$('.idx a[data-img]').forEach(function (a) {
      a.addEventListener('mouseenter', function () { fimg.src = a.getAttribute('data-img'); fl.classList.add('on'); });
      a.addEventListener('mouseleave', function () { fl.classList.remove('on'); });
    });
    window.addEventListener('mousemove', function (e) {
      var x = e.clientX - fl.offsetWidth / 2, y = e.clientY - fl.offsetHeight / 2;
      if (qx) { qx(x); qy(y); } else fl.style.transform = 'translate(' + x + 'px,' + y + 'px)';
    }, { passive: true });
  }

  /* ================= page transitions ================= */
  var pt = $('.pt');
  function internal(a) {
    if (!a || a.target === '_blank' || a.hasAttribute('download') || a.hasAttribute('data-lb')) return false;
    var h = a.getAttribute('href') || '';
    return !!h && h.charAt(0) !== '#' && !/^(mailto|tel|https?:|javascript|sms)/i.test(h);
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a'); if (!a || !internal(a) || e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
    var url = new URL(a.href, location.href);
    if (url.pathname === location.pathname && url.hash) return;
    if (!G || reduce || !pt) return;
    e.preventDefault();
    G.set(pt, { autoAlpha: 1, yPercent: 100 });
    G.to(pt, { yPercent: 0, duration: .75, ease: 'expo.inOut', onComplete: function () { location.href = a.href; } });
  });
  window.addEventListener('pageshow', function (e) { if (e.persisted && pt) { if (G) G.set(pt, { autoAlpha: 0, yPercent: 0 }); root.classList.remove('pre-intro'); } });

  /* ================= MOTION ================= */
  function splitWords(el) {
    var walk = function (node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (t) {
            if (!t) return;
            if (/^\s+$/.test(t)) frag.appendChild(document.createTextNode(t));
            else { var w = document.createElement('span'); w.className = 'w'; var i = document.createElement('span'); i.textContent = t; w.appendChild(i); frag.appendChild(w); }
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    };
    walk(el);
    return $$('.w > span', el);
  }
  function finishIntro() { root.classList.remove('pre-intro'); window.__mx.ready = true; }

  if (!motion) {
    if (pt && G) G.set(pt, { autoAlpha: 0 });
    finishIntro();
    return;
  }

  G.registerPlugin(ST);

  if (window.Lenis && fine) {
    lenis = new window.Lenis({ lerp: .1 });
    lenis.on('scroll', function (e) { ST.update(); onScroll(e.scroll); });
    G.ticker.add(function (t) { lenis.raf(t * 1000); });
    G.ticker.lagSmoothing(0);
    window.__mx.lenis = lenis;
    $$('a[href^="#"]').forEach(function (a) { a.addEventListener('click', function (e) { var t = $(a.getAttribute('href')); if (t) { e.preventDefault(); lenis.scrollTo(t, { offset: -20 }); } }); });
  }

  var vh = window.innerHeight;
  var intro = G.timeline({ paused: true, defaults: { ease: 'expo.out' } });
  var late = (window.performance && performance.now() > 2300);
  var inView = function (el) { return el.getBoundingClientRect().top < vh * .95; };
  var skip = function (el) { return late && inView(el); };

  $$('[data-lines]').forEach(function (h) {
    if (skip(h)) return;
    var s = $$('.ln > span', h);
    G.set(s, { y: 0, yPercent: 112 });
    if (inView(h)) intro.to(s, { yPercent: 0, duration: 1.4, stagger: .09 }, .1);
    else G.to(s, { yPercent: 0, duration: 1.25, stagger: .08, ease: 'expo.out', scrollTrigger: { trigger: h, start: 'top 86%', once: true } });
  });

  $$('[data-words]').forEach(function (h) {
    if (skip(h)) return;
    var ws = splitWords(h);
    G.set(ws, { y: 0, yPercent: 112 });
    if (inView(h)) intro.to(ws, { yPercent: 0, duration: 1.2, stagger: .022 }, .25);
    else G.to(ws, { yPercent: 0, duration: 1.15, stagger: .02, ease: 'expo.out', scrollTrigger: { trigger: h, start: 'top 87%', once: true } });
  });

  $$('[data-r]').forEach(function (el) {
    if (skip(el)) return;
    var d = parseFloat(el.getAttribute('data-r')) || 0;
    G.set(el, { autoAlpha: 0, y: 34 });
    if (inView(el)) intro.to(el, { autoAlpha: 1, y: 0, duration: 1.2, ease: 'power3.out' }, .5 + d);
    else G.to(el, { autoAlpha: 1, y: 0, duration: 1.1, delay: d, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 91%', once: true } });
  });

  $$('[data-line]').forEach(function (el) {
    if (skip(el)) return;
    G.set(el, { scaleX: 0, transformOrigin: 'left center' });
    if (inView(el)) intro.to(el, { scaleX: 1, duration: 1.6, ease: 'expo.inOut' }, 0);
    else G.to(el, { scaleX: 1, duration: 1.5, ease: 'expo.inOut', scrollTrigger: { trigger: el, start: 'top 93%', once: true } });
  });

  $$('[data-stagger]').forEach(function (list) {
    if (skip(list)) return;
    var kids = Array.prototype.slice.call(list.children);
    G.set(kids, { autoAlpha: 0, y: 26 });
    var play = function () { G.to(kids, { autoAlpha: 1, y: 0, duration: 1, stagger: .07, ease: 'power3.out' }); };
    if (inView(list)) intro.add(play, .5); else ST.create({ trigger: list, start: 'top 88%', once: true, onEnter: play });
  });

  $$('[data-veil]').forEach(function (fr) {
    if (skip(fr)) return;
    var v = document.createElement('span'); v.className = 'veil'; fr.appendChild(v);
    var media = $('img, video', fr);
    var tl = G.timeline({ paused: true });
    tl.to(v, { scaleY: 0, duration: 1.35, ease: 'expo.inOut' });
    if (media && !fr.classList.contains('px')) tl.from(media, { scale: 1.22, duration: 2, ease: 'expo.out' }, .1);
    if (inView(fr)) intro.add(function () { tl.play(); }, .3);
    else ST.create({ trigger: fr, start: 'top 87%', once: true, onEnter: function () { tl.play(); } });
  });

  $$('.frame.px').forEach(function (fr) {
    var img = $('img', fr); if (!img) return;
    G.fromTo(img, { yPercent: -7 }, { yPercent: 7, ease: 'none', scrollTrigger: { trigger: fr, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  $$('[data-count]').forEach(function (el) {
    var raw = el.getAttribute('data-count'), end = parseFloat(raw), o = { v: 0 }, dec = (raw.split('.')[1] || '').length;
    el.textContent = (0).toFixed(dec).replace('.', ',');
    ST.create({ trigger: el, start: 'top 92%', once: true, onEnter: function () { G.to(o, { v: end, duration: 2.2, ease: 'power3.out', onUpdate: function () { el.textContent = o.v.toFixed(dec).replace('.', ','); } }); } });
  });

  var mm = G.matchMedia();

  var film = $('.film');
  if (film) {
    var frame = $('.film-frame', film), fv = $('video', frame), cap = $('.film-cap', film), ftop = $('.film-top', film);
    mm.add('(min-width: 641px)', function () {
      G.set(fv, { scale: 1.22 }); G.set(cap, { autoAlpha: 0, y: 40 });
      var tl = G.timeline({ scrollTrigger: { trigger: film, start: 'top top', end: '+=150%', scrub: .9, pin: '.film-stage', anticipatePin: 1 } });
      tl.fromTo(frame, { clipPath: 'inset(17% 24% 17% 24%)' }, { clipPath: 'inset(0% 0% 0% 0%)', ease: 'none', duration: 1, immediateRender: true })
        .to(fv, { scale: 1, ease: 'none', duration: 1 }, 0)
        .to(ftop, { autoAlpha: 0, duration: .3 }, .1)
        .to(cap, { autoAlpha: 1, y: 0, duration: .3, ease: 'power2.out' }, .72);
      return function () { G.set([frame, fv, cap, ftop], { clearProps: 'all' }); };
    });
    mm.add('(max-width: 640px)', function () {
      G.fromTo(frame, { clipPath: 'inset(12% 7% 12% 7%)' }, { clipPath: 'inset(0% 0% 0% 0%)', ease: 'none', scrollTrigger: { trigger: film, start: 'top 85%', end: 'top 5%', scrub: true } });
    });
  }

  var reel = $('.reel');
  if (reel) {
    mm.add('(min-width: 901px)', function () {
      var track = $('.reel-track', reel), bar = $('.reel-progress i', reel), cnt = $('.reel-head .cnt b', reel), panels = $$('.panel', reel);
      var dist = function () { return Math.max(0, track.scrollWidth - window.innerWidth); };
      var tw = G.to(track, { x: function () { return -dist(); }, ease: 'none', scrollTrigger: {
        trigger: reel, start: 'top top', end: function () { return '+=' + dist(); }, scrub: .9, pin: true, invalidateOnRefresh: true, anticipatePin: 1,
        onUpdate: function (s) { if (bar) bar.style.transform = 'scaleX(' + s.progress + ')'; if (cnt) cnt.textContent = ('0' + Math.min(panels.length, 1 + Math.floor(s.progress * panels.length * .999))).slice(-2); }
      } });
      panels.forEach(function (p) {
        var im = $('.frame img', p); if (!im) return;
        G.fromTo(im, { scale: 1.18 }, { scale: 1, ease: 'none', scrollTrigger: { trigger: p, containerAnimation: tw, start: 'left right', end: 'right left', scrub: true } });
      });
      return function () { G.set(track, { clearProps: 'all' }); };
    });
  }

  var circ = $('.circuit');
  if (circ) {
    var path = $('.trace', circ), nodes = $$('.node', circ), len = path.getTotalLength(), stepsEl = $('.steps');
    G.set(path, { strokeDasharray: len, strokeDashoffset: len });
    G.to(path, { strokeDashoffset: 0, ease: 'none', scrollTrigger: { trigger: stepsEl, start: 'top 60%', end: 'bottom 65%', scrub: .6,
      onUpdate: function (s) { nodes.forEach(function (n, i) { n.classList.toggle('on', s.progress >= i / (nodes.length - 1) - .03); }); } } });
  }

  $$('.scan').forEach(function (sc) {
    var top = $('.top', sc), beam = $('.beam', sc);
    var tl = G.timeline({ scrollTrigger: { trigger: sc, start: 'top 78%', end: 'bottom 42%', scrub: .6 } });
    tl.set(beam, { opacity: 1 }, 0)
      .fromTo(top, { clipPath: 'inset(0% 0% 100% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', ease: 'none', duration: 1 }, 0)
      .fromTo(beam, { top: '0%' }, { top: '100%', ease: 'none', duration: 1 }, 0)
      .to(beam, { opacity: 0, duration: .04 }, .97);
  });

  $$('.zone > .frame img').forEach(function (img) {
    G.fromTo(img, { scale: 1.2, yPercent: -5 }, { scale: 1, yPercent: 5, ease: 'none', scrollTrigger: { trigger: img.closest('.zone'), start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  $$('.phero-media').forEach(function (m) {
    var im = $('img, video', m); if (!im) return;
    G.fromTo(im, { scale: 1.14 }, { scale: 1, ease: 'none', scrollTrigger: { trigger: m, start: 'top bottom', end: 'bottom top', scrub: true } });
  });

  var revealed = false;
  var reveal = function () {
    if (revealed) return; revealed = true;
    if (late) { if (pt) G.set(pt, { autoAlpha: 0 }); finishIntro(); intro.play(); ST.refresh(); window.dispatchEvent(new Event('mx:intro')); return; }
    if (pt) {
      G.set(pt, { autoAlpha: 1 });
      finishIntro();
      G.to(pt, { yPercent: -100, duration: 1.05, ease: 'expo.inOut', delay: .1, onComplete: function () { G.set(pt, { autoAlpha: 0, yPercent: 0 }); } });
      intro.delay(.5).play();
    } else { finishIntro(); intro.play(); }
    window.dispatchEvent(new Event('mx:intro'));
    ST.refresh();
  };
  if (document.fonts && document.fonts.ready) Promise.race([document.fonts.ready, new Promise(function (r) { setTimeout(r, 900); })]).then(reveal);
  else reveal();
  setTimeout(reveal, 1800);
  window.addEventListener('load', function () { ST.refresh(); });
})();
