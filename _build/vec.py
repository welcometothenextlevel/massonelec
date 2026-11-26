import numpy as np, potrace
from PIL import Image, ImageFilter
def trace(mask,scale,turd=12):
    bm=potrace.Bitmap(mask); pl=bm.trace(turdsize=turd,alphamax=1.0,opticurve=True)
    d=[]
    for curve in pl:
        pts=[curve.start_point]+[sg.end_point for sg in curve.segments]
        xs_=[p.x for p in pts]; ys_=[p.y for p in pts]
        if max(xs_)-min(xs_)>mask.shape[1]*0.97 and max(ys_)-min(ys_)>mask.shape[0]*0.9: continue
        s=curve.start_point; parts=[f"M{s.x/scale:.1f} {s.y/scale:.1f}"]
        for seg in curve.segments:
            if seg.is_corner: parts.append(f"L{seg.c.x/scale:.1f} {seg.c.y/scale:.1f}L{seg.end_point.x/scale:.1f} {seg.end_point.y/scale:.1f}")
            else: parts.append(f"C{seg.c1.x/scale:.1f} {seg.c1.y/scale:.1f} {seg.c2.x/scale:.1f} {seg.c2.y/scale:.1f} {seg.end_point.x/scale:.1f} {seg.end_point.y/scale:.1f}")
        d.append(''.join(parts)+'Z')
    return ''.join(d)
def load(p,sc):
    im=Image.open(p).convert('RGB'); im=im.resize((im.width*sc,im.height*sc),Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    return np.asarray(im).astype(int), im.size
sc=3
a,(W,H)=load('logo_m.jpg',sc); r,g,b=a[...,0],a[...,1],a[...,2]
blue=(r<90)&(b>170)&(g>110)&(b-r>110)
grey=(abs(r-b)<30)&(abs(r-g)<30)&(r<200)&(r>40)
bl=trace(blue,sc); gr=trace(grey,sc,30)
open('m.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W//sc} {H//sc}"><path fill="#1BA3D9" fill-rule="evenodd" d="{bl}"/><path fill="#8A9099" fill-rule="evenodd" d="{gr}"/></svg>')
a,(W,H)=load('logo_word.jpg',sc); r,g,b=a[...,0],a[...,1],a[...,2]
blue=(b-r>90)&(b>150)
grey=(abs(r-b)<35)&(abs(r-g)<35)&(r<190)
# split grey: swoosh vs "Sarl" text (x > 560 in source)
xs=np.arange(W)[None,:].repeat(H,0)
sw=grey&(xs<555*sc); sarl=grey&(xs>=555*sc)
open('word.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W//sc} {H//sc}"><path fill="#1BA3D9" fill-rule="evenodd" d="{trace(blue,sc)}"/><path fill="#5d636b" fill-rule="evenodd" d="{trace(sw,sc,20)}"/><path fill="#1d2228" fill-rule="evenodd" d="{trace(sarl,sc,6)}"/></svg>')
print('done')
