'MEKSEM RAYANE' 'NAWMI ABDALLAH SINANE'
from fltk import *
from partie_calcul import *
def plateau3(case):  #dessine le plateau et renvoie la liste des coordonnées des points
    point=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    rectangle(0,0,case*4,case*4,remplissage=colorrec,epaisseur=ep)
    rectangle(case,case,case*3,case*3,epaisseur=ep,couleur=colorcercle,remplissage=colorrec)
    ligne(case,case,case*3,case*3,couleur=colorcercle,epaisseur=ep)
    ligne(case,case*3,case*3,case,couleur=colorcercle,epaisseur=ep)
    ligne(case,case*2,case*3,case*2,couleur=colorcercle,epaisseur=ep)
    ligne(case*2,case,case*2,case*3,couleur=colorcercle,epaisseur=ep)
    return point
def plateau6(case):  #dessine le plateau et renvoie la liste des coordonnées des points
    point=[(0,0),(0,2),(0,4),(1,1),(1,2),(1,3),(2,0),(2,1),
           (2,3),(2,4),(3,1),(3,2),(3,3),(4,0),(4,2),(4,4)]
    rectangle(0,0,case*6,case*6,remplissage=colorrec,epaisseur=ep)
    rectangle(case,case,case*5,case*5,epaisseur=ep,couleur=colorcercle,remplissage=colorrec)
    rectangle(case*2,case*2,case*4,case*4,epaisseur=ep,couleur=colorcercle,remplissage=colorrec)
    ligne(case*3,case,case*3,case*2,couleur=colorcercle,epaisseur=ep)
    ligne(case*3,case,case*3,case*2,couleur=colorcercle,epaisseur=ep)
    ligne(case,case*3,case*2,case*3,couleur=colorcercle,epaisseur=ep)
    ligne(case*3,case*5,case*3,case*4,couleur=colorcercle,epaisseur=ep)
    ligne(case*4,case*3,case*5,case*3,couleur=colorcercle,epaisseur=ep)
    return point
def plateau9_12(mode,case):  #dessine le plateau et renvoie la liste des coordonnées des points
    point=[(0,0),(0,3),(0,6),
           (1,1),(1,3),(1,5),
           (2,2),(2,3),(2,4),
           (3,0),(3,1),(3,2),
           (3,4),(3,5),(3,6),
           (4,2),(4,3),(4,4),
           (5,1),(5,3),(5,5),
           (6,0),(6,3),(6,6)]
    rectangle(0,0,case*8,case*8,remplissage=colorrec)
    rectangle(case,case,case*7,case*7,epaisseur=9,couleur=colorcercle,remplissage=colorrec)
    rectangle(case*2,case*2,case*6,case*6,epaisseur=9,couleur=colorcercle,remplissage=colorrec)
    rectangle(case*3,case*3,case*5,case*5,epaisseur=9,couleur=colorcercle,remplissage=colorrec)
    ligne(case,case*4,case*3,case*4,couleur=colorcercle,epaisseur=9)
    ligne(case*4,case*5,case*4,case*  7,couleur=colorcercle,epaisseur=9)
    ligne(case*5,case*4,case*7,case*4,couleur=colorcercle,epaisseur=9)
    ligne(case*4,case,case*4,case*3,couleur=colorcercle,epaisseur=9)
    if mode==12:
        ligne(case,case,case*3,case*3,couleur=colorcercle,epaisseur=ep)
        ligne(case*7,case*7,case*5,case*5,couleur=colorcercle,epaisseur=ep)
        ligne(case,case*7,case*3,case*5,couleur=colorcercle,epaisseur=ep)
        ligne(case*7,case,case*5,case*3,couleur=colorcercle,epaisseur=ep)
    return point
def plateau(jeu,mode,case,d):
    if mode==3:
        point=plateau3(case)
    if mode==6:
        point=plateau6(case)
    if mode in [9,12]:
        point=plateau9_12(mode,case)
    for i in range(len(point)):  #dessine les points en fonction de leurs états
        x=case+(case*point[i][1])
        y=case+(case*point[i][0])
        if jeu[i]==' ':
            cercle(x,y,d,epaisseur=2,remplissage=colorcercle)
        elif jeu[i]=='select':
            cercle(x,y,d*3,epaisseur=2)
        else:
            cercle(x,y,d*3,epaisseur=2,remplissage=jeu[i])
def pixel(x,y,case,d): #transforme les coordos du clic gauche en case du plateau
    r=d/case
    i,j=(y-case)/case,(x-case)/case
    if  r<i%1<1-r or r<j%1<1-r:
        return None,None
    return int(round(i,0)),int(round(j,0))
