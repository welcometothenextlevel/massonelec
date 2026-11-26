# -*- coding: utf-8 -*-
"""Shared pieces: icons, image helper, header, footer, forms, widgets."""
import json, html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
META = json.load(open(os.path.join(ROOT, '_build', 'imgmeta.json')))
META['scanner-poster'] = [1600, 900]
V = '9'  # asset cache-buster

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
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
 'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 'pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 'bolt': '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 'factory': '<path d="M2 20V9l6 4V9l6 4V4h6v16z"/><path d="M2 20h20M17 8h0"/>',
 'network': '<rect x="16" y="16" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="9" y="2" width="6" height="6" rx="1"/><path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3M12 12V8"/>',
 'home': '<path d="M3 10.5 12 3l9 7.5V21H3z"/><path d="M9 21v-6h6v6"/>',
 'bulb': '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2z"/>',
 'wrench': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
 'pulse': '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
 'scan': '<circle cx="12" cy="11" r="8"/><circle cx="12" cy="11" r="3.2"/><path d="M4 22h16"/>',
 'plan': '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.4 2.4 0 0 1 0-3.4l2.6-2.6a2.4 2.4 0 0 1 3.4 0z"/><path d="m14.5 12.5 2-2M11.5 9.5l2-2M8.5 6.5l2-2M17.5 15.5l2-2"/>',
 'cube': '<path d="M21 16V8a2 2 0 0 0-1-1.7l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.7l7 4a2 2 0 0 0 2 0l7-4a2 2 0 0 0 1-1.7z"/><path d="M3.3 7 12 12l8.7-5M12 22V12"/>',
 'check': '<path d="M20 6 9 17l-5-5"/>',
 'arrow': '<path d="M5 12h14M13 5l7 7-7 7"/>',
 'chev': '<path d="m6 9 6 6 6-6"/>',
 'chevl': '<path d="m15 18-6-6 6-6"/>', 'chevr': '<path d="m9 18 6-6-6-6"/>',
 'menu': '<path d="M3 6h18M3 12h18M3 18h18"/>',
 'x': '<path d="M18 6 6 18M6 6l12 12"/>',
 'camera': '<path d="M23 7l-7 5 7 5V7z"/><rect x="1" y="5" width="15" height="14" rx="2"/>',
 'flame': '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3.3.3 1.6 1.5 2.8 2.5 2.8z"/>',
 'lock': '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 'gen': '<rect x="2" y="6" width="20" height="13" rx="2"/><path d="M6 19v2M18 19v2M13 9l-3 4h4l-3 4"/>',
 'doc': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h6"/>',
 'users': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
 'building': '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
 'hospital': '<path d="M12 6v4M14 8h-4"/><path d="M18 22V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v18"/><path d="M2 22h20M10 22v-4h4v4M6 12H4a2 2 0 0 0-2 2v8M18 12h2a2 2 0 0 1 2 2v8"/>',
 'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20"/>',
 'card': '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
 'award': '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
 'flag': '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1zM4 22v-7"/>',
 'plug': '<path d="M12 22v-5M9 8V2M15 8V2M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8z"/>',
 'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 'cpu': '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/>',
 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'alert': '<path d="M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
 'msg': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 'play': '<path d="M7 4v16l13-8z" fill="currentColor" stroke="none"/>',
 'volume': '<path d="M11 5 6 9H2v6h4l5 4V5zM15.5 8.5a5 5 0 0 1 0 7M19 5a10 10 0 0 1 0 14"/>',
 'star': '<path fill="currentColor" stroke="none" d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
}
_B = {
 'wa': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.64.08-.3-.15-1.26-.47-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.07.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.83 9.83 0 0 1 2.89 6.99c0 5.45-4.44 9.88-9.88 9.88m8.41-18.3A11.82 11.82 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.88 11.88 0 0 0 5.68 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.16-3.48-8.41z"/></svg>',
 'fb': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.1 23.7v-8H6.63V12h2.47v-1.58c0-4.08 1.85-5.98 5.86-5.98.76 0 2.07.15 2.61.3v3.32c-.28-.03-.78-.05-1.39-.05-1.97 0-2.73.75-2.73 2.69V12h3.92l-.67 3.67h-3.25v8.25C19.4 23.24 24 18.18 24 12.04c0-6.63-5.37-12-12-12S0 5.41 0 12.04c0 5.63 3.87 10.35 9.1 11.65z"/></svg>',
 'li': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
 'g': '<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.1H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 13 4 4 13 4 24s9 20 20 20 20-9 20-20c0-1.3-.1-2.6-.4-3.9z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-7.9l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.1H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.6-.4-3.9z"/></svg>',
 'lc': '<svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="6" fill="#fff"/><text x="3.2" y="15.6" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="8.4" fill="#1d1d1b">local</text><circle cx="19.4" cy="6.4" r="2.6" fill="#e30613"/></svg>',
}

