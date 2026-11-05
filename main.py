from combat_system import *
import time

pc_name = input("Comment t'appelles-tu ? ")

joueur = Personnage(pc_name, 12, 500, 10)

dragon = Personnage("dragon", 15, 2500, 12)

goblin = Personnage("goblin", 2, 100, 2)

combat(joueur, goblin)
