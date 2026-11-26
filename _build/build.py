# -*- coding: utf-8 -*-
"""Massonelec v2 — build all pages into docs/.  python3 _build/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parts import *  # noqa

OUT = os.path.join(ROOT, 'docs')
P = {}
def add(slug, title, desc, body, **kw): P[slug] = page(slug, title, desc, body, **kw)

FAQ = [
    ('Intervenez-vous en urgence, la nuit et le week-end ?', 'Oui. Le dépannage électrique est assuré 24 h/24 et 7 j/7. Appelez directement le <a href="tel:+41793505519">079 350 55 19</a> : en cas de panne, un appel est toujours plus rapide qu’un formulaire.'),
    ('Le devis est-il payant ?', 'Non. Après un rendez-vous pour comprendre vos besoins et ceux de votre bâtiment, nous rédigeons un devis gratuit et sans engagement.'),
    ('Dans quelle région intervenez-vous ?', 'Depuis Aigle, dans tout le Chablais vaudois (Ollon, Bex, Villeneuve, Leysin, Villars, Les Diablerets…) et jusqu’à Bulle, en passant par la Riviera, la Veveyse et le Pays-d’Enhaut.'),
    ('Remettez-vous un rapport de sécurité ?', 'Oui. Nos installations sont contrôlées conformément à l’art. 31 de l’ordonnance fédérale sur les installations électriques à basse tension (OIBT). Le rapport de conformité est remis au propriétaire et au fournisseur d’énergie.'),
    ('Travaillez-vous pour l’industrie et le secteur médical ?', 'Oui. Nous avons notamment raccordé un scanner et installé l’alimentation d’un mammographe au Centre d’imagerie d’Aigle, mis en place une génératrice de 88 kVA dans un fort militaire et équipé une station de pompage d’eau potable.'),
    ('Quels moyens de paiement acceptez-vous ?', 'Paiement sur facture, cartes Visa, Mastercard, American Express, Maestro et PostFinance Card.'),
    ('Dans quelles langues peut-on vous joindre ?', 'En français et en italien.'),
]
ALL_SVC = [('imagerie-medicale', 'Imagerie médicale', 'Scanner et mammographe raccordés au Centre d’imagerie d’Aigle.', 'scanner-poster')] + SERVICES

def idx_list(items, start=1):
    out = '<ul class="idx" data-stagger>'
    for i, (s, t, d, im) in enumerate(items):
        tag = '<span class="tag">Santé</span>' if s == 'imagerie-medicale' else ''
        out += f'<li><a href="{s}" data-img="assets/img/{im}-sm.webp"><span class="n">{i+start:02d}</span><h3>{t}{tag}</h3><p>{d}</p><span class="go">{ic("arrow")}</span></a></li>'
    return out + '</ul>'

# =====================================================================
# HOME
# =====================================================================
PANELS = [
    ('scanner', 'scanner-poster', 'Santé · Aigle', 'Scanner d’imagerie médicale', 'Mise en place et raccordement d’un scanner au Centre d’imagerie d’Aigle.', [('Lieu', 'Centre d’imagerie d’Aigle'), ('Mission', 'Raccordement, mise en service')]),
    ('mammographe', 'imagerie-transformateur', 'Santé · Aigle', 'Mammographe, avec GE', 'Calcul, réalisation et installation de l’alimentation du mammographe, en collaboration avec GE.', [('Lieu', 'Centre d’imagerie d’Aigle'), ('Mission', 'Calcul, transformateur dédié')]),
    ('station-pompage', 'station-pompage-salle', 'Infrastructure', 'Station de pompage d’eau potable', 'Installation électrique complète d’une station de pompage d’eau potable, réalisée par notre société.', [('Ouvrage', 'Eau potable'), ('Mission', 'Armoires, puissance, pompes')]),
    ('generatrice', 'generatrice-88kva', 'Énergie de secours', 'Génératrice 88 kVA, fort militaire', 'Mise en place et raccordement d’un groupe électrogène dans un ouvrage militaire.', [('Puissance', '88 kVA'), ('Site', 'Fort militaire')]),
    ('jardin', 'eclairage-jardin', 'Particulier', 'Mise en lumière d’un jardin', 'Éclairage d’ambiance : arbres, cheminement, four extérieur.', [('Type', 'Éclairage extérieur'), ('Client', 'Particulier')]),
    ('miroir', 'miroir-retroeclaire', 'Sur mesure', 'Miroir à éclairage périphérique', 'Fabrication et pose d’un miroir avec éclairage au travers du verre.', [('Type', 'Fabrication sur mesure'), ('Pièce', 'Salle de bain')]),
]
panels = ''.join(f'''<article class="panel"><a class="frame" href="realisations#{a}">{img(im, t, "(max-width:900px) 84vw, 40vw")}</a>
  <div><span class="n">{i+1:02d} — {tag}</span><h3>{t}</h3><p>{d}</p>{spec(sp)}</div></article>''' for i, (a, im, tag, t, d, sp) in enumerate(PANELS))

circuit_svg = '''<svg viewBox="0 0 200 920" aria-hidden="true">
  <path class="bg" d="M40 20 V200 L90 250 V430 L40 480 V660 L90 710 V900"/>
  <path class="trace" d="M40 20 V200 L90 250 V430 L40 480 V660 L90 710 V900"/>
  <circle class="node" cx="40" cy="110" r="9"/><text x="62" y="114">01 · relevé</text>
  <circle class="node" cx="90" cy="340" r="9"/><text x="112" y="344">02 · devis</text>
  <circle class="node" cx="40" cy="570" r="9"/><text x="62" y="574">03 · chantier</text>
  <circle class="node" cx="90" cy="800" r="9"/><text x="112" y="804">04 · contrôle</text>
</svg>'''

FIGS = [
    ('st-villa', 'Particuliers & villas', 'Rénovation, extension, salle de bain, domotique, éclairage de jardin.', 'electricite-generale'),
    ('coffrets-comptage', 'Régies & immeubles', 'Tableaux, comptages, mises en conformité, dépannages pour les locataires.', 'electricite-generale'),
    ('vitrine-led', 'Commerces & bureaux', 'Éclairage de vitrines, réseau informatique, téléphonie, interphones.', 'courant-faible-reseaux'),
    ('st-substation', 'Industrie & infrastructures', 'Courant fort, armoires, force motrice, eau potable.', 'courant-fort-industrie'),
    ('st-corridor', 'Santé', 'Centres d’imagerie, cabinets médicaux et dentaires, établissements.', 'imagerie-medicale'),
    ('generatrice-88kva', 'Collectivités & sites sensibles', 'Énergie de secours, ouvrages publics et militaires.', 'courant-fort-industrie'),
]
figs = ''.join(f'''<a class="fig" href="{h}" data-r>{frame(im, t, "r-45", px=False, sizes="(max-width:900px) 100vw, 33vw")}<h3>{t}</h3><p>{d}</p></a>''' for im, t, d, h in FIGS)

WORK_A = [('station-pompage-salle', 'Station de pompage · eau potable'), ('tableau-domotique', 'Tableau domotique'), ('generatrice-88kva', 'Génératrice 88 kVA'), ('plafond-led-violet', 'Plafond LED couleur'), ('imagerie-transformateur', 'Transformateur · mammographe'), ('eclairage-jardin', 'Mise en lumière de jardin'), ('armoire-industrielle', 'Armoire industrielle'), ('miroir-retroeclaire', 'Miroir rétroéclairé'), ('coffrets-comptage', 'Coffrets de comptage'), ('vitrine-led', 'Vitrine lumineuse')]
WORK_B = [('station-pompage-armoire', 'Armoire de commande'), ('salon-eclairage', 'Salon éclairé'), ('cablage-armoire', 'Câblage d’armoire'), ('enseigne-led-gravee', 'Enseigne gravée LED'), ('baie-reseau', 'Baie réseau'), ('plafond-led-blanc', 'Gorges lumineuses'), ('moteur-industriel', 'Moteur industriel'), ('bibliotheque-led', 'Bibliothèque LED'), ('proto-lift-projecteur', 'Lift de projecteur'), ('salle-de-bain-baignoire', 'Salle de bain'), ('plan-electrique-2', 'Plan d’installation'), ('tableau-distribution', 'Tableau de distribution')]
TOWNS = [('Aigle', 'siège'), ('Yvorne', 'Chablais'), ('Ollon', 'Chablais'), ('Bex', 'Chablais'), ('Villeneuve', 'Riviera'), ('Montreux', 'Riviera'), ('Vevey', 'Riviera'), ('Leysin', 'Alpes vaudoises'), ('Villars', 'Alpes vaudoises'), ('Les Diablerets', 'Alpes vaudoises'), ('Château-d’Œx', 'Pays-d’Enhaut'), ('Châtel-St-Denis', 'Veveyse'), ('Bulle', 'Gruyère'), ('Et environs', 'sur demande')]

home = f'''
<section class="hero">
  <div class="wrap">
    <div class="hero-meta"><span>Installateur-électricien CFC</span><span>Aigle — Vaud</span><span>Depuis 2000</span><span>Urgences 24/7 · <a href="tel:{CO['tel']}">{CO['phone']}</a></span></div>
    <div class="hero-body">
      {lines_h('h1', 'd1', ['Courant fort.', 'Courant faible.', 'Imagerie médicale.'])}
      <div class="hero-foot">
        <p class="lead" data-r>Massonelec Sàrl étudie, installe, contrôle et dépanne les réseaux électriques des particuliers, des industries et des centres médicaux — du Chablais vaudois jusqu’à Bulle.</p>
        <div class="hero-ctas" data-r=".1">{btn('devis', 'Demander un devis')}{ulink('tel:' + CO['tel'], 'Urgence 24/7 — ' + CO['phone'])}</div>
      </div>
      <div class="ring" id="ring" aria-hidden="true"></div>
    </div>
  </div>
  <div class="cartouche" data-r=".2"><div><span>Entreprise</span><span>Massonelec Sàrl</span></div><div><span>Siège</span><span>{CO['street']}, {CO['npa']} {CO['city']}</span></div><div><span>IDE</span><span>{CO['ide']}</span></div><div><span>Document</span><span>Accueil · rév. 2026</span></div></div>
  <div class="scroll-hint"><i></i>Défiler</div>
</section>

<section class="film" data-dark>
  <div class="film-stage">
    <div class="film-top"><span>Fig. 01 — Mise en service d’un scanner</span><span>Centre d’imagerie d’Aigle</span></div>
    <div class="film-frame"><video id="film" data-auto autoplay muted loop playsinline preload="metadata" poster="assets/img/scanner-poster.webp" data-full="assets/video/scanner-imagerie-aigle.mp4"><source src="assets/video/scanner-loop.mp4" type="video/mp4"></video></div>
    <div class="film-cap"><h2 class="d2">Un scanner ne tolère aucune approximation.</h2>
      <div class="r"><span class="mono">Calcul · alimentation · raccordement · mise en service</span><button class="sound" data-sound="#film">{ic('volume')}<span>Activer le son</span></button>{ulink('imagerie-medicale', 'Le secteur médical')}</div></div>
  </div>
</section>

<section class="sec intro"><div class="wrap"><div class="grid">
  {label('01', 'L’entreprise')}
  <p class="big" data-r>Fondée à Aigle en 2000 par {CO['boss']}, installateur-électricien titulaire d’un CFC, Massonelec Sàrl s’est imposée comme l’une des références de l’électricité générale du Chablais vaudois. Un seul interlocuteur, du premier relevé au rapport de sécurité.</p>
  <div class="intro-img">{frame('tableau-domotique', 'Tableau électrique avec modules domotiques, réalisation Massonelec', 'r-43')}<div class="cap"><span>Fig. 02 — Tableau avec modules domotiques</span><span>Réalisation Massonelec</span></div></div>
  <div class="intro-spec" data-r>{spec([('Raison sociale', 'Massonelec Sàrl'), ('Fondation', '2000, Aigle (VD)'), ('Qualification', 'Installateur-électricien CFC'), ('Contrôles', 'OIBT art. 31 · rapport de sécurité'), ('Service', 'Dépannage 24 h/24, 7 j/7'), ('Langues', 'Français · italiano')])}
    <div class="sig">{mark()}<div><b>{CO['boss']}</b><span>Gérant</span></div></div>
    <div style="margin-top:30px">{ulink('entreprise', 'Découvrir l’entreprise')}</div></div>
</div></div></section>

{carousel([('l', 34, WORK_A), ('r', 26, WORK_B)], 'Sur nos chantiers.', '—', 'Réalisations Massonelec')}

<section class="sec"><div class="wrap">
  {sec_top('02', 'Prestations', 'Huit métiers, une seule exigence.', act=ulink('prestations', 'Toutes les prestations'))}
  {idx_list(ALL_SVC)}
</div></section>

<section class="reel dark" data-dark>
  <div class="wrap reel-head">{label('03', 'Réalisations')}<h2 class="d2" data-words>Des chantiers qui demandent de l’expérience.</h2><span class="cnt"><b>01</b> / {len(PANELS):02d}</span></div>
  <div class="reel-track">{panels}</div>
  <div class="reel-progress"><i></i></div>
</section>

<section class="sec method"><div class="wrap">
  {sec_top('04', 'Méthode', 'Du relevé au rapport de sécurité.')}
  <div class="grid">
    <div class="circuit">{circuit_svg}</div>
    <ol class="steps">
      <li data-r><span class="mono">01</span><div><h3>Rendez-vous & relevé</h3><p>Avant toute intervention, nous venons sur place pour comprendre vos besoins et ceux de votre habitation, de votre entreprise ou de votre industrie.</p></div></li>
      <li data-r><span class="mono">02</span><div><h3>Étude & devis gratuit</h3><p>Plans, calculs si nécessaire, puis une offre détaillée, gratuite et sans engagement.</p></div></li>
      <li data-r><span class="mono">03</span><div><h3>Réalisation</h3><p>Nos installateurs-électriciens exécutent les travaux proprement, dans les délais convenus, avec un seul interlocuteur du début à la fin.</p></div></li>
      <li data-r><span class="mono">04</span><div><h3>Contrôle & rapport</h3><p>Mesures et contrôle selon l’art. 31 OIBT, rapport de conformité remis au propriétaire et au fournisseur d’énergie.</p></div></li>
    </ol>
  </div>
</div></section>

<section class="sec white scanwrap"><div class="wrap"><div class="grid">
  <div class="txt">{label('05', 'Études & conception')}<h2 class="d3" data-words style="margin:26px 0 24px">Tout commence sur le plan.</h2>
    <p class="lead" data-r>Relevés, plans d’implantation, schémas unifilaires, calculs de dimensionnement : la qualité d’une installation se décide avant le premier câble.</p>
    <div data-r style="margin-top:30px">{ulink('etudes-conception', 'Études & conception')}</div></div>
  <div class="scanbox"><div class="scan"><img class="base" src="assets/img/plan-electrique-2.webp" alt="" loading="lazy"><img class="top" src="assets/img/plan-electrique-2.webp" alt="Plan d’installation électrique dessiné par Massonelec" loading="lazy"><span class="beam"></span></div>
    <div class="scan-meta"><span>Fig. 03 — Plan d’installation électrique</span><span>Massonelec Sàrl</span></div></div>
</div></div></section>

<section class="sec"><div class="wrap">
  {sec_top('06', 'Clientèle', 'La même rigueur, du studio à l’infrastructure.')}
  <div class="figs">{figs}</div>
</div></section>

<section class="zone" data-dark>
  <div class="frame">{img('st-chillon', 'Château de Chillon et Dents du Midi, à quelques minutes d’Aigle', '100vw')}</div>
  <div class="wrap"><div class="grid">
    <div class="lft"><div class="label"><b>07</b><span>Zone d’intervention</span></div><h2 class="d2" data-words>D’Aigle à Bulle.</h2><p data-r>Notre bureau est au cœur du Chablais. Nos équipes interviennent dans tout le Chablais vaudois, sur la Riviera, dans les Alpes vaudoises et jusqu’en Gruyère.</p></div>
    <div class="towns" data-stagger>{''.join(f'<span>{a}<i>{b}</i></span>' for a, b in TOWNS)}</div>
  </div></div>
</section>

<section class="sec"><div class="wrap">
  {sec_top('08', 'Avis', 'Ce que disent nos clients.', act=ulink(CO['gwrite'], 'Laisser un avis Google', ext=True))}
  <div class="rates">
    <div class="rate" data-r><span class="num"><span data-count="5.0">5,0</span><small>/5</small></span>{stars(5)}<span class="src">{ic('g')} Note Google</span>{ulink(CO['greviews'], 'Voir les avis', ext=True)}</div>
    <div class="rate" data-r=".1"><span class="num"><span data-count="4.0">4,0</span><small>/5</small></span>{stars(4)}<span class="src">{ic('lc')} 4 évaluations local.ch</span>{ulink(CO['lc'], 'Voir la fiche', ext=True)}</div>
    <div class="rate" data-r=".2"><q>Électricien au top.</q>{stars(5)}<span class="src">{ic('lc')} Deux avis local.ch · octobre 2023</span>{ulink(CO['lc'], 'Lire sur local.ch', ext=True)}</div>
  </div>
</div></section>

{faq_section(FAQ, '09')}
{contact_block(subject='Demande depuis la page d’accueil', idp='home', num='10')}
{lightbox()}
'''
add('index', 'Massonelec Sàrl · Électricien à Aigle · Courant fort, faible & imagerie médicale',
    'Installateur-électricien CFC à Aigle depuis 2000. Électricité générale, courant fort et industriel, imagerie médicale, domotique, dépannage 24/7 dans le Chablais vaudois jusqu’à Bulle. Devis gratuit.',
    home, active='index', pt_label='Accueil',
    extra_head='<link rel="modulepreload" href="assets/vendor/three.module.min.js">',
    extra_body=f'<script type="module" src="assets/js/ring3d.js?v={V}"></script>')

# =====================================================================
# SERVICE PAGE TEMPLATE
# =====================================================================
ORDER = [s[0] for s in SERVICES]
TITLES = {s[0]: s[1] for s in SERVICES}

def service(slug, h1, lead, hero, hero_alt, intro_label, intro_big, intro_p, items, row_title, rws, pair=None, call=None, faqs=None, pre='', title='', desc='', extra=''):
    i = ORDER.index(slug); nxt = ORDER[(i + 1) % len(ORDER)]
    b = phero(f'<a href="./">Accueil</a> / <a href="prestations">Prestations</a> / {TITLES[slug]}', f'Prestation {i+1:02d} / {len(ORDER):02d}', h1,
              f'<p>{lead}</p>{btn("devis?service=" + quote(pre), "Devis gratuit")}', phero_img(hero, hero_alt))
    b += f'''<section class="sec tb"><div class="wrap"><div class="grid">{label('01', intro_label)}<div class="body"><p class="big" data-r>{intro_big}</p>{''.join(f'<p data-r>{x}</p>' for x in intro_p)}{ulist(items)}</div></div></div></section>'''
    b += f'<section class="sec" style="padding-top:0"><div class="wrap">{sec_top("02", row_title[0], row_title[1], h2cls="d3")}{rows(rws)}</div></section>'
    if pair:
        (a, aa, ac), (bb, ba, bc) = pair
        b += f'''<section class="sec-s"><div class="wrap"><div class="pair"><div class="a">{frame(a, aa, 'r-43')}<div class="cap"><span>{ac}</span></div></div><div class="b">{frame(bb, ba, 'r-45')}<div class="cap"><span>{bc}</span></div></div></div></div></section>'''
    if call:
        im, tg, t, d, sp, href = call
        b += f'''<section class="sec dark" data-dark><div class="wrap"><div class="callbox"><div class="frame r-43 px" data-veil>{img(im, t)}</div><div class="txt"><span class="mono" style="color:#8d8f93">Référence — {tg}</span><h3 data-words>{t}</h3><p class="lead" data-r>{d}</p><div data-r>{spec(sp)}</div><div data-r style="margin-top:28px">{ulink(href, 'Voir la réalisation')}</div></div></div></div></section>'''
    b += extra
    if faqs: b += faq_section(faqs, '03')
    b += next_link(nxt, TITLES[nxt], 'Prestation suivante')
    b += contact_block(subject=f'Demande – {TITLES[slug]}', pre=pre, idp=slug[:4])
    add(slug, title, desc, b, pt_label=TITLES[slug])

service('electricite-generale', ['Électricité', 'générale.'],
    'Construction, transformation ou rénovation : nous étudions, réalisons et contrôlons votre installation intérieure et extérieure.',
    'plafond-led-blanc', 'Séjour rénové avec gorges lumineuses LED',
    'Approche', 'Avant toute intervention, nous prenons rendez-vous pour comprendre vos besoins et ceux de votre bâtiment. Puis nous étudions, chiffrons, réalisons et contrôlons.',
    ['Nos installateurs-électriciens se chargent de tout, du tableau jusqu’au dernier point lumineux. Vous gardez un seul interlocuteur pour l’ensemble de votre réseau électrique.'],
    ['Installations complètes, villas et immeubles', 'Rénovation d’installations anciennes', 'Tableaux de distribution, coffrets de comptage', 'Cuisines, salles de bain, éclairage encastré', 'Installations extérieures et de jardin', 'Retouches OIBT, mises en conformité'],
    ('Sécurité', 'Des installations contrôlées et documentées.'),
    [('Contrôle OIBT', 'Nos installations sont contrôlées conformément à l’art. 31 de l’ordonnance fédérale sur les installations électriques à basse tension.'),
     ('Rapport de sécurité', 'Nous délivrons un rapport de conformité au propriétaire de la construction et au fournisseur d’énergie.'),
     ('Retouches', 'Correction des défauts relevés lors d’un contrôle périodique ou d’une vente immobilière.'),
     ('Rénovation', 'Mise à niveau des installations anciennes : protections, différentiels, mise à terre, tableaux.')],
    pair=(('salle-de-bain-baignoire', 'Salle de bain rénovée', 'Salle de bain · rénovation'), ('coffrets-comptage', 'Coffrets de comptage', 'Coffrets de comptage · immeuble')),
    call=('miroir-retroeclaire', 'Sur mesure', 'Miroir à éclairage périphérique', 'Fabrication et réalisation d’un miroir avec éclairage périphérique au travers du verre.', [('Type', 'Fabrication sur mesure'), ('Pièce', 'Salle de bain')], 'realisations#miroir'),
    faqs=[FAQ[1], FAQ[3], ('Pouvez-vous rénover une installation ancienne sans tout refaire ?', 'Oui. Après un relevé de l’existant, nous proposons la solution adaptée : remplacement du tableau, ajout de protections différentielles, reprise des circuits défectueux ou rénovation complète.')],
    pre='Électricité générale', title='Électricité générale à Aigle · Installation & rénovation · Massonelec',
    desc='Installations électriques neuves et rénovations à Aigle et dans le Chablais vaudois : étude, devis gratuit, réalisation, contrôle OIBT et rapport de sécurité.')

service('courant-fort-industrie', ['Courant fort', '& industrie.'],
    'Armoires, force motrice, énergie de secours, infrastructures : des installations où la fiabilité n’est pas négociable.',
    'station-pompage-armoire', 'Armoire de commande d’une station de pompage d’eau potable',
    'Approche', 'Station de pompage d’eau potable, génératrice dans un fort militaire, raccordement de machines : nous travaillons là où une coupure coûte cher.',
    ['Nous intervenons pour les entreprises, les industries et les collectivités, de l’étude à la mise en service, et assurons le dépannage 24/7 pour limiter l’arrêt de production.'],
    ['Armoires de commande et de puissance', 'Câblage universel et force', 'Raccordement de moteurs et de pompes', 'Groupes électrogènes, énergie de secours', 'Chemins de câbles et distribution', 'Dépannage industriel 24/7'],
    ('Compétences', 'Courant fort, de la distribution à la machine.'),
    [('Force motrice', 'Alimentation et raccordement de machines, moteurs et équipements de production.'),
     ('Armoires électriques', 'Câblage d’armoires de distribution, de commande et d’automatisme.'),
     ('Énergie de secours', 'Génératrices et circuits prioritaires, comme la génératrice de 88 kVA mise en place dans un fort militaire.'),
     ('Infrastructures', 'Stations de pompage d’eau potable et ouvrages techniques.')],
    pair=(('station-pompage-salle', 'Salle des pompes', 'Station de pompage · salle des pompes'), ('moteur-industriel', 'Moteur industriel raccordé', 'Raccordement d’un moteur')),
    call=('generatrice-88kva', 'Énergie de secours', 'Génératrice 88 kVA dans un fort militaire', 'Mise en place et raccordement d’une génératrice de 88 kVA dans un ouvrage militaire : un chantier en milieu confiné, où l’alimentation de secours doit être irréprochable.', [('Puissance', '88 kVA'), ('Site', 'Fort militaire'), ('Mission', 'Mise en place, raccordement')], 'realisations#generatrice'),
    pre='Courant fort / industrie', title='Courant fort & installations industrielles · Massonelec Sàrl, Aigle',
    desc='Courant fort, armoires électriques, force motrice, génératrices et stations de pompage : installations industrielles et d’infrastructure dans le Chablais vaudois.')

service('courant-faible-reseaux', ['Courant faible', '& réseaux.'],
    'Téléphonie, informatique, interphones et caméras IP, détection : les installations qui font communiquer votre bâtiment.',
    'st-fibre', 'Câblage réseau structuré',
    'Approche', 'Un réseau fiable commence par un câblage soigné : chemins de câbles, repérage, baies de brassage et tests.',
    ['Nous installons et raccordons l’ensemble des systèmes à courant faible des habitations, commerces et bureaux, en coordination avec l’électricité générale.'],
    ['Téléphonie analogique et numérique', 'Centraux et raccordements téléphoniques', 'Réseau informatique, prises réseau', 'Caméras de sécurité et interphones IP', 'Alarmes, détection d’intrusion', 'Détection d’incendie'],
    ('Domaines', 'Communication, données, sécurité.'),
    [('Téléphonie', ['Installations analogiques et numériques', 'Centraux téléphoniques', 'Raccordements']),
     ('Informatique', ['Transmission de données', 'Câblage universel', 'Baies de brassage']),
     ('Vidéo & interphonie', ['Caméras de sécurité IP', 'Interphones IP']),
     ('Sécurité', ['Détection d’intrusion', 'Détection d’incendie'])],
    pair=(('baie-reseau', 'Baie de brassage réseau', 'Baie réseau & téléphonie · réalisation'), ('st-cables', 'Câbles réseau', 'Câblage structuré')),
    pre='Courant faible, téléphonie, réseau', title='Courant faible, téléphonie & réseau informatique · Massonelec Aigle',
    desc='Téléphonie, câblage informatique, prises réseau, interphones et caméras IP, alarmes, détection incendie et intrusion à Aigle et dans le Chablais.')

dom_gal = '<section class="sec white"><div class="wrap">' + sec_top('03', 'Galerie', 'La lumière comme matériau.', h2cls='d3') + '<div class="gal">' + ''.join(gi(n, 'eclairage', c) for n, c in [('plafond-led-violet', 'Plafond lumineux LED couleur'), ('salon-eclairage', 'Salon à éclairage encastré'), ('eclairage-jardin', 'Mise en lumière d’un jardin'), ('bibliotheque-led', 'Bibliothèque à LED intégrées'), ('vitrine-led', 'Vitrine à étagères lumineuses'), ('miroir-led', 'Miroir LED de salle de bain'), ('plafond-led-chantier', 'Gorge lumineuse en chantier'), ('projecteur-led', 'Projecteur LED extérieur'), ('st-salon-lac', 'Éclairage d’ambiance, vue sur le Léman')]) + '</div></div></section>' + lightbox()
service('domotique-eclairage', ['Domotique', '& éclairage.'],
    'Un bâtiment programmable selon vos habitudes, et un éclairage qui met en valeur votre intérieur, votre commerce ou votre jardin.',
    'st-salon-lac', 'Séjour éclairé avec vue sur le lac',
    'Approche', 'Nous mettons en place des installations entièrement programmables et ajustables à la demande, et concevons l’éclairage comme un élément d’architecture.',
    ['Gorges lumineuses, LED couleur, meubles et vitrines rétroéclairés, mise en lumière extérieure : chaque projet est pensé sur mesure.'],
    ['Programmation de l’éclairage, du chauffage, des stores', 'Scénarios et commandes centralisées', 'Commande à distance', 'Éclairage LED et décoratif', 'Gorges et plafonds lumineux', 'Éclairage de jardin et de façade'],
    ('Domaines', 'Piloter, éclairer, mettre en valeur.'),
    [('Domotique', 'Installation entièrement programmable : éclairage, chauffage, stores, avec commande à distance.'),
     ('Éclairage intérieur', 'Gorges lumineuses, LED couleur, encastrés, éclairage de meubles et de vitrines.'),
     ('Éclairage extérieur', 'Mise en lumière de jardins, arbres, cheminements et façades.'),
     ('Sur mesure', 'Miroirs rétroéclairés, enseignes lumineuses gravées.')],
    call=('eclairage-jardin', 'Particulier', 'Mise en lumière d’un jardin privé', 'Réalisation d’un éclairage d’ambiance pour le jardin d’un particulier : arbres, cheminement en pierre et four extérieur.', [('Type', 'Éclairage extérieur'), ('Client', 'Particulier')], 'realisations#jardin'),
    extra=dom_gal,
    pre='Domotique / éclairage', title='Domotique & éclairage LED · Massonelec Sàrl, électricien à Aigle',
    desc='Domotique programmable (éclairage, chauffage, stores), éclairage LED décoratif, gorges lumineuses, éclairage de jardin et miroirs rétroéclairés dans le Chablais.')

dep_extra = f'''<section class="sec dark" data-dark><div class="wrap">{sec_top('—', 'En attendant notre arrivée', 'Les bons réflexes.', h2cls='d3')}
{rows([('Ne touchez pas', 'N’intervenez jamais sur un câble, une prise ou un appareil endommagé ou humide.'), ('Coupez si possible', 'Si vous pouvez le faire sans risque, coupez l’alimentation au tableau électrique.'), ('Appelez-nous', f'Décrivez ce que vous observez au <a href="tel:{CO["tel"]}" style="color:#fff;text-decoration:underline">{CO["phone"]}</a> : nous vous guidons et organisons l’intervention.')])}</div></section>'''
service('depannage-electrique-24h', ['Dépannage', '24 h/24, 7 j/7.'],
    f'Une panne ne prévient pas. Appelez le <a href="tel:{CO["tel"]}" style="text-decoration:underline">{CO["phone"]}</a> : nous intervenons rapidement dans tout le Chablais vaudois, jusqu’à Bulle.',
    'st-test', 'Électricien contrôlant un tableau électrique',
    'Urgence', 'Que vous soyez un particulier, un professionnel ou une industrie, Massonelec intervient chez vous en un temps record pour remettre votre électricité en marche.',
    [f'<a class="tel-big" href="tel:{CO["tel"]}">{CO["phone"]}</a>'],
    ['Panne générale ou partielle', 'Disjoncteur ou différentiel qui déclenche', 'Court-circuit, prise ou interrupteur défectueux', 'Odeur de brûlé, échauffement', 'Éclairage hors service', 'Installation industrielle à l’arrêt'],
    ('Clients', 'Pour tous, à toute heure.'),
    [('Particuliers', 'Maisons, appartements, PPE : remise en service et sécurisation.'), ('Professionnels', 'Commerces, bureaux, cabinets : intervention rapide pour reprendre l’activité.'), ('Industries', 'Courant fort et machines : diagnostic et remise en marche.')],
    extra=dep_extra, faqs=[FAQ[0], FAQ[2]],
    pre='Dépannage urgent', title='Dépannage électrique 24h/24 à Aigle et dans le Chablais · Massonelec',
    desc='Électricien d’urgence 24 h/24 et 7 j/7 à Aigle, Ollon, Bex, Villeneuve, Leysin et jusqu’à Bulle. Panne, court-circuit, disjoncteur : 079 350 55 19.')

etu_extra = '<section class="sec white"><div class="wrap">' + sec_top('03', 'Documents', 'Plans et schémas de nos chantiers.', h2cls='d3') + '<div class="gal">' + ''.join(gi(n, 'etudes', c) for n, c in [('plan-electrique-1', 'Plan d’appartement : points lumineux et prises'), ('schema-unifilaire', 'Schéma de principe de distribution'), ('plan-electrique-3', 'Plan d’installation d’un logement'), ('plan-electrique-2', 'Plan d’étage complet')]) + '</div></div></section>' + lightbox()
service('etudes-conception', ['Études', '& conception.'],
    'Relevé, plans, schémas, calculs : un chantier maîtrisé et un devis juste commencent par une étude sérieuse.',
    'plan-electrique-3', 'Plan d’installation électrique',
    'Bureau technique', 'Nous réalisons l’étude complète de votre installation et concevons des plans clairs, partagés avec architectes, maîtres d’ouvrage et fabricants.',
    ['Pour les équipements exigeants, comme le mammographe du Centre d’imagerie d’Aigle, nous calculons l’alimentation selon les spécifications du constructeur.'],
    ['Relevé de l’existant', 'Plans d’implantation par pièce', 'Schémas unifilaires de tableaux', 'Calculs de dimensionnement', 'Coordination avec les autres corps de métier', 'Documentation de fin de chantier'],
    ('Livrables', 'Ce que vous recevez.'),
    [('Plan d’installation', 'Implantation des points lumineux, prises, commandes et équipements.'), ('Schéma unifilaire', 'Architecture de distribution et protections.'), ('Calculs', 'Sections, protections et puissances.'), ('Devis détaillé', 'Gratuit et sans engagement.')],
    extra=etu_extra, pre='Études & plans', title='Études & plans électriques · Massonelec Aigle',
    desc='Relevés, plans d’installation électrique, schémas unifilaires et calculs de dimensionnement pour particuliers, entreprises et établissements médicaux.')

inn_extra = '<section class="sec white"><div class="wrap">' + sec_top('03', 'Atelier', 'Prototypes réalisés.', h2cls='d3') + '<div class="gal">' + ''.join(gi(n, 'proto', c) for n, c in [('proto-lift-projecteur', 'Lift motorisé pour vidéoprojecteur'), ('enseigne-led-gravee', 'Enseigne en verre gravé rétroéclairée'), ('piece-impression-3d', 'Engrenage modélisé en CAO pour impression 3D'), ('proto-moteur-grave', 'Moteur reconditionné et gravé'), ('proto-moteur', 'Ensemble moteur et commande'), ('proto-usinage', 'Usinage d’une pièce sur mesure')]) + '</div></div></section>' + lightbox()
service('innovation-prototypage', ['Innovation', '& prototypage.'],
    'Quand la pièce n’existe plus ou que l’outil n’existe pas encore, nous le concevons.',
    'proto-chassis-levage', 'Châssis de levage motorisé conçu sur mesure',
    'Ingéniosité', 'L’électricité reste notre métier. Mais, à la demande de particuliers ou de professionnels, nous imaginons aussi des objets, des outils et des machines qui simplifient la vie.',
    ['Comme pour les études électriques, nous venons chez vous discuter du projet. Nous avons par exemple conçu différents outils de levage pour aider à la mobilité de nos clients.'],
    ['Outils de levage pour la mobilité', 'Lifts motorisés (vidéoprojecteur)', 'Pièces refaites en impression 3D', 'Enseignes lumineuses gravées', 'Reconditionnement de moteurs', 'Usinage de pièces sur mesure'],
    ('Démarche', 'De l’idée à l’objet.'),
    [('Écoute', 'Visite chez vous pour comprendre le besoin.'), ('Conception', 'Modélisation CAO, choix des composants.'), ('Fabrication', 'Usinage, impression 3D, câblage et motorisation.'), ('Mise en service', 'Installation, réglages, explications.')],
    extra=inn_extra, pre='Innovation / prototypage', title='Innovation & prototypage · Pièces sur mesure, impression 3D · Massonelec',
    desc='Outils de levage, lifts motorisés, enseignes lumineuses et pièces introuvables refaites en impression 3D : Massonelec conçoit des solutions sur mesure.')

# =====================================================================
# PRESTATIONS HUB
# =====================================================================
hub = phero('<a href="./">Accueil</a> / Prestations', f'{len(ALL_SVC):02d} métiers', ['Prestations.'],
            '<p>Du courant faible au courant fort, de l’étude au dépannage : tout ce dont votre bâtiment a besoin, avec un seul interlocuteur.</p>' + btn('devis', 'Devis gratuit'), phero_img('cablage-armoire', 'Câblage d’une armoire de distribution'))
hub += f'<section class="sec"><div class="wrap">{sec_top("01", "Index", "Nos métiers.", h2cls="d3")}{idx_list(ALL_SVC)}</div></section>'
hub += f'''<section class="sec dark" data-dark><div class="wrap">{sec_top('02', 'Catalogue', 'L’ensemble de nos interventions.', h2cls='d3', side='Liste non exhaustive : contactez-nous pour tout besoin spécifique.')}
{rows([('Installations de sécurité', ['Alarmes', 'Caméras IP', 'Détection d’incendie et d’intrusion', 'Interphones IP']), ('Éclairage', ['LED et décoratif', 'Jardin et extérieur', 'Miroirs et meubles rétroéclairés']), ('Domotique', ['Installation programmable', 'Éclairage, chauffage, stores', 'Commande à distance']), ('Téléphonie & informatique', ['Installations analogiques et numériques', 'Centraux, raccordements', 'Câblage universel, prises réseau']), ('Industrie', ['Câblage force', 'Armoires de distribution', 'Génératrices']), ('Rénovation', ['Rénovation d’installations', 'Retouches OIBT', 'Mises en conformité'])])}</div></section>'''
hub += contact_block(subject='Demande depuis la page Prestations', idp='hub')
add('prestations', 'Prestations · Électricité générale, courant fort et faible · Massonelec Aigle',
    'Électricité générale, courant fort et industrie, courant faible et réseaux, domotique, éclairage LED, dépannage 24/7, études et prototypage à Aigle et dans le Chablais.', hub, pt_label='Prestations')

# =====================================================================
# MEDICAL
# =====================================================================
med = phero('<a href="./">Accueil</a> / Secteur médical', 'Santé · Imagerie', ['Imagerie', 'médicale.'],
            '<p>Scanner et mammographe au Centre d’imagerie d’Aigle : des équipements qui exigent une alimentation calculée, réalisée et contrôlée sans approximation.</p>' + btn('devis?service=' + quote('Imagerie médicale / santé'), 'Parler de votre projet'),
            f'<div class="wrap"><div class="frame phero-media video"><video data-auto autoplay muted loop playsinline preload="metadata" poster="assets/img/scanner-poster.webp"><source src="assets/video/scanner-loop.mp4" type="video/mp4"></video></div></div>')
med += f'''<section class="sec tb"><div class="wrap"><div class="grid">{label('01', 'Contexte')}<div class="body"><p class="big" data-r>Un équipement d’imagerie représente un investissement lourd et un service vital pour les patients. Son alimentation électrique doit être pensée avec le fabricant, réalisée sans compromis et documentée.</p><p data-r>Massonelec Sàrl a assuré, au Centre d’imagerie d’Aigle, la mise en place et le raccordement d’un scanner, puis le calcul, la réalisation et l’installation de l’alimentation du mammographe, en collaboration avec GE.</p></div></div></div></section>
<section class="sec dark" data-dark><div class="wrap"><div class="callbox"><div class="frame r-169" style="background:#000"><video id="medv" controls playsinline preload="metadata" poster="assets/img/scanner-poster.webp"><source src="assets/video/scanner-imagerie-aigle.mp4" type="video/mp4"></video></div>
  <div class="txt"><span class="mono" style="color:#8d8f93">Référence 01 — Centre d’imagerie d’Aigle</span><h3 data-words>Scanner d’imagerie médicale</h3><p class="lead" data-r>Mise en place et raccordement d’un scanner. La vidéo montre les premiers tours de l’anneau rotatif, capots ouverts, lors de la mise en service.</p><div data-r>{spec([('Mission', 'Raccordement, mise en service'), ('Lieu', 'Aigle (VD)')])}</div></div></div></div></section>
<section class="sec"><div class="wrap"><div class="callbox"><div class="txt" style="grid-column:1/6;grid-row:1"><span class="mono mute">Référence 02 — En collaboration avec GE</span><h3 data-words>Mammographe</h3><p class="lead" data-r>Calcul, réalisation et installation de l’alimentation du mammographe, avec un transformateur dédié, selon les spécifications du constructeur.</p><div data-r>{spec([('Mission', 'Calcul, transformateur, installation'), ('Partenaire', 'GE'), ('Lieu', 'Centre d’imagerie d’Aigle')])}</div></div>
  <div class="frame r-43 px" data-veil style="grid-column:7/13;grid-row:1">{img('imagerie-transformateur', 'Transformateur dédié au mammographe')}</div></div></div></section>
<section class="sec dark" data-dark><div class="wrap">{sec_top('02', 'Exigences', 'Ce qu’exige une installation médicale.', h2cls='d3')}
{rows([('Étude & calcul', 'Dimensionnement de l’alimentation selon les spécifications du fabricant de l’équipement.'), ('Coordination', 'Travail conjoint avec le constructeur, l’exploitant et les autres corps de métier.'), ('Alimentations dédiées', 'Lignes et transformateurs dédiés aux équipements lourds.'), ('Planification', 'Interventions organisées pour limiter l’impact sur l’activité médicale.'), ('Contrôle OIBT', 'Mesures, contrôle et rapport de conformité remis à l’exploitant.'), ('Dépannage 24/7', 'Une équipe joignable à toute heure.')])}</div></section>
<section class="sec-s"><div class="wrap"><div class="pair"><div class="a">{frame('st-medical-room', 'Salle d’imagerie médicale', 'r-43')}<div class="cap"><span>Salle d’imagerie · illustration</span></div></div><div class="b">{frame('st-bore', 'Tunnel d’un appareil d’imagerie', 'r-34')}<div class="cap"><span>Tunnel d’imagerie · illustration</span></div></div></div></div></section>
<section class="sec"><div class="wrap">{sec_top('03', 'Pour qui', 'Établissements de santé.', h2cls='d3')}{rows([('Centres d’imagerie', 'Scanner, mammographe, radiologie.'), ('Cabinets médicaux & dentaires', 'Installation, rénovation, équipements spécifiques.'), ('Établissements & résidences', 'Tableaux, éclairage, courant faible, dépannage.')])}</div></section>'''
med += next_link('realisations', 'Toutes nos réalisations', 'Voir aussi')
med += contact_block('Votre projet médical.', 'Décrivez l’équipement et le local : nous revenons vers vous pour une visite et une étude.', subject='Demande – secteur médical', pre='Imagerie médicale / santé', idp='med')
add('imagerie-medicale', 'Imagerie médicale · Raccordement scanner & mammographe · Massonelec Aigle',
    'Massonelec a raccordé un scanner et installé l’alimentation d’un mammographe (avec GE) au Centre d’imagerie d’Aigle. Électricité pour la santé : étude, calcul, installation, contrôle OIBT.', med, pt_label='Secteur médical')

# =====================================================================
# RÉALISATIONS
# =====================================================================
CASES = [
    ('scanner', 'Santé · Centre d’imagerie d’Aigle', 'Scanner d’imagerie médicale', 'Mise en place et raccordement d’un scanner d’imagerie médicale au Centre d’imagerie d’Aigle.', None, [('Mission', 'Raccordement, mise en service'), ('Lieu', 'Aigle (VD)')]),
    ('mammographe', 'Santé · avec GE', 'Mammographe', 'Calcul, réalisation et installation du mammographe au Centre d’imagerie d’Aigle en collaboration avec GE.', 'imagerie-transformateur', [('Mission', 'Calcul, transformateur dédié'), ('Partenaire', 'GE')]),
    ('station-pompage', 'Infrastructure · eau potable', 'Station de pompage d’eau potable', 'Installation électrique pour une station de pompage d’eau potable, réalisée par notre société.', 'station-pompage-armoire', [('Mission', 'Armoires, puissance, pompes'), ('Ouvrage', 'Eau potable')]),
    ('generatrice', 'Énergie · site militaire', 'Génératrice 88 kVA', 'Mise en place et raccordement d’une génératrice de 88 kVA dans un fort militaire.', 'generatrice-88kva', [('Puissance', '88 kVA'), ('Site', 'Fort militaire')]),
    ('jardin', 'Particulier · extérieur', 'Éclairage d’ambiance de jardin', 'Réalisation d’un éclairage d’ambiance pour le jardin d’un particulier : arbres, cheminement et four extérieur.', 'eclairage-jardin', [('Type', 'Éclairage extérieur'), ('Client', 'Particulier')]),
    ('miroir', 'Particulier · sur mesure', 'Miroir à éclairage périphérique', 'Fabrication et réalisation d’un miroir avec éclairage périphérique au travers du miroir.', 'miroir-retroeclaire', [('Type', 'Fabrication sur mesure'), ('Pièce', 'Salle de bain')]),
]
cases = ''
for i, (a, tg, t, d, im, sp) in enumerate(CASES):
    media = (f'<div class="frame" style="background:#000">' + '<video controls playsinline preload="metadata" poster="assets/img/scanner-poster.webp"><source src="assets/video/scanner-imagerie-aigle.mp4" type="video/mp4"></video></div>') if im is None else frame(im, t, '', sizes='(max-width:900px) 100vw, 58vw')
    cases += f'<article class="case{" flip" if i % 2 else ""}" id="{a}">{media}<div class="txt"><span class="mono mute">{i+1:02d} — {tg}</span><h3 data-words>{t}</h3><p data-r>{d}</p><div data-r>{spec(sp)}</div></div></article>'
G = [('scanner-poster', 'sante', 'Scanner · Centre d’imagerie d’Aigle (vidéo)', 'assets/video/scanner-imagerie-aigle.mp4'),
     ('imagerie-transformateur', 'sante industrie', 'Transformateur dédié au mammographe', None), ('station-pompage-armoire', 'industrie tableaux', 'Armoire de commande · station de pompage', None),
     ('station-pompage-salle', 'industrie', 'Salle des pompes · eau potable', None), ('generatrice-88kva', 'industrie', 'Génératrice 88 kVA · fort militaire', None),
     ('armoire-industrielle', 'industrie tableaux', 'Armoire électrique industrielle', None), ('moteur-industriel', 'industrie', 'Raccordement d’un moteur industriel', None),
     ('cablage-armoire', 'tableaux industrie', 'Câblage d’une armoire de distribution', None), ('coffrets-comptage', 'tableaux habitat', 'Coffrets de comptage d’immeuble', None),
     ('tableau-domotique', 'tableaux', 'Tableau avec modules domotiques', None), ('tableau-distribution', 'tableaux habitat', 'Tableau de distribution', None),
     ('baie-reseau', 'reseaux', 'Baie de brassage réseau et téléphonie', None), ('plafond-led-violet', 'eclairage', 'Plafond lumineux LED couleur', None),
     ('plafond-led-blanc', 'eclairage habitat', 'Gorges lumineuses LED', None), ('plafond-led-chantier', 'eclairage', 'Gorge lumineuse en chantier', None),
     ('salon-eclairage', 'eclairage habitat', 'Salon à éclairage encastré', None), ('bibliotheque-led', 'eclairage', 'Bibliothèque à LED intégrées', None),
     ('vitrine-led', 'eclairage', 'Vitrine à étagères lumineuses', None), ('eclairage-jardin', 'eclairage', 'Éclairage d’ambiance de jardin', None),
     ('projecteur-led', 'eclairage', 'Projecteur LED extérieur', None), ('miroir-retroeclaire', 'habitat eclairage', 'Miroir à éclairage périphérique', None),
     ('miroir-led', 'habitat eclairage', 'Miroir LED de salle de bain', None), ('salle-de-bain-baignoire', 'habitat', 'Salle de bain rénovée', None),
     ('salle-de-bain-wc', 'habitat', 'WC avec éclairage encastré', None), ('plan-electrique-1', 'etudes', 'Plan d’installation électrique', None),
     ('plan-electrique-2', 'etudes', 'Plan d’étage complet', None), ('schema-unifilaire', 'etudes', 'Schéma de principe de distribution', None),
     ('enseigne-led-gravee', 'proto eclairage', 'Enseigne en verre gravé rétroéclairée', None), ('proto-lift-projecteur', 'proto', 'Lift motorisé pour vidéoprojecteur', None),
     ('proto-chassis-levage', 'proto', 'Châssis de levage sur mesure', None), ('proto-moteur-grave', 'proto', 'Moteur reconditionné et gravé', None),
     ('proto-moteur', 'proto', 'Ensemble moteur et commande', None), ('proto-usinage', 'proto', 'Usinage d’une pièce', None), ('piece-impression-3d', 'proto', 'Pièce redessinée en CAO pour impression 3D', None)]
FIL = [('all', 'Tout'), ('sante', 'Santé'), ('industrie', 'Industrie & énergie'), ('tableaux', 'Tableaux'), ('eclairage', 'Éclairage'), ('habitat', 'Habitat'), ('reseaux', 'Réseaux'), ('etudes', 'Études'), ('proto', 'Prototypes')]
rea = phero('<a href="./">Accueil</a> / Réalisations', f'{len(CASES)} références · {len(G)} documents', ['Réalisations.'],
            '<p>Santé, infrastructures, énergie, habitat, éclairage et prototypes : un aperçu concret du savoir-faire Massonelec, photographié sur nos chantiers.</p>' + btn('devis', 'Un projet similaire ?'), phero_img('station-pompage-salle', 'Station de pompage d’eau potable'))
rea += carousel([('l', 34, WORK_A), ('r', 26, WORK_B)], 'En mouvement.', '—', 'Défilé de chantiers')
rea += f'<section class="sec"><div class="wrap">{sec_top("01", "Références", "Chantiers marquants.", h2cls="d3")}{cases}</div></section>'
rea += f'''<section class="sec white" id="galerie"><div class="wrap">{sec_top('02', 'Galerie', 'Photos de chantier.', h2cls='d3', side=f'{len(G)} photos et vidéos de nos interventions. Cliquez pour agrandir.')}
<div class="filters" role="group" aria-label="Filtrer la galerie">{''.join(f'<button type="button" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{l}</button>' for k, l in FIL)}</div>
<div class="gal">{''.join(gi(n, c, cap, v) for n, c, cap, v in G)}</div></div></section>{lightbox()}'''
rea += contact_block('Un projet similaire ?', subject='Demande depuis la page Réalisations', idp='rea')
add('realisations', 'Réalisations · Scanner, station de pompage, génératrice 88 kVA · Massonelec',
    'Références Massonelec Sàrl : scanner et mammographe au Centre d’imagerie d’Aigle, station de pompage d’eau potable, génératrice 88 kVA, éclairage, domotique, prototypes.', rea, pt_label='Réalisations')

# =====================================================================
# ENTREPRISE
# =====================================================================
ent = phero('<a href="./">Accueil</a> / Entreprise', 'Depuis 2000', ['L’entreprise.'],
            f'<p>Une entreprise d’Aigle fondée par un installateur-électricien CFC, reconnue pour sa conscience professionnelle et sa capacité à mener des chantiers exigeants.</p>{btn("contact", "Nous contacter")}', phero_img('armoire-industrielle', 'Armoire électrique industrielle câblée par Massonelec'))
ent += f'''<section class="sec tb"><div class="wrap"><div class="grid">{label('01', 'Histoire')}<div class="body"><p class="big" data-r>Installateur-électricien de profession et titulaire d’un CFC, {CO['boss']} a toujours souhaité devenir indépendant. En 2000, il fonde sa propre société à Aigle : Massonelec Sàrl.</p>
<p data-r>Depuis, l’entreprise est devenue l’un des spécialistes de l’électricité générale d’Aigle et du Chablais vaudois. Elle intervient sur tous les types d’installations, de la basse tension au courant fort, auprès des particuliers, des entreprises et des industries, jusqu’à Bulle.</p>
<p data-r>Avec Massonelec, vous choisissez la confiance et la rapidité : nos installateurs-électriciens se chargent de tout, de l’étude de vos besoins à la conception de l’installation intérieure et extérieure, jusqu’au dépannage.</p></div></div></div></section>
<section class="sec-s"><div class="wrap"><div class="pair"><div class="a">{frame('coffrets-comptage', 'Coffrets de comptage câblés', 'r-43')}<div class="cap"><span>Coffrets de comptage · immeuble</span></div></div><div class="b">{frame('tableau-distribution', 'Tableau de distribution', 'r-34')}<div class="cap"><span>Tableau de distribution</span></div></div></div></div></section>
<section class="sec"><div class="wrap">{sec_top('02', 'Engagements', 'Ce qui guide chaque intervention.', h2cls='d3')}
{rows([('Conscience professionnelle', 'Nous mettons un point d’honneur à fournir un travail de qualité irréprochable, contrôlé selon l’OIBT.'), ('Un seul interlocuteur', 'De l’étude au dépannage, vous traitez avec la même entreprise pour tout votre réseau électrique.'), ('Rapidité', 'Dépannage 24 h/24 et 7 j/7 dans tout le Chablais vaudois.'), ('Ingéniosité', 'Nous concevons des outils et des objets jusqu’alors inexistants sur le marché.'), ('Transparence', 'Devis gratuit et sans engagement, rapport de conformité remis après les travaux.')])}</div></section>
<section class="sec dark" data-dark><div class="wrap"><div class="grid" style="row-gap:40px"><div style="grid-column:1/6">{label('03', 'Fiche')}<h2 class="d3" data-words style="margin-top:26px">Massonelec Sàrl en bref.</h2></div><div style="grid-column:7/13" data-r>{spec([('Raison sociale', 'Massonelec Sàrl'), ('Gérant', CO['boss']), ('Numéro IDE', CO['ide']), ('Siège', f"{CO['street']}, {CO['npa']} {CO['city']} (VD)"), ('Fondation', '2000'), ('Qualification', 'Installateur-électricien CFC'), ('Langues', 'Français, italien'), ('Paiement', 'Facture, Visa, Mastercard, Amex, Maestro, PostFinance')])}</div></div></div></section>'''
ent += next_link('realisations', 'Nos réalisations', 'Voir aussi')
ent += contact_block(subject='Demande depuis la page Entreprise', idp='ent')
add('entreprise', 'L’entreprise · Massonelec Sàrl, électricien à Aigle depuis 2000',
    'Fondée en 2000 à Aigle par un installateur-électricien CFC, Massonelec Sàrl est spécialiste de l’électricité générale du Chablais vaudois : basse tension, courant fort, dépannage 24/7.', ent, pt_label='Entreprise')

# =====================================================================
# DEVIS
# =====================================================================
def choice(name, value, t, s, lab):
    return f'<label class="choice"><input type="radio" name="{name}" value="{esc(value)}" data-label="{lab}"><span><b>{t}</b><small>{s}</small></span></label>'
dv = phero('<a href="./">Accueil</a> / Devis', 'Gratuit · sans engagement', ['Demande', 'de devis.'],
           f'<p>Quatre étapes, deux minutes. Pour une panne, n’attendez pas : appelez le <a href="tel:{CO["tel"]}" style="text-decoration:underline">{CO["phone"]}</a>.</p>')
dv += f'''<section class="sec"><div class="wrap"><form class="form wz js-form" id="wizard" data-subject="Demande de devis – site web">
<ol class="wz-nav"><li class="on"><span class="mono">01</span>Profil</li><li><span class="mono">02</span>Besoin</li><li><span class="mono">03</span>Projet</li><li><span class="mono">04</span>Coordonnées</li></ol>
<div class="wz-main">
  <div class="wz-step on"><h2 class="d3">Vous êtes…</h2><p class="wz-sub">Pour adapter notre réponse à votre situation.</p>
    <div class="choices" data-need>
      {choice('client', 'Particulier', 'Particulier', 'Maison, appartement, jardin', 'Client')}{choice('client', 'Régie / PPE', 'Régie / PPE', 'Immeubles, copropriétés', 'Client')}{choice('client', 'Entreprise / commerce', 'Entreprise', 'Bureaux, commerces, ateliers', 'Client')}
      {choice('client', 'Industrie / infrastructure', 'Industrie', 'Production, pompage, énergie', 'Client')}{choice('client', 'Établissement médical', 'Santé', 'Imagerie, cabinets, laboratoires', 'Client')}{choice('client', 'Collectivité', 'Collectivité', 'Commune, site public ou militaire', 'Client')}
    </div><p class="wz-miss" hidden>Merci de choisir une option.</p>
    <div class="wz-foot"><span></span><button type="button" class="btn" data-next>Continuer<span class="ar">{ic('arrow')}</span></button></div></div>
  <div class="wz-step"><h2 class="d3">Votre besoin.</h2><p class="wz-sub">Plusieurs choix possibles.</p>
    <div class="chips" data-need>{''.join(f'<label class="chip"><input type="checkbox" name="prestations" value="{esc(o)}" data-label="Prestations"><span>{o}</span></label>' for o in SVC_OPTS)}</div>
    <p class="wz-miss" hidden>Choisissez au moins une prestation.</p>
    <div class="wz-foot"><button type="button" class="ulink" data-prev style="background:none;border:0;cursor:pointer">Retour</button><button type="button" class="btn" data-next>Continuer<span class="ar">{ic('arrow')}</span></button></div></div>
  <div class="wz-step"><h2 class="d3">Votre projet.</h2><p class="wz-sub">Quelques détails pour préparer notre visite.</p>
    <div class="fields" style="display:grid;grid-template-columns:1fr 1fr;column-gap:30px">
      <div class="fld"><select id="w-type" name="travaux" data-label="Type de travaux"><option value="" disabled selected hidden></option><option>Construction neuve</option><option>Rénovation / transformation</option><option>Extension / ajout</option><option>Dépannage / réparation</option><option>Contrôle / mise en conformité OIBT</option><option>Étude seulement</option></select><label for="w-type">Type de travaux</label><span class="bar"></span></div>
      <div class="fld"><select id="w-delai" name="delai" data-label="Délai"><option value="" disabled selected hidden></option><option>Urgent</option><option>Dans le mois</option><option>Dans les 3 mois</option><option>À planifier</option></select><label for="w-delai">Délai souhaité</label><span class="bar"></span></div>
      {fld('w-lieu', 'lieu', 'Localité / NPA')}
      {fld('w-surf', 'surface', 'Surface ou taille', req=False)}
      {fld('w-desc', 'description', 'Description de votre projet', full=True, area=True)}
    </div>
    <div class="wz-foot"><button type="button" class="ulink" data-prev style="background:none;border:0;cursor:pointer">Retour</button><button type="button" class="btn" data-next>Continuer<span class="ar">{ic('arrow')}</span></button></div></div>
  <div class="wz-step"><h2 class="d3">Vos coordonnées.</h2><p class="wz-sub">Pour vous recontacter et fixer un rendez-vous.</p>
    <div class="fields" style="display:grid;grid-template-columns:1fr 1fr;column-gap:30px">
      {fld('w-n', 'nom', 'Nom et prénom', auto='name')}{fld('w-s', 'societe', 'Entreprise', req=False, auto='organization')}
      {fld('w-t', 'tel', 'Téléphone', 'tel', auto='tel')}{fld('w-e', 'email', 'E-mail', 'email', req=False, auto='email')}
      {fld('w-d', 'dispo', 'Disponibilités pour une visite', req=False, full=True)}
    </div>
    <span class="mono mute">Récapitulatif</span><div class="wz-recap"></div>
    <div class="wz-foot"><button type="button" class="ulink" data-prev style="background:none;border:0;cursor:pointer">Retour</button>
      <span style="display:flex;gap:12px;flex-wrap:wrap"><button class="btn ghost" type="submit" value="mail">Par e-mail<span class="ar">{ic('arrow')}</span></button><button class="btn wa" type="submit" value="wa">Envoyer via WhatsApp<span class="ar">{ic('arrow')}</span></button></span></div>
    <p class="form-ok" role="status">Merci. Votre demande est prête : il ne reste qu’à l’envoyer. Nous vous recontactons rapidement.</p>
    <p class="form-note">Gratuit et sans engagement. <a href="confidentialite">Confidentialité</a></p></div>
</div></form></div></section>
<section class="sec white"><div class="wrap">{sec_top('—', 'Et ensuite', 'Après votre demande.', h2cls='d3')}{rows([('Prise de contact', 'Nous vous rappelons pour préciser votre besoin.'), ('Visite sur place', 'Étude de votre bâtiment et de vos attentes.'), ('Devis détaillé', 'Offre gratuite et sans engagement.'), ('Planification', 'Réalisation aux dates convenues.')])}</div></section>'''
add('devis', 'Devis gratuit électricien · Aigle & Chablais · Massonelec Sàrl',
    'Demandez un devis gratuit et sans engagement pour vos travaux électriques : installation, rénovation, courant fort, domotique, imagerie médicale. Aigle et Chablais vaudois.', dv, pt_label='Devis')

# =====================================================================
# CONTACT
# =====================================================================
ct = phero('<a href="./">Accueil</a> / Contact', '<span class="dot"></span> <span data-open>Bureau</span>', ['Contact.'],
           f'<p>Un appel, un message WhatsApp ou le formulaire : choisissez le canal qui vous convient. Pour une urgence, appelez directement, 24 h/24.</p><a class="tel-big" href="tel:{CO["tel"]}">{CO["phone"]}</a>')
ct += contact_block('Écrivez-nous.', 'Décrivez votre projet ou votre panne. Nous revenons vers vous rapidement.', subject='Message depuis la page Contact', idp='ct', num='01')
ct += f'''<section class="sec"><div class="wrap"><div class="grid" style="row-gap:50px">
  <div style="grid-column:1/6">{label('02', 'Horaires du bureau')}<table class="hours" style="margin-top:28px"><tbody>
    <tr data-day="1,2,3,4"><td>Lundi – jeudi</td><td>7:30 – 12:00 · 13:30 – 17:00</td></tr><tr data-day="5"><td>Vendredi</td><td>7:30 – 12:00 · 13:30 – 16:00</td></tr><tr data-day="6,0"><td>Samedi – dimanche</td><td>Urgences 24/7</td></tr></tbody></table></div>
  <div style="grid-column:7/13">{label('03', 'Retrouvez-nous')}<div style="margin-top:28px">{rows([('Google', f'5,0 / 5 — <a href="{CO["greviews"]}" target="_blank" rel="noopener" style="text-decoration:underline">voir les avis</a> · <a href="{CO["gwrite"]}" target="_blank" rel="noopener" style="text-decoration:underline">laisser un avis</a>'), ('local.ch', f'4,0 / 5 — <a href="{CO["lc"]}" target="_blank" rel="noopener" style="text-decoration:underline">fiche Massonelec Sàrl</a>'), ('Facebook', f'<a href="{CO["fb"]}" target="_blank" rel="noopener" style="text-decoration:underline">facebook.com/Massonelec</a>'), ('LinkedIn', f'<a href="{CO["li"]}" target="_blank" rel="noopener" style="text-decoration:underline">{CO["boss"]}</a>')])}</div></div>
</div></div></section>
<section class="sec-s" style="padding-top:0"><div class="wrap">{label('04', 'Plan d’accès')}<div class="map" style="margin-top:28px"><div class="map-load"><div><p>La carte est fournie par Google Maps et ne se charge qu’à votre demande.</p><button class="btn" type="button" data-map>Afficher la carte<span class="ar">{ic('arrow')}</span></button></div></div></div>
<div class="cap"><span>{CO['street']}, {CO['npa']} {CO['city']}</span><a class="ulink" href="{CO['route']}" target="_blank" rel="noopener">Itinéraire{ic('ne')}</a></div></div></section>
<section class="zone" data-dark style="min-height:80svh"><div class="frame">{img('st-leman', 'Lac Léman et Riviera vaudoise', '100vw')}</div><div class="wrap"><div class="grid"><div class="lft"><div class="label"><b>05</b><span>Zone d’intervention</span></div><h2 class="d2" data-words>D’Aigle à Bulle.</h2></div><div class="towns" data-stagger>{''.join(f'<span>{a}<i>{b}</i></span>' for a, b in TOWNS)}</div></div></div></section>'''
add('contact', 'Contact · Massonelec Sàrl, Chemin de la Perrolaz 2, Aigle · 079 350 55 19',
    'Contactez Massonelec Sàrl à Aigle : 079 350 55 19 (urgences 24/7), WhatsApp, e-mail. Chemin de la Perrolaz 2, 1860 Aigle. Horaires et plan d’accès.', ct, pt_label='Contact')

# =====================================================================
# LEGAL + 404
# =====================================================================
def legal(slug, h1, content, title, desc):
    b = phero('<a href="./">Accueil</a> / ' + h1, 'Informations légales', [h1 + '.'], '', h1cls='d2')
    b += f'<section class="sec"><div class="wrap"><div class="grid"><div style="grid-column:4/11" class="legal">{content}</div></div></div></section>'
    add(slug, title, desc, b, pt_label=h1)
L = '<style>.legal h2{font-size:1.5rem;letter-spacing:-.03em;margin:44px 0 14px}.legal h2:first-child{margin-top:0}.legal p{color:var(--ink-3)}.legal a{text-decoration:underline}@media(max-width:900px){.legal{grid-column:1/-1!important}}</style>'
legal('mentions-legales', 'Mentions légales', L + f'''
<h2>Éditeur du site</h2><p><strong>{CO['name']}</strong><br>{CO['street']}<br>{CO['npa']} {CO['city']}, Suisse<br>Téléphone : <a href="tel:{CO['tel']}">{CO['phone']}</a><br>E-mail : <a href="mailto:{CO['email']}">{CO['email']}</a><br>Numéro IDE : {CO['ide']}<br>Gérant : {CO['boss']}</p>
<h2>Responsabilité</h2><p>Les informations publiées sur ce site sont fournies avec le plus grand soin. {CO['name']} ne peut toutefois garantir leur exactitude, leur exhaustivité ni leur actualité. Toute responsabilité pour des dommages résultant de l’utilisation de ce site est exclue dans la mesure permise par la loi.</p>
<h2>Liens externes</h2><p>Ce site contient des liens vers des sites tiers (Google, local.ch, Facebook, LinkedIn, WhatsApp). Leur contenu relève de la seule responsabilité de leurs exploitants.</p>
<h2>Droits d’auteur</h2><p>Les photographies de chantier, vidéos et plans sont la propriété de {CO['name']}. Certaines images d’illustration proviennent d’Unsplash (licence Unsplash). Toute reproduction requiert un accord préalable.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>''',
    'Mentions légales · Massonelec Sàrl', 'Mentions légales du site de Massonelec Sàrl, installateur-électricien à Aigle.')
legal('confidentialite', 'Protection des données', L + f'''
<p>{CO['name']} attache une grande importance à la protection de vos données personnelles et respecte la loi fédérale sur la protection des données (nLPD).</p>
<h2>Responsable du traitement</h2><p>{CO['name']}, {CO['street']}, {CO['npa']} {CO['city']} · <a href="mailto:{CO['email']}">{CO['email']}</a></p>
<h2>Formulaires</h2><p>Les formulaires de ce site ne stockent aucune donnée sur un serveur. Lorsque vous les validez, votre message est pré-rempli dans WhatsApp ou dans votre messagerie, et vous décidez vous-même de l’envoyer. Les données transmises servent uniquement à traiter votre demande.</p>
<h2>WhatsApp</h2><p>Si vous nous écrivez via WhatsApp, le service est fourni par WhatsApp Ireland Ltd. et soumis à sa propre politique de confidentialité.</p>
<h2>Google Maps</h2><p>La carte de la page Contact n’est chargée qu’après votre clic. Google peut alors collecter des données de connexion selon sa politique de confidentialité.</p>
<h2>Polices et cookies</h2><p>Ce site n’utilise ni cookies publicitaires ni outil de mesure d’audience. Les polices de caractères sont chargées depuis Google Fonts.</p>
<h2>Vos droits</h2><p>Vous pouvez demander l’accès, la rectification ou la suppression de vos données en écrivant à <a href="mailto:{CO['email']}">{CO['email']}</a>.</p>''',
    'Protection des données · Massonelec Sàrl', 'Déclaration de protection des données de Massonelec Sàrl (nLPD).')
nf = phero('<a href="./">Accueil</a> / 404', 'Erreur 404', ['Page', 'introuvable.'], f'<p>Le courant ne passe pas ici.</p>{btn("./", "Retour à l’accueil")}')
P['404'] = page('404', 'Page introuvable · Massonelec Sàrl', 'Page introuvable.', nf, base='/massonelec/', pt_label='404')

for slug, h in P.items():
    with open(os.path.join(OUT, f'{slug}.html'), 'w', encoding='utf-8') as f: f.write(h)
with open(os.path.join(OUT, 'assets', 'img', 'logo-m.svg'), 'w') as f: f.write(logo_m_svg())
open(os.path.join(OUT, '.nojekyll'), 'w').close()
print('built', len(P), 'pages')