def ic(name, cls=''):
    if name in _B: return _B[name]
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_I[name]}</svg>'

def stars(n=5):
    return '<span class="stars" aria-label="%d sur 5">%s</span>' % (n, ''.join(ic('star') if i < n else ic('star').replace('currentColor', '#d6dce2') for i in range(5)))

# ---------------------------------------------------------------- images
def img(name, alt, cls='', sizes='(max-width: 720px) 100vw, 50vw', lazy=True, full=False):
    w, h = META[name]
    if w > 1600: h = round(h * 1600 / w); w = 1600
    srcset = f'assets/img/{name}-sm.webp 720w, assets/img/{name}.webp {w}w' if w > 720 else f'assets/img/{name}.webp {w}w'
    c = f' class="{cls}"' if cls else ''
    ld = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img{c} src="assets/img/{name}.webp" srcset="{srcset}" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}"{ld}>'

# ---------------------------------------------------------------- logos
def _svg_inner(path):
    s = open(path).read(); i = s.index('>') + 1; vb = s.split('viewBox="')[1].split('"')[0]
    return vb, s[i:s.rindex('</svg>')]
_mvb, _m = _svg_inner(os.path.join(ROOT, '_build', 'm.svg'))
_wvb, _w = _svg_inner(os.path.join(ROOT, '_build', 'word.svg'))
_w = _w.replace('fill="#1d2228"', 'class="sarl"')
def logo():
    return (f'<svg class="m" viewBox="{_mvb}" aria-hidden="true">{_m}</svg>'
            f'<svg class="w" viewBox="0 30 {_wvb.split()[2]} 150" aria-hidden="true">{_w}</svg>')
def logo_m_svg():
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{_mvb}">{_m}</svg>'

# ---------------------------------------------------------------- navigation
SERVICES = [
    # slug, title, short, icon, image
    ('electricite-generale', 'Électricité générale', 'Installations neuves et rénovations, intérieur et extérieur', 'bolt', 'plafond-led-blanc'),
    ('courant-fort-industrie', 'Courant fort & industrie', 'Armoires, force motrice, génératrices, infrastructures', 'factory', 'station-pompage-armoire'),
    ('courant-faible-reseaux', 'Courant faible & réseaux', 'Téléphonie, informatique, interphones, sécurité', 'network', 'baie-reseau'),
    ('domotique-eclairage', 'Domotique & éclairage LED', 'Pilotage du bâtiment, éclairage décoratif et extérieur', 'bulb', 'plafond-led-violet'),
    ('depannage-electrique-24h', 'Dépannage 24 h/24', 'Intervention rapide, 7 jours sur 7', 'wrench', 'tableau-distribution'),
    ('etudes-conception', 'Études & conception', 'Relevés, plans, schémas et calculs', 'plan', 'plan-electrique-2'),
    ('innovation-prototypage', 'Innovation & prototypage', 'Outils, pièces et objets conçus sur mesure', 'cube', 'piece-impression-3d'),
]
SVC_OPTS = ['Électricité générale', 'Courant fort / industrie', 'Courant faible, téléphonie, réseau', 'Domotique / éclairage LED',
            'Dépannage urgent', 'Imagerie médicale / santé', 'Études & plans', 'Innovation / prototypage', 'Autre demande']

