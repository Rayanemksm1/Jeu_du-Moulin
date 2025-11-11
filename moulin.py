'MEKSEM RAYANE' 'NAWMI ABDALLAH SINANE'
from partie_calcul import *
from partie_graph import *
taille=800  #taille fenetre
d=taille*0.01  #diametre des cercles qui represenent les points
jeu=[' ']*24   #liste des points
color1='Red'   #couleurs des pions du joueur 1
color2='Blue'  #couleurs des pions du joueur 2 
joueur1=[]     #liste des points joué par le joueur 1
joueur2=[]     #liste des points joué par le joueur 2
t=0
mode,case,saut=definir_mode(taille)
cree_fenetre(taille,taille)
jouer=True
while jouer:
    if t%2==0:
        color=color1
        coloradverse=color2
        joueur=joueur1
        adverse=joueur2
    else:
        color=color2
        coloradverse=color1
        joueur=joueur2
        adverse=joueur1
    if t<mode*2:
        plateau(jeu,mode,case,d)
        placer(jeu,mode,case,joueur,color,d)
        if coup_gagnant(joueur,mode):
            supp(jeu,mode,case,adverse,coloradverse,d)
            if mode==3:
                break
    else:
        if fin_de_partie(jeu,mode,joueur,adverse):
            break
        deplacer(jeu,mode,case,joueur,color,saut,d)
        if coup_gagnant(joueur,mode):
            supp(jeu,mode,case,adverse,coloradverse,d)
    t+=1
couleur_gagnante(taille,jeu,mode,joueur,adverse,color,coloradverse)
attend_fermeture()