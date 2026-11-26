/* Massonelec — assistant virtuel (base de connaissances locale, aucune donnée envoyée) */
(function () {
  'use strict';
  var TEL = '+41793505519', TELH = '079 350 55 19', WA = 'https://wa.me/41793505519', MAIL = 'picpus_ch@hotmail.com';
  var A = {
    call: { label: 'Appeler ' + TELH, href: 'tel:' + TEL },
    wa: { label: 'WhatsApp', href: WA, ext: 1 },
    devis: { label: 'Demander un devis', href: 'devis' },
    mail: { label: 'E-mail', href: 'mailto:' + MAIL },
    route: { label: 'Itinéraire', href: 'https://www.google.com/maps/dir/?api=1&destination=Massonelec+S%C3%A0rl%2C+Chemin+de+la+Perrolaz+2%2C+1860+Aigle', ext: 1 },
    rea: { label: 'Voir les réalisations', href: 'realisations' },
    med: { label: 'Secteur médical', href: 'imagerie-medicale' },
    ent: { label: 'L’entreprise', href: 'entreprise' },
    pres: { label: 'Toutes les prestations', href: 'prestations' },
    contact: { label: 'Page contact', href: 'contact' }
  };
  function page(slug, label) { return { label: label, href: slug }; }

  /* ---------- knowledge base ---------- */
  // k: keywords (accent-free, lowercase; multi-word allowed), w: weight bonus
  var KB = [
    { id: 'urgence', w: 3, k: ['urgence', 'urgent', 'panne', 'plus de courant', 'plus d electricite', 'coupure', 'court circuit', 'disjoncteur', 'disjoncte', 'saute', 'differentiel', 'fi saute', 'odeur de brule', 'brule', 'etincelle', 'fumee', 'depannage', 'depanner', 'noir', '24h', '24 24', '7j'],
      a: function () { return '<b>Pour une urgence, appelez directement le ' + TELH + '.</b> Massonelec assure le dépannage électrique <b>24 h/24 et 7 j/7</b>, pour les particuliers, les professionnels et l’industrie, dans tout le Chablais vaudois jusqu’à Bulle.<br><br>En attendant : ne touchez pas un câble ou un appareil endommagé ou humide, et coupez l’alimentation au tableau seulement si vous pouvez le faire sans risque.'; },
      act: ['call', 'wa'], f: ['Quelle est votre zone d’intervention ?', 'Le devis est-il gratuit ?'] },
    { id: 'qui', k: ['qui etes vous', 'qui est massonelec', 'presentation', 'presente', 'massonelec', 'entreprise', 'societe', 'votre boite', 'a propos', 'activite', 'metier'],
      a: 'Massonelec Sàrl est une entreprise d’électricité générale basée à <b>Aigle (VD)</b>, fondée en <b>2000</b> par un installateur-électricien titulaire d’un CFC. Elle intervient sur tous les types d’installations, de la <b>basse tension au courant fort</b>, pour les particuliers, les entreprises, les industries et les <b>centres médicaux</b>, du Chablais vaudois jusqu’à Bulle. Son credo : un seul interlocuteur, de l’étude au dépannage.',
      act: ['ent', 'pres'], f: ['Qui dirige l’entreprise ?', 'Quels sont vos services ?', 'Montrez-moi des réalisations'] },
    { id: 'patron', k: ['patron', 'gerant', 'directeur', 'fondateur', 'fonde', 'proprietaire', 'chef', 'jean gilbert', 'jean', 'masson', 'qui dirige', 'responsable'],
      a: 'L’entreprise est dirigée par <b>Jean-Gilbert Masson</b>, gérant de Massonelec Sàrl. Installateur-électricien de profession, titulaire d’un <b>CFC</b>, il a toujours souhaité être indépendant et a créé sa société à Aigle en 2000. On le retrouve aussi sur LinkedIn, où il partage les chantiers de l’entreprise.',
      act: [{ label: 'Profil LinkedIn', href: 'https://www.linkedin.com/in/jean-gilbert-masson-139bb510b/', ext: 1 }, 'ent'], f: ['Depuis quand existe l’entreprise ?', 'Quelles sont vos qualifications ?'] },
    { id: 'histoire', k: ['depuis quand', 'annee', 'fondation', 'creation', 'cree', 'histoire', 'experience', 'combien d annees', 'anciennete', 'registre', 'ide', 'rc', 'numero ide', 'sarl', 'legal', 'raison sociale'],
      a: 'Massonelec a été créée à <b>Aigle en 2000</b>. La société est inscrite au registre du commerce vaudois sous la raison sociale <b>Massonelec Sàrl</b> (IDE <b>CHE-101.430.065</b>), avec pour but les activités relatives aux <b>installations électriques et téléphoniques</b>. Siège : Chemin de la Perrolaz 2, 1860 Aigle.',
      act: ['ent'], f: ['Qui dirige l’entreprise ?', 'Quels sont vos services ?'] },
    { id: 'qualif', k: ['qualification', 'diplome', 'cfc', 'certifie', 'certification', 'agree', 'autorisation', 'concession', 'norme', 'normes', 'oibt', 'conforme', 'conformite', 'securite', 'rapport de securite', 'rasi', 'controle', 'controles', 'garantie'],
      a: 'Les installations Massonelec sont <b>contrôlées conformément à l’art. 31 de l’OIBT</b> (ordonnance fédérale sur les installations électriques à basse tension). Un <b>rapport de conformité</b> est remis au propriétaire et au fournisseur d’énergie. Le gérant est installateur-électricien titulaire d’un <b>CFC</b>. Nous réalisons aussi les <b>retouches OIBT</b> après un contrôle périodique ou une vente.',
      act: [page('electricite-generale', 'Électricité générale'), 'devis'], f: ['Faites-vous des rénovations ?', 'Le devis est-il gratuit ?'] },
    { id: 'services', k: ['services', 'prestations', 'faites quoi', 'vous faites', 'que faites vous', 'faites vous', 'que proposez', 'proposez vous', 'faites vous quoi', 'domaines', 'competences', 'liste', 'offre', 'catalogue'],
      a: 'Nos métiers :<ul><li><b>Électricité générale</b> : neuf, rénovation, contrôles OIBT</li><li><b>Courant fort & industrie</b> : armoires, force motrice, génératrices, stations de pompage</li><li><b>Courant faible</b> : téléphonie, réseau informatique, interphones et caméras IP, alarmes, détection incendie</li><li><b>Domotique & éclairage LED</b></li><li><b>Dépannage 24/7</b></li><li><b>Études & plans</b> : relevés, schémas, calculs</li><li><b>Imagerie médicale</b> : scanner, mammographe</li><li><b>Innovation</b> : outils sur mesure, impression 3D</li></ul>',
      act: ['pres', 'devis'], f: ['Travaillez-vous dans le médical ?', 'Faites-vous de la domotique ?', 'Montrez-moi des réalisations'] },
    { id: 'medical', w: 1, k: ['medical', 'medicale', 'imagerie', 'scanner', 'irm', 'radiologie', 'radio', 'mammographe', 'mammographie', 'hopital', 'clinique', 'cabinet', 'dentiste', 'dentaire', 'medecin', 'sante', 'ge', 'general electric', 'centre d imagerie', 'laboratoire', 'ems'],
      a: 'Oui, c’est l’une de nos spécialités. Au <b>Centre d’imagerie d’Aigle</b>, Massonelec a réalisé :<ul><li>la <b>mise en place et le raccordement d’un scanner</b> d’imagerie médicale (la vidéo de la mise en service est sur le site) ;</li><li>le <b>calcul, la réalisation et l’installation de l’alimentation du mammographe</b>, avec un transformateur dédié, <b>en collaboration avec GE</b>.</li></ul>Nous intervenons aussi pour les cabinets médicaux et dentaires et les établissements de santé : étude, alimentations dédiées, coordination avec le fabricant, contrôle OIBT.',
      act: ['med', 'devis'], f: ['Faites-vous des calculs de dimensionnement ?', 'Quelles autres réalisations ?'] },
    { id: 'industrie', k: ['industrie', 'industriel', 'usine', 'courant fort', 'haute tension', 'force', 'moteur', 'machine', 'armoire', 'armoires', 'tableau industriel', 'production', 'infrastructure', 'pompage', 'eau potable', 'station', 'generatrice', 'groupe electrogene', 'secours', 'kva', 'militaire', 'fort', 'armee', 'commune', 'collectivite'],
      a: 'Côté <b>courant fort</b>, Massonelec équipe entreprises, industries et collectivités :<ul><li><b>Station de pompage d’eau potable</b> : installation électrique complète (armoires de commande et de puissance, raccordement des pompes) ;</li><li><b>Génératrice de 88 kVA dans un fort militaire</b> : mise en place et raccordement ;</li><li>armoires de distribution, câblage force, raccordement de moteurs, dépannage industriel 24/7.</li></ul>',
      act: [page('courant-fort-industrie', 'Courant fort & industrie'), 'rea'], f: ['Intervenez-vous en urgence ?', 'Quelle est votre zone ?'] },
    { id: 'faible', k: ['courant faible', 'telephone', 'telephonie', 'central telephonique', 'reseau', 'informatique', 'internet', 'wifi', 'wi fi', 'ethernet', 'prise reseau', 'baie', 'fibre', 'interphone', 'camera', 'cameras', 'video surveillance', 'videosurveillance', 'alarme', 'intrusion', 'incendie', 'detecteur', 'detection'],
      a: 'Oui. Pour le <b>courant faible</b>, nous installons et raccordons : téléphonie analogique et numérique, centraux et raccordements téléphoniques ; <b>réseau informatique</b> (câblage universel, prises réseau, baies de brassage) ; <b>interphones et caméras de sécurité IP</b> ; <b>alarmes</b>, détection d’intrusion et <b>détection d’incendie</b>.',
      act: [page('courant-faible-reseaux', 'Courant faible & réseaux'), 'devis'], f: ['Faites-vous de la domotique ?', 'Le devis est-il gratuit ?'] },
    { id: 'domotique', k: ['domotique', 'maison connectee', 'connecte', 'smart', 'automatisation', 'stores', 'volets', 'chauffage', 'programmable', 'commande a distance', 'scenario', 'knx'],
      a: 'Oui. Nous mettons en place des installations de <b>domotique entièrement programmables</b> : éclairage, chauffage, stores, scénarios et <b>commande à distance</b>. Le site montre par exemple un tableau électrique équipé de modules domotiques réalisé par Massonelec.',
      act: [page('domotique-eclairage', 'Domotique & éclairage'), 'devis'], f: ['Et pour l’éclairage LED ?', 'Montrez-moi des réalisations'] },
    { id: 'eclairage', k: ['eclairage', 'lumiere', 'luminaire', 'led', 'leds', 'spot', 'spots', 'plafond', 'gorge lumineuse', 'jardin', 'exterieur', 'facade', 'miroir', 'salle de bain', 'vitrine', 'enseigne', 'ambiance', 'decoratif'],
      a: 'L’éclairage est un point fort : <b>gorges et plafonds lumineux LED</b>, LED couleur, encastrés, <b>miroirs à éclairage périphérique</b> fabriqués sur mesure, vitrines et bibliothèques rétroéclairées, <b>mise en lumière de jardins</b> (arbres, cheminements, four extérieur) et même une <b>enseigne en verre gravé</b> rétroéclairée.',
      act: [page('domotique-eclairage', 'Voir la galerie lumière'), 'devis'], f: ['Faites-vous de la domotique ?', 'Quelle est votre zone ?'] },
    { id: 'renovation', k: ['renovation', 'renover', 'refaire', 'ancienne installation', 'vieille installation', 'mise aux normes', 'mise en conformite', 'tableau electrique', 'changer le tableau', 'prise', 'prises', 'interrupteur', 'cuisine', 'construction', 'neuf', 'villa', 'maison', 'appartement', 'immeuble', 'regie', 'ppe', 'extension', 'transformation'],
      a: 'Oui, construction neuve comme rénovation. Après un <b>relevé sur place</b>, nous proposons la solution adaptée : remplacement du tableau, protections différentielles, reprise des circuits, rénovation complète, cuisines, salles de bain, éclairage, prises et installations extérieures. Les travaux se terminent par un <b>contrôle OIBT</b> et un rapport de conformité.',
      act: [page('electricite-generale', 'Électricité générale'), 'devis'], f: ['Le devis est-il gratuit ?', 'Combien de temps pour un rendez-vous ?'] },
    { id: 'etudes', k: ['plan', 'plans', 'etude', 'etudes', 'schema', 'unifilaire', 'calcul', 'calculs', 'dimensionnement', 'architecte', 'bureau technique', 'conception', 'releve'],
      a: 'Nous réalisons l’<b>étude complète</b> de votre installation : relevé de l’existant, <b>plans d’implantation</b>, <b>schémas unifilaires</b>, <b>calculs de dimensionnement</b> (sections, protections, puissances), coordination avec architectes et fabricants. C’est ainsi qu’a été calculée l’alimentation du mammographe du Centre d’imagerie d’Aigle.',
      act: [page('etudes-conception', 'Études & conception')], f: ['Travaillez-vous dans le médical ?', 'Le devis est-il gratuit ?'] },
    { id: 'innovation', k: ['innovation', 'invention', 'prototype', 'prototypes', 'sur mesure', 'impression 3d', 'imprimante 3d', '3d', 'piece', 'piece cassee', 'introuvable', 'engrenage', 'levage', 'lift', 'mobilite', 'handicap', 'outil', 'machine speciale', 'projecteur', 'cao'],
      a: 'Au-delà de l’électricité, Massonelec <b>conçoit des objets et des outils sur mesure</b> : outils de levage pour aider à la mobilité, <b>lift motorisé pour vidéoprojecteur</b>, enseignes lumineuses gravées, reconditionnement de moteurs. Et quand une <b>pièce cassée ne se fabrique plus</b>, nous la redessinons en CAO et la refaisons en <b>impression 3D</b>.',
      act: [page('innovation-prototypage', 'Innovation & prototypage')], f: ['Montrez-moi des réalisations', 'Comment vous contacter ?'] },
    { id: 'realisations', k: ['realisation', 'realisations', 'reference', 'references', 'chantier', 'chantiers', 'projet', 'projets', 'exemple', 'exemples', 'portfolio', 'photos', 'travaux realises'],
      a: 'Quelques références :<ul><li><b>Scanner</b> et <b>mammographe</b> (avec GE) au Centre d’imagerie d’Aigle</li><li><b>Station de pompage d’eau potable</b></li><li><b>Génératrice 88 kVA</b> dans un fort militaire</li><li>Mise en lumière d’un <b>jardin privé</b></li><li><b>Miroir à éclairage périphérique</b> sur mesure</li><li>Tableaux domotiques, coffrets de comptage, armoires industrielles, plafonds LED…</li></ul>La page Réalisations réunit plus de 30 photos et la vidéo du scanner.',
      act: ['rea', 'med'], f: ['Travaillez-vous dans le médical ?', 'Demander un devis'] },
    { id: 'zone', k: ['zone', 'region', 'secteur', 'ou intervenez', 'vous deplacez', 'deplacement', 'deplacer', 'jusqu ou', 'chablais', 'riviera', 'vaud', 'valais', 'gruyere', 'fribourg', 'aigle', 'yvorne', 'ollon', 'bex', 'villeneuve', 'roche', 'leysin', 'villars', 'diablerets', 'montreux', 'vevey', 'clarens', 'corbeyrier', 'gryon', 'chateau d oex', 'pays d enhaut', 'chatel', 'bulle', 'monthey', 'saint maurice', 'lausanne', 'geneve', 'sion', 'martigny', 'noville', 'rennaz', 'lavey'],
      a: function (q) {
        var far = ['lausanne', 'geneve', 'sion', 'martigny'], vs = ['monthey', 'saint maurice'];
        var extra = '';
        if (far.some(function (t) { return q.indexOf(t) > -1; })) extra = '<br><br>Pour une localité plus éloignée, le plus simple est de nous appeler : nous vous dirons rapidement si nous pouvons intervenir.';
        else if (vs.some(function (t) { return q.indexOf(t) > -1; })) extra = '<br><br>Pour le Chablais valaisan, appelez-nous pour vérifier la disponibilité.';
        return 'Depuis notre bureau d’<b>Aigle</b>, nous intervenons dans tout le <b>Chablais vaudois</b> (Yvorne, Ollon, Bex, Villeneuve, Roche, Leysin, Villars, Les Diablerets…), sur la <b>Riviera</b> (Montreux, Vevey), au Pays-d’Enhaut, en Veveyse et <b>jusqu’à Bulle</b>.' + extra;
      }, act: ['call', 'devis'], f: ['Intervenez-vous en urgence ?', 'Quels sont vos horaires ?'] },
    { id: 'horaires', k: ['horaire', 'horaires', 'heure', 'heures', 'ouvert', 'ouverts', 'ouverte', 'samedi', 'dimanche', 'week end', 'weekend', 'ferme', 'fermeture', 'ouverture', 'quand', 'disponible', 'disponibilite', 'joignable', 'aujourd hui', 'maintenant'],
      a: function () { return 'Le bureau est ouvert :<ul><li><b>lundi – jeudi</b> : 7:30–12:00 et 13:30–17:00</li><li><b>vendredi</b> : 7:30–12:00 et 13:30–16:00</li><li><b>week-end</b> : fermé</li></ul>' + (isOpen() ? '<b>Le bureau est ouvert en ce moment.</b>' : '<b>Le bureau est fermé en ce moment</b>, mais le dépannage reste assuré 24 h/24 au ' + TELH + '.'); },
      act: ['call', 'contact'], f: ['Où se trouve votre bureau ?', 'Intervenez-vous en urgence ?'] },
    { id: 'contact', k: ['contact', 'contacter', 'joindre', 'telephone', 'numero', 'appeler', 'mail', 'email', 'e mail', 'courriel', 'whatsapp', 'message', 'ecrire', 'rappeler', 'rappel'],
      a: 'Vous pouvez joindre Massonelec :<ul><li>par téléphone au <b>' + TELH + '</b> (urgences 24/7)</li><li>sur <b>WhatsApp</b> (photos bienvenues)</li><li>par e-mail : <b>' + MAIL + '</b></li><li>ou via le formulaire présent en bas de chaque page.</li></ul>',
      act: ['call', 'wa', 'mail'], f: ['Où se trouve votre bureau ?', 'Quels sont vos horaires ?'] },
    { id: 'adresse', k: ['adresse', 'ou etes vous', 'ou se trouve', 'situe', 'localisation', 'bureau', 'siege', 'local', 'venir', 'itineraire', 'plan d acces', 'perrolaz'],
      a: 'Notre bureau se trouve <b>Chemin de la Perrolaz 2, 1860 Aigle</b> (VD), au cœur du Chablais.',
      act: ['route', 'contact'], f: ['Quels sont vos horaires ?', 'Quelle est votre zone ?'] },
    { id: 'devis', w: 1.5, k: ['devis', 'prix', 'tarif', 'tarifs', 'combien coute', 'combien ca coute', 'cout', 'coute', 'combien', 'budget', 'estimation', 'gratuit', 'payant', 'offre de prix', 'chiffrer', 'cher'],
      a: 'Le <b>devis est gratuit et sans engagement</b>. Chaque installation étant différente, nous ne publions pas de prix forfaitaires : après un <b>rendez-vous sur place</b> pour comprendre vos besoins, nous établissons une offre détaillée. Le formulaire « Devis » prend environ deux minutes.',
      act: ['devis', 'call'], f: ['Combien de temps pour un rendez-vous ?', 'Quels moyens de paiement ?'] },
    { id: 'delai', k: ['delai', 'delais', 'rapidement', 'vite', 'combien de temps', 'rendez vous', 'rdv', 'quand pouvez', 'disponibilite', 'attente', 'planning'],
      a: 'Pour une <b>urgence</b>, nous intervenons 24 h/24 et 7 j/7 : appelez le ' + TELH + '. Pour un <b>projet</b>, nous fixons un rendez-vous sur place puis vous remettons un devis ; les délais de réalisation dépendent du chantier et sont convenus avec vous dans l’offre.',
      act: ['call', 'devis'], f: ['Le devis est-il gratuit ?', 'Intervenez-vous en urgence ?'] },
    { id: 'paiement', k: ['paiement', 'payer', 'carte', 'twint', 'facture', 'visa', 'mastercard', 'postfinance', 'maestro', 'american express', 'amex', 'cash', 'especes', 'acompte'],
      a: 'Moyens de paiement acceptés : <b>sur facture</b>, cartes <b>Visa, Mastercard, American Express</b>, <b>Maestro</b> et <b>PostFinance Card</b>. Pour un autre moyen (TWINT, par exemple), demandez-nous directement.',
      act: ['contact'], f: ['Le devis est-il gratuit ?'] },
    { id: 'langues', k: ['langue', 'langues', 'italien', 'italiano', 'parlez', 'anglais', 'english', 'allemand', 'deutsch', 'portugais', 'espagnol'],
      a: 'Vous pouvez nous joindre en <b>français</b> et en <b>italien</b>. <i>Parliamo anche italiano.</i>',
      act: ['call', 'wa'], f: ['Comment vous contacter ?'] },
    { id: 'avis', w: 1, k: ['avis clients', 'avis', 'note', 'notes', 'evaluation', 'evaluations', 'temoignage', 'temoignages', 'google', 'local ch', 'satisfait', 'fiable', 'serieux', 'confiance', 'recommande', 'reputation'],
      a: 'Massonelec est noté <b>5,0/5 sur Google</b> et <b>4,0/5 sur local.ch</b> (4 évaluations, dont deux avis intitulés « Électricien au top »). Si nous avons travaillé pour vous, un avis Google aide beaucoup !',
      act: [{ label: 'Avis Google', href: 'https://search.google.com/local/reviews?placeid=ChIJ_ZxNjNmXjkcRi_nlAPzc_Lw', ext: 1 }, { label: 'Laisser un avis', href: 'https://search.google.com/local/writereview?placeid=ChIJ_ZxNjNmXjkcRi_nlAPzc_Lw', ext: 1 }], f: ['Montrez-moi des réalisations'] },
    { id: 'reseaux', k: ['facebook', 'linkedin', 'instagram', 'reseaux sociaux', 'reseau social', 'social', 'site', 'local.ch'],
      a: 'Retrouvez Massonelec sur <b>Facebook</b>, sur le profil <b>LinkedIn</b> de Jean-Gilbert Masson (où il publie les chantiers), sur <b>Google</b> et sur <b>local.ch</b>. Les liens sont en bas de chaque page.',
      act: [{ label: 'Facebook', href: 'https://www.facebook.com/Massonelec', ext: 1 }, { label: 'LinkedIn', href: 'https://www.linkedin.com/in/jean-gilbert-masson-139bb510b/', ext: 1 }], f: ['Qui dirige l’entreprise ?'] },
    { id: 'nonlistes', k: ['solaire', 'photovoltaique', 'panneaux', 'pv', 'borne', 'recharge', 'voiture electrique', 'wallbox', 'pompe a chaleur', 'batterie', 'climatisation', 'clim', 'sanitaire', 'plomberie', 'chauffage electrique'],
      a: function (q) { return 'Je n’ai pas d’information publiée sur ce type de prestation (' + esc(pick(q, ['photovoltaique', 'solaire', 'borne', 'recharge', 'wallbox', 'pompe a chaleur', 'batterie', 'climatisation', 'plomberie', 'sanitaire']) || 'celle-ci') + ') dans les références de Massonelec. Le plus fiable est de poser la question directement : l’équipe vous dira si elle peut s’en charger ou vous orienter.'; },
      act: ['call', 'wa'], f: ['Quels sont vos services ?'] },
    { id: 'emploi', k: ['emploi', 'travail', 'job', 'poste', 'recrutement', 'recrutez', 'embauche', 'apprentissage', 'apprenti', 'stage', 'candidature', 'cv'],
      a: 'Pour une candidature, un apprentissage ou un stage, envoyez votre dossier par e-mail à <b>' + MAIL + '</b> ou appelez le ' + TELH + '. Je n’ai pas d’offre d’emploi publiée à vous communiquer.',
      act: ['mail', 'call'], f: ['Qui dirige l’entreprise ?'] },
    { id: 'bot', k: ['qui es tu', 'tu es qui', 'robot', 'bot', 'ia', 'intelligence artificielle', 'humain', 'chatgpt', 'assistant'],
      a: 'Je suis l’<b>assistant virtuel</b> de Massonelec. Je réponds instantanément aux questions générales sur l’entreprise, ses services, ses réalisations, sa zone et ses horaires. Pour un diagnostic ou un devis précis, l’équipe prend le relais par téléphone ou WhatsApp.',
      act: ['call', 'wa'], f: ['Quels sont vos services ?', 'Le devis est-il gratuit ?'] },
    { id: 'salut', k: ['bonjour', 'bonsoir', 'salut', 'hello', 'coucou', 'hey', 'buongiorno', 'ciao', 'hi'],
      a: function (q) { return (/(buongiorno|ciao)/.test(q) ? 'Buongiorno ! Parliamo anche italiano al ' + TELH + '. ' : 'Bonjour ! ') + 'Je suis l’assistant de Massonelec. Posez-moi une question sur l’entreprise, ses services, ses réalisations ou un dépannage.'; },
      act: [], f: ['Que fait Massonelec ?', 'Intervenez-vous en urgence ?', 'Le devis est-il gratuit ?'] },
    { id: 'merci', k: ['merci', 'super', 'parfait', 'genial', 'top', 'ok merci', 'grazie', 'thanks', 'au revoir', 'bonne journee'],
      a: 'Avec plaisir ! Si besoin, l’équipe est joignable au <b>' + TELH + '</b>. Bonne journée.',
      act: ['call', 'devis'], f: [] }
  ];
  var SYN = { electricien: 'electricite', electrique: 'electricite', courant: 'electricite', tarifs: 'tarif', photos: 'photo', irm: 'irm', tableaux: 'tableau' };

  /* ---------- NLP-lite ---------- */
  function norm(s) { return (' ' + String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[’'`´-]/g, ' ').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ') + ' '); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function pick(q, arr) { for (var i = 0; i < arr.length; i++) if (q.indexOf(' ' + arr[i]) > -1) return arr[i].replace('photovoltaique', 'photovoltaïque').replace('pompe a chaleur', 'pompe à chaleur'); return ''; }
  function stem(w) { return w.length > 4 ? w.replace(/(ements|ement|ations|ation|eurs|eur|ees|ee|es|s|x)$/, '') : w; }
  function score(q, e) {
    var s = 0, toks = q.trim().split(' ').map(stem);
    e.k.forEach(function (k) {
      if (k.indexOf(' ') > -1) { if (q.indexOf(' ' + k + ' ') > -1 || q.indexOf(' ' + k) > -1) s += 2 + k.split(' ').length; }
      else { var sk = stem(k); if (q.indexOf(' ' + k + ' ') > -1) s += 2; else if (sk.length > 3 && toks.some(function (t) { return t === sk || (t.length > 4 && (t.indexOf(sk) === 0 || sk.indexOf(t) === 0)); })) s += 1.2; }
    });
    return s ? s + (e.w || 0) : 0;
  }
  function isOpen() {
    try {
      var p = {}; new Intl.DateTimeFormat('fr-CH', { timeZone: 'Europe/Zurich', weekday: 'short', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
      var d = { 'lun.': 1, 'mar.': 2, 'mer.': 3, 'jeu.': 4, 'ven.': 5 }[p.weekday], m = (+p.hour) * 60 + (+p.minute);
      if (!d) return false; return (m >= 450 && m < 720) || (m >= 810 && m < (d === 5 ? 960 : 1020));
    } catch (e) { return false; }
  }
  function answer(text) {
    var q = norm(text); Object.keys(SYN).forEach(function (k) { q = q.replace(' ' + k + ' ', ' ' + k + ' ' + SYN[k] + ' '); });
    var ranked = KB.map(function (e) { return { e: e, s: score(q, e) }; }).filter(function (x) { return x.s > 0; }).sort(function (a, b) { return b.s - a.s; });
    // greetings only win if nothing else matched
    if (ranked.length > 1 && (ranked[0].e.id === 'salut' || ranked[0].e.id === 'merci')) ranked.shift();
    if (!ranked.length || ranked[0].s < 1.2) return { html: 'Je n’ai pas trouvé de réponse précise à cette question. Je peux vous parler des <b>services</b>, des <b>réalisations</b> (dont le médical), de la <b>zone d’intervention</b>, des <b>horaires</b> ou du <b>devis</b>. Pour toute question technique, l’équipe vous répond directement.', act: ['call', 'wa'], f: ['Que fait Massonelec ?', 'Quels sont vos services ?', 'Intervenez-vous en urgence ?'] };
    var e = ranked[0].e, html = typeof e.a === 'function' ? e.a(q) : e.a;
    var act = e.act, f = e.f;
    // add a short pointer to a strong second topic
    if (ranked[1] && ranked[1].s >= ranked[0].s * .8 && ranked[1].e.id !== 'salut' && ranked[1].e.id !== 'merci') {
      var e2 = ranked[1].e; html += '<br><br>' + (typeof e2.a === 'function' ? e2.a(q) : e2.a);
      act = act.concat(e2.act).filter(function (v, i, a) { return a.indexOf(v) === i; }).slice(0, 3);
    }
    return { html: html, act: act, f: f };
  }

  window.__aiAnswer = answer;

  /* ---------- UI ---------- */
  var root = document.getElementById('ai');
  if (!root) return;
  var log = root.querySelector('.ai-log'), form = root.querySelector('form'), input = root.querySelector('input'), chips = root.querySelector('.ai-chips'), launcher = document.querySelector('.ai-launch');
  var KEY = 'mx-ai-v1', hist = [];
  try { hist = JSON.parse(sessionStorage.getItem(KEY) || '[]'); } catch (e) {}

  function btns(list) {
    if (!list || !list.length) return '';
    return '<div class="ai-act">' + list.map(function (k) { var a = typeof k === 'string' ? A[k] : k; if (!a) return ''; return '<a href="' + a.href + '"' + (a.ext ? ' target="_blank" rel="noopener"' : '') + '>' + esc(a.label) + '</a>'; }).join('') + '</div>';
  }
  function add(who, html, extra, instant) {
    var el = document.createElement('div'); el.className = 'ai-m ' + who; log.appendChild(el);
    if (who === 'bot' && !instant && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
      el.innerHTML = '<div class="ai-b"></div>';
      var b = el.firstChild, tmp = document.createElement('div'); tmp.innerHTML = html;
      typeInto(b, tmp, function () { if (extra) el.insertAdjacentHTML('beforeend', extra); scroll(); });
    } else { el.innerHTML = '<div class="ai-b">' + html + '</div>' + (extra || ''); }
    scroll();
  }
  function typeInto(target, src, done) {
    // reveal word by word, preserving markup
    var nodes = [];
    (function walk(n, parent) { Array.prototype.slice.call(n.childNodes).forEach(function (c) {
      if (c.nodeType === 3) c.textContent.split(/(\s+)/).forEach(function (t) { if (t) nodes.push({ p: parent, t: t }); });
      else { var cl = c.cloneNode(false); nodes.push({ p: parent, el: cl }); walk(c, cl); }
    }); })(src, target);
    var i = 0;
    (function step() {
      var n = 0;
      while (i < nodes.length && n < 3) { var x = nodes[i++]; if (x.el) x.p.appendChild(x.el); else { x.p.appendChild(document.createTextNode(x.t)); n++; } }
      scroll();
      if (i < nodes.length) setTimeout(step, 28); else done();
    })();
  }
  function scroll() { log.scrollTop = log.scrollHeight; }
  function setChips(list) { chips.innerHTML = (list || []).map(function (t) { return '<button type="button">' + esc(t) + '</button>'; }).join(''); }
  function save() { try { sessionStorage.setItem(KEY, JSON.stringify(hist.slice(-30))); } catch (e) {} }
  function ask(text) {
    text = String(text).trim(); if (!text) return;
    add('me', esc(text)); hist.push({ w: 'me', t: text }); save();
    input.value = ''; setChips([]);
    var dots = document.createElement('div'); dots.className = 'ai-m bot'; dots.innerHTML = '<div class="ai-b ai-typing"><i></i><i></i><i></i></div>'; log.appendChild(dots); scroll();
    setTimeout(function () {
      dots.remove();
      var r = answer(text);
      add('bot', r.html, btns(r.act)); hist.push({ w: 'bot', h: r.html, x: btns(r.act) }); save();
      setChips(r.f);
    }, 520 + Math.random() * 380);
  }
  form.addEventListener('submit', function (e) { e.preventDefault(); ask(input.value); });
  chips.addEventListener('click', function (e) { var b = e.target.closest('button'); if (b) ask(b.textContent); });
  log.addEventListener('click', function (e) { var b = e.target.closest('.ai-sugg button'); if (b) ask(b.textContent); });

  function open() {
    root.classList.add('open'); root.setAttribute('aria-hidden', 'false'); if (launcher) launcher.setAttribute('aria-expanded', 'true');
    document.documentElement.classList.add('ai-open');
    if (window.__mx && window.__mx.lenis && innerWidth < 641) window.__mx.lenis.stop();
    if (!log.children.length) {
      if (hist.length) hist.forEach(function (m) { if (m.w === 'me') add('me', esc(m.t)); else add('bot', m.h, m.x, true); });
      else { add('bot', 'Bonjour ! Je suis l’<b>assistant de Massonelec</b>. Je connais l’entreprise, ses services, ses réalisations (scanner, mammographe, station de pompage…), sa zone et ses horaires. Que voulez-vous savoir ?', '', true); }
      setChips(['Que fait Massonelec ?', 'Intervenez-vous en urgence ?', 'Travaillez-vous dans le médical ?', 'Le devis est-il gratuit ?', 'Quelle est votre zone ?']);
    }
    setTimeout(function () { if (innerWidth > 640) input.focus(); }, 250);
  }
  function close() { root.classList.remove('open'); root.setAttribute('aria-hidden', 'true'); if (launcher) launcher.setAttribute('aria-expanded', 'false'); document.documentElement.classList.remove('ai-open'); if (window.__mx && window.__mx.lenis) window.__mx.lenis.start(); }
  document.querySelectorAll('[data-ai]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); root.classList.contains('open') ? close() : open(); }); });
  root.querySelector('.ai-x').addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('open')) close(); });

  /* ---------- gentle nudge after 30 s (once per visit, never intrusive) ---------- */
  (function nudge() {
    var NK = 'mx-ai-nudge', DELAY = 30000, SHOW = 12000;
    try { if (sessionStorage.getItem(NK) || sessionStorage.getItem(KEY)) return; } catch (e) {}
    if (!launcher) return;
    var bubble = document.createElement('div');
    bubble.className = 'ai-nudge'; bubble.setAttribute('role', 'status');
    bubble.innerHTML = '<button type="button" class="ai-nudge-msg">Besoin d’aide ? Je réponds à vos questions sur Massonelec.</button><button type="button" class="ai-nudge-x" aria-label="Masquer">×</button>';
    document.body.appendChild(bubble);
    var shown = false, hideT = 0, waited = 0, lastTick = Date.now(), lastInput = 0;
    ['keydown', 'input'].forEach(function (ev) { document.addEventListener(ev, function () { lastInput = Date.now(); }, true); });
    function done() { try { sessionStorage.setItem(NK, '1'); } catch (e) {} }
    function hide() { bubble.classList.remove('on'); clearTimeout(hideT); }
    function busy() {
      var a = document.activeElement, tag = a && a.tagName;
      return document.hidden || root.classList.contains('open') || document.body.classList.contains('menu-open') ||
        (document.getElementById('lightbox') && document.getElementById('lightbox').classList.contains('open')) ||
        (document.querySelector('.wa-panel') && document.querySelector('.wa-panel').classList.contains('open')) ||
        tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || Date.now() - lastInput < 4000;
    }
    var iv = setInterval(function () {
      var now = Date.now(), dt = now - lastTick; lastTick = now;
      if (!document.hidden) waited += dt;            // only count time the page is actually visible
      if (waited < DELAY || shown || busy()) return;
      shown = true; clearInterval(iv); done();
      bubble.classList.add('on');
      hideT = setTimeout(hide, SHOW);
    }, 1000);
    bubble.querySelector('.ai-nudge-msg').addEventListener('click', function () { hide(); open(); });
    bubble.querySelector('.ai-nudge-x').addEventListener('click', hide);
    launcher.addEventListener('click', function () { hide(); done(); clearInterval(iv); });
    window.addEventListener('scroll', function () { if (bubble.classList.contains('on') && Date.now() - lastTick > 0) { /* keep */ } }, { passive: true });
  })();
  window.__ai = { ask: ask, open: open, answer: answer };
})();