def L(slug):
    return './' if slug in ('', 'index') else slug

def topbar():
    return f'''<div class="topbar"><div class="wrap">
  <span class="tb-item"><i class="dot-live"></i><span data-open-status>Dépannage 24/7</span></span>
  <a class="tb-item tb-urgent" href="tel:{CO['tel']}">{ic('phone')}<span>Urgence 24/7 · {CO['phone']}</span></a>
  <a class="tb-item tb-mail" href="mailto:{CO['email']}">{ic('mail')}<span>{CO['email']}</span></a>
  <span class="tb-item tb-addr">{ic('pin')}<span>{CO['street']}, {CO['npa']} {CO['city']}</span></span>
  <div class="tb-right">{socials()}</div>
</div></div>'''

def socials():
    return f'''<div class="socials">
  <a href="{CO['fb']}" target="_blank" rel="noopener" aria-label="Massonelec sur Facebook">{ic('fb')}</a>
  <a href="{CO['li']}" target="_blank" rel="noopener" aria-label="Jean-Gilbert Masson sur LinkedIn">{ic('li')}</a>
  <a href="{CO['gmaps']}" target="_blank" rel="noopener" aria-label="Massonelec sur Google">{ic('g')}</a>
  <a href="{CO['lc']}" target="_blank" rel="noopener" aria-label="Massonelec sur local.ch">{ic('lc')}</a>
</div>'''

def header(active):
    mega_items = ''.join(
        f'<a class="mi" href="{L(s)}"><span class="mi-ico">{ic(i)}</span><span><b>{t}</b><span>{d}</span></span></a>'
        for s, t, d, i, _ in SERVICES)
    mega_items += f'<a class="mi" href="prestations"><span class="mi-ico">{ic("arrow")}</span><span><b>Toutes les prestations</b><span>Vue d’ensemble de nos métiers</span></span></a>'
    def a(slug, label):
        cur = ' aria-current="page"' if active == slug else ''
        cls = ' active' if active == slug else ''
        return f'<li><a class="nav-link{cls}" href="{L(slug)}"{cur}>{label}</a></li>'
    svc_active = ' active' if active in [s[0] for s in SERVICES] + ['prestations'] else ''
    return f'''{topbar()}
<header class="hdr"><div class="wrap">
  <a class="brand" href="./" aria-label="Massonelec Sàrl, accueil">{logo()}</a>
  <nav aria-label="Navigation principale"><ul class="nav">
    {a('entreprise','Entreprise')}
    <li class="has-mega"><button class="nav-link{svc_active}" aria-expanded="false" aria-haspopup="true">Prestations {ic('chev')}</button>
      <div class="mega">{mega_items}
        <a class="mega-feature" href="imagerie-medicale">{img('scanner-poster','',sizes='280px')}<b>Imagerie médicale</b><span>Scanner et mammographe raccordés au Centre d’imagerie d’Aigle</span></a>
      </div></li>
    {a('imagerie-medicale','Secteur médical')}
    {a('realisations','Réalisations')}
    {a('contact','Contact')}
  </ul></nav>
  <div class="hdr-cta">
    <a class="hdr-phone" href="tel:{CO['tel']}">Dépannage 24/7<strong>{CO['phone']}</strong></a>
    <a class="btn btn-primary btn-sm" href="devis">Devis gratuit</a>
    <button class="burger" data-drawer-open aria-label="Ouvrir le menu" aria-controls="drawer">{ic('menu')}</button>
  </div>
</div></header>
<div class="drawer" id="drawer" aria-hidden="true" role="dialog" aria-label="Menu">
  <div class="drawer-top"><a class="brand" href="./">{logo()}</a><button class="burger" style="display:inline-flex" data-drawer-close aria-label="Fermer le menu">{ic('x')}</button></div>
  <nav aria-label="Menu mobile">
    <a href="./">Accueil {ic('chevr')}</a>
    <a href="entreprise">Entreprise {ic('chevr')}</a>
    <a href="prestations">Prestations {ic('chevr')}</a>
    <div class="sub">{''.join(f'<a href="{s}">{t}</a>' for s,t,_,_,_ in SERVICES)}</div>
    <a href="imagerie-medicale">Secteur médical {ic('chevr')}</a>
    <a href="realisations">Réalisations {ic('chevr')}</a>
    <a href="devis">Demande de devis {ic('chevr')}</a>
    <a href="contact">Contact {ic('chevr')}</a>
  </nav>
  <div class="drawer-cta">
    <a class="btn btn-dark" href="tel:{CO['tel']}">{ic('phone')} {CO['phone']}</a>
    <a class="btn btn-wa" href="https://wa.me/{CO['wa']}" target="_blank" rel="noopener">{ic('wa')} WhatsApp</a>
    <a class="btn btn-primary" href="devis">Devis gratuit</a>
    <div class="drawer-social">{socials()}</div>
  </div>
</div>'''

