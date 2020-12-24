from flask import jsonify
from modele.Utilisateur import Utilisateur

def connexion(request):
    try:
        pseudo = request.form.get('pseudo')
        return Utilisateur.connexionUtilisateur(pseudo)
    except:
        return jsonify(error=True)


def inscription(request):
    try:
        pseudo = request.form.get('pseudo')

        return Utilisateur.inscriptionUtilisateur(pseudo)

    except:
        return jsonify(error = True)