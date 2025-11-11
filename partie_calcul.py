'MEKSEM RAYANE' 'NAWMI ABDALLAH SINANE' 
def definir_mode(taille):
    mode=int(input('Notre jeu propose 4 variante, Veuillez choisir laquelle vous désirez jouer: 3-6-9-12'))
    while mode not in [3,6,9,12]:
        mode=int(input('Notre jeu propose 4 variante, Veuillez choisir laquelle vous désirez jouer: 3-6-9-12'))
    if mode==3:
        case=taille/4
    if mode==6:
        case=taille/6
    if mode in [9,12]:
        case=taille/8
    saut=str(input('Voulez-vous appliquer la phase 3? o/n'))
    while saut not in ['o','n']:
        saut=str(input('Voulez-vous appliquer la phase 3? o/n'))
    if saut=='o':
        saut=True
    else:
        saut=False
    return mode,case,saut
def coup_gagnant(joueur,mode): #fonction qui vérifie si un moulin est formé à chaque coup
    if mode==3:
        liste=[[0,1,2],[0,3,6],[6,7,8],[2,5,8],[0,4,8],[2,4,6],[1,4,7],[3,4,5]] #liste de combis de points qui forme un moulin 
    if mode==6:
        liste=[[0,1,2],[3,4,5],[10,11,12],[13,14,15],[0,6,13],[2,9,15],[3,7,10],[5,8,12]] #liste de combis de points qui forme un moulin
    if mode==9:
        liste=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],
               [0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]] #liste de combis de points qui forme un moulin
    if mode==12:
        liste=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],[0,9,21],[3,10,18],
           [6,11,15],[8,12,17],[5,13,20],[2,14,23],[0,3,6],[1,4,7],[2,5,8],[15,18,21],[16,19,22],[17,20,23]]  #liste de combis de points qui forme un moulin
    for i in range(len(liste)):
        if (liste[i][0] in joueur and liste[i][1] in joueur and liste[i][2] in joueur) and (joueur[len(joueur)-1] in liste[i]) :  #Verifie si le dernier coup de la liste des pions du joueur forme un moulin 
            return True
    return False
def point_moulin(joueur,mode): #fonction qui renvoie les pions que l'adverse ne peut pas supprimer
    if mode==3:
        liste=[[0,1,2],[0,3,6],[6,7,8],[2,5,8],[0,4,8],[2,4,6],[1,4,7],[3,4,5]] #liste de combis de pions qui forme un moulin
    if mode==6:
        liste=[[0,1,2],[3,4,5],[10,11,12],[13,14,15],[0,6,13],[2,9,15],[3,7,10],[5,8,12]] #liste de combis de pions qui forme un moulin
    if mode==9:
        liste=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23], #liste de combis de pions qui forme un moulin
               [0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]]
    if mode==12:
        liste=[[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],[0,9,21],[3,10,18], #liste de combis de pions qui forme un moulin
           [6,11,15],[8,12,17],[5,13,20],[2,14,23],[0,3,6],[1,4,7],[2,5,8],[15,18,21],[16,19,22],[17,20,23]]
    res=[]
    for i in range(len(liste)):
        if (liste[i][0] in joueur and liste[i][1] in joueur and liste[i][2] in joueur): #ajoute les cordos du moulin à res
            res.append(liste[i][0])
            res.append(liste[i][1])
            res.append(liste[i][2])
    for j in range(len(joueur)): #verifie si il reste un pion qui ne forme pas un moulin
        if joueur[j] not in res:
            return res  #renvoie la liste des points à ne pas supprimer
    return [] #renvoie une liste vide si tous les points forme à un moulin
def voisine(i,mode): #fonction qui renvoie les voisines d'une case
    if mode==3:
        voisine=[[1,3,4],[0,2,4],[1,4,5],[0,4,6],[0,1,2,3,5,6,7,8],[2,4,8],[3,4,7],[6,4,8],[4,5,7]] #liste des voisines de chaque case dont le numéro est l'indice de la liste voisine
    if mode==6:
        voisine=[[1,6],[0,2,4],[1,9],[4,7],[1,3,5],[4,8],[0,7,13],[3,6,10],[5,9,12], #liste des voisines de chaque case dont le numéro est l'indice de la liste voisine
                 [2,8,15],[7,11],[10,12,14],[8,11],[6,14],[13,11,15],[9,14]]
    if mode==9:
        voisine=[[1,9],[0,2,4],[1,14],[4,10],[1,3,5,7],[4,13],[7,11],[6,8,4],[7,12],[0,10,21],[3,9,11,18],[6,10,15],[8,13,17],#liste des voisines de chaque case dont le numéro est l'indice de la liste voisine
             [5,12,14,20],[2,13,23],[11,16],[15,17,19],[12,16],[10,19],[16,18,20,22],[13,19],[9,22],[19,21,23],[14,22]]
    if mode==12:
        voisine=[[1,3,9],[0,2,4],[1,5,14],[0,4,6,10],[1,3,5,7],[2,4,8,13],[3,7,11],[6,8,4],[5,7,12],[0,10,21],[3,9,11,18],[6,10,15],[8,13,17], #liste des voisines de chaque case dont le numéro est l'indice de la liste voisine
             [5,12,14,20],[2,13,23],[11,16,18],[15,17,19],[12,16,20],[10,15,19,21],[16,18,20,22],[13,17,19,23],[9,18,22],[19,21,23],[14,20,22]]
    return voisine[i]
def pas_possible(jeu,mode,i): #fonction qui vérifie si un deplaçement est possible pour le pion i 
    voisines=voisine(i,mode)
    for j in range(len(voisines)):
        if jeu[voisines[j]]==' ':   #verifie si une des voisines est vide
            return False
    return True
def pas_de_coup(jeu,mode,joueur): #fonction qui vérifie si un joueur est capable de se deplaçer
    for i in range(len(joueur)):
        if not(pas_possible(jeu,mode,joueur[i])): #verifie si un deplaçement est possible pour chaque pion du joueur
            return False
    return True
def fin_de_partie(jeu,mode,joueur,adverse): #détecte la fin de la partie
    if (mode==12 and len(joueur)+len(adverse)==24) or len(joueur)<3 or pas_de_coup(jeu,mode,joueur):
        return True
    return False