def footer():
    svc = ''.join(f'<li><a href="{s}">{t}</a></li>' for s, t, _, _, _ in SERVICES)
    return f'''<footer class="ftr">
  <div class="wrap ftr-top">
    <div>
      <a class="brand" href="./" aria-label="Massonelec Sàrl">{logo()}</a>
      <p class="about">Installateur-électricien à Aigle depuis 2000. Courant fort, courant faible, dépannage 24/7 et installations techniques exigeantes, du Chablais vaudois jusqu’à Bulle.</p>
      {socials()}
    </div>
    <div><h4>Prestations</h4><ul>{svc}<li><a href="imagerie-medicale">Imagerie médicale</a></li></ul></div>
    <div><h4>Entreprise</h4><ul>
      <li><a href="entreprise">Qui sommes-nous</a></li><li><a href="realisations">Réalisations</a></li>
      <li><a href="devis">Demande de devis</a></li><li><a href="contact">Contact & accès</a></li>
      <li><a href="{CO['greviews']}" target="_blank" rel="noopener">Avis Google</a></li><li><a href="{CO['lc']}" target="_blank" rel="noopener">Fiche local.ch</a></li>
    </ul></div>
    <div><h4>Contact</h4><ul>
      <li>{CO['name']}<br>{CO['street']}<br>{CO['npa']} {CO['city']} VD</li>
      <li><a href="tel:{CO['tel']}">{CO['phone']}</a> · 24/7</li>
      <li><a href="mailto:{CO['email']}">{CO['email']}</a></li>
    </ul>
    <div class="ftr-hours" style="margin-top:14px"><span>Lun – Jeu</span><span>7:30–12:00 · 13:30–17:00</span><span>Vendredi</span><span>7:30–12:00 · 13:30–16:00</span><span>Sam – Dim</span><span>Urgences uniquement</span></div>
    </div>
  </div>
  <div class="wrap ftr-bot">
    <span>© <span data-year>2026</span> {CO['name']} · IDE {CO['ide']}</span>
    <span>Installateur-électricien CFC · Aigle (VD)</span>
    <span class="r"><a href="mentions-legales">Mentions légales</a><a href="confidentialite">Protection des données</a></span>
  </div>
</footer>'''

