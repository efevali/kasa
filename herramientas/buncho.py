# Avatar de Claude para los créditos: un 文鳥 (bunchō, «pájaro de las letras») en pixel art, 48x48,
# con hachimaki de estudiante y parado sobre un pincel. Uso: python3 buncho.py salida.png [escala]
import sys
from PIL import Image
N=48
C={'.':(228,234,238),'K':(31,42,68),'B':(120,132,146),'b':(96,108,124),'l':(150,162,174),
   'P':(214,196,200),'p':(190,172,178),'W':(251,253,252),'w':(222,228,232),
   'S':(232,132,138),'s':(196,96,106),'E':(214,88,92),'H':(251,253,252),'h':(206,214,220),'D':(184,57,43),
   'M':(201,164,106),'m':(166,128,76),'N':(31,42,68),'F':(232,160,164)}
g=[['.']*N for _ in range(N)]
def put(x,y,c):
    if 0<=x<N and 0<=y<N: g[y][x]=c
def el(cx,cy,rx,ry,c,cond=lambda x,y:True):
    for y in range(N):
        for x in range(N):
            if ((x-cx)/rx)**2+((y-cy)/ry)**2<=1 and cond(x,y): put(x,y,c)
# pincel (fude) horizontal: mango de bambú y punta de pelo negro a la derecha
for x in range(4,36):
    put(x,39,'M'); put(x,40,'m')
for x in (12,22):
    put(x,39,'m')
for x,y in [(36,39),(37,39),(38,39),(36,40),(37,40),(38,40),(39,40),(40,40)]: put(x,y,'N')
# cola negra, hacia atrás y abajo
for i in range(7):
    put(10-i,31+i//2,'K'); put(10-i,32+i//2,'K'); put(11-i,32+i//2,'K')
# cuerpo gris, panza rosada abajo
el(21,28,12,9,'B')
el(23,32,9,5,'P',lambda x,y:y>=30)
el(25,34,6,3,'p',lambda x,y:y>=35)
# ala, más oscura, con borde claro
el(17,26.5,9,5,'b')
for x in range(10,25): 
    if g[29][x]=='b': put(x,29,'l')
# cabeza negra
el(30,17,9,8.5,'K')
# mejilla blanca
el(30.5,20.5,6,3.8,'W')
el(28,22,3,1.6,'w',lambda x,y:y>=22)
# ojo: anillo rojo y punto negro, con brillo
for x,y in [(32,14),(33,14),(34,15),(34,16),(33,17),(32,17),(31,16),(31,15)]: put(x,y,'E')
put(32,15,'K'); put(33,15,'K'); put(32,16,'K'); put(33,16,'K'); put(33,15,'W')
# pico grueso rosado
for y in range(14,22):
    w=[0,3,5,6,6,5,4,2][y-14]
    for x in range(38,38+w): put(x,y,'S' if y<18 else 's')
# hachimaki: banda blanca en la frente, con el círculo rojo adelante y dos puntas atrás
for x in range(23,38):
    put(x,11,'H'); put(x,12,'H' if x>25 else 'h')
put(33,11,'D'); put(34,11,'D'); put(33,12,'D'); put(34,12,'D')
for x,y in [(22,11),(22,12),(21,11),(21,12)]: put(x,y,'h')          # el nudo
for x in range(15,22):                                              # punta de arriba
    d=1 if x<18 else 0
    put(x,9+d,'H'); put(x,10+d,'H')
for x in range(15,22):                                              # punta de abajo
    d=1 if x<18 else 0
    put(x,13+d,'H'); put(x,14+d,'H')
# patas
for x,y in [(22,37),(22,38),(26,37),(26,38),(21,38),(23,38),(25,38),(27,38)]: put(x,y,'F')
# contorno
borde=set()
for y in range(N):
    for x in range(N):
        if g[y][x]!='.':
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                X,Y=x+dx,y+dy
                if 0<=X<N and 0<=Y<N and g[Y][X]=='.': borde.add((X,Y))
for x,y in borde: put(x,y,'K')
img=Image.new('RGB',(N,N))
for y in range(N):
    for x in range(N): img.putpixel((x,y),C[g[y][x]])
s=int(sys.argv[2]) if len(sys.argv)>2 else 10
img.resize((N*s,N*s),Image.NEAREST).save(sys.argv[1])
