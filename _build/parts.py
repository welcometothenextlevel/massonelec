# -*- coding: utf-8 -*-
"""Massonelec v2 — shared building blocks (Swiss engineering design)."""
import json, html, os, re
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = json.load(open(os.path.join(ROOT, '_build', 'imgmeta.json')))
META['scanner-poster'] = [1600, 900]
V = '31'

CO = dict(
    name='Massonelec Sàrl', phone='079 350 55 19', tel='+41793505519', wa='41793505519',
    email='picpus_ch@hotmail.com', street='Chemin de la Perrolaz 2', npa='1860', city='Aigle',
    ide='CHE-101.430.065', boss='Jean-Gilbert Masson',
    fb='https://www.facebook.com/Massonelec',
    li='https://www.linkedin.com/in/jean-gilbert-masson-139bb510b/',
    lc='https://www.local.ch/fr/d/aigle/1860/electricien/massonelec-sarl-1u3pTgRhQD-CVCJqm2c1HA',
    gmaps='https://maps.google.com/?cid=13618002348166478219',
    greviews='https://search.google.com/local/reviews?placeid=ChIJ_ZxNjNmXjkcRi_nlAPzc_Lw',
    gwrite='https://search.google.com/local/writereview?placeid=ChIJ_ZxNjNmXjkcRi_nlAPzc_Lw',
    route='https://www.google.com/maps/dir/?api=1&destination=Massonelec+S%C3%A0rl%2C+Chemin+de+la+Perrolaz+2%2C+1860+Aigle',
    site='https://welcometothenextlevel.github.io/massonelec/',
)

