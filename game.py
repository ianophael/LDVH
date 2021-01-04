# Les imports--------------------------------------------------------------------------------------------------------------------------------------------------------

import random   # Pas besoin d'expliquer je pense
import pickle   # Permet de sauvegarder

# Définition des classes----------------------------------------------------------------------------------------------------------------------------------------------

class Hero:    #classe qui va créer toute les données du hero
    
    def __init__(self, maxEndurance, habileté, diciplineKai, bourse, maitrise = None):
        self.maxEndurance = maxEndurance
        self.habileté = habileté
        self.diciplineKai = diciplineKai
        self.bourse = bourse
        self.maitrise = maitrise
        self.armes = []
        self.pv = maxEndurance
        self.objet = []
        self.objetSpé = []
    
    def info(self):    # Fonction a utiliser pour avoir disposer de toute les info du joueur
        print(f"vous avez {self.pv}/{self.maxEndurance} point d'endurance\n{self.habileté} points d'habileté\nvotre bourse contient {self.bourse} pièces d'or")    # Nous envoi PV,PH et PO
        print(f"vos diciplines kai sont :{self.diciplineKai[0]}, {self.diciplineKai[1]}, {self.diciplineKai[2]}, {self.diciplineKai[3]}, {self.diciplineKai[4]}")   # Nous envoi nos disciplines kai

        if len(self.armes) == 0:    # Nous renvoi nos armes
            print("vous n'avez pas d'arme")
        elif len(self.armes) == 1:
            print(f"votre arme est : {self.armes[0]}")
        else:
            print(f"votre premiere arme est : {self.armes[0]}\n votre deuxieme arme est : {self.armes[1]}")
        if "maitrise des armes" in self.diciplineKai:   # Si on a la discipline kai "maitrise des armes", nous envoi l'arme maitrisée
            print(f"vous maitrisez l'arme {self.maitrise}")

        if len(self.objet) == 0:    # Nous envoi nos objets normaux
            print("Il n'y a aucun objet dans votre sac !")
        else:
            print(f"\nil y a {len(self.objet)} objets dans votre sac :")
            for i in self.objet:
                print(i)
        
        if len(self.objetSpé) == 0:    # Nous envoi nos objets spéciaux
            print("vous n'avez aucun objet spécial !")
        else:
            print(f"vous avez {len(self.objetSpé)} objets spéciaux sur vous :")
            for i in self.objetSpé:
                print(i)
        
    def addGold(self, montant):    # Fonction a utiler pour une action qui ajoute de l'or
        self.bourse += montant
        if self.bourse >= 50:
            self.bourse = 50
            print("le nombre de pièces que vous vouliez ajouter dépassait la capacité maximale de votre bourse (50 pièces), quelques pièces ont donc été jetée.")
        else:    
            print(montant, "pièces ont été ajouté a votre bourse.\n votre total est donc de", self.bourse)
    
    def useGold(self, montant):    # Fonction a utiliser pour une action qui retire de l'or
        self.bourse -= montant
        if self.bourse < 0:
            self.bourse = 0
        print("il vous reste", self.bourse,"pièces.")

    def addArmes(self, nom):   # Ajoute une arme
        self.armes.append(nom)

    def addObjet(self, nom):    # Ajoute un objet
        self.objet.append(nom)

    def addObjetSpé(self, objet):   # Ajoute un objet spécial
        self.objetSpé.append(objet)
        if objet.stat == "endurance":   
            self.maxEndurance += objet.valeur
            print(f"grace a cet objet, votre endurance maximum monte a {self.maxEndurance}")
        elif objet.stat == "habileté":
            self.habileté += objet.valeur
            print(f"grace a cet objet, votre habileté maximum monte a {self.habileté}")
        else: 
            input("aucune stat n'a été ajouté. si c'est une erreur, veillez a ce que ce que vous avez rentré en effet d'objet soit bien écrit 'endurance' ou 'habileté'")

    def dmgSubit(self, dmg):    # Fonction a utiliser si le joueur prend des dégats
        self.pv -= dmg
        if self.pv < 0:
            self.pv = 0
        print(f"vous subissez {dmg} dégats, il vous reste donc {self.pv} points d'endurance")

    def soins(self, heal):  # Fontion a utiliser si le joueur récupère des pv
        self.pv += heal
        if self.pv > self.maxEndurance:
            self.pv = self.maxEndurance
            print(f"vous avez atteint votre endurance maximum ({self.pv})")
        else:
            print(f"vous vous êtes soigné {heal} PE et avez donc {self.pv} points d'endurance")

class Objetspéciaux:    #classe des objet qui va donner leur stats et nom

    def __init__(self, nomObjet, valeur, stat = None):
        self.nomObjet = nomObjet
        self.valeur = valeur
        self.stat = stat

    def donnée(self):
        return self.valeur, self.stat

    def __repr__(self):
        return self.nomObjet

class Enemy:    #classe des ennemis qu'on rencontrera dans l'aventure

    def __init__(self, endurance, habileté):
        self.endurance = endurance
        self.habileté = habileté

    def resistancePsy(self,res = True):
        if res == False:
            self.habileté -= 2

