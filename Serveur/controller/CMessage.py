from flask import jsonify

from modele.Message import Message

def envoieMessageUtil(request):
    try:
        texte = request.form.get('texte')
        idUtil = request.form.get('idUtil')
        idSalon = request.form.get('idSalon')

        Message.envoieMessage(texte, idUtil, idSalon)

        return jsonify({'data':{'Message':{'success':True, 'message':"Message envoyé"}}})

    except:
        return jsonify({'data':{'error':True}})