def wa_widget():
    def opt(label, text):
        from urllib.parse import quote
        return f'<a href="https://wa.me/{CO["wa"]}?text={quote(text)}" target="_blank" rel="noopener">{label} {ic("arrow")}</a>'
    return f'''<button class="wa-fab" aria-label="Écrire à Massonelec sur WhatsApp" aria-expanded="false" aria-controls="wa-panel">{ic('wa')}<span class="badge">1</span></button>
<div class="wa-panel" id="wa-panel" aria-hidden="true" role="dialog" aria-label="WhatsApp Massonelec">
  <div class="wa-head"><span class="av"><svg viewBox="{_mvb}" style="width:100%">{_m}</svg></span><span><b>Massonelec Sàrl</b><small><i class="dot-live"></i> Électricien à Aigle</small></span><button class="x" aria-label="Fermer">{ic('x')}</button></div>
  <div class="wa-body"><div class="wa-msg">Bonjour 👋 Comment pouvons-nous vous aider ? Décrivez votre besoin, photos bienvenues.<small class="wa-time">08:00</small></div></div>
  <div class="wa-opts">
    {opt('⚡ Dépannage urgent', 'Bonjour Massonelec, j’ai besoin d’un dépannage électrique urgent. Adresse : ')}
    {opt('📋 Demander un devis', 'Bonjour Massonelec, je souhaiterais un devis pour : ')}
    {opt('💬 Poser une question', 'Bonjour Massonelec, j’ai une question : ')}
  </div>
</div>
<nav class="mbar" aria-label="Actions rapides">
  <a class="call" href="tel:{CO['tel']}">{ic('phone')}Appeler</a>
  <a class="wa" href="https://wa.me/{CO['wa']}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
  <a class="quote" href="devis">{ic('doc')}Devis</a>
</nav>'''

# ---------------------------------------------------------------- forms
def _opts(pre=''):
    return '<option value="">Choisir…</option>' + ''.join(f'<option{" selected" if o==pre else ""}>{o}</option>' for o in SVC_OPTS)

def quick_form(subject='Demande rapide – site web', pre='', idp='q'):
    return f'''<form class="js-form" data-subject="{esc(subject)}">
  <div class="form-grid">
    <div class="f"><label for="{idp}-n">Nom et prénom</label><input id="{idp}-n" name="nom" data-label="Nom" autocomplete="name" required></div>
    <div class="f"><label for="{idp}-t">Téléphone</label><input id="{idp}-t" name="tel" data-label="Téléphone" type="tel" autocomplete="tel" required></div>
    <div class="f"><label for="{idp}-s">Votre besoin</label><select id="{idp}-s" name="prestation" data-label="Prestation" required>{_opts(pre)}</select></div>
  </div>
  <div class="form-actions"><button class="btn btn-primary" type="submit" value="wa">{ic('wa')} Être rappelé</button></div>
  <p class="form-ok" role="status">Merci ! WhatsApp s’ouvre avec votre demande pré-remplie : il ne reste qu’à l’envoyer.</p>
</form>'''

def full_form(subject='Demande depuis le site', pre='', idp='c'):
    return f'''<form class="form js-form" data-subject="{esc(subject)}">
  <div class="form-grid">
    <div class="f"><label for="{idp}-n">Nom et prénom</label><input id="{idp}-n" name="nom" data-label="Nom" autocomplete="name" required></div>
    <div class="f"><label for="{idp}-c">Entreprise <span class="opt">(facultatif)</span></label><input id="{idp}-c" name="societe" data-label="Entreprise" autocomplete="organization"></div>
    <div class="f"><label for="{idp}-t">Téléphone</label><input id="{idp}-t" name="tel" data-label="Téléphone" type="tel" autocomplete="tel" required></div>
    <div class="f"><label for="{idp}-e">E-mail <span class="opt">(facultatif)</span></label><input id="{idp}-e" name="email" data-label="E-mail" type="email" autocomplete="email"></div>
    <div class="f"><label for="{idp}-l">Localité / NPA</label><input id="{idp}-l" name="lieu" data-label="Localité" autocomplete="address-level2" placeholder="Ex. 1860 Aigle"></div>
    <div class="f"><label for="{idp}-s">Prestation</label><select id="{idp}-s" name="prestation" data-label="Prestation" required>{_opts(pre)}</select></div>
    <div class="f full"><label for="{idp}-m">Votre projet ou votre panne</label><textarea id="{idp}-m" name="message" data-label="Message" required placeholder="Décrivez en quelques lignes : type de bâtiment, travaux souhaités, délais…"></textarea></div>
  </div>
  <div class="form-actions">
    <button class="btn btn-primary" type="submit" value="wa">{ic('wa')} Envoyer via WhatsApp</button>
    <button class="btn btn-ghost" type="submit" value="mail">{ic('mail')} Envoyer par e-mail</button>
  </div>
  <p class="form-note">Devis gratuit et sans engagement. Vos données servent uniquement à traiter votre demande (<a href="confidentialite">confidentialité</a>).</p>
  <p class="form-ok" role="status">Merci ! Votre message est pré-rempli dans WhatsApp ou votre messagerie : il ne reste qu’à l’envoyer. Nous revenons vers vous rapidement.</p>
</form>'''