def esc(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- icons
_I = {
 'arrow': '<path d="M5 12h14M13 5l7 7-7 7"/>',
 'ne': '<path d="M7 17 17 7M8 7h9v9"/>',
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 'pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 'doc': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>',
 'x': '<path d="M18 6 6 18M6 6l12 12"/>',
 'chevl': '<path d="m15 18-6-6 6-6"/>', 'chevr': '<path d="m9 18 6-6-6-6"/>',
 'volume': '<path d="M11 5 6 9H2v6h4l5 4V5zM15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/>',
 'star': '<path fill="currentColor" stroke="none" d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
 'play': '<path d="M7 4v16l13-8z" fill="currentColor" stroke="none"/>',
 'spark': '<path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/><circle cx="12" cy="12" r="2.5"/>',
 'send': '<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>',
}
_B = {
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.47-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/></svg>',
 'fb': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.1 23.7v-8H6.63V12h2.47v-1.58c0-4.08 1.85-5.98 5.86-5.98.76 0 2.07.15 2.61.3v3.32c-.28-.03-.78-.05-1.39-.05-1.97 0-2.73.75-2.73 2.69V12h3.92l-.67 3.67h-3.25v8.25C19.4 23.24 24 18.18 24 12.04c0-6.63-5.37-12-12-12S0 5.41 0 12.04c0 5.63 3.87 10.35 9.1 11.65z"/></svg>',
 'li': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
 'g': '<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.1H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 13 4 4 13 4 24s9 20 20 20 20-9 20-20c0-1.3-.1-2.6-.4-3.9z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-7.9l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.1H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.6-.4-3.9z"/></svg>',
 'gmono': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.35 11.1H12v2.98h5.4c-.24 1.37-1.67 4.02-5.4 4.02-3.25 0-5.9-2.69-5.9-6.01S8.75 6.08 12 6.08c1.85 0 3.09.79 3.8 1.47l2.59-2.49C16.73 3.5 14.58 2.5 12 2.5 6.75 2.5 2.5 6.75 2.5 12S6.75 21.5 12 21.5c5.48 0 9.12-3.85 9.12-9.28 0-.62-.07-1.1-.15-1.57z"/></svg>',
 'lc': '<svg viewBox="0 0 24 24" aria-hidden="true"><text x="0.2" y="15.8" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="10" fill="currentColor">local</text><circle cx="20.2" cy="6.6" r="2.4" fill="#e30613"/></svg>',
}
def ic(name):
    if name in _B: return _B[name]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>'

def stars(n=5):
    off = ic('star').replace('currentColor', '#c9c8c3')
    return '<span class="stars" aria-label="%d sur 5">%s</span>' % (n, ''.join(ic('star') if i < n else off for i in range(5)))

# ---------------------------------------------------------------- images
def img(name, alt, sizes='(max-width: 900px) 100vw, 50vw', lazy=True, cls=''):
    w, h = META[name]
    cap = 1800 if name.startswith('st-') else 1600
    if w > cap: h = round(h * cap / w); w = cap
    srcset = f'assets/img/{name}-sm.webp 720w, assets/img/{name}.webp {w}w' if w > 720 else f'assets/img/{name}.webp {w}w'
    c = f' class="{cls}"' if cls else ''
    ld = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img{c} src="assets/img/{name}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}"{ld}>'

def frame(name, alt, ratio='r-43', px=True, veil=True, sizes='(max-width: 900px) 100vw, 50vw', lazy=True, extra=''):
    return f'<div class="frame {ratio}{" px" if px else ""}"{" data-veil" if veil else ""}{extra}>{img(name, alt, sizes, lazy)}</div>'

# ---------------------------------------------------------------- logo
def _svg_inner(path):
    s = open(path).read(); i = s.index('>') + 1; vb = s.split('viewBox="')[1].split('"')[0]
    return vb, s[i:s.rindex('</svg>')]
_mvb, _m = _svg_inner(os.path.join(ROOT, '_build', 'm.svg'))
def mark(cls='m'):
    return f'<svg class="{cls}" viewBox="{_mvb}" aria-hidden="true">{_m}</svg>'
def brand():
    return f'<a class="brand" href="./" aria-label="Massonelec Sàrl, accueil">{mark()}<span class="t"><b>Massonelec</b><span>Sàrl · Électricité · Aigle</span></span></a>'
def logo_m_svg():
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{_mvb}">{_m}</svg>'

# ---------------------------------------------------------------- site map
SERVICES = [
    ('electricite-generale', 'Électricité générale', 'Installations neuves et rénovations, intérieur et extérieur, contrôles OIBT.', 'plafond-led-blanc'),
    ('courant-fort-industrie', 'Courant fort & industrie', 'Armoires, force motrice, énergie de secours, stations de pompage.', 'station-pompage-armoire'),
    ('courant-faible-reseaux', 'Courant faible & réseaux', 'Téléphonie, informatique, interphones et caméras IP, détection.', 'st-fibre'),
    ('domotique-eclairage', 'Domotique & éclairage', 'Bâtiment programmable, LED décoratives, mise en lumière extérieure.', 'plafond-led-violet'),
    ('depannage-electrique-24h', 'Dépannage 24/7', 'Intervention rapide, jour et nuit, dans tout le Chablais.', 'st-test'),
    ('etudes-conception', 'Études & conception', 'Relevés, plans d’installation, schémas et calculs.', 'plan-electrique-2'),
    ('innovation-prototypage', 'Innovation & prototypage', 'Outils, lifts, pièces refaites en impression 3D.', 'proto-chassis-levage'),
]
SVC_OPTS = ['Électricité générale', 'Courant fort / industrie', 'Courant faible, téléphonie, réseau', 'Domotique / éclairage',
            'Dépannage urgent', 'Imagerie médicale / santé', 'Études & plans', 'Innovation / prototypage', 'Autre demande']
MENU = [('./', 'Accueil', 'st-villa'), ('prestations', 'Prestations', 'cablage-armoire'), ('imagerie-medicale', 'Secteur médical', 'scanner-poster'),
        ('realisations', 'Réalisations', 'station-pompage-salle'), ('entreprise', 'Entreprise', 'tableau-domotique'),
        ('devis', 'Devis gratuit', 'plan-electrique-2'), ('contact', 'Contact', 'st-chillon')]

# ---------------------------------------------------------------- chrome
def socials():
    return f'''<div class="soc">
  <a href="{CO['fb']}" target="_blank" rel="noopener" aria-label="Facebook">{ic('fb')}</a>
  <a href="{CO['li']}" target="_blank" rel="noopener" aria-label="LinkedIn">{ic('li')}</a>
  <a href="{CO['gmaps']}" target="_blank" rel="noopener" aria-label="Google">{ic('gmono')}</a>
  <a href="{CO['lc']}" target="_blank" rel="noopener" aria-label="local.ch">{ic('lc')}</a>
</div>'''

def header(active):
    def a(href, label, key):
        cur = ' aria-current="page"' if active == key else ''
        return f'<a href="{href}"{cur}>{label}</a>'
    svc_keys = [s[0] for s in SERVICES] + ['prestations']
    cur_attr = ' aria-current="page"'
    menu_items = ''.join(f'<li><a href="{h}"{cur_attr if (h.strip("./") or "index") == active else ""}><span class="mono">{i+1:02d}</span>{t}</a></li>' for i, (h, t, _) in enumerate(MENU))
    return f'''<header class="hdr"><div class="wrap">
  {brand()}
  <nav class="nav" aria-label="Navigation principale">
    {a('prestations', 'Prestations', 'prestations' if active in svc_keys else '')}
    {a('imagerie-medicale', 'Secteur médical', 'imagerie-medicale')}
    {a('realisations', 'Réalisations', 'realisations')}
    {a('entreprise', 'Entreprise', 'entreprise')}
    {a('contact', 'Contact', 'contact')}
  </nav>
  <span class="hdr-meta"><span class="dot"></span><span data-clock>Aigle</span></span>
  <a class="hdr-tel" href="tel:{CO['tel']}">{CO['phone']}</a>
  <a class="btn sm" href="devis">Devis <span class="ar">{ic('arrow')}</span></a>
  <button class="menu-btn" data-menu aria-controls="menu" aria-label="Ouvrir le menu"><i></i>Menu</button>
</div></header>
<div class="menu" id="menu" aria-hidden="true" role="dialog" aria-label="Menu">
  <div class="menu-top"><span style="color:#fff">{brand()}</span><button class="menu-close">Fermer</button></div>
  <div class="menu-in">
    <ul class="menu-list">{menu_items}</ul>
    <div class="menu-side">
      <div class="menu-img">{''.join(img(im, '', '40vw').replace('<img ', '<img class="on" ' if i == 0 else '<img ', 1) for i, (_, _, im) in enumerate(MENU))}</div>
      <div class="menu-contact">
        <div><span class="mono">Urgences 24/7</span><a href="tel:{CO['tel']}">{CO['phone']}</a></div>
        <div><span class="mono">E-mail</span><a href="mailto:{CO['email']}">{CO['email']}</a></div>
        <div><span class="mono">Bureau</span>{CO['street']}<br>{CO['npa']} {CO['city']} (VD)</div>
        <div><span class="mono">Réseaux</span>{socials()}</div>
      </div>
    </div>
  </div>
</div>'''

def footer():
    svc = ''.join(f'<li><a href="{s}">{t}</a></li>' for s, t, _, _ in SERVICES)
    return f'''<footer class="ftr" data-dark><div class="wrap">
  <div class="grid">
    <div class="c1">{brand()}
      <p class="about">Installateur-électricien CFC à Aigle depuis 2000. Courant fort, courant faible, imagerie médicale et dépannage 24/7, du Chablais vaudois jusqu’à Bulle.</p>
      {socials()}
    </div>
    <div class="c2"><h4>Prestations</h4><ul>{svc}<li><a href="imagerie-medicale">Imagerie médicale</a></li></ul></div>
    <div class="c3"><h4>Entreprise</h4><ul><li><a href="entreprise">Qui sommes-nous</a></li><li><a href="realisations">Réalisations</a></li><li><a href="devis">Demande de devis</a></li><li><a href="contact">Contact & accès</a></li><li><a href="{CO['greviews']}" target="_blank" rel="noopener">Avis Google</a></li><li><a href="{CO['lc']}" target="_blank" rel="noopener">local.ch</a></li></ul></div>
    <div class="c4"><h4>Contact</h4><ul>
      <li><a href="tel:{CO['tel']}">{CO['phone']}</a> — urgences 24/7</li>
      <li><a href="mailto:{CO['email']}">{CO['email']}</a></li>
      <li><a href="{CO['route']}" target="_blank" rel="noopener">{CO['street']}, {CO['npa']} {CO['city']}</a></li></ul>
      <div class="ftr-hours"><span>Lun–Jeu</span><span>7:30–12:00 · 13:30–17:00</span><span>Vendredi</span><span>7:30–12:00 · 13:30–16:00</span><span>Sam–Dim</span><span>Urgences uniquement</span></div>
    </div>
  </div>
  <div class="ftr-bot"><span>© <span data-year>2026</span> {CO['name']}</span><span>IDE {CO['ide']}</span><span>46.3087° N · 6.9658° E</span>
    <span class="r"><a href="mentions-legales">Mentions légales</a><a href="confidentialite">Protection des données</a></span></div>
</div></footer>'''

def wa_widget():
    def opt(label, text): return f'<a href="https://wa.me/{CO["wa"]}?text={quote(text)}" target="_blank" rel="noopener">{label}{ic("arrow")}</a>'
    return f'''<button class="wa-fab" aria-label="Écrire sur WhatsApp" aria-expanded="false" aria-controls="wa-panel"><span class="ic">{ic('wa')}</span><span>WhatsApp</span></button>
<div class="wa-panel" id="wa-panel" aria-hidden="true" role="dialog" aria-label="WhatsApp Massonelec">
  <div class="wa-head">{mark()}<span><b>Massonelec Sàrl</b><small><span class="dot"></span><span data-open>Électricien à Aigle</span></small></span><button class="x" aria-label="Fermer">{ic('x')}</button></div>
  <p class="wa-msg">Bonjour. Décrivez votre besoin, photos bienvenues : nous vous répondons rapidement.</p>
  <div class="wa-opts">
    {opt('Dépannage urgent', 'Bonjour Massonelec, j’ai besoin d’un dépannage électrique urgent. Adresse : ')}
    {opt('Demander un devis', 'Bonjour Massonelec, je souhaiterais un devis pour : ')}
    {opt('Poser une question', 'Bonjour Massonelec, j’ai une question : ')}
  </div>
</div>
<nav class="mbar" aria-label="Actions rapides">
  <a href="tel:{CO['tel']}">{ic('phone')}Appeler</a>
  <a class="w" href="https://wa.me/{CO['wa']}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
  <a class="q" href="devis">Devis gratuit</a>
</nav>'''


def ai_widget():
    return f'''<button class="ai-launch" data-ai aria-controls="ai" aria-expanded="false" aria-label="Poser une question à l’assistant"><span class="ic">{ic('spark')}</span><span>Une question ?</span></button>
<section class="ai" id="ai" aria-hidden="true" role="dialog" aria-label="Assistant Massonelec">
  <div class="ai-head">{mark()}<span><b>Assistant Massonelec</b><small><span class="dot"></span>Répond instantanément</small></span><button class="ai-x" aria-label="Fermer l’assistant">{ic('x')}</button></div>
  <div class="ai-log" aria-live="polite"></div>
  <div class="ai-chips"></div>
  <form class="ai-form" autocomplete="off"><input type="text" name="q" placeholder="Votre question sur Massonelec…" aria-label="Votre question" maxlength="300"><button type="submit" aria-label="Envoyer">{ic('send')}</button></form>
  <p class="ai-note">Assistant virtuel · réponses basées sur les informations publiques de Massonelec Sàrl</p>
</section>'''

# ---------------------------------------------------------------- blocks
def lines_h(tag, cls, parts):
    return f'<{tag} class="{cls}" data-lines>' + ''.join(f'<span class="ln"><span>{p}</span></span>' for p in parts) + f'</{tag}>'

def btn(href, label, cls='', ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="btn {cls}" href="{href}"{t}>{label}<span class="ar">{ic("arrow")}</span></a>'

def ulink(href, label, ext=False, attrs=''):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="ulink" href="{href}"{t}{attrs}>{label}{ic("ne")}</a>'

def label(num, name):
    return f'<div class="label"><b>{num}</b><span>{name}</span></div>'

def sec_top(num, name, h2, side='', act='', h2cls='d2'):
    s = f'<p class="lead side" data-r>{side}</p>' if side else ''
    a = f'<div class="act" data-r>{act}</div>' if act else ''
    return f'<div class="sec-top">{label(num, name)}<h2 class="{h2cls}" data-words>{h2}</h2>{s}{a}</div>'

def spec(rows):
    return '<table class="spec"><tbody>' + ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows) + '</tbody></table>'

def ulist(items):
    return '<ul class="list" data-stagger>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def rows(items):
    out = '<div class="rows">'
    for i, (t, d) in enumerate(items):
        body = d if isinstance(d, str) else '<ul>' + ''.join(f'<li>{x}</li>' for x in d) + '</ul>'
        if isinstance(d, str): body = f'<p>{d}</p>'
        out += f'<div class="row" data-r><span class="mono">{i+1:02d}</span><h3>{t}</h3><div>{body}</div></div>'
    return out + '</div>'

def faq(items):
    det = ''.join(f'<details><summary>{q}<i></i></summary><div class="ans">{a}</div></details>' for q, a in items)
    d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in items]}
    return f'<div class="faq" data-r>{det}</div><script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>'