# Définition des fonctions--------------------------------------------------------------------------------------------------------------------------------------------

def rng():  # Fonction qui permet de prendre un chiffre au hasard entre 0 et 9
    hasard = random.randint(0,9)
    return hasard

def sauvegarde():   # Fonction a utiliser pour sauvegarder
    with open("Sauvegarde1.data","wb") as f:
        save = pickle.Pickler(f)
        save.dump(loupSolitaire)

def setupCombat(adversaire):    # Fonction a utiliser pour paramétrer le combat

    habiletéCombat = loupSolitaire.habileté    # Variable intermédiaire utilisée pour modifier l'habileté uniquement pour le combat, sans avoir a vraiment la toucher

    if len(loupSolitaire.armes) >= 1:   # Vérifie si le joueur a un arme
        if "maitrise des armes" in loupSolitaire.diciplineKai:  # Vérifie si il a la maitrise de l'arme
            for i in loupSolitaire.armes:
                if i == loupSolitaire.maitrise:
                    print("Vous avez la totale maitrise de votre arme, 2 points d'habileté supplémentaire vous ont donc été accordé.")
                    habiletéCombat += 2 
    else:   # Comme le joueur n'a pas d'arme il prend un malus
        input("Vous ne disposez d'aucune arme, 4 points d'habileté vous ont donc été retiré.")
        habiletéCombat -= 4
    
    if "puissance psychique" in loupSolitaire.diciplineKai:    # Vérifie si le joueur a la discipline kai "puissance psychique"
        question = input("Votre ennemi est il résistant a votre dicipline kai 'puissance psychique'?")   # Demande si l'ennemi est résistant ou pas
        if question == "non":
            print("Très bien, deux points d'habileté vous ont donc été accordé.")
            habiletéCombat += 2
    else:
        print("Très bien")

    input("Parfait, passons maintenant a la suite, nous allons maintenant soustraire les point d'habileté de votre adversaire aux votres pour créer votre quotient d'attaque.\nAppuyez sur enter pour passer a la suite..")
    quotientAttaque = habiletéCombat - adversaire.habileté
    print(f"\nL'habileté ennemie ({adversaire.habileté}) a été soustraite a votre propre habileté ({habiletéCombat}), le quotient d'attaque est donc de {quotientAttaque}.")
    input("Ensuite, il faut choisir un chiffre aléatoire entre 0 et 9, appuyez sur entrer pour faire un tirage..")
    
    return quotientAttaque

def enduranceAjusteur(enduheroless = -1, enduennemiless = -1):   # Fonction qui applique les points de dégats

    if enduheroless == enduennemiless == -1:    # Si le joueur et l'adversaire meurent
        ennemi.endurance = 0
        loupSolitaire.pv = 0
        input("Vous et l'ennemi êtes mort en 1 coup.")
    elif enduheroless == -1:    # Si on se fait one shot
        loupSolitaire.pv = 0
        input("Vous vous êtes fait annihilé et êtes mort en 1 coup.")
    elif enduennemiless == -1:   # Si l'ennemi se fait one shot
        ennemi.endurance = 0
        input("Coup critique! Vous avez one shot votre adversaire.")
    else:
        loupSolitaire.pv -= enduheroless
        ennemi.endurance -= enduennemiless
        if enduheroless == enduennemiless:   # Si le joueur et son advairesaire prennent le meme nombre de point de dégat
            if enduheroless == 1:   # Si chacun prend 1 point de dégat
                input(f"Vous perdez tout les deux {enduheroless} point d'endurance.")
            else:
                input(f"Vous perdez tout les deux {enduheroless} points d'endurance.")
        elif enduennemiless != 0 and enduheroless == 0:    # Si seulement l'énnemi prend des dégats
            input(f"Coup critique! l'ennemi perd {enduennemiless} point d'endurance et vous n'en perdez aucun")
        elif enduennemiless == 0 and enduheroless != 0:    # Si seulement le joueur prend des dégats
            input(f"Vous perdez {enduheroless} points d'endurance et l'ennemi n'en perd aucun.")
        elif enduennemiless == 1 and enduheroless != 0:    # Si l'ennemi ne prend qu'un dégat et le joueur plus
            input(f"Vous perdez {enduheroless} points d'endurance et l'ennemi n'en perd qu'un")
        elif enduennemiless != 0 and enduheroless == 1:    # Si le joueur ne prend qu'un dégat et l'ennemi plus
            input(f"Vous perdez qu'un point d'endurance et l'ennemi en perd {enduennemiless}")
        else:   # Les autres cas
            input(f"Vous perdez {enduheroless} points d'endurance et l'ennemi en perd {enduennemiless}")

