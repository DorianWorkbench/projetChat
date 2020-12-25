from flask import jsonify

from modele.Message import Message

def envoieMessageUtil(texte, idUtil, idSalon):
    try:
        #texte = request.form.get('texte')
        #idUtil = request.form.get('idUtil')
        #idSalon = request.form.get('idSalon')

        return Message.envoieMessage(texte, idUtil, idSalon)
    except:
        return jsonify({'data':{'error':True}})