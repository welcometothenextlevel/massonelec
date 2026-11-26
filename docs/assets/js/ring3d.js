/* Massonelec — hero 3D: CT gantry, scroll-driven exploded view with live current */
import * as THREE from 'three';
import { RoomEnvironment } from '../vendor/RoomEnvironment.js';

const box = document.getElementById('ring');
if (box) init();

function rrect(w, h, r) {
  const s = new THREE.Shape(), x = -w / 2, y = -h / 2;
  s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.quadraticCurveTo(x + w, y, x + w, y + r);
  s.lineTo(x + w, y + h - r); s.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  s.lineTo(x + r, y + h); s.quadraticCurveTo(x, y + h, x, y + h - r);
  s.lineTo(x, y + r); s.quadraticCurveTo(x, y, x + r, y);
  return s;
}
function holed(w, h, r, hole) { const s = rrect(w, h, r); const p = new THREE.Path(); p.absarc(0, 0, hole, 0, Math.PI * 2, true); s.holes.push(p); return s; }
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const seg = (p, a, b) => clamp((p - a) / (b - a));
const ease = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;

function init() {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = () => innerWidth < 900;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' }); } catch (e) { return fallback(); }
  if (!renderer.getContext()) return fallback();
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile() ? 1.75 : 2));
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  box.prepend(renderer.domElement); renderer.domElement.setAttribute('aria-hidden', 'true');

  const scene = new THREE.Scene();
  const pm = new THREE.PMREMGenerator(renderer);
  scene.environment = pm.fromScene(new RoomEnvironment(), .04).texture;
  const camera = new THREE.PerspectiveCamera(30, 1, .1, 100);

  scene.add(new THREE.HemisphereLight(0xffffff, 0xd8d4cb, .7));
  const key = new THREE.DirectionalLight(0xffffff, 2.2); key.position.set(6, 9, 7); key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048); Object.assign(key.shadow.camera, { left: -7, right: 7, top: 7, bottom: -7 }); key.shadow.radius = 8; key.shadow.bias = -.0004;
  scene.add(key);
  const blueLight = new THREE.PointLight(0x00a4d8, 0, 9, 1.6); blueLight.position.set(0, 0, 1); scene.add(blueLight);

  const M = (c, r, m, extra = {}) => new THREE.MeshStandardMaterial(Object.assign({ color: c, roughness: r, metalness: m, envMapIntensity: .9 }, extra));
  const white = M(0xf6f5f1, .28, .02), grey = M(0xd4d1ca, .5, .05), dark = M(0x1d2024, .45, .4), steel = M(0xa9aeb4, .22, .9), red = M(0xc62f29, .4, .1);
  const glow = new THREE.MeshBasicMaterial({ color: 0x00a4d8, transparent: true, opacity: 1 });

  const G = new THREE.Group(); scene.add(G);
  const gantry = new THREE.Group(); G.add(gantry);

  // back housing
  const backGeo = new THREE.ExtrudeGeometry(holed(4.3, 4.5, .6, 1.1), { depth: .9, bevelEnabled: true, bevelThickness: .1, bevelSize: .1, bevelSegments: 8, curveSegments: 96 });
  backGeo.translate(0, 0, -1.0);
  const back = new THREE.Mesh(backGeo, grey); back.castShadow = back.receiveShadow = true; gantry.add(back);
  const backPlate = new THREE.Mesh(new THREE.BoxGeometry(1.6, .5, .06), dark); backPlate.position.set(0, -1.6, -1.12); gantry.add(backPlate);

  // rotating drum
  const drum = new THREE.Group(); gantry.add(drum);
  const ringFace = new THREE.Mesh(new THREE.RingGeometry(1.15, 1.95, 128), dark); ringFace.position.z = -.08; drum.add(ringFace);
  const rim = new THREE.Mesh(new THREE.CylinderGeometry(1.97, 1.97, .55, 128, 1, true), steel); rim.rotation.x = Math.PI / 2; rim.position.z = -.32; drum.add(rim);
  const innerRim = new THREE.Mesh(new THREE.CylinderGeometry(1.16, 1.16, .55, 128, 1, true), steel); innerRim.rotation.x = Math.PI / 2; innerRim.position.z = -.32; drum.add(innerRim);
  for (let i = 0; i < 20; i++) {
    const a = i / 20 * Math.PI * 2; if (i % 10 === 0) continue;
    const mat = i % 5 === 2 ? red : (i % 3 === 0 ? white : dark);
    const m = new THREE.Mesh(new THREE.BoxGeometry(.32, .28, .3), mat); m.position.set(Math.cos(a) * 1.56, Math.sin(a) * 1.56, .1); m.rotation.z = a; m.castShadow = true; drum.add(m);
  }
  const tube = new THREE.Mesh(new THREE.BoxGeometry(.82, .52, .46), white); tube.position.set(0, 1.52, .14); tube.castShadow = true; drum.add(tube);
  const detArc = new THREE.Mesh(new THREE.TorusGeometry(1.5, .07, 10, 80, Math.PI * .62), glow); detArc.rotation.z = Math.PI * 1.19; detArc.position.z = .18; drum.add(detArc);
  // x-ray fan (tube → detector)
  const fanGeo = new THREE.BufferGeometry();
  const fanPts = [0, 1.3, .14]; for (let i = 0; i <= 24; i++) { const a = Math.PI * 1.19 + i / 24 * Math.PI * .62; fanPts.push(Math.cos(a) * 1.45, Math.sin(a) * 1.45, .14); }
  const idx = []; for (let i = 1; i <= 24; i++) idx.push(0, i, i + 1);
  fanGeo.setAttribute('position', new THREE.Float32BufferAttribute(fanPts, 3)); fanGeo.setIndex(idx);
  const fan = new THREE.Mesh(fanGeo, new THREE.MeshBasicMaterial({ color: 0x00a4d8, transparent: true, opacity: 0, side: THREE.DoubleSide, depthWrite: false }));
  drum.add(fan);

  // bore
  const bore = new THREE.Mesh(new THREE.CylinderGeometry(1.1, 1.1, 1.5, 128, 1, true), M(0xeceae4, .55, 0, { side: THREE.BackSide }));
  bore.rotation.x = Math.PI / 2; bore.position.z = -.4; gantry.add(bore);

  // front cover
  const cover = new THREE.Group(); gantry.add(cover);
  const cov = new THREE.Mesh(new THREE.ExtrudeGeometry(holed(4.3, 4.5, .6, 1.1), { depth: .2, bevelEnabled: true, bevelThickness: .09, bevelSize: .09, bevelSegments: 8, curveSegments: 96 }), white);
  cov.castShadow = cov.receiveShadow = true; cover.add(cov);
  const led = new THREE.Mesh(new THREE.TorusGeometry(1.22, .028, 16, 200), glow); led.position.z = .31; cover.add(led);
  const ledHalo = new THREE.Mesh(new THREE.RingGeometry(1.16, 1.34, 128), new THREE.MeshBasicMaterial({ color: 0x00a4d8, transparent: true, opacity: .18, depthWrite: false })); ledHalo.position.z = .305; cover.add(ledHalo);
  const panel = new THREE.Mesh(new THREE.BoxGeometry(.95, .28, .04), dark); panel.position.set(1.2, 1.72, .31); cover.add(panel);
  const pdot = new THREE.Mesh(new THREE.CircleGeometry(.04, 20), glow); pdot.position.set(.86, 1.72, .335); cover.add(pdot);

  // base, power cabinet, couch
  const base = new THREE.Mesh(new THREE.BoxGeometry(3.5, .5, 1.7), grey); base.position.set(0, -2.55, -.45); base.castShadow = base.receiveShadow = true; G.add(base);
  const cab = new THREE.Group(); G.add(cab); cab.position.set(3.9, -1.75, -1.3);
  const cabBody = new THREE.Mesh(new THREE.BoxGeometry(1.1, 2.1, .8), white); cabBody.castShadow = true; cab.add(cabBody);
  const cabDoor = new THREE.Mesh(new THREE.BoxGeometry(.96, 1.9, .04), grey); cabDoor.position.z = .42; cab.add(cabDoor);
  const cabLed = new THREE.Mesh(new THREE.CircleGeometry(.045, 16), glow); cabLed.position.set(.3, .78, .45); cab.add(cabLed);
  const cabLbl = new THREE.Mesh(new THREE.PlaneGeometry(.42, .14), new THREE.MeshBasicMaterial({ color: 0x00a4d8 })); cabLbl.position.set(-.18, .78, .445); cab.add(cabLbl);
  const couch = new THREE.Group(); G.add(couch);
  const ped = new THREE.Mesh(new THREE.BoxGeometry(.75, 1.2, 1.25), grey); ped.position.set(0, -2.2, 3.15); ped.castShadow = true; couch.add(ped);
  const top = new THREE.Mesh(new THREE.BoxGeometry(.86, .12, 4.6), white); top.position.set(0, -1.54, 2.05); top.castShadow = true; couch.add(top);
  const pad = new THREE.Mesh(new THREE.BoxGeometry(.76, .06, 4.4), M(0x24272c, .85, 0)); pad.position.set(0, -1.45, 2.05); couch.add(pad);
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(40, 40), new THREE.ShadowMaterial({ opacity: .13 })); floor.rotation.x = -Math.PI / 2; floor.position.y = -2.8; floor.receiveShadow = true; G.add(floor);

  // cable from cabinet to gantry base + current pulses + arcs
  const cableCurve = new THREE.CatmullRomCurve3([new THREE.Vector3(3.9, -2.79, -1.3), new THREE.Vector3(3.2, -2.79, -1.0), new THREE.Vector3(2.2, -2.79, -.6), new THREE.Vector3(1.4, -2.55, -.5), new THREE.Vector3(.9, -2.2, -.55)]);
  const cable = new THREE.Mesh(new THREE.TubeGeometry(cableCurve, 80, .035, 8, false), dark); G.add(cable);
  const pulseN = 14, pulseGeo = new THREE.BufferGeometry(); pulseGeo.setAttribute('position', new THREE.Float32BufferAttribute(new Float32Array(pulseN * 3), 3));
  const pulses = new THREE.Points(pulseGeo, new THREE.PointsMaterial({ color: 0x00a4d8, size: .17, transparent: true, opacity: 0, depthWrite: false })); G.add(pulses);
  const arcs = [];
  for (let i = 0; i < 3; i++) {
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(new Float32Array(18 * 3), 3));
    const l = new THREE.Line(g, new THREE.LineBasicMaterial({ color: i === 1 ? 0x5fd0f5 : 0x0090c4, transparent: true, opacity: 0, linewidth: 2 })); G.add(l); arcs.push(l);
  }
  function zap(line, a, b, amp) {
    const p = line.geometry.attributes.position, n = p.count;
    for (let i = 0; i < n; i++) {
      const t = i / (n - 1), j = (i === 0 || i === n - 1) ? 0 : amp;
      p.setXYZ(i, a.x + (b.x - a.x) * t + (Math.random() - .5) * j, a.y + (b.y - a.y) * t + (Math.random() - .5) * j, a.z + (b.z - a.z) * t + (Math.random() - .5) * j);
    }
    p.needsUpdate = true;
  }

  // callouts
  const anchors = [
    { obj: cover, v: new THREE.Vector3(-1.7, 1.9, .3), txt: '01 — Capot du statif', a: .12, b: .55, l: 1 },
    { obj: drum, v: new THREE.Vector3(1.6, 1.25, .2), txt: '02 — Anneau rotatif', a: .3, b: .8 },
    { obj: cab, v: new THREE.Vector3(.55, .7, .4), txt: '03 — Alimentation dédiée', a: .5, b: 1.01 }
  ].map(a => { const el = document.createElement('div'); el.className = 'callout' + (a.l ? ' l' : ''); el.innerHTML = '<i></i><span></span>'; el.querySelector('span').textContent = a.txt; box.appendChild(el); return Object.assign(a, { el }); });

  // state
  let w = 1, h = 1, visible = true, mx = 0, my = 0, tx = 0, ty = 0, p = 0, intro = reduce ? 1 : 0, t0 = performance.now(), lastZap = 0, vel = 0, lastP = 0;
  function resize() { w = box.clientWidth; h = box.clientHeight; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  new ResizeObserver(resize).observe(box); resize();
  new IntersectionObserver(es => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(box);
  addEventListener('pointermove', e => { tx = e.clientX / innerWidth - .5; ty = e.clientY / innerHeight - .5; }, { passive: true });
  const start = () => {
    const g = window.gsap, o = { v: 0 };
    if (g && !reduce) g.to(o, { v: 1, duration: 2.6, ease: 'expo.out', delay: .3, onUpdate: () => { intro = o.v; } }); else intro = 1;
  };
  if (window.__mx && window.__mx.ready) start(); else addEventListener('mx:intro', start, { once: true });
  setTimeout(() => { if (intro === 0) start(); }, 3200);

  const v3 = new THREE.Vector3(), A = new THREE.Vector3(), B = new THREE.Vector3();
  function frame(now) {
    const t = Math.max(0, (now - t0) / 1000);
    const hr = box.getBoundingClientRect(); const target = clamp(-hr.top / Math.max(1, hr.height));
    p += (target - p) * .09;
    vel += (Math.abs(p - lastP) * 60 - vel) * .1; lastP = p;
    mx += (tx - mx) * .05; my += (ty - my) * .05;
    const ie = ease(intro), mob = mobile();

    const ex = .1 * ie + ease(seg(p, 0, .8)) * .28;       // gentle opening
    const turn = ease(seg(p, 0, 1)) * .35;
    G.rotation.y = -0.55 - turn * .62 + (1 - ie) * -.7 + mx * .35 + (reduce ? 0 : Math.sin(t * .35) * .04);
    G.rotation.x = .08 + my * .1 - turn * .04;
    G.position.y = -.1 - (1 - ie) * .9 + (reduce ? 0 : Math.sin(t * .8) * .04);
    G.position.x = 0;
    G.scale.setScalar(.86 + ie * .14);

    cover.position.z = .15 * ie + ex * 3.4; cover.position.y = ex * .25; cover.rotation.y = ex * .22; cover.rotation.x = -ex * .05;
    back.position.z = -ex * 1.3;
    drum.position.z = ex * .55;
    couch.position.z = (1 - ie) * 1.5 + ex * 1.6;
    cab.position.x = 3.9 + (1 - ie) * 2 - ex * .2;
    drum.rotation.z = reduce ? 0 : drum.rotation.z - .008;

    // current & x-ray
    const live = 0;
    const beam = live * (0.55 + 0.45 * Math.random());
    fan.material.opacity = beam * .28;
    detArc.material.opacity = .6 + live * .4;
    blueLight.intensity = 0;
    ledHalo.material.opacity = .16 + (reduce ? 0 : Math.sin(t * 1.6) * .05);
    const pp = pulses.geometry.attributes.position;
    for (let i = 0; i < pulseN; i++) { const u = (((t * .55 + i / pulseN) % 1) + 1) % 1; cableCurve.getPoint(u, v3); pp.setXYZ(i, v3.x, v3.y + .04, v3.z); }
    pp.needsUpdate = true; pulses.material.opacity = .55 * ie;
    if (now - lastZap > 70) {
      lastZap = now;
      A.set(-.5, .3, .45).add(cab.position); B.set(1.9, -1.2, -.3).add(back.position);
      zap(arcs[0], A, B, .55); zap(arcs[1], A, B, .32);
      v3.set(Math.cos(t * 3) * 1.22, Math.sin(t * 3) * 1.22, .35); B.copy(v3).applyMatrix4(cover.matrix);
      A.set(Math.cos(t * 3 + 1) * 1.22, Math.sin(t * 3 + 1) * 1.22, .35).applyMatrix4(cover.matrix);
      zap(arcs[2], A, B, .2);
    }
    const flick = Math.random() > .25 ? 1 : .3;
    arcs[0].material.opacity = live * .95 * flick; arcs[1].material.opacity = live * .6 * flick; arcs[2].material.opacity = live * ex * .7 * flick;

    camera.position.set(mob ? 0 : .3, 1.5, mob ? 14.5 : 18.5);
    camera.lookAt(mob ? .3 : 0, -.45, 0);
    renderer.render(scene, camera);

    anchors.forEach(a => {
      a.obj.updateMatrixWorld(); v3.copy(a.v).applyMatrix4(a.obj.matrixWorld).project(camera);
      a.el.style.left = ((v3.x + 1) / 2 * w).toFixed(1) + 'px'; a.el.style.top = ((1 - v3.y) / 2 * h - 5).toFixed(1) + 'px';
      a.el.classList.remove('on');
    });
  }
  let raf = 0;
  function loop() { cancelAnimationFrame(raf); const step = now => { if (!visible) return; frame(now); raf = requestAnimationFrame(step); }; raf = requestAnimationFrame(step); }
  loop();
}
function fallback() { const img = document.createElement('img'); img.className = 'fb'; img.src = 'assets/img/scanner-poster.webp'; img.alt = ''; box.appendChild(img); }
