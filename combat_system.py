import time

class Personnage:
    def __init__(self, nom, niveau, HP, force):
        self.nom = nom
        self.niveau = niveau
        self.HP = HP
        self.force = force

    def pres(self):
        print("\nNom :", self.nom)
        time.sleep(0.3)
        print("Niveau :", self.niveau)
        time.sleep(0.3)
        print("HP :", self.HP)
        time.sleep(0.3)

    def attaquer(self, cible):
        cible.HP -= self.force * 10
        print(f"{self.nom} attaque !")
        time.sleep(1)
        print(f"-{self.force * 10} HP !")

    def defendre(self, attaquant):
        self.HP -= attaquant.force * 5
        print(f"{self.nom} se défend !")
        time.sleep(1)
        print(f"{attaquant.nom} attaque !")
        time.sleep(1)
        print("-", attaquant.force * 5, 'HP !')

def combat(joueur, ennemy):
    print(f"Un", ennemy.nom, "s'avance. Le combat commence !")
    time.sleep(1)
    while ennemy.HP > 0:
        if joueur.HP <= 0:
            break
        joueur.pres()
        time.sleep(0.5)
        ennemy.pres()
        time.sleep(1)
        print("""
[a] Attaquer.
[b] Défendre.
[c] Fuir.
""")
        dmd = input("> ")
        if dmd == "a":
            joueur.attaquer(ennemy)
            if ennemy.HP <= 0:
                time.sleep(1)
                break
            time.sleep(1)
            ennemy.attaquer(joueur)
            time.sleep(1)
            continue
        elif dmd == "b":
            joueur.defendre(ennemy)
            time.sleep(1)
            continue
        elif dmd == "c":
            print("Vous fuyez !")
            time.sleep(1)
            break
        else:
            print("Commande introuvable")
            time.sleep(1)
            continue

    if joueur.HP <= 0:
        print(f"Vous êtes vaincu par le", ennemy.nom, "!")
    elif ennemy.HP <= 0:
        print(f"Félicitation, vous avez vaincu le", ennemy.nom, "!")
