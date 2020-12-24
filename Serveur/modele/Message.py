from tools import bdd


class Message:
    id = 0
    texte = ""
    dateMessage = ""
    idUtil = 0
    idSalon = 0

    def __init__(self, id, texte, dateMessage, idUtil, idSalon):
        self.id = id
        self.texte = texte
        self.dateMessage = dateMessage
        self.idUtil = idUtil
        self.idSalon = idSalon

    #Recup message salon

    #Envoie message
    @staticmethod
    def envoieMessage(texte, idUtil, idSalon):
        return bdd.addMessage(texte, idUtil, idSalon)