def contact_list():
    return f'''<ul class="contact-list">
  <li><span class="ci">{ic('phone')}</span><span><small>Téléphone · urgences 24/7</small><a href="tel:{CO['tel']}">{CO['phone']}</a></span></li>
  <li><span class="ci wa">{ic('wa')}</span><span><small>WhatsApp · photos bienvenues</small><a href="https://wa.me/{CO['wa']}" target="_blank" rel="noopener" data-wa-open>Écrire sur WhatsApp</a></span></li>
  <li><span class="ci">{ic('mail')}</span><span><small>E-mail</small><a href="mailto:{CO['email']}">{CO['email']}</a></span></li>
  <li><span class="ci">{ic('pin')}</span><span><small>Bureau</small><a href="{CO['route']}" target="_blank" rel="noopener">{CO['street']}, {CO['npa']} {CO['city']}</a></span></li>
</ul>'''

def form_section(title='Parlons de votre projet', text=None, subject='Demande depuis le site', pre='', idp='c'):
    text = text or 'Un rendez-vous sur place pour comprendre vos besoins, puis un devis gratuit et sans engagement. Pour une panne, appelez directement : nous intervenons 24 h/24.'
    return f'''<section class="sec form-sec" id="formulaire"><div class="wrap form-wrap">
  <div class="form-aside" data-reveal>
    <span class="kicker">{ic('msg')} Contact & devis</span>
    <h2>{title}</h2>
    <p class="lead">{text}</p>
    {contact_list()}
  </div>
  <div data-reveal>{full_form(subject, pre, idp)}</div>
</div></section>'''

def cta_band(title='Une panne, un projet, une question ?', text='Un seul numéro, 24 h/24 et 7 j/7 pour les urgences.'):
    return f'''<section class="cta-band">{ic('bolt','bolt-bg')}<div class="wrap">
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="btns"><a class="btn btn-dark" href="tel:{CO['tel']}">{ic('phone')} {CO['phone']}</a><a class="btn btn-light" href="devis">Demander un devis</a></div>
</div></section>'''

def phero(crumb, h1, lead, image=None, video=None, card_title='Devis gratuit et sans engagement', card_text='Étude sur place, conseil et devis détaillé.', service=''):
    media = ''
    if video:
        media = f'<video data-autoplay autoplay muted loop playsinline preload="metadata" poster="assets/img/scanner-poster.webp"><source src="{video}" type="video/mp4"></video>'
    elif image:
        media = img(image, '', sizes='100vw', lazy=False)
    q = f'?service={esc(service)}' if service else ''
    return f'''<section class="phero">{media}<div class="wrap">
  <div>
    <nav class="crumbs" aria-label="Fil d’Ariane"><a href="./">Accueil</a><span aria-hidden="true">/</span>{crumb}</nav>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="hero-ctas"><a class="btn btn-primary" href="#formulaire">Demander un devis {ic('arrow')}</a><a class="btn btn-light" href="tel:{CO['tel']}">{ic('phone')} {CO['phone']}</a></div>
  </div>
  <aside class="phero-card"><b>{card_title}</b><p>{card_text}</p>
    <a class="btn btn-primary" href="devis{q}">{ic('doc')} Devis en ligne</a>
    <a class="btn btn-light" href="https://wa.me/{CO['wa']}" target="_blank" rel="noopener" data-wa-open>{ic('wa')} WhatsApp</a>
  </aside>
</div></section>'''

