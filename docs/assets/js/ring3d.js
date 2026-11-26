/* Massonelec — hero 3D: CT gantry with exploded cover on scroll */
import * as THREE from '../vendor/three.module.min.js';

const box = document.getElementById('ring');
if (box) init();

function roundedRectShape(w, h, r) {
  const s = new THREE.Shape(), x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r); s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
  return s;
}
function holed(w, h, r, hole) {
  const s = roundedRectShape(w, h, r); const p = new THREE.Path(); p.absarc(0, 0, hole, 0, Math.PI * 2, true); s.holes.push(p); return s;
}

function init() {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' }); }
  catch (e) { fallback(); return; }
  if (!renderer.getContext()) { fallback(); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  box.prepend(renderer.domElement);
  renderer.domElement.setAttribute('aria-hidden', 'true');

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(28, 1, .1, 100);

  // lights
  scene.add(new THREE.HemisphereLight(0xffffff, 0xdcd8cf, 1.7));
  const key = new THREE.DirectionalLight(0xffffff, 2.1); key.position.set(5, 7, 8); key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024); key.shadow.camera.left = -5; key.shadow.camera.right = 5; key.shadow.camera.top = 5; key.shadow.camera.bottom = -5; key.shadow.radius = 6; key.shadow.bias = -.0005;
  scene.add(key);
  const rim = new THREE.DirectionalLight(0xbfe9ff, .9); rim.position.set(-6, 3, -4); scene.add(rim);

  const white = new THREE.MeshStandardMaterial({ color: 0xfbfaf6, roughness: .34, metalness: .02 });
  const grey = new THREE.MeshStandardMaterial({ color: 0xd9d7d1, roughness: .55, metalness: .05 });
  const dark = new THREE.MeshStandardMaterial({ color: 0x24272c, roughness: .5, metalness: .35 });
  const steel = new THREE.MeshStandardMaterial({ color: 0x9fa4aa, roughness: .3, metalness: .8 });
  const red = new THREE.MeshStandardMaterial({ color: 0xc8302b, roughness: .45, metalness: .1 });
  const blue = new THREE.MeshBasicMaterial({ color: 0x00a4d8 });

  const G = new THREE.Group(); scene.add(G);
  const gantry = new THREE.Group(); G.add(gantry);

  // back housing
  const backGeo = new THREE.ExtrudeGeometry(holed(4.3, 4.5, .55, 1.08), { depth: .95, bevelEnabled: true, bevelThickness: .08, bevelSize: .08, bevelSegments: 6, curveSegments: 72 });
  backGeo.translate(0, 0, -1.05);
  const back = new THREE.Mesh(backGeo, grey); back.castShadow = true; back.receiveShadow = true; gantry.add(back);

  // rotating drum (visible when cover lifts)
  const drum = new THREE.Group(); gantry.add(drum);
  const ringGeo = new THREE.RingGeometry(1.12, 1.92, 96);
  const ringFace = new THREE.Mesh(ringGeo, dark); ringFace.position.z = -.06; drum.add(ringFace);
  const drumRim = new THREE.Mesh(new THREE.CylinderGeometry(1.94, 1.94, .5, 96, 1, true), steel); drumRim.rotation.x = Math.PI / 2; drumRim.position.z = -.3; drum.add(drumRim);
  for (let i = 0; i < 18; i++) {
    const a = i / 18 * Math.PI * 2;
    if (i % 9 === 0) continue;
    const m = new THREE.Mesh(new THREE.BoxGeometry(.34, .3, .28), i % 6 === 3 ? red : (i % 3 === 0 ? white : dark));
    m.position.set(Math.cos(a) * 1.55, Math.sin(a) * 1.55, .1); m.rotation.z = a; m.castShadow = true; drum.add(m);
  }
  const tube = new THREE.Mesh(new THREE.BoxGeometry(.78, .5, .42), white); tube.position.set(0, 1.5, .14); tube.castShadow = true; drum.add(tube);
  const det = new THREE.Mesh(new THREE.CylinderGeometry(1.62, 1.62, .4, 48, 1, true, Math.PI * 1.2, Math.PI * .6), dark); det.rotation.x = Math.PI / 2; det.position.z = .1; drum.add(det);
  [-1, 1].forEach(s => { const b = new THREE.Mesh(new THREE.BoxGeometry(.3, .42, .3), red); b.position.set(s * 1.45, -.55, .14); drum.add(b); });

  // bore liner
  const bore = new THREE.Mesh(new THREE.CylinderGeometry(1.08, 1.08, 1.4, 96, 1, true), new THREE.MeshStandardMaterial({ color: 0xe9e7e1, roughness: .6, side: THREE.BackSide }));
  bore.rotation.x = Math.PI / 2; bore.position.z = -.35; gantry.add(bore);

  // front cover (explodes)
  const cover = new THREE.Group(); gantry.add(cover);
  const covGeo = new THREE.ExtrudeGeometry(holed(4.3, 4.5, .55, 1.08), { depth: .22, bevelEnabled: true, bevelThickness: .07, bevelSize: .07, bevelSegments: 6, curveSegments: 72 });
  const covMesh = new THREE.Mesh(covGeo, white); covMesh.castShadow = true; covMesh.receiveShadow = true; cover.add(covMesh);
  const led = new THREE.Mesh(new THREE.TorusGeometry(1.2, .022, 12, 160), blue); led.position.z = .3; cover.add(led);
  const panel = new THREE.Mesh(new THREE.BoxGeometry(.9, .26, .04), dark); panel.position.set(1.25, 1.7, .3); cover.add(panel);
  const dotL = new THREE.Mesh(new THREE.CircleGeometry(.035, 16), blue); dotL.position.set(.92, 1.7, .33); cover.add(dotL);

  // base + couch
  const base = new THREE.Mesh(new THREE.BoxGeometry(3.4, .55, 1.6), grey); base.position.set(0, -2.5, -.45); base.castShadow = true; base.receiveShadow = true; G.add(base);
  const couch = new THREE.Group(); G.add(couch);
  const ped = new THREE.Mesh(new THREE.BoxGeometry(.7, 1.15, 1.2), grey); ped.position.set(0, -2.15, 3.1); ped.castShadow = true; couch.add(ped);
  const top = new THREE.Mesh(new THREE.BoxGeometry(.82, .12, 4.4), white); top.position.set(0, -1.52, 2.0); top.castShadow = true; couch.add(top);
  const pad = new THREE.Mesh(new THREE.BoxGeometry(.72, .06, 4.2), new THREE.MeshStandardMaterial({ color: 0x2a2d32, roughness: .9 })); pad.position.set(0, -1.43, 2.0); couch.add(pad);

  // floor shadow catcher
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(30, 30), new THREE.ShadowMaterial({ opacity: .12 }));
  floor.rotation.x = -Math.PI / 2; floor.position.y = -2.78; floor.receiveShadow = true; G.add(floor);

  // callouts (HTML)
  const anchors = [
    { v: new THREE.Vector3(1.55, 1.2, .2), obj: drum, txt: 'Anneau rotatif', side: 'r' },
    { v: new THREE.Vector3(0, 0, .3), obj: gantry, txt: 'Tunnel du scanner', side: 'l' },
    { v: new THREE.Vector3(1.7, -2.3, .1), obj: G, txt: 'Alimentation dédiée', side: 'r' }
  ].map(a => { const el = document.createElement('div'); el.className = 'callout' + (a.side === 'l' ? ' l' : ''); el.innerHTML = '<i></i><span></span>'; el.querySelector('span').textContent = a.txt; box.appendChild(el); return Object.assign(a, { el }); });
  anchors[2].obj = base; anchors[2].v.set(1.7, .2, .5);
  anchors[0].obj = gantry;

  // state
  let w = 1, h = 1, visible = true, mx = 0, my = 0, tx = 0, ty = 0, prog = 0, intro = reduce ? 1 : 0, t0 = performance.now(), showCallouts = false;
  function resize() { w = box.clientWidth; h = box.clientHeight; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  new ResizeObserver(resize).observe(box); resize();
  new IntersectionObserver(es => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(box);
  addEventListener('pointermove', e => { tx = e.clientX / innerWidth - .5; ty = e.clientY / innerHeight - .5; }, { passive: true });

  const start = () => {
    const g = window.gsap; const o = { v: 0 };
    if (g && !reduce) g.to(o, { v: 1, duration: 2.4, ease: 'expo.out', delay: .35, onUpdate: () => { intro = o.v; } });
    else intro = 1;
    setTimeout(() => { showCallouts = true; }, reduce ? 0 : 1700);
  };
  if (window.__mx && window.__mx.ready) start(); else addEventListener('mx:intro', start, { once: true });
  setTimeout(() => { if (intro === 0) start(); }, 3000);

  const v3 = new THREE.Vector3();
  const hero = box.closest('.hero') || box;
  function frame(now) {
    const t = (now - t0) / 1000;
    const r = hero.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, -r.top / Math.max(1, r.height * .8)));
    prog += (p - prog) * .12;
    mx += (tx - mx) * .05; my += (ty - my) * .05;

    // intro: assemble from slightly turned & lowered
    const ie = intro;
    G.rotation.y = -0.62 + (1 - ie) * -0.5 + mx * .22 + prog * .55;
    G.rotation.x = 0.06 + my * .08 - prog * .05;
    G.position.y = -.15 - (1 - ie) * .6;
    const s = .9 + ie * .1; G.scale.setScalar(s);

    // exploded cover with scroll (+ a little at rest after intro)
    const ex = Math.min(1, .18 * ie + prog * 1.25);
    cover.position.z = ex * 2.1;
    cover.position.y = ex * .15;
    cover.rotation.y = ex * .18;
    drum.rotation.z = reduce ? 0 : -t * (1.2 + prog * 2.2);
    couch.position.z = (1 - ie) * 1.4 + prog * -.6;

    camera.position.set(0, 1.3, 18.5 - prog * 1.6);
    camera.lookAt(0, -.35, 0);
    renderer.render(scene, camera);

    anchors.forEach(a => {
      a.obj.updateMatrixWorld(); v3.copy(a.v).applyMatrix4(a.obj.matrixWorld).project(camera);
      const x = (v3.x + 1) / 2 * w, y = (1 - v3.y) / 2 * h;
      a.el.style.left = x.toFixed(1) + 'px'; a.el.style.top = (y - 5).toFixed(1) + 'px';
      a.el.classList.toggle('on', showCallouts && prog < .55);
    });
  }
  let raf = 0;
  function loop() { cancelAnimationFrame(raf); const step = now => { if (!visible) return; frame(now); raf = requestAnimationFrame(step); }; raf = requestAnimationFrame(step); }
  loop();
}

function fallback() {
  const img = document.createElement('img'); img.className = 'fb'; img.src = 'assets/img/scanner-poster.webp'; img.alt = ''; box.appendChild(img);
}
