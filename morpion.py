def nouveau_plateau():
    plateau=[3*[""] for _ in range(3)]
    return plateau

print(nouveau_plateau())

def demander_mouvement():
    for i in range(3):
        for j in range(3):
            if nouveau_plateau()[i][j]=="":
                ligne=i
                colonne=j
    return ligne, colonne

def jouer_mouvement(plateau, joueur, ligne, colonne):
    if plateau[ligne][colonne] != "":
        #on suppose que le joueur joue X
        if joueur=='X':
            plateau[ligne][colonne]='X'
            #on suppose que le joueur joue O
        elif joueur=='O':
                plateau[ligne][colonne]='O'
    return plateau

def partie_finie(plateau):
    for i in range(3):
        for j in range(3):
            if plateau[i][j]!= "":
                if plateau[i][i]=='X' or plateau[i][j]=='X' or plateau[j][i]=='X':                
                    return 'X'
                elif plateau[i][i]=='O' or plateau[i][j]=='O' or plateau[j][i]=='O':                
                    return 'O'
def score(plateau,joueur):
    if partie_finie(plateau)==joueur:
        return +10
    elif partie_finie(plateau)!=joueur:
        return -10
    else:
        return 0
    
def mvmts_possibles(plateau):
    Mvmt=[]
    for i in range(3):
        for j in range(3):
            if plateau[i][j]=="":
                Mvmt.append(plateau[i][j])
    return Mvmt

def MinMax(plateau,joueur):
    if partie_finie(plateau)==joueur :
        return score(plateau,joueur)
    else:
        Mvmt=mvmts_possibles(plateau)
        while Mvmt:
            plateau2=plateau[:]
            return MinMax(plateau2, joueur) 
        
def main():
    """logique du jeux"""
    plateau = nouveau_plateau()

    gagnant = None
    joueur = 0
    while gagnant is None:
       afficher(plateau)

       mouvement_valide = False
       while not mouvement_valid:
           ligne, colonne = demander_mouvement()
           mouvement_valid = jouer_mouvement(plateau, joueur, ligne, colonne)

       gagnant = partie_finie(plateau)

    print("La partie est terminée et",gagnant,"a gagné")  

if __name__ == '__main__':
    main()
