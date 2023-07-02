# class Plateau:
#    def __init__(self):
#        self.mon_plateau = [3*[""] for _ in range(3)]
#    def get_place(lignr, colonne):
#    
#    def jouer_mouvement(self, joueur, ligne, colonne):
#        
#plateau = Plateau()
#plateau.jouer_mouvement(joueur, sdfsdf)

import sys

def nouveau_plateau():
    plateau=[3*[" "] for _ in range(3)]
    return plateau

def afficher(plateau):
    for i in range(3):
        for j in range(3):
            sys.stdout.write(plateau[i][j])
        sys.stdout.write("\n")

def demander_mouvement(joueur):
    print("Entrez les coordonée à jouer pour le joueur", joueur)
    entrees = input("Coord: ")
    c = entrees.split()
    return int(c[0]), int(c[1])
    

def jouer_mouvement(plateau, joueur, ligne, colonne):
    if ligne >= 0 and ligne < 3 and \
        colonne >= 0 and colonne < 3 and \
        plateau[ligne][colonne] == " ":
        plateau[ligne][colonne] = joueur
        return True
    return False

def partie_finie(plateau):
    for i in range(3):
        for j in range(3):
            if plateau[i][j]!= " ":
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
            if plateau[i][j]==" ":
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
    joueurs = ["X", "Y"]
    while gagnant is None:
       afficher(plateau)

       mouvement_valide = False
       while not mouvement_valide:
           ligne, colonne = demander_mouvement(joueurs[joueur])
           mouvement_valide = jouer_mouvement(plateau, joueurs[joueur], ligne, colonne)
           if not mouvement_valide:
               print("Inpossible de jouer",ligne,colonne)

       gagnant = partie_finie(plateau)
       joueur = (joueur + 1) % 2

    print("La partie est terminée et",gagnant,"a gagné")  

if __name__ == '__main__':
    main()
    