def tableDesCoupsPorté(quotientAttaque):    # Le bordel monstre de la table de dégat
    chiffreAléatoire = rng()    #  Comme il est marqué en suivant les règles, il y a de la rng dans les combats
    input(f"votre chiffre aléatoire est {chiffreAléatoire}, appuyez sur entrer pour voir les resultats")

    # Bonne chance pour lire la suite

    # -11 + 
    if quotientAttaque <= -11 and chiffreAléatoire <= 2:
        enduranceAjusteur(-1,0)
    elif quotientAttaque <= -11 and chiffreAléatoire == 3 or quotientAttaque <= -11 and chiffreAléatoire == 4:
        enduranceAjusteur(8,0)
    elif quotientAttaque <= -11 and chiffreAléatoire == 5:
        enduranceAjusteur(7,1)
    elif quotientAttaque <= -11 and chiffreAléatoire == 6:
        enduranceAjusteur(6,2)
    elif quotientAttaque <= -11 and chiffreAléatoire == 7:
        enduranceAjusteur(5,3)
    elif quotientAttaque <= -11 and chiffreAléatoire == 8:
        enduranceAjusteur(4,4)
    elif quotientAttaque <= -11 and chiffreAléatoire == 9:
        enduranceAjusteur(3,5)
    elif quotientAttaque <= -11 and chiffreAléatoire == 0:
        enduranceAjusteur(0,6)

    # -10 -9
    elif quotientAttaque == -10 and chiffreAléatoire == 1 or quotientAttaque == -9 and chiffreAléatoire == 1:
        enduranceAjusteur(-1,0)
    elif quotientAttaque == -10 and chiffreAléatoire == 2 or quotientAttaque == -9 and chiffreAléatoire == 2:
        enduranceAjusteur(8,0)
    elif quotientAttaque == -10 and chiffreAléatoire == 3 or quotientAttaque == -9 and chiffreAléatoire == 3:
        enduranceAjusteur(7,0)
    elif quotientAttaque == -10 and chiffreAléatoire == 4 or quotientAttaque == -9 and chiffreAléatoire == 4:
        enduranceAjusteur(7,1)
    elif quotientAttaque == -10 and chiffreAléatoire == 5 or quotientAttaque == -9 and chiffreAléatoire == 5:
        enduranceAjusteur(6,2)
    elif quotientAttaque == -10 and chiffreAléatoire == 6 or quotientAttaque == -9 and chiffreAléatoire == 6:
        enduranceAjusteur(6,3)
    elif quotientAttaque == -10 and chiffreAléatoire == 7 or quotientAttaque == -9 and chiffreAléatoire == 7:
        enduranceAjusteur(5,4)
    elif quotientAttaque == -10 and chiffreAléatoire == 8 or quotientAttaque == -9 and chiffreAléatoire == 8:
        enduranceAjusteur(4,5)
    elif quotientAttaque == -10 and chiffreAléatoire == 9 or quotientAttaque == -9 and chiffreAléatoire == 9:
        enduranceAjusteur(3,6)
    elif quotientAttaque == -10 and chiffreAléatoire == 0 or quotientAttaque == -9 and chiffreAléatoire == 0:
        enduranceAjusteur(0,7)
    
    # -8 -7
    elif quotientAttaque == -8 and chiffreAléatoire == 1 or quotientAttaque == -7 and chiffreAléatoire == 1:
        enduranceAjusteur(8,0)
    elif quotientAttaque == -8 and chiffreAléatoire == 2 or quotientAttaque == -7 and chiffreAléatoire == 2:
        enduranceAjusteur(7,0)
    elif quotientAttaque == -8 and chiffreAléatoire == 3 or quotientAttaque == -7 and chiffreAléatoire == 3:
        enduranceAjusteur(6,1)
    elif quotientAttaque == -8 and chiffreAléatoire == 4 or quotientAttaque == -7 and chiffreAléatoire == 4:
        enduranceAjusteur(6,2)
    elif quotientAttaque == -8 and chiffreAléatoire == 5 or quotientAttaque == -7 and chiffreAléatoire == 5:
        enduranceAjusteur(5,3)
    elif quotientAttaque == -8 and chiffreAléatoire == 6 or quotientAttaque == -7 and chiffreAléatoire == 6:
        enduranceAjusteur(5,4)
    elif quotientAttaque == -8 and chiffreAléatoire == 7 or quotientAttaque == -7 and chiffreAléatoire == 7:
        enduranceAjusteur(4,5)
    elif quotientAttaque == -8 and chiffreAléatoire == 8 or quotientAttaque == -7 and chiffreAléatoire == 8:
        enduranceAjusteur(3,6)
    elif quotientAttaque == -8 and chiffreAléatoire == 9 or quotientAttaque == -7 and chiffreAléatoire == 9:
        enduranceAjusteur(2,7)
    elif quotientAttaque == -8 and chiffreAléatoire == 0 or quotientAttaque == -7 and chiffreAléatoire == 0:
        enduranceAjusteur(0,8)
        
    # -6 -5
    elif quotientAttaque == -6 and chiffreAléatoire == 1 or quotientAttaque == -5 and chiffreAléatoire == 1:
        enduranceAjusteur(6,0)
    elif quotientAttaque == -6 and chiffreAléatoire == 2 or quotientAttaque == -5 and chiffreAléatoire == 2:
        enduranceAjusteur(6,1)
    elif quotientAttaque == -6 and chiffreAléatoire == 3 or quotientAttaque == -5 and chiffreAléatoire == 3:
       enduranceAjusteur(5,2)
    elif quotientAttaque == -6 and chiffreAléatoire == 4 or quotientAttaque == -5 and chiffreAléatoire == 4:
        enduranceAjusteur(5,3)
    elif quotientAttaque == -6 and chiffreAléatoire == 5 or quotientAttaque == -5 and chiffreAléatoire == 5:
        enduranceAjusteur(4,4)
    elif quotientAttaque == -6 and chiffreAléatoire == 6 or quotientAttaque == -5 and chiffreAléatoire == 6:
        enduranceAjusteur(4,5)
    elif quotientAttaque == -6 and chiffreAléatoire == 7 or quotientAttaque == -5 and chiffreAléatoire == 7:
        enduranceAjusteur(3,6)
    elif quotientAttaque == -6 and chiffreAléatoire == 8 or quotientAttaque == -5 and chiffreAléatoire == 8:
        enduranceAjusteur(2,7)
    elif quotientAttaque == -6 and chiffreAléatoire == 9 or quotientAttaque == -5 and chiffreAléatoire == 9:
        enduranceAjusteur(0,8)
    elif quotientAttaque == -6 and chiffreAléatoire == 0 or quotientAttaque == -5 and chiffreAléatoire == 0:
        enduranceAjusteur(0,9)

    # -4 -3
    elif quotientAttaque == -4 and chiffreAléatoire == 1 or quotientAttaque == -3 and chiffreAléatoire == 1:
        enduranceAjusteur(6,1)
    elif quotientAttaque == -4 and chiffreAléatoire == 2 or quotientAttaque == -3 and chiffreAléatoire == 2:
        enduranceAjusteur(5,2)
    elif quotientAttaque == -4 and chiffreAléatoire == 3 or quotientAttaque == -3 and chiffreAléatoire == 3:
        enduranceAjusteur(5,3)
    elif quotientAttaque == -4 and chiffreAléatoire == 4 or quotientAttaque == -3 and chiffreAléatoire == 4:
        enduranceAjusteur(4,4)
    elif quotientAttaque == -4 and chiffreAléatoire == 5 or quotientAttaque == -3 and chiffreAléatoire == 5:
        enduranceAjusteur(4,5)
    elif quotientAttaque == -4 and chiffreAléatoire == 6 or quotientAttaque == -3 and chiffreAléatoire == 6:
        enduranceAjusteur(3,6)
    elif quotientAttaque == -4 and chiffreAléatoire == 7 or quotientAttaque == -3 and chiffreAléatoire == 7:
        enduranceAjusteur(2,7)
    elif quotientAttaque == -4 and chiffreAléatoire == 8 or quotientAttaque == -3 and chiffreAléatoire == 8:
        enduranceAjusteur(1,8)
    elif quotientAttaque == -4 and chiffreAléatoire == 9 or quotientAttaque == -3 and chiffreAléatoire == 9:
        enduranceAjusteur(0,9)
    elif quotientAttaque == -4 and chiffreAléatoire == 0 or quotientAttaque == -3 and chiffreAléatoire == 0:
        enduranceAjusteur(0,10)

    # -2 -1
    elif quotientAttaque == -2 and chiffreAléatoire == 1 or quotientAttaque == -1 and chiffreAléatoire == 1:
        enduranceAjusteur(5,2)
    elif quotientAttaque == -2 and chiffreAléatoire == 2 or quotientAttaque == -1 and chiffreAléatoire == 2:
        enduranceAjusteur(5,3)
    elif quotientAttaque == -2 and chiffreAléatoire == 3 or quotientAttaque == -1 and chiffreAléatoire == 3:
        enduranceAjusteur(4,4)
    elif quotientAttaque == -2 and chiffreAléatoire == 4 or quotientAttaque == -1 and chiffreAléatoire == 4:
        enduranceAjusteur(4,5)
    elif quotientAttaque == -2 and chiffreAléatoire == 5 or quotientAttaque == -1 and chiffreAléatoire == 5:
        enduranceAjusteur(3,6)
    elif quotientAttaque == -2 and chiffreAléatoire == 6 or quotientAttaque == -1 and chiffreAléatoire == 6:
        enduranceAjusteur(2,7)
    elif quotientAttaque == -2 and chiffreAléatoire == 7 or quotientAttaque == -1 and chiffreAléatoire == 7:
        enduranceAjusteur(2,8)
    elif quotientAttaque == -2 and chiffreAléatoire == 8 or quotientAttaque == -1 and chiffreAléatoire == 8:
        enduranceAjusteur(1,9)
    elif quotientAttaque == -2 and chiffreAléatoire == 9 or quotientAttaque == -1 and chiffreAléatoire == 9:
        enduranceAjusteur(0,10)
    elif quotientAttaque == -2 and chiffreAléatoire == 0 or quotientAttaque == -1 and chiffreAléatoire == 0:
        enduranceAjusteur(0,11)

    # 0
    elif quotientAttaque == 0 and chiffreAléatoire == 1:
        enduranceAjusteur(5,3)
    elif quotientAttaque == 0 and chiffreAléatoire == 2:
       enduranceAjusteur(4,4)
    elif quotientAttaque == 0 and chiffreAléatoire == 3:
        enduranceAjusteur(4,5)
    elif quotientAttaque == 0 and chiffreAléatoire == 4:
        enduranceAjusteur(3,6)
    elif quotientAttaque == 0 and chiffreAléatoire == 5:
        enduranceAjusteur(2,7)
    elif quotientAttaque == 0 and chiffreAléatoire == 6:
        enduranceAjusteur(2,8)
    elif quotientAttaque == 0 and chiffreAléatoire == 7:
        enduranceAjusteur(1,9)
    elif quotientAttaque == 0 and chiffreAléatoire == 8:
        enduranceAjusteur(0,10)
    elif quotientAttaque == 0 and chiffreAléatoire == 9:
        enduranceAjusteur(0,11)
    elif quotientAttaque == 0 and chiffreAléatoire == 0:
        enduranceAjusteur(0,12)

    # 1 2
    elif quotientAttaque == 1 and chiffreAléatoire == 1 or quotientAttaque == 2 and chiffreAléatoire == 1:
        enduranceAjusteur(5,4)
    elif quotientAttaque == 1 and chiffreAléatoire == 2 or quotientAttaque == 2 and chiffreAléatoire == 2:
        enduranceAjusteur(4,5)
    elif quotientAttaque == 1 and chiffreAléatoire == 3 or quotientAttaque == 2 and chiffreAléatoire == 3:
        enduranceAjusteur(3,6)
    elif quotientAttaque == 1 and chiffreAléatoire == 4 or quotientAttaque == 2 and chiffreAléatoire == 4:
        enduranceAjusteur(3,7)
    elif quotientAttaque == 1 and chiffreAléatoire == 5 or quotientAttaque == 2 and chiffreAléatoire == 5:
        enduranceAjusteur(2,8)
    elif quotientAttaque == 1 and chiffreAléatoire == 6 or quotientAttaque == 2 and chiffreAléatoire == 6:
        enduranceAjusteur(2,9)
    elif quotientAttaque == 1 and chiffreAléatoire == 7 or quotientAttaque == 2 and chiffreAléatoire == 7:
        enduranceAjusteur(1,10)
    elif quotientAttaque == 1 and chiffreAléatoire == 8 or quotientAttaque == 2 and chiffreAléatoire == 8:
        enduranceAjusteur(0,11)
    elif quotientAttaque == 1 and chiffreAléatoire == 9 or quotientAttaque == 2 and chiffreAléatoire == 9:
        enduranceAjusteur(0,12)
    elif quotientAttaque == 1 and chiffreAléatoire == 0 or quotientAttaque == 2 and chiffreAléatoire == 0:
        enduranceAjusteur(0,14)

    # 3 4
    elif quotientAttaque == 3 and chiffreAléatoire == 1 or quotientAttaque == 4 and chiffreAléatoire == 1:
        enduranceAjusteur(4,5)
    elif quotientAttaque == 3 and chiffreAléatoire == 2 or quotientAttaque == 4 and chiffreAléatoire == 2:
        enduranceAjusteur(3,6)
    elif quotientAttaque == 3 and chiffreAléatoire == 3 or quotientAttaque == 4 and chiffreAléatoire == 3:
        enduranceAjusteur(3,7)
    elif quotientAttaque == 3 and chiffreAléatoire == 4 or quotientAttaque == 4 and chiffreAléatoire == 4:
        enduranceAjusteur(2,8)
    elif quotientAttaque == 3 and chiffreAléatoire == 5 or quotientAttaque == 4 and chiffreAléatoire == 5:
        enduranceAjusteur(2,9)
    elif quotientAttaque == 3 and chiffreAléatoire == 6 or quotientAttaque == 4 and chiffreAléatoire == 6:
        enduranceAjusteur(2,10)
    elif quotientAttaque == 3 and chiffreAléatoire == 7 or quotientAttaque == 4 and chiffreAléatoire == 7:
        enduranceAjusteur(1,11)
    elif quotientAttaque == 3 and chiffreAléatoire == 8 or quotientAttaque == 4 and chiffreAléatoire == 8:
        enduranceAjusteur(0,12)
    elif quotientAttaque == 3 and chiffreAléatoire == 9 or quotientAttaque == 4 and chiffreAléatoire == 9:
       enduranceAjusteur(0,14)
    elif quotientAttaque == 3 and chiffreAléatoire == 0 or quotientAttaque == 4 and chiffreAléatoire == 0:
        enduranceAjusteur(0,16)

    # 5 6
    elif quotientAttaque == 5 and chiffreAléatoire == 1 or quotientAttaque == 6 and chiffreAléatoire == 1:
        enduranceAjusteur(4,6)
    elif quotientAttaque == 5 and chiffreAléatoire == 2 or quotientAttaque == 6 and chiffreAléatoire == 2:
        enduranceAjusteur(3,7)
    elif quotientAttaque == 5 and chiffreAléatoire == 3 or quotientAttaque == 6 and chiffreAléatoire == 3:
        enduranceAjusteur(3,8)
    elif quotientAttaque == 5 and chiffreAléatoire == 4 or quotientAttaque == 6 and chiffreAléatoire == 4:
        enduranceAjusteur(2,9)
    elif quotientAttaque == 5 and chiffreAléatoire == 5 or quotientAttaque == 6 and chiffreAléatoire == 5:
        enduranceAjusteur(2,10)
    elif quotientAttaque == 5 and chiffreAléatoire == 6 or quotientAttaque == 6 and chiffreAléatoire == 6:
        enduranceAjusteur(1,11)
    elif quotientAttaque == 5 and chiffreAléatoire == 7 or quotientAttaque == 6 and chiffreAléatoire == 7:
        enduranceAjusteur(0,12)
    elif quotientAttaque == 5 and chiffreAléatoire == 8 or quotientAttaque == 6 and chiffreAléatoire == 8:
        enduranceAjusteur(0,14)
    elif quotientAttaque == 5 and chiffreAléatoire == 9 or quotientAttaque == 6 and chiffreAléatoire == 9:
        enduranceAjusteur(0,16)
    elif quotientAttaque == 5 and chiffreAléatoire == 0 or quotientAttaque == 6 and chiffreAléatoire == 0:
        enduranceAjusteur(0,18)

    # 7 8
    elif quotientAttaque == 7 and chiffreAléatoire == 1 or quotientAttaque == 8 and chiffreAléatoire == 1:
        enduranceAjusteur(4,7)
    elif quotientAttaque == 7 and chiffreAléatoire == 2 or quotientAttaque == 8 and chiffreAléatoire == 2:
        enduranceAjusteur(3,8)
    elif quotientAttaque == 7 and chiffreAléatoire == 3 or quotientAttaque == 8 and chiffreAléatoire == 3:
        enduranceAjusteur(2,9)
    elif quotientAttaque == 7 and chiffreAléatoire == 4 or quotientAttaque == 8 and chiffreAléatoire == 4:
        enduranceAjusteur(2,10)
    elif quotientAttaque == 7 and chiffreAléatoire == 5 or quotientAttaque == 8 and chiffreAléatoire == 5:
        enduranceAjusteur(2,11)
    elif quotientAttaque == 7 and chiffreAléatoire == 6 or quotientAttaque == 8 and chiffreAléatoire == 6:
        enduranceAjusteur(1,12)
    elif quotientAttaque == 7 and chiffreAléatoire == 7 or quotientAttaque == 8 and chiffreAléatoire == 7:
        enduranceAjusteur(0,14)
    elif quotientAttaque == 7 and chiffreAléatoire == 8 or quotientAttaque == 8 and chiffreAléatoire == 8:
        enduranceAjusteur(0,16)
    elif quotientAttaque == 7 and chiffreAléatoire == 9 or quotientAttaque == 8 and chiffreAléatoire == 9:
        enduranceAjusteur(0,18)
    elif quotientAttaque == 7 and chiffreAléatoire == 0 or quotientAttaque == 8 and chiffreAléatoire == 0:
        enduranceAjusteur(0,-1)
    
    # 9 10
    elif quotientAttaque == 9 and chiffreAléatoire == 1 or quotientAttaque == 10 and chiffreAléatoire == 1:
        enduranceAjusteur(3,8)
    elif quotientAttaque == 9 and chiffreAléatoire == 2 or quotientAttaque == 10 and chiffreAléatoire == 2:
        enduranceAjusteur(3,9)
    elif quotientAttaque == 9 and chiffreAléatoire == 3 or quotientAttaque == 10 and chiffreAléatoire == 3:
        enduranceAjusteur(2,10)
    elif quotientAttaque == 9 and chiffreAléatoire == 4 or quotientAttaque == 10 and chiffreAléatoire == 4:
        enduranceAjusteur(2,11)
    elif quotientAttaque == 9 and chiffreAléatoire == 5 or quotientAttaque == 10 and chiffreAléatoire == 5:
        enduranceAjusteur(2,12)
    elif quotientAttaque == 9 and chiffreAléatoire == 6 or quotientAttaque == 10 and chiffreAléatoire == 6:
        enduranceAjusteur(1,14)
    elif quotientAttaque == 9 and chiffreAléatoire == 7 or quotientAttaque == 10 and chiffreAléatoire == 7:
        enduranceAjusteur(0,16)
    elif quotientAttaque == 9 and chiffreAléatoire == 8 or quotientAttaque == 10 and chiffreAléatoire == 8:
        enduranceAjusteur(0,18)
    elif quotientAttaque == 9 and chiffreAléatoire == 9 or quotientAttaque == 10 and chiffreAléatoire == 9:
        enduranceAjusteur(0,-1)
    elif quotientAttaque == 9 and chiffreAléatoire == 0 or quotientAttaque == 10 and chiffreAléatoire == 0:
        enduranceAjusteur(0,-1)

    # 11 +
    elif quotientAttaque >= 11 and chiffreAléatoire == 1:
        enduranceAjusteur(3,9)
    elif quotientAttaque >= 11 and chiffreAléatoire == 2:
        enduranceAjusteur(2,10)
    elif quotientAttaque >= 11 and chiffreAléatoire == 3:
        enduranceAjusteur(2,11)
    elif quotientAttaque >= 11 and chiffreAléatoire == 4:
        enduranceAjusteur(2,12)
    elif quotientAttaque >= 11 and chiffreAléatoire == 5:
        enduranceAjusteur(1,14)
    elif quotientAttaque >= 11 and chiffreAléatoire == 6:
        enduranceAjusteur(1,16)
    elif quotientAttaque >= 11 and chiffreAléatoire == 7:
        enduranceAjusteur(0,18)
    elif quotientAttaque >= 11 and chiffreAléatoire >= 8:
        enduranceAjusteur(0,-1)
    elif quotientAttaque >= 11 and chiffreAléatoire >= 9:
        enduranceAjusteur(0,-1)
    elif quotientAttaque >= 11 and chiffreAléatoire == 0:
        enduranceAjusteur(0,-1)

