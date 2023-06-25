# Exercise: Jeu du Morpion

Le jeu du morpion se joue normalement sur papier sur une grille de 3x3 carreaux.
Deux joueurs placent chacun leur tour leur symbole (X ou O) sur une des cases libres de la grille.
Dès qu'un des deux joueurs arrive à aligner trois de ses symboles sur une ligne, une colonne, ou une diagonale, il a gagné la partie. Si la grille est remplie est que personne n'a gagné, c'est un match nul.

![exemple](image001.png)

Règles du jeu

- le jeu est terminé quand toutes les cases sont remplies
- le jeu est terminé si toutes les case d'une colonne ont le même symbole
- le jeu est terminé si toutes les case d'une ligne ont le même symbole
- le jeu est terminé si toutes les case d'une diagonale ont le même symbole
- un jeu ne peux pas poser son symbole sur une case déjà prise
- les joueurs jouent chacun leur tour jusqu'à ce que le jeu soit terminé


## Première partie: la logique de jeu

Objectif: implémenter le jeu de morpion:

- choisir une représentation d'un jeu de morpion (plateau 3x3, initialisé à vide " ", les symboles sont "X" et "O")
- une fonction prennant un plateau et determinant si le jeux est terminé
- une fonction pour jouer qui prends en entrée un plateau, et un mouvement (symbole + coordonnée) et renvoie si le coup est valide et modifie le plateau de jeu
- une fonction qui affiche un pleateu dans la console

Exemple d'affichage: 

```
   1 2 3
  +-+-+-+
A | | | |
B | | | |
C | | | |
  +-+-+-+
```


Pour facilier la communication voici un canevas (pas testé)

```
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
```

## Deuxième partie: jouons contre l'odrinateur

A partir de ce qui a été implémenté précédement, nous allons maintenant coder un opposant. Pour cela, nous allons utiliser un algorithme de MinMax. Pas besoin de connaitre la théorie, nous allons juste voir l'application.

Le MinMax consiste a essayer les différentes possibilité de coup suivants et d'en choisir un en fonction de ce que l'on souhaite (appeler score). Donc l'algorithmen va simuler toutes les possibilité et choisir celle qui lui permet de gagner.

![minmax]image003.png)

Implémentation:

1. Tout d'abord implmenter une fonction qu prends en paramètre un plateau terminé et un joueur et renvoie
   - +10 si le joueur gagne
   - -10 si l'opposant gagne
   - 0 si c'est un match nul
2. Ensuite faire une fonction qui retourne un liste de mouvement possible (la liste des emplacement libres)
3. Enfin faire un fonction qui revoie le minmax
   - si le jeux est terminé renvoie le score
   - sinon, pour chaque mouvemement possible, duplique le pleateau et applique le coup et appelle la fonction minmax dessus
     - si c'est le tour du joueur prends la plus grande valeur (la première si il y en a plusieurs)
     - si c'est le tour de l'opposant, prends la plus petite valeur (la première si il y en a plusieurs)

Tu peux noter que la fonction minmax est une fonction réccursive qui passe d'un joueur à l'autre jusq'à trouver le score final.

## Troisième partie: faire un joueur parfait

Si tu as envie.

