# -*- coding: utf-8 -*-
"""Build the Massonelec site into docs/.  Run: python3 _build/build.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parts import *  # noqa

OUT = os.path.join(ROOT, 'docs')
PAGES = {}

def add(slug, title, desc, body, **kw):
    PAGES[slug] = page(slug, title, desc, body, **kw)

def faq_block(items, schema_out=True):
    det = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    import json, re
    js = ''
    if schema_out:
        d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in items]}
        js = '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'
    return f'<div class="faq">{det}</div>{js}'

def ticks(items, cols=False):
    return f'<ul class="ticks{" cols" if cols else ""}">' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'

def feats(items, cols=3):
    return '<div class="feat-grid">' + ''.join(
        f'<div class="feat" data-reveal><div class="fi">{ic(i)}</div><h3>{t}</h3>' + (f'<p>{d}</p>' if isinstance(d, str) else '<ul>' + ''.join(f'<li>{x}</li>' for x in d) + '</ul>') + '</div>'
        for i, t, d in items) + '</div>'

def split(kicker_icon, kicker, h2, html_body, image, alt, cap='', rev=False, alt_bg=False):
    c = f'<span class="cap">{cap}</span>' if cap else ''
    return f'''<section class="sec{' sec-alt' if alt_bg else ''}"><div class="wrap split{' rev' if rev else ''}">
  <div data-reveal><span class="kicker">{ic(kicker_icon)} {kicker}</span><h2>{h2}</h2>{html_body}</div>
  <div class="split-img" data-reveal>{img(image, alt)}{c}</div>
</div></section>'''

FAQ_MAIN = [
    ('Intervenez-vous en urgence, la nuit et le week-end ?', 'Oui. Le dépannage électrique est assuré 24 h/24 et 7 j/7. Appelez directement le <a href="tel:+41793505519">079 350 55 19</a> : en cas de panne, un appel est plus rapide qu’un formulaire.'),
    ('Le devis est-il payant ?', 'Non. Après un rendez-vous pour comprendre vos besoins et ceux de votre bâtiment, nous rédigeons un devis gratuit et sans engagement.'),
    ('Dans quelle région travaillez-vous ?', 'Depuis notre bureau d’Aigle, nous intervenons dans tout le Chablais vaudois (Aigle, Ollon, Bex, Villeneuve, Leysin, Villars, Les Diablerets…) et jusqu’à Bulle, en passant par la Riviera et le Pays-d’Enhaut.'),
    ('Remettez-vous un rapport de sécurité après les travaux ?', 'Oui. Nos installations sont contrôlées conformément à l’art. 31 de l’ordonnance fédérale sur les installations électriques à basse tension (OIBT). Nous délivrons un rapport de conformité au propriétaire et au fournisseur d’énergie.'),
    ('Travaillez-vous pour les entreprises, l’industrie et le médical ?', 'Oui : particuliers, régies, commerces, industries, infrastructures et établissements de santé. Nous avons notamment raccordé un scanner et un mammographe au Centre d’imagerie d’Aigle, une génératrice de 88 kVA et une station de pompage d’eau potable.'),
    ('Quels moyens de paiement acceptez-vous ?', 'Paiement sur facture, cartes Visa, Mastercard, American Express, Maestro et PostFinance Card.'),
    ('Dans quelles langues peut-on vous joindre ?', 'En français et en italien.'),
]

# =====================================================================
# HOME
# =====================================================================
home_services = [
    ('electricite-generale', 'Électricité générale', 'Installations neuves, rénovations, mises en conformité OIBT, intérieur comme extérieur.', 'bolt', 'plafond-led-blanc'),
    ('courant-fort-industrie', 'Courant fort & industrie', 'Armoires de distribution, force motrice, génératrices, stations de pompage.', 'factory', 'station-pompage-armoire'),
    ('courant-faible-reseaux', 'Courant faible & réseaux', 'Téléphonie analogique et IP, câblage informatique, interphones et caméras IP.', 'network', 'baie-reseau'),
    ('domotique-eclairage', 'Domotique & éclairage LED', 'Programmation de l’éclairage, du chauffage et des stores. Éclairage décoratif et de jardin.', 'bulb', 'plafond-led-violet'),
    ('depannage-electrique-24h', 'Dépannage 24 h/24', 'Panne générale, disjoncteur, court-circuit : intervention rapide dans tout le Chablais.', 'wrench', 'tableau-distribution'),
    ('etudes-conception', 'Études & conception', 'Relevés, plans d’installation, schémas unifilaires et calculs de dimensionnement.', 'plan', 'plan-electrique-2'),
    ('innovation-prototypage', 'Innovation & prototypage', 'Outils de levage, pièces introuvables en impression 3D, objets sur mesure.', 'cube', 'piece-impression-3d'),
]
svc_cards = f'''<a class="svc feature" href="imagerie-medicale" data-tilt data-reveal><span class="svc-ico">{ic('scan')}</span><div class="svc-img">{img('scanner-poster','Scanner d’imagerie médicale raccordé par Massonelec au Centre d’imagerie d’Aigle',sizes='(max-width:720px) 100vw, 50vw')}</div><div class="svc-body"><h3>Imagerie médicale & santé</h3><p>Alimentation, calcul et raccordement d’équipements d’imagerie : scanner et mammographe au Centre d’imagerie d’Aigle.</p><span class="link-arrow">Voir le secteur médical {ic('arrow')}</span></div></a>'''
svc_cards += ''.join(f'''<a class="svc" href="{s}" data-tilt data-reveal><span class="svc-ico">{ic(i)}</span><div class="svc-img">{img(im, t, sizes='(max-width:720px) 100vw, 25vw')}</div><div class="svc-body"><h3>{t}</h3><p>{d}</p><span class="link-arrow">En savoir plus {ic('arrow')}</span></div></a>''' for s, t, d, i, im in home_services)

home = f'''
<section class="hero">
  <div class="hero-media"><video data-autoplay autoplay muted loop playsinline preload="auto" poster="assets/img/scanner-poster.webp" aria-hidden="true"><source src="assets/video/scanner-loop.mp4" type="video/mp4"></video></div>
  <div class="wrap">
    <div>
      <span class="kicker" style="color:#5fd0f5">{ic('award')} Installateur-électricien CFC · Aigle, depuis 2000</span>
      <h1>Du tableau électrique au <em>scanner médical</em>, une installation pensée et réalisée sans compromis.</h1>
      <p class="hero-lead">Massonelec Sàrl étudie, installe, contrôle et dépanne les réseaux électriques des particuliers, des entreprises, des industries et des centres médicaux, du Chablais vaudois jusqu’à Bulle.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="devis">Demander un devis gratuit {ic('arrow')}</a>
        <a class="btn btn-light" href="tel:{CO['tel']}">{ic('phone')} Urgence 24/7 · {CO['phone']}</a>
      </div>
      <div class="hero-badges">
        <span>{ic('shield')} Contrôles OIBT & rapport de sécurité</span>
        <span>{ic('clock')} Dépannage 24 h/24, 7 j/7</span>
        <span>{ic('globe')} Français · Italiano</span>
      </div>
    </div>
    <div class="qcard">
      <h2>Être rappelé rapidement</h2>
      <p class="sub">Laissez votre numéro, nous vous recontactons pour fixer un rendez-vous ou une intervention.</p>
      {quick_form('Demande de rappel – page d’accueil', idp='hq')}
    </div>
  </div>
  <span class="hero-video-tag"><i></i> Mise en service d’un scanner · Centre d’imagerie d’Aigle</span>
</section>

<section class="facts"><div class="wrap"><div class="facts-grid">
  <div class="fact"><span class="fact-ico">{ic('calendar')}</span><div><b>Depuis 2000</b><span>Entreprise fondée à Aigle, spécialiste de l’électricité générale du Chablais</span></div></div>
  <div class="fact"><span class="fact-ico">{ic('clock')}</span><div><b>24 h/24 · 7 j/7</b><span>Dépannage électrique pour particuliers, entreprises et industries</span></div></div>
  <div class="fact"><span class="fact-ico">{ic('shield')}</span><div><b>OIBT art. 31</b><span>Installations contrôlées, rapport de conformité remis</span></div></div>
  <div class="fact"><span class="fact-ico">{ic('g')}</span><div><b>5,0 / 5 sur Google</b><span>4,0 / 5 sur local.ch · <a href="#avis">voir les avis</a></span></div></div>
</div></div></section>

<section class="sec"><div class="wrap split">
  <div data-reveal>
    <span class="kicker">{ic('users')} L’entreprise</span>
    <h2>Un seul interlocuteur pour tout votre réseau électrique</h2>
    <p class="lead">Installateur-électricien de profession et titulaire d’un CFC, {CO['boss']} a fondé Massonelec Sàrl à Aigle en 2000. Depuis, l’entreprise s’est imposée comme l’une des références de l’électricité générale dans le Chablais vaudois.</p>
    <p>Basse tension ou courant fort, villa ou site industriel : nos installateurs-électriciens se chargent de tout, de l’étude de vos besoins à la mise en service, puis du dépannage. Vous n’avez qu’un interlocuteur, du premier rendez-vous au rapport de sécurité.</p>
    {ticks(['Étude et conseil sur place, devis gratuit','Conception des installations intérieures et extérieures','Réalisation, contrôle OIBT et rapport de conformité','Service de dépannage 24 h/24 et 7 j/7'])}
    <a class="link-arrow" href="entreprise">Découvrir l’entreprise {ic('arrow')}</a>
  </div>
  <div class="split-img" data-reveal>{img('tableau-domotique','Tableau électrique avec modules de domotique réalisé et étiqueté par Massonelec Sàrl')}<span class="cap">Tableau avec modules domotiques · réalisation Massonelec</span></div>
</div></section>

<section class="sec sec-alt" id="prestations"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('bolt')} Prestations</span><h2>Toute l’électricité du bâtiment, du courant faible au courant fort</h2><p>Huit métiers complémentaires, une même exigence de qualité et de sécurité.</p></div><a class="btn btn-ghost" href="prestations">Toutes les prestations {ic('arrow')}</a></div>
  <div class="svc-grid">{svc_cards}</div>
</div></section>

<section class="sec sec-dark" id="medical"><div class="wrap med">
  <div data-reveal>
    <div class="med-video"><video id="medvid" data-autoplay autoplay muted loop playsinline preload="none" poster="assets/img/scanner-poster.webp"><source src="assets/video/scanner-imagerie-aigle.mp4" type="video/mp4"></video>
      <button class="btn btn-light btn-sm play" data-unmute="#medvid">{ic('volume')} <span>Activer le son</span></button></div>
    <div class="med-thumbs">
      <figure>{img('imagerie-transformateur','Transformateur installé pour le mammographe du Centre d’imagerie d’Aigle',sizes='300px')}<figcaption>Transformateur dédié · mammographe</figcaption></figure>
      <figure>{img('scanner-poster','Anneau du scanner en rotation lors de la mise en service',sizes='300px')}<figcaption>Scanner en rotation · mise en service</figcaption></figure>
    </div>
  </div>
  <div data-reveal>
    <span class="kicker">{ic('pulse')} Secteur médical</span>
    <h2>Les équipements d’imagerie ne tolèrent aucune approximation</h2>
    <p>Au Centre d’imagerie d’Aigle, Massonelec Sàrl a assuré la mise en place et le raccordement d’un scanner, puis le calcul, la réalisation et l’installation de l’alimentation du mammographe, en collaboration avec GE.</p>
    <ul class="med-list">
      <li><span class="ck">{ic('check')}</span><span><b>Calcul et dimensionnement</b><span>Alimentation dédiée selon les exigences du fabricant.</span></span></li>
      <li><span class="ck">{ic('check')}</span><span><b>Coordination avec le constructeur</b><span>Travail conjoint avec les techniciens de l’équipement.</span></span></li>
      <li><span class="ck">{ic('check')}</span><span><b>Mise en service et contrôle</b><span>Raccordement, essais et rapport de conformité OIBT.</span></span></li>
    </ul>
    <a class="btn btn-primary" href="imagerie-medicale">Voir le secteur médical {ic('arrow')}</a>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('award')} Réalisations</span><h2>Des chantiers qui demandent de l’expérience</h2><p>Infrastructures, défense, santé, habitat : un aperçu de nos interventions récentes.</p></div><a class="btn btn-ghost" href="realisations">Toutes les réalisations {ic('arrow')}</a></div>
  <div class="proj-grid">
    <a class="proj tall" href="realisations#station-pompage" data-reveal>{img('station-pompage-salle','Salle des pompes d’une station de pompage d’eau potable équipée par Massonelec',sizes='(max-width:720px) 100vw, 33vw')}<div class="proj-body"><span class="proj-tag">Infrastructure · eau potable</span><h3>Station de pompage d’eau potable</h3><p>Installation électrique complète : armoires de commande, puissance et câblage des pompes.</p></div></a>
    <a class="proj" href="realisations#generatrice" data-reveal>{img('generatrice-88kva','Génératrice de 88 kVA installée dans un fort militaire',sizes='(max-width:720px) 100vw, 33vw')}<div class="proj-body"><span class="proj-tag">Énergie de secours</span><h3>Génératrice 88 kVA, fort militaire</h3><p>Mise en place et raccordement.</p></div></a>
    <a class="proj" href="realisations#scanner" data-reveal>{img('scanner-poster','Scanner médical du Centre d’imagerie d’Aigle',sizes='(max-width:720px) 100vw, 33vw')}<div class="proj-body"><span class="proj-tag">Santé</span><h3>Scanner & mammographe, Aigle</h3><p>Centre d’imagerie d’Aigle, en collaboration avec GE.</p></div></a>
    <a class="proj" href="realisations#jardin" data-reveal>{img('eclairage-jardin','Éclairage d’ambiance d’un jardin privé',sizes='(max-width:720px) 100vw, 33vw')}<div class="proj-body"><span class="proj-tag">Extérieur</span><h3>Éclairage d’ambiance de jardin</h3><p>Mise en lumière d’arbres, cheminements et four extérieur.</p></div></a>
    <a class="proj" href="realisations#miroir" data-reveal>{img('miroir-retroeclaire','Miroir avec éclairage périphérique fabriqué sur mesure',sizes='(max-width:720px) 100vw, 33vw')}<div class="proj-body"><span class="proj-tag">Sur mesure</span><h3>Miroir à éclairage périphérique</h3><p>Fabrication et pose d’un miroir rétroéclairé.</p></div></a>
  </div>
</div></section>

<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('flag')} Méthode</span><h2>Votre projet en quatre étapes claires</h2><p>Du premier appel au rapport de sécurité, vous savez toujours où en est votre installation.</p></div></div>
  <div class="steps">
    <div class="step" data-reveal><div class="step-n">1</div><h3>Rendez-vous & étude</h3><p>Nous venons sur place pour comprendre vos besoins et ceux de votre habitation ou de votre industrie.</p></div>
    <div class="step" data-reveal><div class="step-n">2</div><h3>Devis gratuit</h3><p>Une offre détaillée, gratuite et sans engagement, avec plans si nécessaire.</p></div>
    <div class="step" data-reveal><div class="step-n">3</div><h3>Réalisation</h3><p>Nos installateurs-électriciens réalisent les travaux proprement, dans les délais convenus.</p></div>
    <div class="step" data-reveal><div class="step-n">4</div><h3>Contrôle & rapport</h3><p>Contrôle selon l’art. 31 OIBT et rapport de conformité au propriétaire et au distributeur d’énergie.</p></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('building')} Clientèle</span><h2>Pour qui nous travaillons</h2><p>La même rigueur pour un studio que pour une infrastructure publique.</p></div></div>
  {feats([('home','Particuliers & villas','Rénovation, extension, salle de bain, éclairage, domotique, jardin.'),('building','Régies, PPE & immeubles','Tableaux, comptages, mises en conformité, dépannages pour les locataires.'),('card','Commerces & bureaux','Éclairage de vitrines, réseau informatique, téléphonie, interphones.'),('factory','Industrie & infrastructures','Courant fort, armoires, force motrice, station de pompage d’eau potable.'),('hospital','Santé & imagerie médicale','Raccordement de scanner et de mammographe, alimentations dédiées.'),('shield','Collectivités & sites sensibles','Génératrice de secours de 88 kVA dans un fort militaire.')])}
</div></section>

<section class="sec sec-alt" id="zone"><div class="wrap zone">
  <div data-reveal>
    <span class="kicker">{ic('pin')} Zone d’intervention</span>
    <h2>D’Aigle à Bulle, tout le Chablais vaudois</h2>
    <p class="lead">Notre bureau est au cœur du Chablais, à Aigle. Nos équipes interviennent chez les particuliers, entreprises et industries de toute la région, jusqu’à Bulle.</p>
    <div class="towns">{''.join(f'<span>{t}</span>' for t in ['Aigle','Yvorne','Ollon','Bex','Villeneuve','Roche','Leysin','Villars','Les Diablerets','Montreux','Vevey','Château-d’Œx','Châtel-St-Denis','Bulle'])}</div>
    <a class="btn btn-primary" href="contact">Nous trouver {ic('arrow')}</a>
  </div>
  <div class="zone-canvas" id="zone3d" data-src="assets/js/zone3d.js?v={V}" data-reveal><div class="labels"></div><div class="zone-fallback">Carte 3D de la zone d’intervention</div><span class="zone-legend">Carte 3D · Lac Léman, Rhône et localités desservies</span></div>
</div></section>

<section class="sec"><div class="wrap split rev">
  <div data-reveal>
    <span class="kicker">{ic('cube')} Innovation</span>
    <h2>Quand la pièce n’existe plus, nous la fabriquons</h2>
    <p class="lead">L’électricité reste notre métier. Mais à la demande de particuliers ou de professionnels, nous imaginons aussi des objets, des outils et des machines qui simplifient la vie.</p>
    <p>Outils de levage pour aider à la mobilité, pièces mécaniques introuvables redessinées en CAO puis imprimées en 3D, enseignes lumineuses gravées : nous mettons notre ingéniosité au service de votre confort.</p>
    <a class="link-arrow" href="innovation-prototypage">Voir nos prototypes {ic('arrow')}</a>
  </div>
  <div class="split-img" data-reveal>{img('proto-chassis-levage','Châssis de levage motorisé conçu sur mesure par Massonelec')}<span class="cap">Châssis de levage motorisé · prototype</span></div>
</div></section>

<section class="sec sec-alt" id="avis"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('star')} Avis clients</span><h2>Ce que disent nos clients</h2><p>Notes publiques sur Google et local.ch.</p></div><a class="btn btn-ghost" href="{CO['gwrite']}" target="_blank" rel="noopener">{ic('g')} Laisser un avis</a></div>
  <div class="rev-grid">
    <div class="rev-sum" data-reveal><span class="src">{ic('g')} Google</span><span class="rev-score">5,0</span>{stars(5)}<small>Note moyenne sur Google</small><span class="links"><a href="{CO['greviews']}" target="_blank" rel="noopener">Voir les avis Google →</a><a href="{CO['gwrite']}" target="_blank" rel="noopener">Écrire un avis →</a></span></div>
    <div class="rev-sum" data-reveal><span class="src">{ic('lc')} local.ch</span><span class="rev-score">4,0</span>{stars(4)}<small>Moyenne de 4 évaluations</small><span class="links"><a href="{CO['lc']}" target="_blank" rel="noopener">Voir la fiche local.ch →</a></span></div>
    <div class="rev-card" data-reveal>{stars(5)}<q>Électricien au top</q><span class="n">Titre de 2 avis 5 étoiles publiés sur local.ch</span><span class="who">{ic('lc')} local.ch · 17 octobre 2023</span></div>
    <div class="rev-card" data-reveal>{stars(5)}<q>Note maximale, photos de l’intervention à l’appui</q><span class="n">Josiane D., Local Guide Google</span><span class="who">{ic('g')} Avis Google</span></div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sec-head" style="justify-content:center;text-align:center"><div class="intro" style="margin-inline:auto"><span class="kicker">{ic('msg')} Questions fréquentes</span><h2>Vos questions, nos réponses</h2></div></div>
  {faq_block(FAQ_MAIN)}
</div></section>

{form_section(subject='Demande depuis la page d’accueil', idp='home')}
{cta_band()}
'''
add('index', 'Massonelec Sàrl · Électricien à Aigle · Courant fort, faible & dépannage 24/7',
    'Installateur-électricien CFC à Aigle depuis 2000. Électricité générale, courant fort et industriel, imagerie médicale, domotique, dépannage 24 h/24 dans le Chablais vaudois jusqu’à Bulle. Devis gratuit.',
    home, active='index', extra_head='<link rel="preload" as="image" href="assets/img/scanner-poster.webp">')

# =====================================================================
# ENTREPRISE
# =====================================================================
ent = phero('<span>Entreprise</span>', 'Massonelec Sàrl, l’électricité générale du Chablais depuis 2000',
            'Une entreprise d’Aigle fondée par un installateur-électricien CFC, reconnue pour sa conscience professionnelle et sa capacité à mener des chantiers techniques exigeants.', image='armoire-industrielle')
ent += split('users', 'Notre histoire', 'Un artisan devenu une référence régionale',
    f'''<p class="lead">Installateur-électricien de profession et titulaire d’un CFC, {CO['boss']} a toujours souhaité devenir indépendant. En 2000, il fonde sa propre société à Aigle : Massonelec Sàrl.</p>
    <p>Depuis, l’entreprise est devenue l’un des spécialistes de l’électricité générale d’Aigle et du Chablais vaudois. Elle intervient sur tous les types d’installations, de la basse tension au courant fort, auprès des particuliers, des entreprises et des industries, jusqu’à Bulle.</p>
    <p>Avec Massonelec, vous choisissez la confiance et la rapidité : nos installateurs-électriciens se chargent de tout, de l’étude de vos besoins à la conception de l’installation intérieure et extérieure, jusqu’au dépannage.</p>''',
    'coffrets-comptage', 'Coffrets de comptage et de distribution câblés par Massonelec', 'Coffrets de comptage · immeuble')
ent += f'''<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('award')} Nos engagements</span><h2>Ce qui guide chaque intervention</h2></div></div>
  {feats([('shield','La conscience professionnelle avant tout','Nous mettons un point d’honneur à fournir un travail de qualité irréprochable, contrôlé selon l’OIBT.'),('users','Un seul interlocuteur','De l’étude au dépannage, vous traitez avec la même entreprise pour tout votre réseau électrique.'),('clock','Rapidité','Dépannage 24 h/24 et 7 j/7, partout dans le Chablais vaudois.'),('cube','Ingéniosité','Nous concevons des outils et des objets jusqu’alors inexistants sur le marché.'),('doc','Transparence','Devis gratuit et sans engagement, rapport de conformité remis après les travaux.'),('globe','Proximité','Une entreprise locale, joignable en français et en italien.')])}
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('building')} En bref</span><h2>Massonelec Sàrl en quelques repères</h2></div></div>
  <div class="facts-grid" style="box-shadow:none;border:1px solid var(--line)">
    <div class="fact"><span class="fact-ico">{ic('calendar')}</span><div><b>2000</b><span>Fondation à Aigle</span></div></div>
    <div class="fact"><span class="fact-ico">{ic('award')}</span><div><b>CFC</b><span>Installateur-électricien qualifié</span></div></div>
    <div class="fact"><span class="fact-ico">{ic('bolt')}</span><div><b>88 kVA</b><span>Génératrice raccordée dans un fort militaire</span></div></div>
    <div class="fact"><span class="fact-ico">{ic('scan')}</span><div><b>Scanner & mammographe</b><span>Centre d’imagerie d’Aigle</span></div></div>
  </div>
  <table class="hours" style="margin-top:36px;max-width:720px"><tbody>
    <tr><td>Raison sociale</td><td>Massonelec Sàrl</td></tr><tr><td>Gérant</td><td>{CO['boss']}</td></tr>
    <tr><td>Numéro IDE</td><td>{CO['ide']}</td></tr><tr><td>Siège</td><td>{CO['street']}, {CO['npa']} {CO['city']} (VD)</td></tr>
    <tr><td>Langues</td><td>Français, italien</td></tr><tr><td>Paiement</td><td>Facture, Visa, Mastercard, Amex, Maestro, PostFinance</td></tr>
  </tbody></table>
</div></section>'''
ent += split('pin', 'Implantation', 'Au cœur du Chablais, à Aigle',
    f'''<p class="lead">Notre bureau du {CO['street']} nous place à quelques minutes de Bex, Ollon, Villeneuve, Leysin et Villars, avec un accès direct vers la Riviera, le Pays-d’Enhaut et la Gruyère.</p>{ticks(['Particuliers et PPE','Entreprises, commerces et bureaux','Industries et infrastructures','Établissements de santé'])}<a class="btn btn-primary" href="contact">Contact & accès {ic('arrow')}</a>''',
    'station-pompage-armoire', 'Armoire électrique d’une station de pompage d’eau potable', 'Station de pompage · armoire de commande', rev=True, alt_bg=True)
ent += form_section(subject='Demande depuis la page Entreprise', idp='ent') + cta_band()
add('entreprise', 'L’entreprise · Massonelec Sàrl, électricien à Aigle depuis 2000',
    'Fondée en 2000 à Aigle par un installateur-électricien CFC, Massonelec Sàrl est spécialiste de l’électricité générale du Chablais vaudois : basse tension, courant fort, dépannage 24/7.', ent)

# =====================================================================
# PRESTATIONS (hub)
# =====================================================================
hub = phero('<span>Prestations</span>', 'Nos prestations en électricité', 'Courant fort et courant faible, études, installation, contrôle, dépannage et innovation : tout ce dont votre bâtiment a besoin, avec un seul interlocuteur.', image='cablage-armoire')
hub += f'''<section class="sec"><div class="wrap"><div class="svc-grid">{svc_cards}</div></div></section>
<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('check')} Catalogue détaillé</span><h2>L’ensemble de nos interventions</h2><p>Liste non exhaustive : contactez-nous pour tout besoin spécifique.</p></div></div>
  {feats([('lock','Installations de sécurité',['Alarmes','Caméras de sécurité IP','Détection d’incendie','Détection d’intrusion','Interphones IP']),('bulb','Éclairage',['Éclairage LED','Éclairage décoratif','Éclairage de jardin et extérieur','Miroirs et meubles rétroéclairés']),('cpu','Domotique',['Installation entièrement programmable','Éclairage, chauffage, stores','Commande à distance']),('phone','Téléphonie',['Installations analogiques et numériques','Centraux téléphoniques','Raccordements téléphoniques']),('network','Informatique',['Réseau et transmission de données','Câblage universel','Prises réseau']),('factory','Industrie',['Câblage universel et force','Armoires de distribution','Génératrices et énergie de secours']),('home','Rénovation',['Rénovation d’installations électriques','Retouches OIBT','Mises en conformité']),('plan','Études',['Relevés et plans','Schémas unifilaires','Calculs de dimensionnement']),('wrench','Dépannage',['24 h/24 et 7 j/7','Particuliers, pros et industries','Tout le Chablais jusqu’à Bulle'])])}
</div></section>''' + form_section(subject='Demande depuis la page Prestations', idp='pr') + cta_band()
add('prestations', 'Prestations · Électricité générale, courant fort et faible · Massonelec Aigle',
    'Électricité générale, courant fort et industrie, courant faible et réseaux, domotique, éclairage LED, dépannage 24/7, études et prototypage à Aigle et dans le Chablais.', hub)

# =====================================================================
# SERVICE PAGES
# =====================================================================
def service_page(slug, crumb, h1, lead, hero_img, sections, faq=None, pre='', title='', desc=''):
    b = phero(f'<a href="prestations">Prestations</a><span aria-hidden="true">/</span><span>{crumb}</span>', h1, lead, image=hero_img, service=pre)
    b += sections
    if faq:
        b += f'<section class="sec"><div class="wrap"><div class="sec-head"><div class="intro"><span class="kicker">{ic("msg")} Questions fréquentes</span><h2>{crumb} : vos questions</h2></div></div>{faq_block(faq)}</div></section>'
    b += related(slug) + form_section(f'Votre projet : {crumb.lower()}', subject=f'Demande – {crumb}', pre=pre, idp=slug[:4]) + cta_band()
    add(slug, title, desc, b)

# --- électricité générale
service_page('electricite-generale', 'Électricité générale', 'Électricité générale : installations neuves et rénovations',
    'Construction, transformation ou rénovation : nous étudions, concevons et réalisons votre installation électrique intérieure et extérieure, puis la contrôlons selon l’OIBT.',
    'plafond-led-blanc',
    split('bolt', 'Neuf & rénovation', 'Une étude sur mesure avant toute intervention',
        '''<p class="lead">Avant de commencer, nous prenons rendez-vous avec vous afin de comprendre vos besoins et ceux de votre habitation ou de votre entreprise.</p><p>Nous réalisons ensuite une étude et rédigeons un devis gratuit et sans engagement. Une fois les travaux validés, nos installateurs-électriciens s’occupent de tout, du tableau jusqu’au dernier point lumineux.</p>''' +
        ticks(['Installations électriques complètes, villas et immeubles','Rénovation d’installations anciennes','Tableaux de distribution et coffrets de comptage','Prises, éclairage, appareils, cuisines et salles de bain','Installations extérieures et de jardin','Retouches OIBT et mises en conformité'], cols=True),
        'tableau-distribution', 'Tableau de distribution électrique', 'Tableau de distribution') +
    f'''<section class="sec sec-dark"><div class="wrap">
      <div class="sec-head"><div class="intro"><span class="kicker">{ic('shield')} Sécurité</span><h2>Des installations contrôlées et documentées</h2><p>Nos installations sont contrôlées conformément à l’art. 31 de l’ordonnance fédérale sur les installations électriques à basse tension (OIBT).</p></div></div>
      {feats([('doc','Rapport de sécurité','Nous délivrons un rapport de conformité au propriétaire de la construction et au fournisseur d’énergie.'),('shield','Retouches OIBT','Correction des défauts relevés lors d’un contrôle périodique ou d’une vente immobilière.'),('home','Rénovation','Mise à niveau des installations anciennes : protections, terres, différentiels, tableaux.')])}
    </div></section>''' +
    split('home', 'Finitions', 'Le soin du détail jusque dans la salle de bain',
        '<p class="lead">Éclairage intégré, miroirs rétroéclairés fabriqués sur mesure, prises placées au bon endroit : une installation réussie se voit aussi au quotidien.</p>' + ticks(['Salles de bain et cuisines','Éclairage encastré et gorges lumineuses','Miroirs avec éclairage périphérique','Points de recharge et prises extérieures']),
        'salle-de-bain-baignoire', 'Salle de bain rénovée avec installation électrique Massonelec', 'Salle de bain · rénovation', rev=True, alt_bg=True),
    faq=[FAQ_MAIN[1], FAQ_MAIN[3], ('Pouvez-vous rénover une installation ancienne sans tout casser ?', 'Oui. Après un relevé de l’existant, nous proposons la solution la plus adaptée : remplacement du tableau, ajout de protections différentielles, reprise des circuits défectueux ou rénovation complète.')],
    pre='Électricité générale', title='Électricité générale à Aigle · Installation & rénovation · Massonelec',
    desc='Installations électriques neuves et rénovations à Aigle et dans le Chablais vaudois : étude, devis gratuit, réalisation, contrôle OIBT et rapport de sécurité.')

# --- courant fort & industrie
service_page('courant-fort-industrie', 'Courant fort & industrie', 'Courant fort, industrie et infrastructures',
    'Armoires de distribution, force motrice, énergie de secours, stations de pompage : nous réalisons des installations à courant fort pour les entreprises, l’industrie et les collectivités.',
    'station-pompage-armoire',
    split('factory', 'Infrastructure', 'Station de pompage d’eau potable',
        '<p class="lead">Installation électrique d’une station de pompage d’eau potable, réalisée entièrement par notre société : armoires de commande et de puissance, chemins de câbles et raccordement des groupes de pompage.</p>' + ticks(['Armoires de commande et de puissance','Câblage universel et force','Raccordement de moteurs et de pompes','Chemins de câbles et distribution']),
        'station-pompage-salle', 'Salle des pompes d’une station d’eau potable', 'Station de pompage · salle des pompes') +
    split('gen', 'Énergie de secours', 'Génératrice de 88 kVA dans un fort militaire',
        '<p class="lead">Mise en place et raccordement d’une génératrice de 88 kVA dans un fort militaire : un chantier en milieu confiné, où la fiabilité de l’alimentation de secours est essentielle.</p>' + ticks(['Groupes électrogènes et alimentation de secours','Raccordement au tableau principal','Essais et mise en service']),
        'generatrice-88kva', 'Génératrice de 88 kVA dans un fort militaire', 'Génératrice 88 kVA', rev=True, alt_bg=True) +
    f'''<section class="sec"><div class="wrap">
      <div class="sec-head"><div class="intro"><span class="kicker">{ic('factory')} Compétences</span><h2>Installations industrielles</h2></div></div>
      {feats([('plug','Force motrice','Alimentation et raccordement de machines, moteurs et équipements de production.'),('cpu','Armoires électriques','Câblage d’armoires de distribution, de commande et d’automatisme.'),('gen','Énergie de secours','Génératrices, inverseurs de source et circuits prioritaires.'),('network','Câblage universel','Réseau de données et transmission pour sites industriels.'),('shield','Contrôles','Mesures, contrôles et rapports de sécurité OIBT.'),('wrench','Dépannage industriel','Remise en service rapide pour limiter l’arrêt de production.')])}
    </div></section>''',
    pre='Courant fort / industrie', title='Courant fort & installations industrielles · Massonelec Sàrl, Aigle',
    desc='Courant fort, armoires électriques, force motrice, génératrices et stations de pompage : installations industrielles et d’infrastructure dans le Chablais vaudois.')

# --- courant faible
service_page('courant-faible-reseaux', 'Courant faible & réseaux', 'Courant faible : téléphonie, réseaux et sécurité',
    'Téléphonie analogique et numérique, réseau informatique, interphones et caméras IP, alarmes et détection : les installations à courant faible qui font vivre votre bâtiment.',
    'baie-reseau',
    f'''<section class="sec"><div class="wrap">
      <div class="sec-head"><div class="intro"><span class="kicker">{ic('network')} Courant faible</span><h2>Communication, données et sécurité</h2><p>Des installations propres, repérées et documentées, faciles à faire évoluer.</p></div></div>
      {feats([('phone','Téléphonie',['Installations analogiques et numériques','Centraux téléphoniques','Raccordements téléphoniques']),('network','Réseau informatique',['Transmission de données','Câblage universel','Prises réseau, baies de brassage']),('camera','Vidéo & interphonie',['Caméras de sécurité IP','Interphones IP','Contrôle d’accès']),('lock','Intrusion','Systèmes d’alarme et détection d’intrusion pour habitations et locaux professionnels.'),('flame','Incendie','Installations de détection d’incendie.'),('cpu','Intégration','Coordination avec la domotique, l’éclairage et les automatismes.')])}
    </div></section>''' +
    split('network', 'Réalisation', 'Baies de brassage et câblage structuré',
        '<p class="lead">Un réseau fiable commence par un câblage soigné : chemins de câbles, repérage, baies de brassage et tests.</p>' + ticks(['Câblage cuivre catégorie adaptée','Brassage et repérage','Raccordement téléphonie et internet','Wi-Fi et points d’accès']),
        'baie-reseau', 'Baie de brassage réseau et téléphonie', 'Baie réseau & téléphonie', alt_bg=True),
    pre='Courant faible, téléphonie, réseau', title='Courant faible, téléphonie & réseau informatique · Massonelec Aigle',
    desc='Téléphonie, câblage informatique, prises réseau, interphones et caméras IP, alarmes, détection incendie et intrusion à Aigle et dans le Chablais.')

# --- domotique & éclairage
service_page('domotique-eclairage', 'Domotique & éclairage', 'Domotique et éclairage LED',
    'Une installation entièrement programmable et ajustable à la demande, et un éclairage qui met en valeur votre intérieur, votre commerce ou votre jardin.',
    'plafond-led-violet',
    split('cpu', 'Domotique', 'Votre bâtiment, piloté selon vos habitudes',
        '<p class="lead">Nous mettons en place des installations entièrement programmables et ajustables à la demande.</p>' + ticks(['Programmation de l’éclairage, du chauffage et des stores','Scénarios et commandes centralisées','Commande à distance','Tableaux avec modules domotiques repérés']),
        'tableau-domotique', 'Tableau électrique avec modules domotiques', 'Tableau domotique') +
    f'''<section class="sec sec-alt"><div class="wrap">
      <div class="sec-head"><div class="intro"><span class="kicker">{ic('bulb')} Éclairage</span><h2>La lumière comme élément d’architecture</h2><p>Gorges lumineuses, LED couleur, meubles et vitrines rétroéclairés, mise en lumière de jardin.</p></div></div>
      <div class="gal" style="columns:3 260px">
        {''.join(f'<button class="gal-item" data-lb data-full="assets/img/{n}.webp" data-caption="{esc(c)}">{img(n, c, sizes="(max-width:720px) 100vw, 33vw")}<figcaption>{c}</figcaption></button>' for n, c in [('plafond-led-violet','Plafond lumineux LED couleur'),('salon-eclairage','Salon avec éclairage encastré'),('eclairage-jardin','Éclairage d’ambiance pour un jardin privé'),('bibliotheque-led','Bibliothèque à LED intégrées'),('vitrine-led','Vitrine à étagères lumineuses'),('miroir-retroeclaire','Miroir à éclairage périphérique sur mesure'),('plafond-led-chantier','Gorge lumineuse en cours de chantier'),('projecteur-led','Projecteur LED extérieur')])}
      </div>
    </div></section>''',
    pre='Domotique / éclairage LED', title='Domotique & éclairage LED · Massonelec Sàrl, électricien à Aigle',
    desc='Domotique programmable (éclairage, chauffage, stores), éclairage LED décoratif, gorges lumineuses, éclairage de jardin et miroirs rétroéclairés dans le Chablais.')

# --- dépannage
dep_sections = f'''<section class="sec"><div class="wrap split">
  <div data-reveal><span class="kicker">{ic('alert')} Urgence</span><h2>Votre installation électrique est en panne ?</h2>
    <p class="lead">Que vous soyez un particulier, un professionnel ou une industrie, Massonelec intervient chez vous en un temps record. Nos installateurs-électriciens expérimentés se déplacent dans tout le Chablais vaudois, jusqu’à Bulle, pour remettre votre électricité en marche.</p>
    <a class="btn btn-primary" href="tel:{CO['tel']}" style="margin:6px 0 18px">{ic('phone')} Appeler le {CO['phone']}</a>
    {ticks(['Panne générale ou partielle','Disjoncteur ou différentiel qui déclenche','Court-circuit, prise ou interrupteur défectueux','Odeur de brûlé, échauffement','Éclairage hors service','Machine ou installation industrielle à l’arrêt'], cols=True)}
  </div>
  <div class="split-img" data-reveal>{img('cablage-armoire','Intervention sur une armoire électrique')}<span class="cap">Intervention 24/7</span></div>
</div></section>
<section class="sec sec-dark"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('shield')} En attendant notre arrivée</span><h2>Les bons réflexes</h2><p>Votre sécurité passe avant tout. En cas de doute, ne touchez à rien et appelez-nous.</p></div></div>
  {feats([('alert','Ne touchez pas','N’intervenez jamais sur un câble, une prise ou un appareil endommagé ou humide.'),('bolt','Coupez si possible','Si vous pouvez le faire sans risque, coupez l’alimentation au tableau électrique.'),('phone','Appelez-nous','Décrivez ce que vous observez : nous vous guidons et organisons l’intervention.')])}
</div></section>'''
service_page('depannage-electrique-24h', 'Dépannage 24/7', 'Dépannage électrique 24 h/24 et 7 j/7',
    'Une panne ne prévient pas. Nous intervenons rapidement, jour et nuit, week-end compris, partout dans le Chablais vaudois jusqu’à Bulle.',
    'tableau-distribution', dep_sections,
    faq=[FAQ_MAIN[0], FAQ_MAIN[2], ('Intervenez-vous aussi pour les entreprises et l’industrie ?', 'Oui. Nous dépannons les installations des particuliers, des professionnels et des industries, y compris le courant fort.')],
    pre='Dépannage urgent', title='Dépannage électrique 24h/24 à Aigle et dans le Chablais · Massonelec',
    desc='Électricien d’urgence 24 h/24 et 7 j/7 à Aigle, Ollon, Bex, Villeneuve, Leysin et jusqu’à Bulle. Panne, court-circuit, disjoncteur : appelez le 079 350 55 19.')

# --- études & conception
etu = f'''<section class="sec"><div class="wrap split">
  <div data-reveal><span class="kicker">{ic('plan')} Bureau technique</span><h2>Des plans précis avant le premier câble</h2>
    <p class="lead">Relevé de l’existant, plan d’installation, schéma unifilaire, calcul de dimensionnement : la qualité d’une installation se joue d’abord sur le papier.</p>
    {ticks(['Plans d’implantation électrique par pièce','Schémas unifilaires de tableaux','Calculs de dimensionnement (sections, protections, puissances)','Coordination avec architectes, maîtres d’ouvrage et fabricants','Documentation remise en fin de chantier'])}
  </div>
  <div class="split-img" data-reveal>{img('plan-electrique-2','Plan d’installation électrique réalisé par Massonelec')}<span class="cap">Plan d’installation électrique</span></div>
</div></section>
<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('doc')} Exemples</span><h2>Plans et schémas</h2></div></div>
  <div class="gal" style="columns:3 280px">{''.join(f'<button class="gal-item" data-lb data-full="assets/img/{n}.webp" data-caption="{esc(c)}">{img(n, c, sizes="(max-width:720px) 100vw, 33vw")}<figcaption>{c}</figcaption></button>' for n, c in [('plan-electrique-1','Plan d’appartement : points lumineux et prises'),('schema-unifilaire','Schéma de principe de distribution'),('plan-electrique-3','Plan d’installation d’un logement'),('plan-electrique-2','Plan d’étage complet')])}</div>
</div></section>'''
service_page('etudes-conception', 'Études & conception', 'Études, plans et conception électrique',
    'Nous réalisons l’étude complète de votre installation et concevons des plans clairs, pour un chantier maîtrisé et un devis juste.',
    'plan-electrique-3', etu, pre='Études & plans', title='Études & plans électriques · Conception d’installations · Massonelec Aigle',
    desc='Relevés, plans d’installation électrique, schémas unifilaires et calculs de dimensionnement pour particuliers, entreprises et établissements médicaux.')

# --- innovation
inn = f'''<section class="sec"><div class="wrap split">
  <div data-reveal><span class="kicker">{ic('cube')} Innovation</span><h2>Notre créativité au service de votre bien-être</h2>
    <p class="lead">L’activité de Massonelec Sàrl est avant tout l’électricité générale. Cependant, à la demande de particuliers ou de professionnels, nous imaginons des objets, des outils ou des machines qui vous simplifient la vie.</p>
    <p>Comme pour les études électriques, nous nous déplaçons chez vous pour discuter du projet et connaître vos besoins. Nous mettons ensuite notre ingéniosité à votre service et inventons des objets jusqu’alors inexistants sur le marché. Nous avons par exemple conçu différents outils de levage pour aider à la mobilité de nos clients.</p>
  </div>
  <div class="split-img" data-reveal>{img('proto-chassis-levage','Châssis de levage motorisé conçu par Massonelec')}<span class="cap">Outil de levage sur mesure</span></div>
</div></section>
<section class="sec sec-dark"><div class="wrap split rev">
  <div data-reveal><span class="kicker">{ic('cpu')} Impression 3D</span><h2>Quand une pièce est cassée et ne se fabrique plus</h2>
    <p class="lead" style="color:#c9d5e0">… nous la redessinons en CAO et la refabriquons en impression 3D.</p>
    <p>Engrenages, supports, boîtiers : une solution rapide pour remettre en service un appareil ou une machine dont la pièce d’origine est introuvable.</p></div>
  <div class="split-img" data-reveal>{img('piece-impression-3d','Engrenage modélisé en CAO avant impression 3D')}<span class="cap">Engrenage modélisé en CAO</span></div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('wrench')} Atelier</span><h2>Prototypes réalisés</h2></div></div>
  <div class="gal" style="columns:3 260px">{''.join(f'<button class="gal-item" data-lb data-full="assets/img/{n}.webp" data-caption="{esc(c)}">{img(n, c, sizes="(max-width:720px) 100vw, 33vw")}<figcaption>{c}</figcaption></button>' for n, c in [('proto-lift-projecteur','Lift motorisé pour vidéoprojecteur encastré au plafond'),('enseigne-led-gravee','Enseigne en verre gravé rétroéclairée par LED'),('proto-moteur-grave','Moteur reconditionné et gravé'),('proto-moteur','Ensemble moteur et commande'),('proto-usinage','Usinage d’une pièce sur mesure'),('proto-chassis-levage','Châssis de levage')])}</div>
</div></section>'''
service_page('innovation-prototypage', 'Innovation & prototypage', 'Innovation, prototypes et pièces sur mesure',
    'Outils de levage, lift de projecteur, enseignes lumineuses, pièces refaites en impression 3D : nous concevons ce qui n’existe pas encore.',
    'enseigne-led-gravee', inn, pre='Innovation / prototypage', title='Innovation & prototypage · Pièces sur mesure, impression 3D · Massonelec',
    desc='Outils de levage, lifts motorisés, enseignes lumineuses et pièces introuvables refaites en impression 3D : Massonelec conçoit des solutions sur mesure.')

# =====================================================================
# IMAGERIE MÉDICALE
# =====================================================================
med = phero('<span>Secteur médical</span>', 'Électricité pour l’imagerie médicale et la santé',
    'Scanner et mammographe au Centre d’imagerie d’Aigle : des équipements de pointe qui exigent une alimentation calculée, réalisée et contrôlée sans la moindre approximation.',
    video='assets/video/scanner-loop.mp4', card_title='Un projet médical ?', card_text='Cabinet, centre d’imagerie, laboratoire : parlons-en.', service='Imagerie médicale / santé')
med += f'''<section class="sec"><div class="wrap med" style="grid-template-columns:1.15fr .85fr">
  <div data-reveal><div class="med-video"><video id="medvid2" controls playsinline preload="none" poster="assets/img/scanner-poster.webp"><source src="assets/video/scanner-imagerie-aigle.mp4" type="video/mp4"></video></div>
  <p style="font-size:.86rem;color:var(--steel);margin-top:10px">Mise en place et raccordement d’un scanner d’imagerie médicale au Centre d’imagerie d’Aigle : premiers tours de l’anneau, capots ouverts.</p></div>
  <div data-reveal><span class="kicker">{ic('scan')} Référence</span><h2>Scanner, Centre d’imagerie d’Aigle</h2>
    <p class="lead">Mise en place et raccordement d’un scanner d’imagerie médicale.</p>
    <p>Un équipement de cette puissance doit être alimenté selon des exigences strictes. Nous avons réalisé son raccordement et participé à sa mise en service aux côtés des équipes techniques.</p>
    {ticks(['Alimentation dédiée du scanner','Raccordement et essais','Contrôle et rapport de conformité'])}
  </div>
</div></section>
<section class="sec sec-alt"><div class="wrap split rev">
  <div data-reveal><span class="kicker">{ic('pulse')} Référence</span><h2>Mammographe, en collaboration avec GE</h2>
    <p class="lead">Calcul, réalisation et installation de l’alimentation du mammographe au Centre d’imagerie d’Aigle, en collaboration avec GE.</p>
    <p>De l’étude au raccordement, en passant par l’installation du transformateur dédié, nous avons travaillé avec le constructeur pour respecter ses spécifications.</p>
    {ticks(['Calcul de l’alimentation','Transformateur dédié','Installation et raccordement'])}
  </div>
  <div class="split-img" data-reveal>{img('imagerie-transformateur','Transformateur dédié au mammographe du Centre d’imagerie d’Aigle')}<span class="cap">Transformateur dédié · mammographe</span></div>
</div></section>
<section class="sec sec-dark"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('hospital')} Ce que nous apportons</span><h2>Ce qu’exige une installation médicale</h2><p>Un environnement de soins ne s’improvise pas : continuité de service, précision et coordination.</p></div></div>
  {feats([('plan','Étude & calcul','Dimensionnement de l’alimentation selon les spécifications du fabricant de l’équipement.'),('users','Coordination','Travail conjoint avec le constructeur, l’exploitant et les autres corps de métier.'),('bolt','Alimentations dédiées','Lignes et transformateurs dédiés aux équipements lourds.'),('calendar','Planification','Interventions organisées pour limiter l’impact sur l’activité médicale.'),('shield','Contrôle OIBT','Mesures, contrôle et rapport de conformité remis à l’exploitant.'),('wrench','Dépannage 24/7','Une équipe joignable à toute heure en cas de panne.')])}
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('building')} Pour qui</span><h2>Établissements de santé</h2></div></div>
  {feats([('scan','Centres d’imagerie','Scanner, mammographe, équipements de radiologie.'),('hospital','Cabinets médicaux & dentaires','Installation, rénovation, équipements spécifiques.'),('building','Établissements & résidences','Tableaux, éclairage, courant faible, dépannage.')])}
</div></section>'''
med += form_section('Votre projet médical', 'Décrivez l’équipement et le local : nous revenons vers vous pour une visite et une étude.', subject='Demande – secteur médical', pre='Imagerie médicale / santé', idp='med') + cta_band()
add('imagerie-medicale', 'Imagerie médicale · Raccordement scanner & mammographe · Massonelec Aigle',
    'Massonelec a raccordé un scanner et installé l’alimentation d’un mammographe (avec GE) au Centre d’imagerie d’Aigle. Électricité pour la santé : étude, calcul, installation, contrôle OIBT.', med)

# =====================================================================
# RÉALISATIONS
# =====================================================================
def case(anchor, tags, title, text, media, bullets):
    return f'''<article class="case" id="{anchor}" data-reveal><div class="case-media">{media}</div><div class="case-body"><div class="case-meta">{''.join(f'<span>{t}</span>' for t in tags)}</div><h3>{title}</h3><p>{text}</p>{ticks(bullets)}</div></article>'''
cases = ''.join([
    case('scanner', ['Santé', 'Centre d’imagerie d’Aigle'], 'Scanner d’imagerie médicale', 'Mise en place et raccordement d’un scanner d’imagerie médicale au Centre d’imagerie d’Aigle.',
         '<video controls playsinline preload="none" poster="assets/img/scanner-poster.webp"><source src="assets/video/scanner-imagerie-aigle.mp4" type="video/mp4"></video>', ['Raccordement du scanner', 'Essais et mise en service']),
    case('mammographe', ['Santé', 'En collaboration avec GE'], 'Mammographe', 'Calcul, réalisation et installation du mammographe au Centre d’imagerie d’Aigle en collaboration avec GE.',
         img('imagerie-transformateur', 'Transformateur du mammographe'), ['Calcul de l’alimentation', 'Transformateur dédié', 'Installation']),
    case('station-pompage', ['Infrastructure', 'Eau potable'], 'Station de pompage d’eau potable', 'Installation électrique pour une station de pompage d’eau potable, réalisée par notre société.',
         img('station-pompage-armoire', 'Armoire de commande de la station de pompage'), ['Armoires de commande et de puissance', 'Raccordement des pompes', 'Câblage et distribution']),
    case('generatrice', ['Énergie', 'Site militaire'], 'Génératrice 88 kVA, fort militaire', 'Mise en place et raccordement d’une génératrice de 88 kVA dans un fort militaire.',
         img('generatrice-88kva', 'Génératrice 88 kVA'), ['Mise en place', 'Raccordement', 'Mise en service']),
    case('jardin', ['Particulier', 'Extérieur'], 'Éclairage d’ambiance de jardin', 'Réalisation d’un éclairage d’ambiance pour le jardin d’un particulier : arbres, cheminement et four extérieur mis en lumière.',
         img('eclairage-jardin', 'Éclairage de jardin'), ['Projecteurs et balises', 'Mise en valeur des arbres', 'Installation extérieure étanche']),
    case('miroir', ['Particulier', 'Sur mesure'], 'Miroir à éclairage périphérique', 'Fabrication et réalisation d’un miroir avec éclairage périphérique au travers du miroir.',
         img('miroir-retroeclaire', 'Miroir rétroéclairé'), ['Fabrication sur mesure', 'Éclairage LED périphérique', 'Pose et raccordement']),
])
G = [  # name, cats, caption
    ('scanner-poster', 'sante', 'Scanner · Centre d’imagerie d’Aigle (vidéo)', 'assets/video/scanner-imagerie-aigle.mp4'),
    ('imagerie-transformateur', 'sante industrie', 'Transformateur dédié au mammographe · Aigle', None),
    ('station-pompage-armoire', 'industrie tableaux', 'Armoire de commande · station de pompage d’eau potable', None),
    ('station-pompage-salle', 'industrie', 'Salle des pompes · station d’eau potable', None),
    ('generatrice-88kva', 'industrie', 'Génératrice 88 kVA · fort militaire', None),
    ('armoire-industrielle', 'industrie tableaux', 'Armoire électrique industrielle', None),
    ('moteur-industriel', 'industrie', 'Raccordement d’un moteur industriel', None),
    ('cablage-armoire', 'tableaux industrie', 'Câblage d’une armoire de distribution', None),
    ('coffrets-comptage', 'tableaux habitat', 'Coffrets de comptage d’immeuble', None),
    ('tableau-domotique', 'tableaux eclairage', 'Tableau avec modules domotiques', None),
    ('tableau-distribution', 'tableaux habitat', 'Tableau de distribution', None),
    ('baie-reseau', 'reseaux', 'Baie de brassage réseau et téléphonie', None),
    ('plafond-led-violet', 'eclairage', 'Plafond lumineux LED couleur', None),
    ('plafond-led-blanc', 'eclairage habitat', 'Gorges lumineuses LED, séjour rénové', None),
    ('plafond-led-chantier', 'eclairage', 'Gorge lumineuse en phase de chantier', None),
    ('salon-eclairage', 'eclairage habitat', 'Salon à éclairage encastré', None),
    ('bibliotheque-led', 'eclairage', 'Bibliothèque à LED intégrées', None),
    ('vitrine-led', 'eclairage', 'Vitrine à étagères lumineuses', None),
    ('eclairage-jardin', 'eclairage', 'Éclairage d’ambiance de jardin', None),
    ('projecteur-led', 'eclairage', 'Projecteur LED extérieur', None),
    ('miroir-retroeclaire', 'habitat eclairage', 'Miroir à éclairage périphérique', None),
    ('miroir-led', 'habitat eclairage', 'Miroir LED de salle de bain', None),
    ('salle-de-bain-baignoire', 'habitat', 'Salle de bain rénovée', None),
    ('salle-de-bain-wc', 'habitat', 'WC avec éclairage encastré', None),
    ('plan-electrique-1', 'etudes', 'Plan d’installation électrique', None),
    ('plan-electrique-2', 'etudes', 'Plan d’étage complet', None),
    ('schema-unifilaire', 'etudes', 'Schéma de principe de distribution', None),
    ('enseigne-led-gravee', 'prototypage eclairage', 'Enseigne en verre gravé rétroéclairée', None),
    ('proto-lift-projecteur', 'prototypage', 'Lift motorisé pour vidéoprojecteur', None),
    ('proto-chassis-levage', 'prototypage', 'Châssis de levage sur mesure', None),
    ('proto-moteur-grave', 'prototypage', 'Moteur reconditionné et gravé', None),
    ('proto-moteur', 'prototypage', 'Ensemble moteur et commande', None),
    ('proto-usinage', 'prototypage', 'Usinage d’une pièce', None),
    ('piece-impression-3d', 'prototypage', 'Pièce redessinée en CAO pour impression 3D', None),
]
FIL = [('all', 'Tout'), ('sante', 'Santé'), ('industrie', 'Industrie & énergie'), ('tableaux', 'Tableaux'), ('eclairage', 'Éclairage & LED'), ('habitat', 'Habitat'), ('reseaux', 'Réseaux'), ('etudes', 'Études & plans'), ('prototypage', 'Prototypage')]
gal = ''.join(
    f'<button class="gal-item" data-cat="{c}" data-full="assets/img/{n}.webp" data-caption="{esc(cap)}"' + (f' data-video="{v}"' if v else '') + f'>{img(n, cap, sizes="(max-width:720px) 100vw, 33vw")}' + (f'<span class="vid-badge">{ic("play")} Vidéo</span>' if v else '') + f'<figcaption>{cap}</figcaption></button>'
    for n, c, cap, v in G)
rea = phero('<span>Réalisations</span>', 'Nos réalisations', 'Santé, infrastructures, énergie, habitat, éclairage et prototypes : un aperçu concret du savoir-faire Massonelec, photographié sur nos chantiers.', image='station-pompage-salle')
rea += f'''<section class="sec"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('award')} Références</span><h2>Chantiers marquants</h2></div></div>
  {cases}
</div></section>
<section class="sec sec-alt" id="galerie"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('camera')} Galerie</span><h2>Photos de chantier</h2><p>{len(G)} photos et vidéos de nos interventions. Cliquez pour agrandir.</p></div></div>
  <div class="filters" role="group" aria-label="Filtrer la galerie">{''.join(f'<button type="button" data-filter="{k}" aria-pressed="{str(k=="all").lower()}">{l}</button>' for k, l in FIL)}</div>
  <div class="gal">{gal}</div>
</div></section>
<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Agrandissement"><button class="lb-x" aria-label="Fermer">{ic('x')}</button><button class="lb-p" aria-label="Précédent">{ic('chevl')}</button><figure></figure><button class="lb-n" aria-label="Suivant">{ic('chevr')}</button></div>'''
rea += form_section('Un projet similaire ?', subject='Demande depuis la page Réalisations', idp='rea') + cta_band()
add('realisations', 'Réalisations · Scanner, station de pompage, génératrice 88 kVA · Massonelec',
    'Références Massonelec Sàrl : scanner et mammographe au Centre d’imagerie d’Aigle, station de pompage d’eau potable, génératrice 88 kVA, éclairage, domotique, prototypes.', rea)

# lightbox on pages that use data-lb galleries
for s in ('domotique-eclairage', 'etudes-conception', 'innovation-prototypage'):
    PAGES[s] = PAGES[s].replace('</main>', f'<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Agrandissement"><button class="lb-x" aria-label="Fermer">{ic("x")}</button><button class="lb-p" aria-label="Précédent">{ic("chevl")}</button><figure></figure><button class="lb-n" aria-label="Suivant">{ic("chevr")}</button></div></main>')

# =====================================================================
# DEVIS (wizard)
# =====================================================================
def choice(name, value, icon, title, small, typ='radio'):
    return f'<label class="choice"><input type="{typ}" name="{name}" value="{esc(value)}" data-label="{ "Client" if name=="client" else "Prestations" if name=="prestations" else "Type de bien" }"><span>{ic(icon)}<b>{title}</b><small>{small}</small></span></label>'
dv = phero('<span>Demande de devis</span>', 'Demande de devis gratuit', 'Quatre étapes, deux minutes. Nous revenons vers vous pour fixer un rendez-vous et établir une offre détaillée, gratuite et sans engagement.', image='plan-electrique-2', card_title='Une urgence ?', card_text='Pour une panne, n’attendez pas le devis : appelez directement, 24 h/24.')
dv = dv.replace('href="#formulaire">Demander un devis', 'href="#wizard">Commencer')
dv = dv.replace(f'<a class="btn btn-primary" href="devis">{ic("doc")} Devis en ligne</a>', f'<a class="btn btn-primary" href="tel:{CO["tel"]}">{ic("phone")} Appeler le {CO["phone"]}</a>')
dv += f'''<section class="sec" id="formulaire"><div class="wrap">
<form class="form wizard js-form" id="wizard" data-subject="Demande de devis – site web">
  <div class="wz-progress" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <div class="wz-step"><p class="wz-title">1. Vous êtes…</p><p class="wz-sub">Pour adapter notre réponse à votre situation.</p>
    <div class="choice-grid" data-need>
      {choice('client','Particulier','home','Particulier','Maison, appartement, jardin')}
      {choice('client','Régie / PPE','building','Régie / PPE','Immeubles, copropriétés')}
      {choice('client','Entreprise / commerce','card','Entreprise / commerce','Bureaux, boutiques, ateliers')}
      {choice('client','Industrie / infrastructure','factory','Industrie / infrastructure','Production, pompage, énergie')}
      {choice('client','Établissement médical','hospital','Établissement médical','Imagerie, cabinets, laboratoires')}
      {choice('client','Collectivité','shield','Collectivité','Commune, site public ou militaire')}
    </div><p class="wz-miss form-note" hidden style="color:var(--red)">Merci de choisir une option.</p>
    <div class="wz-nav"><span></span><button type="button" class="btn btn-primary" data-next>Continuer {ic('arrow')}</button></div></div>
  <div class="wz-step"><p class="wz-title">2. Votre besoin</p><p class="wz-sub">Plusieurs choix possibles.</p>
    <div class="chips" data-need>{''.join(f'<label class="chip"><input type="checkbox" name="prestations" value="{esc(o)}" data-label="Prestations"><span>{o}</span></label>' for o in SVC_OPTS)}</div>
    <p class="wz-miss form-note" hidden style="color:var(--red)">Choisissez au moins une prestation.</p>
    <div class="wz-nav"><button type="button" class="btn btn-ghost" data-prev>Retour</button><button type="button" class="btn btn-primary" data-next>Continuer {ic('arrow')}</button></div></div>
  <div class="wz-step"><p class="wz-title">3. Votre projet</p><p class="wz-sub">Quelques détails pour préparer notre visite.</p>
    <div class="form-grid">
      <div class="f"><label for="w-type">Type de travaux</label><select id="w-type" name="travaux" data-label="Type de travaux"><option value="">Choisir…</option><option>Construction neuve</option><option>Rénovation / transformation</option><option>Extension / ajout</option><option>Dépannage / réparation</option><option>Contrôle / mise en conformité OIBT</option><option>Étude seulement</option></select></div>
      <div class="f"><label for="w-delai">Délai souhaité</label><select id="w-delai" name="delai" data-label="Délai"><option value="">Choisir…</option><option>Urgent</option><option>Dans le mois</option><option>Dans les 3 mois</option><option>Plus tard / à planifier</option></select></div>
      <div class="f"><label for="w-lieu">Localité / NPA</label><input id="w-lieu" name="lieu" data-label="Localité" required placeholder="Ex. 1860 Aigle"></div>
      <div class="f"><label for="w-surf">Surface ou taille <span class="opt">(facultatif)</span></label><input id="w-surf" name="surface" data-label="Surface / taille" placeholder="Ex. villa 180 m², 3 étages…"></div>
      <div class="f full"><label for="w-desc">Description</label><textarea id="w-desc" name="description" data-label="Description" required placeholder="Décrivez vos besoins : nombre de pièces, équipements, contraintes…"></textarea></div>
    </div>
    <div class="wz-nav"><button type="button" class="btn btn-ghost" data-prev>Retour</button><button type="button" class="btn btn-primary" data-next>Continuer {ic('arrow')}</button></div></div>
  <div class="wz-step"><p class="wz-title">4. Vos coordonnées</p><p class="wz-sub">Pour vous recontacter et fixer un rendez-vous.</p>
    <div class="form-grid">
      <div class="f"><label for="w-n">Nom et prénom</label><input id="w-n" name="nom" data-label="Nom" autocomplete="name" required></div>
      <div class="f"><label for="w-s">Entreprise <span class="opt">(facultatif)</span></label><input id="w-s" name="societe" data-label="Entreprise" autocomplete="organization"></div>
      <div class="f"><label for="w-t">Téléphone</label><input id="w-t" name="tel" type="tel" data-label="Téléphone" autocomplete="tel" required></div>
      <div class="f"><label for="w-e">E-mail <span class="opt">(facultatif)</span></label><input id="w-e" name="email" type="email" data-label="E-mail" autocomplete="email"></div>
      <div class="f full"><label for="w-dispo">Disponibilités pour une visite <span class="opt">(facultatif)</span></label><input id="w-dispo" name="dispo" data-label="Disponibilités" placeholder="Ex. matins en semaine"></div>
    </div>
    <p class="wz-title" style="font-size:1rem;margin-top:22px">Récapitulatif</p><div class="wz-recap"></div>
    <div class="wz-nav"><button type="button" class="btn btn-ghost" data-prev>Retour</button>
      <span style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-ghost" type="submit" value="mail">{ic('mail')} Par e-mail</button><button class="btn btn-primary" type="submit" value="wa">{ic('wa')} Envoyer via WhatsApp</button></span></div>
    <p class="form-ok" role="status">Merci ! Votre demande est pré-remplie : il ne reste qu’à l’envoyer. Nous vous recontactons rapidement.</p>
    <p class="form-note">Gratuit et sans engagement. Vos données servent uniquement à traiter votre demande (<a href="confidentialite">confidentialité</a>).</p>
  </div>
</form></div></section>
<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('flag')} Et ensuite ?</span><h2>Après votre demande</h2></div></div>
  <div class="steps"><div class="step"><div class="step-n">1</div><h3>Prise de contact</h3><p>Nous vous rappelons pour préciser votre besoin.</p></div><div class="step"><div class="step-n">2</div><h3>Visite sur place</h3><p>Étude de votre bâtiment et de vos attentes.</p></div><div class="step"><div class="step-n">3</div><h3>Devis détaillé</h3><p>Offre gratuite et sans engagement.</p></div><div class="step"><div class="step-n">4</div><h3>Planification</h3><p>Réalisation aux dates convenues.</p></div></div>
</div></section>''' + cta_band()
add('devis', 'Devis gratuit électricien · Aigle & Chablais · Massonelec Sàrl',
    'Demandez un devis gratuit et sans engagement pour vos travaux électriques : installation, rénovation, courant fort, domotique, imagerie médicale. Aigle et Chablais vaudois.', dv)

# =====================================================================
# CONTACT
# =====================================================================
ct = phero('<span>Contact</span>', 'Contact & accès', 'Un appel, un message WhatsApp ou le formulaire : choisissez le canal qui vous convient. Pour une urgence, appelez directement, 24 h/24.', image='tableau-domotique', card_title='Urgence électrique ?', card_text='Nous intervenons 24 h/24 et 7 j/7.')
ct += f'''<section class="sec"><div class="wrap form-wrap">
  <div>
    <span class="kicker">{ic('pin')} Coordonnées</span><h2>Massonelec Sàrl</h2>
    <p class="lead">{CO['street']}<br>{CO['npa']} {CO['city']} (VD), Suisse</p>
    {contact_list()}
    <h3 style="margin-top:34px">Heures d’ouverture du bureau <span style="font-size:.85rem;font-weight:500;color:var(--steel)">· <i class="dot-live" style="display:inline-block"></i> <span data-open-status></span></span></h3>
    <table class="hours"><tbody>
      <tr data-day="1,2,3,4"><td>Lundi – jeudi</td><td>7:30 – 12:00 · 13:30 – 17:00</td></tr>
      <tr data-day="5"><td>Vendredi</td><td>7:30 – 12:00 · 13:30 – 16:00</td></tr>
      <tr data-day="6,0"><td>Samedi – dimanche</td><td>Fermé · urgences 24/7</td></tr>
    </tbody></table>
    <h3 style="margin-top:34px">Retrouvez-nous</h3>
    <div class="socials" style="gap:10px">
      <a class="btn btn-ghost btn-sm" style="width:auto;height:auto" href="{CO['fb']}" target="_blank" rel="noopener">{ic('fb')} Facebook</a>
      <a class="btn btn-ghost btn-sm" style="width:auto;height:auto" href="{CO['li']}" target="_blank" rel="noopener">{ic('li')} LinkedIn</a>
      <a class="btn btn-ghost btn-sm" style="width:auto;height:auto" href="{CO['gmaps']}" target="_blank" rel="noopener">{ic('g')} Google</a>
      <a class="btn btn-ghost btn-sm" style="width:auto;height:auto" href="{CO['lc']}" target="_blank" rel="noopener">{ic('lc')} local.ch</a>
    </div>
  </div>
  <div id="formulaire"><span class="kicker">{ic('msg')} Écrivez-nous</span><h2>Envoyer un message</h2>{full_form('Message depuis la page Contact', idp='ct')}</div>
</div></section>
<section class="sec sec-alt"><div class="wrap">
  <div class="sec-head"><div class="intro"><span class="kicker">{ic('pin')} Plan d’accès</span><h2>Nous trouver à Aigle</h2></div><a class="btn btn-ghost" href="{CO['route']}" target="_blank" rel="noopener">Itinéraire {ic('arrow')}</a></div>
  <div class="map"><div class="map-load"><div><p style="max-width:460px;color:var(--steel)">La carte est fournie par Google Maps. Elle ne se charge qu’à votre demande.</p><button class="btn btn-primary" type="button" data-map>{ic('pin')} Afficher la carte</button></div></div></div>
</div></section>
<section class="sec" id="zone"><div class="wrap zone">
  <div><span class="kicker">{ic('globe')} Zone d’intervention</span><h2>Du Chablais vaudois jusqu’à Bulle</h2><p class="lead">Aigle, Yvorne, Ollon, Bex, Villeneuve, Roche, Leysin, Villars, Les Diablerets, Montreux, Vevey, Château-d’Œx, Châtel-St-Denis, Bulle et environs.</p>
  <div class="rev-sum" style="margin-top:20px"><span class="src">{ic('g')} Votre avis compte</span><p style="margin:0 0 12px;color:var(--steel)">Satisfait de notre intervention ? Un avis sur Google aide d’autres clients à nous trouver.</p><a class="btn btn-ghost" href="{CO['gwrite']}" target="_blank" rel="noopener">{ic('star')} Laisser un avis Google</a></div></div>
  <div class="zone-canvas" id="zone3d" data-src="assets/js/zone3d.js?v={V}"><div class="labels"></div><div class="zone-fallback">Carte 3D de la zone d’intervention</div><span class="zone-legend">Carte 3D · Lac Léman, Rhône et localités desservies</span></div>
</div></section>''' + cta_band()
add('contact', 'Contact · Massonelec Sàrl, Chemin de la Perrolaz 2, Aigle · 079 350 55 19',
    'Contactez Massonelec Sàrl à Aigle : 079 350 55 19 (urgences 24/7), WhatsApp, e-mail picpus_ch@hotmail.com. Chemin de la Perrolaz 2, 1860 Aigle. Horaires et plan d’accès.', ct)

# =====================================================================
# LEGAL
# =====================================================================
def legal(slug, h1, content, title, desc):
    b = f'''<section class="phero"><div class="wrap" style="grid-template-columns:1fr;padding:56px 0 60px"><div><nav class="crumbs"><a href="./">Accueil</a><span aria-hidden="true">/</span><span>{h1}</span></nav><h1>{h1}</h1></div></div></section>
<section class="sec"><div class="wrap" style="max-width:860px">{content}</div></section>''' + cta_band()
    add(slug, title, desc, b)
legal('mentions-legales', 'Mentions légales', f'''
<h2>Éditeur du site</h2><p><strong>{CO['name']}</strong><br>{CO['street']}<br>{CO['npa']} {CO['city']}, Suisse<br>Téléphone : <a href="tel:{CO['tel']}">{CO['phone']}</a><br>E-mail : <a href="mailto:{CO['email']}">{CO['email']}</a><br>Numéro IDE : {CO['ide']}<br>Gérant : {CO['boss']}</p>
<h2>Responsabilité</h2><p>Les informations publiées sur ce site sont fournies avec le plus grand soin. {CO['name']} ne peut toutefois garantir leur exactitude, leur exhaustivité ni leur actualité. Toute responsabilité pour des dommages résultant de l’utilisation de ce site est exclue dans la mesure permise par la loi.</p>
<h2>Liens externes</h2><p>Ce site contient des liens vers des sites tiers (Google, local.ch, Facebook, LinkedIn, WhatsApp). Leur contenu relève de la seule responsabilité de leurs exploitants.</p>
<h2>Droits d’auteur</h2><p>Les textes, photographies, vidéos et plans présentés sur ce site sont la propriété de {CO['name']}, sauf mention contraire. Toute reproduction requiert un accord écrit préalable.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>''',
    'Mentions légales · Massonelec Sàrl', 'Mentions légales du site de Massonelec Sàrl, installateur-électricien à Aigle.')
legal('confidentialite', 'Protection des données', f'''
<p>{CO['name']} attache une grande importance à la protection de vos données personnelles et respecte la loi fédérale sur la protection des données (nLPD).</p>
<h2>Responsable du traitement</h2><p>{CO['name']}, {CO['street']}, {CO['npa']} {CO['city']} · <a href="mailto:{CO['email']}">{CO['email']}</a></p>
<h2>Formulaires de contact et de devis</h2><p>Les formulaires de ce site ne stockent aucune donnée sur un serveur. Lorsque vous les validez, votre message est pré-rempli dans WhatsApp ou dans votre logiciel de messagerie, et vous décidez vous-même de l’envoyer. Les données transmises (nom, téléphone, e-mail, description du projet) servent uniquement à traiter votre demande et ne sont jamais revendues.</p>
<h2>WhatsApp</h2><p>Si vous choisissez de nous écrire via WhatsApp, le service est fourni par WhatsApp Ireland Ltd. et soumis à sa propre politique de confidentialité.</p>
<h2>Google Maps</h2><p>La carte de la page Contact n’est chargée qu’après votre clic. Google peut alors collecter des données de connexion selon sa politique de confidentialité.</p>
<h2>Polices et cookies</h2><p>Ce site n’utilise ni cookies publicitaires ni outil de mesure d’audience. Les polices de caractères sont chargées depuis Google Fonts.</p>
<h2>Vos droits</h2><p>Vous pouvez à tout moment demander l’accès, la rectification ou la suppression de vos données en écrivant à <a href="mailto:{CO['email']}">{CO['email']}</a>.</p>''',
    'Protection des données · Massonelec Sàrl', 'Déclaration de protection des données de Massonelec Sàrl (nLPD).')

# 404
nf = f'''<section class="phero"><div class="wrap" style="grid-template-columns:1fr;padding:90px 0 100px"><div><h1>Page introuvable</h1><p class="lead">Le courant ne passe pas ici. Revenez à l’accueil ou contactez-nous directement.</p><div class="hero-ctas"><a class="btn btn-primary" href="./">Retour à l’accueil</a><a class="btn btn-light" href="tel:{CO['tel']}">{ic('phone')} {CO['phone']}</a></div></div></div></section>'''
PAGES['404'] = page('404', 'Page introuvable · Massonelec Sàrl', 'Page introuvable.', nf, base='/massonelec/')

# =====================================================================
for slug, h in PAGES.items():
    with open(os.path.join(OUT, f'{slug}.html'), 'w', encoding='utf-8') as f:
        f.write(h)
with open(os.path.join(OUT, 'assets', 'img', 'logo-m.svg'), 'w') as f:
    f.write(logo_m_svg())
open(os.path.join(OUT, '.nojekyll'), 'w').close()
print('built', len(PAGES), 'pages:', ', '.join(PAGES))