# Récupération de la sauvegarde---------------------------------------------------------------------------------------------------------------------------------------

with open("Sauvegarde1.data", "rb") as f:
    getSave = pickle.Unpickler(f)
    loupSolitaire = getSave.load()

# Jeu------------------------------------------------------------------------------------------------------------------------------

game = True

while game:    # Boucle principale du jeu

    if loupSolitaire.pv == 0:   # Vérifie si le joueur est mort
        input("Vous avez perdu cette partie, veuillez supprimer le fichier de sauvegarde et en relancer une autre.")
        game = False
    if loupSolitaire.pv > loupSolitaire.maxEndurance:    # Si les pv rendu sont suppérieurs aux pv max, reéquilibre le tout
        loupSolitaire.pv = loupSolitaire.maxEndurance

    # LISTES DE TOUTE LES COMMANDES

    commande = input("\nEntrez une commande pour effectuer l'action désirée.\n")

    if commande == "exit" or commande == "quit" or commande == "quitter" or commande == "stop":
        sauvegarde()
        game = False
        input("Vous allez quitter la partie...")

    elif commande == "info" or commande == "information" or commande == "informations" or commande == "stat" or commande == "stats":
        loupSolitaire.info()
    
    elif commande == "addgold":
        piece = input("Combien de pièces avez vous gagné? ")
        piece = int(piece)
        loupSolitaire.addGold(piece)
    
    elif commande == "usegold" or commande == "losegold" or commande == "useor" or commande == "usepiece":
        moinpiece = int(input("Combien de pièces avez vous utilisé?"))
        loupSolitaire.useGold(moinpiece)

    elif commande == "addpv" or commande == "addendurance" or commande == "heal":
        heal = input("Combien de point d'endurance vous êtes vous soigné?")
        heal = int(heal)
        loupSolitaire.soins(heal)
        
    elif commande == "losepv" or commande == "loseendurance":
        dmg = input("Combien de dégats avez vous subis?")
        dmg = int(dmg)
        loupSolitaire.dmgSubit(dmg)

    elif commande == "losemaxpv":
        question = int(input("Combien de point d'endurance doivent etre supprimé?\n"))
        loupSolitaire.maxEndurance -= question
        if loupSolitaire.maxEndurance < 1:
            loupSolitaire.maxEndurance = 1
        print(f"Vous perdez {question} point d'endurance. Il vous en reste {loupSolitaire.maxEndurance}.")
    
    elif commande == "addmaxpv":
        question = int(input("Combien de point d'endurance doivent etre ajouté?\n"))
        loupSolitaire.maxEndurance += question
        print(f"Vous gagnez {question} point d'endurance. Vous en avez donc {loupSolitaire.maxEndurance}.")

    elif commande == "addhabileté":
        question = int(input("Combien de point d'habileté doivent etre ajouté?\n"))
        loupSolitaire.habileté += question
        print(f"Vous gagnez {question} point d'habileté. Vous en avez donc {loupSolitaire.habileté}.")
        
    elif commande == "losehabileté":
        question = int(input("Combien de point d'habileté doivent etre retiré?\n"))
        loupSolitaire.habileté -= question
        print(f"Vous perdez {question} point d'habileté. Il vous en reste donc {loupSolitaire.habileté}.")

    elif commande == "combat" or commande == "fight" or commande == "bataille":
        fuite = False
        question = input("Avez vous la possibilité de prendre la fuite?\n")
        if question == "oui":
            question = input("Le voulez vous? (une fois en combat vous n'aurez plus la possibilité de fuire)")
            if question == "oui":
                fuite = True
                print("Vous prenez la fuite...")
            
        if fuite == False:
            combat = True
            enduranceEnnemi = int(input("Veuillez ici entrer l'endurance de votre ennemi.\n"))    
            habiletéEnnemi = int(input("Veuillez ici entrer l'habileté au combat de votre ennemi.\n"))
            ennemi = Enemy(enduranceEnnemi, habiletéEnnemi)

            quotientAttaque = setupCombat(ennemi)

            while combat:
                tableDesCoupsPorté(quotientAttaque)

                if ennemi.endurance <= 0:
                    print("\nVous gagnez le combat, votre ennemi s'écroule au sol.")
                    combat = False
                else:
                    print(f"\nIl reste {ennemi.endurance} points d'endurance a votre adversaire.")
                if loupSolitaire.pv <= 0:
                    input("Vous avez perdu la partie, et avec ca la mission qui vous avait été confiée, veuillez supprimer la sauvegarde, et si vous le voulez, recommencer une partie.")
                    combat = False
                else:
                    print(f"Il vous reste {loupSolitaire.pv} points d'endurance.")

        sauvegarde()

    elif commande == "addobjet":
        if len(loupSolitaire.objet) < 8:
            question = input("Quel est le nom de l'objet que vous voulez prendre?\n")
            loupSolitaire.addObjet(question)
            print(f"Vous avez mit l'objet {question} dans votre sac.")
        else:
            print("Votre sac est plein, peut etre voulez vous jeter un objet qui ne vous sert pas, dans ce cas utilisez la commande 'delobjet'.")

    elif commande == "delobjet":
        if len(loupSolitaire.objet) == 0:
            print("Vous n'avez pas d'objet dans votre sac.")
        elif len(loupSolitaire.objet) == 1:
            question = input(f"Voulez vous jeter l'objet {loupSolitaire.objet[0]}?\n")
            if question == "oui":
                del loupSolitaire.objet[0]
                print("L'objet a été jeté.")
            else:
                print("très bien")
        else:
            n = 0
            for i in loupSolitaire.objet:
                print(f"Tapez '{n}' pour jeter l'objet {i}.")
                n += 1
            reponse = int(input())
            del loupSolitaire.objet[reponse]
            print("L'objet a été jeté.")
    
    elif commande == "addobjetspé" or commande == "addobjetspéciaux":
        nomObjet = input("Quel est le nom de cet objet?\n")
        effetObjet = input("Quel est l'effet de cet objet? (endurance ou habileté)\n")
        valeurObjet = input("Quelle est la valeur de cet effet?\n")
        valeurObjet = int(valeurObjet)
        newObjet = Objetspéciaux(nomObjet, valeurObjet, effetObjet)
        loupSolitaire.addObjetSpé(newObjet)

    elif commande == "delobjetspé":
        if len(loupSolitaire.objetSpé) == 0:
            print("Vous n'avez pas d'objet spéciaux sur vous.")
        elif len(loupSolitaire.objetSpé) == 1:
            question = input(f"Voulez vous jeter l'objet {loupSolitaire.objetSpé[0]}?\n")
            if question == "oui":
                del loupSolitaire.objetSpé[0]
                print("L'objet a été jeté.")
            else:
                print("très bien")
        else:
            n = 0
            for i in loupSolitaire.objetSpé:
                print(f"Tapez '{n}' pour jeter l'objet {i}.")
                n += 1
            reponse = int(input())
            del loupSolitaire.objetSpé[reponse]
            print("L'objet a été jeté.")

    elif commande == "addarme" or commande == "addweapon":
            if len(loupSolitaire.armes) >= 2:
                input("Vos n'avez pas assez de place pour supprimer une arme, veuillez entrer la commande 'delarme' pour remplacer l'arme de votre choix, ou tout simplment ne rien faire pour garder vos armes actuelles.")
            else:
                arme = input("Quel est le nom de l'arme que vous voulez prendre?")
                print("Très bien, cette arme sera ajouté a votre ceinture.")
                loupSolitaire.addArmes(arme)

    elif commande == "delarme":
        if len(loupSolitaire.armes) == 2:
            question = input(f"Quelle arme voulez vous jeter? \ntapez '1' pour la première : {loupSolitaire.armes[0]} \ntapez '2' pour la deuxième : {loupSolitaire.armes[1]}\n")
            if question == "1":
                print(f"L'arme {loupSolitaire.armes[0]} a été jetée.")
                del loupSolitaire.armes[0]
            elif question == "2":
                print(f"L'arme {loupSolitaire.armes[1]} a été jetée.")
                del loupSolitaire.armes[1]
            else:
                print("Veuillez répondre par '1' ou '2'.")
        elif len(loupSolitaire.armes) == 1:
            question = input(f"Voulez vous jeter votre {loupSolitaire.armes[0]}?")
            if question == "oui":
                print(f"L'arme {loupSolitaire.armes[0]} a été jetée.")
                del loupSolitaire.armes[0]
            else:
                print("Aucune arme n'est jetée")
        else:
            print("Vous n'avez aucune arme a votre ceinture.")

    elif commande == "sauvegarde":
        sauvegarde()
        print("Partie sauvegardée.")

    elif commande == "random" or commande == "tabledeshasard" or commande == "aléatoire":
        n = rng()
        print(f"Vous obtenez le chiffre {n}.")
        
    else:
        print("Commande introuvable, entrez une commande valide.")
