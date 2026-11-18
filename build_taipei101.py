import numpy as np, trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual import TextureVisuals
scene = trimesh.Scene(); n=[0]
def mat(c, rough=0.4, metal=0.2, emis=None):
    kw=dict(baseColorFactor=[*c,1.0], roughnessFactor=rough, metallicFactor=metal)
    if emis: kw['emissiveFactor']=emis
    return PBRMaterial(**kw)
def add(m, material):
    m.visual=TextureVisuals(material=material); n[0]+=1
    scene.add_geometry(m, node_name=f"n{n[0]}", geom_name=f"g{n[0]}")
def frustum(w0, w1, y0, y1, material, cx=0, cz=0):
    v=[]
    for w,y in ((w0,y0),(w1,y1)):
        h=w/2; v += [[cx-h,y,cz-h],[cx+h,y,cz-h],[cx+h,y,cz+h],[cx-h,y,cz+h]]
    f=[[0,1,2],[0,2,3],[4,6,5],[4,7,6]]
    for i in range(4):
        j=(i+1)%4; f += [[i,i+4,j+4],[i,j+4,j]]
    m=trimesh.Trimesh(vertices=np.array(v,float), faces=np.array(f), process=False); m.fix_normals()
    add(m, material)
def box(x0,z0,x1,z1,y0,y1,material):
    m=trimesh.creation.box(extents=[x1-x0,y1-y0,z1-z0]); m.apply_translation([(x0+x1)/2,(y0+y1)/2,(z0+z1)/2]); add(m,material)
def cyl(x,z,r,y0,y1,material,sections=48, axis='y'):
    m=trimesh.creation.cylinder(radius=r,height=y1-y0,sections=sections)
    m.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0])); m.apply_translation([x,(y0+y1)/2,z]); add(m,material)

G1=mat((0.20,0.52,0.50),0.25,0.4); G2=mat((0.14,0.40,0.40),0.25,0.4)
RIM=mat((0.70,0.78,0.78),0.35,0.8); SILVER=mat((0.80,0.83,0.85),0.3,0.9); GOLD=mat((0.85,0.70,0.30),0.3,0.9)
BASE=mat((0.06,0.08,0.11),0.4,0.6); GLOW=mat((0.1,0.9,1.0),0.4,0,[0.1,0.9,1.0]); STONE=mat((0.62,0.64,0.64),0.7,0.1)
TIP=mat((1.0,0.95,0.7),0.4,0,[1.0,0.9,0.5])

# stage
cyl(0,0,82,-6,-2,BASE,64); cyl(0,0,78,-2,-1.2,GLOW,64); cyl(0,0,75.5,-1.6,-0.8,BASE,64)
# podium (mall) and plinth
box(-34,-34,34,34,0,6,STONE); box(34,-30,74,30,0,26,STONE); box(36,-28,72,28,26,29,RIM)
# lower section: floors 1-25, tapering inward
def slices(w0,w1,y0,y1,k):
    for i in range(k):
        a,b=i/k,(i+1)/k
        frustum(w0+(w1-w0)*a, w0+(w1-w0)*b, y0+(y1-y0)*a, y0+(y1-y0)*b, G1 if i%2==0 else G2)
slices(62,49,6,112,13)
frustum(51,51,112,115,RIM)
# coin medallions on each face
for ang in range(4):
    m=trimesh.creation.cylinder(radius=7,height=1.6,sections=40); m.apply_translation([0,0,26.2])
    m.apply_transform(trimesh.transformations.rotation_matrix(np.radians(-14),[1,0,0]))   # lean with the taper
    m.apply_translation([0,104,0]); m.apply_transform(trimesh.transformations.rotation_matrix(ang*np.pi/2,[0,1,0])); add(m,GOLD)
# eight modules of eight floors, each flaring outward
y=115; MH=33.5
for k in range(8):
    slices(44,53,y,y+MH-2,8)
    frustum(55,55,y+MH-2,y+MH,RIM)
    for sx in (-1,1):
        for sz in (-1,1): box(sx*27.5-1.6, sz*27.5-1.6, sx*27.5+1.6, sz*27.5+1.6, y+MH-5, y+MH+2.5, SILVER)   # corner ornaments
    y+=MH
# crown
slices(40,36,y,y+22,3); frustum(38,38,y+22,y+24,RIM); y+=24
slices(27,23,y,y+18,2); frustum(25,25,y+18,y+20,RIM); y+=20
slices(16,13,y,y+18,2); y+=18
cyl(0,0,5,y,y+10,SILVER,24); y+=10
# spire to 508 m
for r,h in ((3.2,18),(2.2,18),(1.3,16)):
    cyl(0,0,r,y,y+h,SILVER,16); y+=h
cyl(0,0,0.7,y,508,TIP,12)
scene.export('taipei101.glb')
print(n[0], scene.bounds.round(1).tolist())
