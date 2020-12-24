from tools import bdd


class Utilisateur:

    id = 0
    pseudo = ""

    def __init__(self, id, pseudo):
        self.id = id
        self.pseudo = pseudo

    @staticmethod
    def connexionUtilisateur(pseudo):
        print("here")
        return bdd.connexion(pseudo)

    @staticmethod
    def inscriptionUtilisateur(pseudo):
        return bdd.ajouterUtilisateur(pseudo)