def faq_section(items, num='—', title='Questions fréquentes.'):
    return f'''<section class="sec faq-wrap"><div class="wrap"><div class="grid">{label(num, 'FAQ')}<h2 class="d3" data-words>{title}</h2>{faq(items)}</div></div></section>'''

def _opts(pre=''):
    return '<option value="" disabled selected hidden></option>' + ''.join(f'<option{" selected" if o == pre else ""}>{o}</option>' for o in SVC_OPTS)

def fld(id_, name, lab, typ='text', req=True, full=False, auto='', area=False):
    r = ' required' if req else ''
    a = f' autocomplete="{auto}"' if auto else ''
    lab2 = lab + ('' if req else ' (facultatif)')
    ctl = f'<textarea id="{id_}" name="{name}" data-label="{lab}" placeholder=" "{r}></textarea>' if area else f'<input id="{id_}" name="{name}" type="{typ}" data-label="{lab}" placeholder=" "{a}{r}>'
    return f'<div class="fld{" full" if full else ""}">{ctl}<label for="{id_}">{lab2}</label><span class="bar"></span></div>'

def form(subject, pre='', idp='c'):
    return f'''<form class="form js-form" data-subject="{esc(subject)}">
  <div class="fields">
    {fld(idp+'-n','nom','Nom et prénom',auto='name')}
    {fld(idp+'-t','tel','Téléphone','tel',auto='tel')}
    {fld(idp+'-e','email','E-mail','email',req=False,auto='email')}
    {fld(idp+'-l','lieu','Localité',req=False,auto='address-level2')}
    <div class="fld full"><select id="{idp}-s" name="prestation" data-label="Prestation" required>{_opts(pre)}</select><label for="{idp}-s">Prestation</label><span class="bar"></span></div>
    {fld(idp+'-m','message','Votre projet ou votre panne',full=True,area=True)}
  </div>
  <div class="form-actions">
    <button class="btn wa" type="submit" value="wa">Envoyer via WhatsApp<span class="ar">{ic('arrow')}</span></button>
    <button class="btn ghost" type="submit" value="mail">Par e-mail<span class="ar">{ic('arrow')}</span></button>
  </div>
  <p class="form-note">Devis gratuit et sans engagement. Votre message s’ouvre pré-rempli dans WhatsApp ou votre messagerie : vous gardez la main sur l’envoi. <a href="confidentialite">Confidentialité</a></p>
  <p class="form-ok" role="status">Merci. Votre demande est prête : il ne reste qu’à l’envoyer. Nous revenons vers vous rapidement.</p>
</form>'''

