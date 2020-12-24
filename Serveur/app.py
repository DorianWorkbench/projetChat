from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send
from flask_cors import CORS

from controller import CUtilisateur, CMessage, CSalon

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins = '*')

@app.route('/', methods=['GET'])
def home():
    return jsonify(accueil = "Connected")

@socketio.on('message')
def handleMessage(msg):
    print('Message: '+msg)
    send(msg, broadcast=True)

#Utilisateur
#Fait
#Fait client
@app.route('/utilisateurConnexion', methods=['POST'])
def connexion():
    return CUtilisateur.connexion(request)

#Fait
#Fait client
@app.route('/utilisateurInscription', methods=['POST'])
def inscription():
    return CUtilisateur.inscription(request)


#Message
#Fait
#Fait client
@app.route('/messageEnvoie', methods=['POST'])
def envoie():
    return CMessage.envoieMessageUtil(request)

#Salon
#Fait
#Fait client
@app.route('/creationSalon', methods=['POST'])
def creationSalon():
    return CSalon.creationSalon(request)

#Fait
#Fait client
@app.route('/rejoindreSalon', methods=['POST'])
def rejoindreSalon():
    return CSalon.rejoindreSalon(request)

#Fait
#Fait client
@app.route('/listeServeur', methods=['POST'])
def listeServeur():
    return CSalon.listeSalon(request)

#Fait
#Fait client
@app.route('/listeMessageServeur', methods=['POST'])
def listMessageServeur():
    return CSalon.listeMessageSalon(request)

if __name__ == "__main__":
    socketio.run(app, port=9000)
    #app.run(port="9000")