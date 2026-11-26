/* Massonelec — 3D service-area map (Chablais vaudois → Bulle) */
import * as THREE from '../vendor/three.module.min.js';

const box = document.getElementById('zone3d');
if (box) init();

function init() {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fallback = box.querySelector('.zone-fallback');
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' }); }
  catch (e) { return; }
  if (fallback) fallback.remove();
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  box.prepend(renderer.domElement);
  renderer.domElement.setAttribute('aria-hidden', 'true');

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x0b1724, 38, 90);
  const camera = new THREE.PerspectiveCamera(38, 1, 0.1, 200);

  // ---- geo projection ----
  const LON0 = 6.97, LAT0 = 46.40, K = 110, COS = Math.cos(LAT0 * Math.PI / 180);
  const P = (lon, lat) => new THREE.Vector2((lon - LON0) * K * COS, -(lat - LAT0) * K);

  const lake = [[6.66,46.50],[6.73,46.488],[6.80,46.474],[6.843,46.462],[6.89,46.44],[6.91,46.432],[6.927,46.40],[6.90,46.388],[6.86,46.384],[6.805,46.392],[6.72,46.408],[6.66,46.42]].map(p => P(p[0], p[1]));
  const rhone = [[6.86,46.386],[6.90,46.345],[6.95,46.31],[6.975,46.28],[6.995,46.25],[7.003,46.218],[7.03,46.18],[7.07,46.15]].map(p => P(p[0], p[1]));

  const towns = [
    ['Aigle', 6.9706, 46.3180, 1], ['Ollon', 6.9930, 46.2950], ['Bex', 7.0110, 46.2517], ['Yvorne', 6.9606, 46.3315],
    ['Roche', 6.9310, 46.3640], ['Villeneuve', 6.9270, 46.3970], ['Montreux', 6.9106, 46.4312], ['Vevey', 6.8430, 46.4628],
    ['Leysin', 7.0130, 46.3420], ['Villars', 7.0570, 46.2980], ['Les Diablerets', 7.1590, 46.3500],
    ['Châtel-St-Denis', 6.9010, 46.5270], ['Château-d’Œx', 7.1310, 46.4750], ['Bulle', 7.0570, 46.6190]
  ];

  // ---- helpers ----
  function segDist(p, a, b) {
    const abx = b.x - a.x, aby = b.y - a.y, t = Math.max(0, Math.min(1, ((p.x - a.x) * abx + (p.y - a.y) * aby) / (abx * abx + aby * aby)));
    const dx = a.x + abx * t - p.x, dy = a.y + aby * t - p.y; return Math.sqrt(dx * dx + dy * dy);
  }
  function polyDist(p, pts, closed) { let d = 1e9; for (let i = 0; i < pts.length - (closed ? 0 : 1); i++) d = Math.min(d, segDist(p, pts[i], pts[(i + 1) % pts.length])); return d; }
  function inPoly(p, pts) { let c = false; for (let i = 0, j = pts.length - 1; i < pts.length; j = i++) { if (((pts[i].y > p.y) !== (pts[j].y > p.y)) && (p.x < (pts[j].x - pts[i].x) * (p.y - pts[i].y) / (pts[j].y - pts[i].y) + pts[i].x)) c = !c; } return c; }
  function hash(x, y) { const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453; return s - Math.floor(s); }
  function noise(x, y) { const ix = Math.floor(x), iy = Math.floor(y), fx = x - ix, fy = y - iy, u = fx * fx * (3 - 2 * fx), v = fy * fy * (3 - 2 * fy);
    return (hash(ix, iy) * (1 - u) + hash(ix + 1, iy) * u) * (1 - v) + (hash(ix, iy + 1) * (1 - u) + hash(ix + 1, iy + 1) * u) * v; }
  function fbm(x, y) { let a = 0, f = 1, amp = .55; for (let i = 0; i < 5; i++) { a += noise(x * f, y * f) * amp; f *= 2.03; amp *= .5; } return a; }
  const smooth = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
  function height(x, z) {
    const p = new THREE.Vector2(x, z);
    if (inPoly(p, lake)) return -0.15;
    const d = Math.min(polyDist(p, rhone, false), polyDist(p, lake, true));
    const m = smooth(1.2, 7.5, d);
    const alps = 0.6 + smooth(10, -20, z) * 0.6 + smooth(-6, 14, x) * 0.5; // higher to the south-east
    return m * fbm(x * .085 + 3, z * .085 + 7) * 6.2 * alps;
  }

  // ---- terrain as points ----
  const SIZE = 74, N = 150, pos = [], col = [];
  const cLow = new THREE.Color(0x1b4a6c), cHigh = new THREE.Color(0x8fe0fa), tmp = new THREE.Color();
  for (let i = 0; i <= N; i++) for (let j = 0; j <= N; j++) {
    const x = -SIZE / 2 + SIZE * i / N, z = -SIZE / 2 + SIZE * j / N;
    if (inPoly(new THREE.Vector2(x, z), lake)) continue;
    const h = height(x, z); pos.push(x, h, z);
    tmp.copy(cLow).lerp(cHigh, Math.min(1, h / 5.5)); col.push(tmp.r, tmp.g, tmp.b);
  }
  const tg = new THREE.BufferGeometry();
  tg.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  tg.setAttribute('color', new THREE.Float32BufferAttribute(col, 3));
  const terrain = new THREE.Points(tg, new THREE.PointsMaterial({ size: 0.13, vertexColors: true, transparent: true, opacity: .9, sizeAttenuation: true }));
  scene.add(terrain);

  // ---- lake ----
  const shape = new THREE.Shape(lake.map(p => new THREE.Vector2(p.x, -p.y)));
  const lakeMesh = new THREE.Mesh(new THREE.ShapeGeometry(shape), new THREE.MeshBasicMaterial({ color: 0x0f3a5e, transparent: true, opacity: .85 }));
  lakeMesh.rotation.x = -Math.PI / 2; lakeMesh.position.y = -0.12; scene.add(lakeMesh);
  const lakeLine = new THREE.LineLoop(new THREE.BufferGeometry().setFromPoints(lake.map(p => new THREE.Vector3(p.x, -0.05, p.y))), new THREE.LineBasicMaterial({ color: 0x3a9bd0, transparent: true, opacity: .7 }));
  scene.add(lakeLine);

  // ---- river ----
  const rc = new THREE.CatmullRomCurve3(rhone.map(p => new THREE.Vector3(p.x, 0.04, p.y)));
  scene.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(rc.getPoints(120)), new THREE.LineBasicMaterial({ color: 0x3a9bd0, transparent: true, opacity: .8 })));

  // ---- towns + arcs ----
  const labelsBox = box.querySelector('.labels');
  const hqP = P(towns[0][1], towns[0][2]); const hq = new THREE.Vector3(hqP.x, height(hqP.x, hqP.y) + .12, hqP.y);
  const nodes = [], arcs = [];
  const dotGeo = new THREE.SphereGeometry(.22, 16, 12);
  towns.forEach((t, i) => {
    const p = P(t[1], t[2]); const v = new THREE.Vector3(p.x, Math.max(0, height(p.x, p.y)) + .12, p.y);
    const m = new THREE.Mesh(i === 0 ? new THREE.SphereGeometry(.42, 24, 16) : dotGeo, new THREE.MeshBasicMaterial({ color: i === 0 ? 0x00a4d8 : 0xffffff }));
    m.position.copy(v); scene.add(m);
    const el = document.createElement('div'); el.className = 'lbl' + (i === 0 ? ' hq' : ''); el.textContent = i === 0 ? 'Aigle · siège' : t[0]; labelsBox.appendChild(el);
    nodes.push({ v, el });
    if (i > 0) {
      const mid = hq.clone().lerp(v, .5); mid.y += 1.2 + hq.distanceTo(v) * .18;
      const curve = new THREE.QuadraticBezierCurve3(hq, mid, v);
      const g = new THREE.BufferGeometry().setFromPoints(curve.getPoints(64)); g.setDrawRange(0, 0);
      const line = new THREE.Line(g, new THREE.LineBasicMaterial({ color: 0x00a4d8, transparent: true, opacity: .75 }));
      scene.add(line); arcs.push({ g, delay: i * .12 });
    }
  });
  // HQ pulse rings
  const rings = [0, 1, 2].map(k => { const r = new THREE.Mesh(new THREE.RingGeometry(.5, .58, 48), new THREE.MeshBasicMaterial({ color: 0x00a4d8, transparent: true, side: THREE.DoubleSide })); r.rotation.x = -Math.PI / 2; r.position.copy(hq); r.userData.o = k / 3; scene.add(r); return r; });
  // beam
  const beam = new THREE.Mesh(new THREE.CylinderGeometry(.03, .03, 6, 8), new THREE.MeshBasicMaterial({ color: 0x00a4d8, transparent: true, opacity: .5 }));
  beam.position.set(hq.x, hq.y + 3, hq.z); scene.add(beam);

  // ---- camera rig ----
  const target = new THREE.Vector3(1.5, 0, -4);
  let mx = 0, my = 0, tx = 0, ty = 0;
  box.addEventListener('pointermove', e => { const r = box.getBoundingClientRect(); tx = (e.clientX - r.left) / r.width - .5; ty = (e.clientY - r.top) / r.height - .5; });
  box.addEventListener('pointerleave', () => { tx = 0; ty = 0; });

  function resize() { const w = box.clientWidth, h = box.clientHeight; renderer.setSize(w, h, false); camera.aspect = w / h; camera.fov = w / h < 1 ? 48 : 38; camera.updateProjectionMatrix(); }
  new ResizeObserver(resize).observe(box); resize();

  let visible = true, t0 = performance.now();
  new IntersectionObserver(es => { visible = es[0].isIntersecting; if (visible) loop(); }, { threshold: 0 }).observe(box);
  const v3 = new THREE.Vector3();
  function frame(now) {
    const t = (now - t0) / 1000;
    mx += (tx - mx) * .05; my += (ty - my) * .05;
    const ang = -0.55 + (reduce ? 0 : Math.sin(t * .12) * .16) + mx * .35;
    const rad = 44, el = 27 - my * 6;
    camera.position.set(target.x + Math.sin(ang) * rad, el, target.z + Math.cos(ang) * rad);
    camera.lookAt(target);
    arcs.forEach(a => { const k = reduce ? 1 : Math.max(0, Math.min(1, (t - .4 - a.delay) / 1.4)); a.g.setDrawRange(0, Math.floor(65 * (1 - Math.pow(1 - k, 3)))); });
    rings.forEach(r => { const k = ((t * .45 + r.userData.o) % 1); r.scale.setScalar(1 + k * 5); r.material.opacity = (1 - k) * .7; });
    renderer.render(scene, camera);
    const w = box.clientWidth, h = box.clientHeight;
    nodes.forEach(n => { v3.copy(n.v).project(camera); const vis = v3.z < 1 && Math.abs(v3.x) < 1.05 && Math.abs(v3.y) < 1.05; n.el.style.display = vis ? '' : 'none'; if (vis) { n.el.style.left = ((v3.x + 1) / 2 * w).toFixed(1) + 'px'; n.el.style.top = ((1 - v3.y) / 2 * h).toFixed(1) + 'px'; } });
  }
  let raf = 0;
  function loop() { cancelAnimationFrame(raf); const step = now => { if (!visible) return; frame(now); raf = requestAnimationFrame(step); }; raf = requestAnimationFrame(step); }
  loop();
}