def contact_block(title='Parlons de votre installation.', text='Un rendez-vous sur place, une étude, puis un devis gratuit et sans engagement. Pour une panne, appelez directement : nous intervenons 24 h/24.', subject='Demande depuis le site', pre='', idp='c', num='—'):
    return f'''<section class="sec dark contact" id="contact" data-dark><div class="wrap"><div class="grid">
  <div class="left">
    {label(num, 'Contact & devis')}
    <h2 class="d2" data-words>{title}</h2>
    <p class="lead" data-r>{text}</p>
    <a class="tel-big" href="tel:{CO['tel']}" data-r>{CO['phone']}</a>
    <div class="lines" data-stagger>
      <a href="https://wa.me/{CO['wa']}" target="_blank" rel="noopener" data-wa><span class="mono">WhatsApp</span><span>Écrire un message</span>{ic('ne')}</a>
      <a href="mailto:{CO['email']}"><span class="mono">E-mail</span><span>{CO['email']}</span>{ic('ne')}</a>
      <a href="{CO['route']}" target="_blank" rel="noopener"><span class="mono">Bureau</span><span>{CO['street']}, {CO['npa']} {CO['city']}</span>{ic('ne')}</a>
      <div><span class="mono">Horaires</span><span>Lun–Jeu 7:30–17:00 · Ven –16:00</span><span class="dot"></span></div>
    </div>
  </div>
  <div class="right" data-r>{form(subject, pre, idp)}</div>
</div></div></section>'''

