# -*- coding: utf-8 -*-
import unittest

import morpion

class TestMorpion(unittest.TestCase):

    def test_nouveau_plateau_est_vide(self):
        # Arranger
        
        # Agir
        plateau = morpion.nouveau_plateau()
        
        # Vérifier (Assert)
        for ligne in plateau:
            for place in ligne:
                self.assertEqual(place, "")

    def test_jouer_mouvement_reussi_quand_la_place_est_libre(self):
        plateau = morpion.nouveau_plateau()
        
        ret = morpion.jouer_mouvement(plateau, "X", 1, 1)
        
        self.assertTrue(ret)
        self.assertEqual(plateau[1][1], "X")

    def test_jouer_mouvement_rate_quand_la_place_n_existe_pas(self):
        plateau = morpion.nouveau_plateau()
        
        ret = morpion.jouer_mouvement(plateau, "X", 42, 54)
        
        self.assertFalse(ret)



if __name__ == '__main__':
    unittest.main()