def related(exclude):
    items = [s for s in SERVICES if s[0] != exclude][:4]
    cards = ''.join(f'''<a class="svc" href="{s}" data-tilt data-reveal><span class="svc-ico">{ic(i)}</span><div class="svc-img">{img(im, t, sizes='(max-width:720px) 100vw, 25vw')}</div><div class="svc-body"><h3>{t}</h3><p>{d}</p><span class="link-arrow">Découvrir {ic('arrow')}</span></div></a>''' for s, t, d, i, im in items)
    return f'''<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('bolt')} Nos autres métiers</span><h2>Un seul interlocuteur pour tout le réseau électrique</h2></div><a class="link-arrow" href="prestations">Toutes les prestations {ic('arrow')}</a></div>
  <div class="svc-grid">{cards}</div>
</div></section>'''

# ---------------------------------------------------------------- page shell
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,500..800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'

def schema():
    d = {
        "@context": "https://schema.org", "@type": "Electrician", "name": "Massonelec Sàrl",
        "image": CO['site'] + "assets/img/tableau-domotique.webp", "logo": CO['site'] + "assets/img/logo-m.svg",
        "url": CO['site'], "telephone": "+41 79 350 55 19", "email": CO['email'],
        "address": {"@type": "PostalAddress", "streetAddress": CO['street'], "postalCode": CO['npa'], "addressLocality": CO['city'], "addressRegion": "VD", "addressCountry": "CH"},
        "geo": {"@type": "GeoCoordinates", "latitude": 46.308658, "longitude": 6.965828},
        "foundingDate": "2000", "founder": {"@type": "Person", "name": CO['boss']},
        "taxID": CO['ide'], "knowsLanguage": ["fr", "it"],
        "areaServed": ["Aigle", "Chablais vaudois", "Ollon", "Bex", "Villeneuve", "Leysin", "Villars-sur-Ollon", "Les Diablerets", "Montreux", "Vevey", "Château-d'Œx", "Châtel-Saint-Denis", "Bulle"],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "07:30", "closes": "12:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "13:30", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "07:30", "closes": "12:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "13:30", "closes": "16:00"}],
        "paymentAccepted": "Visa, Mastercard, American Express, Maestro, PostFinance Card, facture",
        "sameAs": [CO['fb'], CO['li'], CO['lc'], CO['gmaps']],
    }
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'

def page(slug, title, desc, body, active=None, extra_head='', base=None):
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
<meta name="theme-color" content="#0b1724">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_CH"><meta property="og:site_name" content="Massonelec Sàrl">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="{CO['site']}assets/img/og.jpg"><meta property="og:url" content="{canon}">
<link rel="icon" href="assets/img/logo-m.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
{FONTS}
<link rel="stylesheet" href="assets/css/site.css?v={V}">
<script>document.documentElement.classList.add('js')</script>
{schema() if slug in ('index','contact','entreprise') else ''}{extra_head}
</head>
<body>
<a class="skip" href="#main">Aller au contenu</a>
{header(active or slug)}
<main id="main">
{body}
</main>
{footer()}
{wa_widget()}
<script src="assets/vendor/gsap.min.js" defer></script>
<script src="assets/vendor/ScrollTrigger.min.js" defer></script>
<script src="assets/js/main.js?v={V}" defer></script>
</body>
</html>'''