def phero(meta_l, meta_r, h1_parts, aside, media='', h1cls='d1'):
    return f'''<section class="phero"><div class="wrap">
  <div class="meta"><span class="crumbs">{meta_l}</span><span>{meta_r}</span></div>
  <div class="grid">{lines_h('h1', h1cls, h1_parts)}<div class="aside" data-r>{aside}</div></div>
</div>{media}</section>'''

def phero_img(name, alt):
    return f'<div class="wrap"><div class="frame phero-media" data-veil>{img(name, alt, "100vw", lazy=False)}</div></div>'

def next_link(href, title, num='Page suivante'):
    return f'<a class="next wrap" href="{href}" style="display:block"><span class="mono">{num}</span><span class="d2">{title}{ic("arrow")}</span></a>'


def carousel(rows, title='Sur nos chantiers.', num='—', name='En images', dark=False):
    out = f'<section class="mq{" dark" if dark else ""}"{" data-dark" if dark else ""}><div class="wrap">{sec_top(num, name, title, h2cls="d3")}</div>'
    for r, (direction, speed, items) in enumerate(rows):
        cells = ''
        for dup in (False, True):
            for n, cap in items:
                d = ' data-dup aria-hidden="true" tabindex="-1"' if dup else ''
                cells += f'<button class="mq-item" data-lb data-full="assets/img/{n}.webp" data-caption="{esc(cap)}"{d}>{img(n, cap, "(max-width:900px) 60vw, 30vw")}<span>{cap}</span></button>'
        out += f'<div class="mq-row{" b" if r else ""}" data-dir="{direction}" data-speed="{speed}"><div class="mq-track">{cells}</div></div>'
    out += f'<div class="wrap"><div class="mq-hint"><span>Glissez pour parcourir · cliquez pour agrandir</span><a class="ulink" href="realisations">Toutes les réalisations{ic("ne")}</a></div></div></section>'
    return out

