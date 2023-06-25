# -*- coding: utf-8 -*-
import unittest

import morpion

class TestMorpion(unittest.TestCase):

    def test_qui_rate(self):
        self.assertFalse(True)

    def test_nouveau_plateau_est_vide(self):
        plateau = morpion.nouveau_plateau()
        for ligne in plateau:
            for place in ligne:
                self.assertEqual(place, "")


if __name__ == '__main__':
    unittest.main()

