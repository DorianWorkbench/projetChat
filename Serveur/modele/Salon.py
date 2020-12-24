from tools import bdd

class Salon:
    id = 0
    nomSalon = ""
    idUtil = 0

    def __init__(self, id, nomSalon, idUtil):
        self.id =id
        self.nomSalon = nomSalon
        self.idUtil = idUtil

    @staticmethod
    def ajoutSalon(nomSalon, idUtil):
        return bdd.creationSalon(nomSalon, idUtil)

    @staticmethod
    def listerSalonUtil(idUtil):
        return bdd.listerSalonParUtil(idUtil)

    @staticmethod
    def rejoindreSalon(idUtil, nomSalon):
        return bdd.rejoindreSalon(idUtil, nomSalon)

    @staticmethod
    def listeMessageSalon(idSalon):
        return bdd.listeMessageSalon(idSalon)