def lightbox():
    return f'<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Agrandissement"><button class="x" aria-label="Fermer">{ic("x")}</button><button class="p" aria-label="Précédent">{ic("chevl")}</button><figure></figure><button class="n" aria-label="Suivant">{ic("chevr")}</button></div>'

def gi(name, cats, cap, video=None):
    v = f' data-video="{video}"' if video else ''
    b = '<span class="vid">Vidéo</span>' if video else ''
    return f'<button class="gi" data-lb data-cat="{cats}" data-full="assets/img/{name}.webp" data-caption="{esc(cap)}"{v}><span class="fr">{img(name, cap, "(max-width:900px) 100vw, 33vw")}{b}</span><span class="cap"><span>{cap}</span></span></button>'

# ---------------------------------------------------------------- page shell
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter+Tight:wght@400;500;600&display=swap" rel="stylesheet">'

def schema():
    d = {
        "@context": "https://schema.org", "@type": "Electrician", "name": "Massonelec Sàrl",
        "image": CO['site'] + "assets/img/tableau-domotique.webp", "logo": CO['site'] + "assets/img/logo-m.svg",
        "url": CO['site'], "telephone": "+41 79 350 55 19", "email": CO['email'],
        "address": {"@type": "PostalAddress", "streetAddress": CO['street'], "postalCode": CO['npa'], "addressLocality": CO['city'], "addressRegion": "VD", "addressCountry": "CH"},
        "geo": {"@type": "GeoCoordinates", "latitude": 46.308658, "longitude": 6.965828},
        "foundingDate": "2000", "founder": {"@type": "Person", "name": CO['boss']}, "taxID": CO['ide'], "knowsLanguage": ["fr", "it"],
        "areaServed": ["Aigle", "Chablais vaudois", "Ollon", "Bex", "Villeneuve", "Leysin", "Villars-sur-Ollon", "Les Diablerets", "Montreux", "Vevey", "Château-d'Œx", "Châtel-Saint-Denis", "Bulle"],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "07:30", "closes": "12:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "13:30", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "07:30", "closes": "12:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "13:30", "closes": "16:00"}],
        "sameAs": [CO['fb'], CO['li'], CO['lc'], CO['gmaps']],
    }
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'