def point(x,y,mode,case,d): #transorme la case en point 
    if mode==3:
        point=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    if mode in [9,12]:
        point=[(0,0),(0,3),(0,6),(1,1),(1,3),(1,5),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),
           (3,4),(3,5),(3,6),(4,2),(4,3),(4,4),(5,1),(5,3),(5,5),(6,0),(6,3),(6,6)]
    if mode==6:
        point=[(0,0),(0,2),(0,4),(1,1),(1,2),(1,3),(2,0),(2,1),
           (2,3),(2,4),(3,1),(3,2),(3,3),(4,0),(4,2),(4,4)]
    a,b=pixel(x,y,case,d)
    for i in range(len(point)):
        if (a,b)==point[i]:
            return i
    return None
def placer(jeu,mode,case,joueur,color,d): #fonction qui place les pions
    texte(0,0,'Tour au '+color+' de plaçer un pion',police='Courier')
    x,y=attend_clic_gauche()
    i=point(x,y,mode,case,d)
    while i==None or jeu[i]!=' ': #verifie si le point existe et non joué
        x,y=attend_clic_gauche()
        i=point(x,y,mode,case,d)
    jeu[i]=color  #modifie l'etat de la liste jeu
    joueur.append(i) #ajoute le pion à la liste du joueur
    mise_a_jour()
    efface_tout()
    plateau(jeu,mode,case,d) #efface tout et redissine le plateau
def supp(jeu,mode,case,adverse,coloradverse,d):  #suprrime un pion adverse
    texte(0,0,'Choisir un pion '+coloradverse+' à supprimer',police='Courier')
    x,y=attend_clic_gauche()
    i=point(x,y,mode,case,d*3)
    while i==None or jeu[i]!=coloradverse or i in point_moulin(adverse,mode): #vérifie si le point existe, joué par l'adversaire et n'appartient pas à un moulin
        x,y=attend_clic_gauche()
        i=point(x,y,mode,case,d*3)
    jeu[i]=' '
    adverse.remove(i)
    mise_a_jour()
    efface_tout()
    plateau(jeu,mode,case,d)
def deplacer(jeu,mode,case,joueur,color,saut,d): #fonction qui deplace les pions
    texte(0,0,'tour au '+color+' de choisir un pion à deplacer',police='Courier')
    x,y=attend_clic_gauche()
    i=point(x,y,mode,case,d*3)
    if len(joueur)==3 and saut:
        while i==None or jeu[i]!=color: #verifie si le point existe et joué par le joueur
            x,y=attend_clic_gauche()
            i=point(x,y,mode,case,d*3)
    else:
        while i==None or jeu[i]!=color or pas_possible(jeu,mode,i): #verifie si le point existe,joué par le joueur et si un deplaçement est possible
            x,y=attend_clic_gauche()
            i=point(x,y,mode,case,d*3)
    jeu[i]='select'
    mise_a_jour()
    efface_tout()
    plateau(jeu,mode,case,d) #efface tout et redissine le plateau
    texte(0,0,'tour au '+color+' de choisir une case',police='Courier')
    a,b=attend_clic_gauche()
    j=point(a,b,mode,case,d)
    if len(joueur)>3 or not(saut):
        while j==None or jeu[j]!=' ' or not ( j in (voisine(i,mode))): #verifie si le point existe, pas joué et si les deux points sont adjacent
            x,y=attend_clic_gauche()
            j=point(x,y,mode,case,d)
    else:
        while j==None or jeu[j]!=' ': #verifie si le point existe, pas joué
            x,y=attend_clic_gauche()
            j=point(x,y,mode,case,d)
    jeu[i]=' '
    jeu[j]=color
    joueur.remove(i)
    joueur.append(j)
    mise_a_jour()
    efface_tout()
    plateau(jeu,mode,case,d) #efface tout et redissine le plateau
def deco_fin_partie(taille,color): #decoration à la fin de partie
    case=int(taille/6)
    for i in range(5,case*6,case//2):
        for j in range(5,case*6,case//2):
            cercle(i,j,taille*0.01,remplissage=color)
def couleur_gagnante(taille,jeu,mode,joueur,adverse,color,coloradverse): #annonce le vainceur à la fin de la partie
    if (mode==12 and len(joueur)+len(adverse)==24):
        deco_fin_partie(taille,'')
        texte(taille*0.4,taille*0.4,'Match Nul',taille=50,couleur='white',police='Courier')
    elif pas_de_coup(jeu,mode,joueur) or len(joueur)<3:
        deco_fin_partie(taille,coloradverse)
        texte(taille*0.4,taille*0.4,coloradverse+' a gagné',taille=40,couleur='white',police='Courier')
    if len(adverse)<3:
        deco_fin_partie(taille,color)
        texte(taille*0.4,taille*0.4,color+' a gagné',taille=40,couleur='white',police='Courier')
colorrec='grey'
colorcercle='black'
ep=5