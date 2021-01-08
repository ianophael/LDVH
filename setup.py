import random
import pickle

diciplineKaiList = ["camouflage","chasse","sixème sens","orientation","guérison","maitrise des armes","bouclier psychique","puissance psychique","communication animale","maitrise psychique de la matière"]
diciplineKai = []

class Hero:  #classe qui va créer toute les données du hero
    
    def __init__(self, maxEndurance, habileté, diciplineKai, bourse):
        assert isinstance
        self.maxEndurance = maxEndurance
        self.habileté = habileté
        self.diciplineKai = diciplineKai
        self.bourse = bourse
        self.armes = []
        self.pv = maxEndurance
        self.objet = []
        self.objetSpé = []

def rng(): # assez explicite pour se passer d'explication
    hasard = random.randint(0,9)
    return hasard


try:
    with open("Sauvegarde1.data","rb") as f: # vérifie que le fichier existe ou non
        getSave = pickle.Unpickler(f)
    input("Le fichier existe déja, pour poursuivre la partie, veuillez executer le fichier game, et si vous voulez recommencer une partie supprimez la sauvegarde.")
except:
    # mise en place des pv
    print("Bienvenue dans le livre dont vous etes le héro! vous etes sur le point de vivre une aventure au travers de ce livre!"\
    " J'éspère que vous avez lu la fiche de commande car vous allez en avoir besoin pour effectuer les commandes de base du jeu!"\
    "\nAllons directement a la création de votre personnage. nous commencerons par l'endurance (point de vie)")
    input("\nVeuillez appuyer sur entrer pour choisir un chiffre aléatoire entre 1 et 9, 20 points seront ajouté a ce chiffre, ce qui définira votre endurance.\n")
    maxEndurance = rng() + 20
    input(f"Vous êtes tombé sur le chiffre {maxEndurance - 20}\n ce qui montre votre endurance maximale à {maxEndurance}! \n appuyez sur entrer pour poursuivre la création du personnage.")

    # mise en place de l'habileté au combat
    print("\nOn va maintenant définir votre habileté au combat, qui va vous permettre de voir si vous etes bon au combat.")
    input("Comme pour l'endurance, appuyez sur entrer pour choisir un chiffre aléatoire entre 1 et 9, auquel sera ajouté cette fois 10 points, pour faire votre total d'habileté.")
    habileté = rng() + 10
    input(f"Vous êtes tombé sur le chiffre {habileté - 10}\n ce qui monte votre habileté au combat maximale à {habileté}!\nappuyez sur entrer pour passer au choix des disciplines kai.")

    # mise en place des disciplines kai
    print("\nVeuillez choisir 5 discipline Kai, parmis les disciplines suivantes :\n"\
    "\ncamouflage\nPermet de passer inapercus aux yeux de l'ennemi, ou dans les ville avoir l'air d'un habitant, permettant d'avoir plus facilement un abris\n"\
    "\nchasse :\n Permet de ne jamais avoir besoin de consommer un repas, sauf dans les zones arides comme les déserts\n"\
    "\nsixème sens :\n Permet de deviner les dangers imminents, les intentions d'un inconnu ou la nature d'un objet\n"\
    "\norientation : \n Permet de toujours choisir le bon chemin, de découvrir dans les villes les endoits cachés d'une personne ou d'un objet et de poursuivre une cible avec des empreintes\n"\
    "\nguérison : \n Permet de récupérer des points d'endurances perdu lors de combat, a coups d'un point pour chaque paragraphe parcouru sans combat\n"\
    "\nmaitrise des armes : \n Utilisez la table du random pour obtenir un chiffre qui correspondra a une arme, vous en optiendrez la maitrise total et gagnez le bonus de 2 points d'habileté supplémentaire quand vous maniez cette arme\n"\
    "\nbouclier psychique : \n Permet de ne pas prendre de dégats lors d'une attaque psychique d'un ennemi\n"\
    "\npuissance psychique : \n Permet d'avoir deux points d'habileté supplémentaire contre les ennemis sensible a cette capacité, vous serez averti si c'est le cas\n"\
    "\ncommunication animale : \n Permet de communiquer avec certains animaux, et deviner les intentions de certains autres\n"\
    "\nmaitrise psychique de la matière : \n Vous donne la possibilité de déplacer des petits objets par la pensée\n")

    ouaip = True
    n = 0
    while ouaip:
        faute = False
        if n <= 5:
            if n == 0:
                diciplineKai.append((input(f"Choisissez votre {n+1}ère discipline : ")))
            elif n > 0:
                diciplineKai.append((input(f"Choisissez votre {n+1}ème discipline : ")))
            if diciplineKai[n] not in diciplineKaiList:
                faute = True
                del diciplineKai[n]
                print("Veuillez entrer une discipline kai correcte, peut etre vous etes vous trompé dans l'hortographe, dans ce cas vous pouvez copier/coller le nom dans le message précédent.\n")                
            if faute == False:
                n+=1
        else:
            print("Vous avez fini de choisir vos disciplines kai, les voici:")
            ouaip = False
        

    print(diciplineKai)
    input("Appuyez sur entrer pour passer a la suite.")

    # mise en place de la bourse
    input("\nEnsuite, on va définir combien d'or vous aurez lors du début de votre aventure, apuyez sur entrer pour générer un un chiffre aléatoire entre 1 et 9, auquel sera ajouté 10 pièce d'or")
    bourse = rng() + 10 
    print("Vous etes tombé sur", bourse - 10, "\n ce qui amène votre montant totale d'or a ", bourse,"!")
    input("\nVoila la mise en place de vos stats sont terminées, pour poursuivre la partie il va falloir lancer le programme 'game', et appuyez sur enter pour fermer cette page")


    player = Hero(maxEndurance, habileté, diciplineKai, bourse)

    with open("Sauvegarde1.data","wb") as f:
        save = pickle.Pickler(f)
        save.dump(player)