def page(slug, title, desc, body, active=None, extra_head='', extra_body='', base=None, pt_label=''):
    canon = CO['site'] + ('' if slug == 'index' else slug)
    b = f'<base href="{base}">' if base else ''
    return f'''<!doctype html>
<html lang="fr-CH">
<head>
<meta charset="utf-8">{b}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#f4f3ef">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_CH"><meta property="og:site_name" content="Massonelec Sàrl">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="{CO['site']}assets/img/og.jpg"><meta property="og:url" content="{canon}">
<link rel="icon" href="assets/img/logo-m.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<script>document.documentElement.classList.add('pre-intro')</script>
<script type="importmap">{{"imports":{{"three":"./assets/vendor/three.module.min.js"}}}}</script>
{FONTS}
<link rel="stylesheet" href="assets/css/site.css?v={V}">
{schema() if slug in ('index', 'contact', 'entreprise') else ''}{extra_head}
</head>
<body>
<div class="pt" aria-hidden="true">{mark()}<span class="mono">{esc(pt_label or 'Massonelec Sàrl')}</span><span class="bar"><i></i></span></div>
<a class="skip" href="#main">Aller au contenu</a>
{header(active or slug)}
<main id="main">
{body}
</main>
{footer()}
{wa_widget()}
{ai_widget()}
<div class="idx-float" aria-hidden="true"><img alt="" src="data:image/gif;base64,R0lGODlhAQABAAAAACw="></div>
<script src="assets/vendor/gsap.min.js?v={V}"></script>
<script src="assets/vendor/ScrollTrigger.min.js?v={V}"></script>
<script src="assets/vendor/lenis.min.js?v={V}"></script>
<script src="assets/js/main.js?v={V}"></script>
<script src="assets/js/assistant.js?v={V}" defer></script>
{extra_body}
</body>
</html>'''
