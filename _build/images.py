from PIL import Image, ImageOps
import os, json
O='/Users/obss/~:projects/massonelec/_old/'
C='/Users/obss/~:projects/massonelec/_crops/'
OUT='/Users/obss/~:projects/massonelec/docs/assets/img/'
M = {
 # own photos (old site)
 'tableau-domotique': O+'img/20150514_112023_65.jpg',
 'tableau-distribution': O+'img/20150522_202351.jpg',
 'plafond-led-violet': O+'img/20141107_175345_598.jpg',
 'enseigne-led-gravee': O+'img/20150220_120053_631.jpg',
 'plafond-led-blanc': O+'img/20160330_163112-2880w.jpg',
 'bibliotheque-led': O+'img/20170504_161235.jpg',
 'vitrine-led': O+'img/20170511_155420_536.jpg',
 'coffrets-comptage': O+'img/20180526_144410_869_957.jpg',
 'armoire-industrielle': O+'img/20190223_015644_384_144.jpg',
 'salle-de-bain-baignoire': O+'img/20190502_155042_819.jpg',
 'salle-de-bain-wc': O+'img/20190502_155217_837_264.jpg',
 'miroir-retroeclaire': O+'img/MassonelecSrl42_393.jpg',
 'baie-reseau': O+'img/20130906_182223_166.jpg',
 'proto-usinage': O+'img/10_145.jpg',
 'proto-chassis-levage': O+'img/11_853.jpg',
 'proto-lift-projecteur': O+'img/7-2880w.jpg',
 'proto-moteur': O+'img/8_261.jpg',
 'proto-moteur-grave': O+'img/9_826.jpg',
 'plan-electrique-1': O+'img/2.jpg',
 'schema-unifilaire': O+'img/3.jpg',
 'plan-electrique-2': O+'img/4.jpg',
 'plan-electrique-3': O+'img/plan.jpg',
 # local.ch / Google Business Profile
 'salon-eclairage': O+'lc/2d9117b1_upload1.jpg',
 'moteur-industriel': O+'lc/66b30660_upload1.jpg',
 'miroir-led': O+'lc/83d1c5e9_002fded3ef674d56ae1798e62ccaae90.jpg',
 'plafond-led-chantier': O+'lc/9e2acd79_upload1.jpg',
 'cablage-armoire': O+'lc/c85d1b5b_83d80dd8ea3a4d238d2c63baada6edbc.jpg',
 'projecteur-led': O+'lc/ec297a57_upload1.jpg',
 # LinkedIn
 'station-pompage-armoire': C+'pompage_tableau.png',
 'station-pompage-salle': C+'pompage_salle.png',
 'imagerie-transformateur': C+'mammo_transfo.png',
 'generatrice-88kva': C+'generatrice.png',
 'eclairage-jardin': C+'jardin.png',
 'piece-impression-3d': C+'piece3d.png',
}
TRIM={'station-pompage-armoire':(10,4,10,4),'station-pompage-salle':(4,4,4,4),'imagerie-transformateur':(4,4,4,4)}
meta={}
for k,p in M.items():
    im=Image.open(p); im=ImageOps.exif_transpose(im).convert('RGB')
    if k in TRIM:
        l,t,r,b=TRIM[k]; im=im.crop((l,t,im.width-r,im.height-b))
    meta[k]=im.size
    for w,suf in ((1600,''),(720,'-sm')):
        x=im.copy()
        if x.width>w: x=x.resize((w,round(x.height*w/x.width)),Image.LANCZOS)
        x.save(OUT+k+suf+'.webp','WEBP',quality=80,method=6)
json.dump(meta,open('/Users/obss/~:projects/massonelec/_build/imgmeta.json','w'),indent=0)
print(len(meta))
