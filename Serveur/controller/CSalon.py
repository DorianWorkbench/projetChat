from modele.Salon import Salon


def listeSalon(request):
    idUtil = request.form.get('idUtil')
    return Salon.listerSalonUtil(idUtil)

def creationSalon(request):

    nomSalon = request.form.get('nomSalon')
    idUtil = request.form.get('idUtil')

    return Salon.ajoutSalon(nomSalon, idUtil)


def rejoindreSalon(request):

    idUtil = request.form.get('idUtil')
    nomSalon = request.form.get('nomSalon')

    return Salon.rejoindreSalon(idUtil, nomSalon)


def listeMessageSalon(request):

    idSalon = request.form.get('idSalon')

    return Salon.listeMessageSalon(idSalon)