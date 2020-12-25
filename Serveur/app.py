from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send, join_room, leave_room, emit
from flask_cors import CORS

from controller import CUtilisateur, CMessage, CSalon

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins = '*')


@socketio.on('message')
def handleMessage(msg):
    #texte, idUtil, idSalon
    message = CMessage.envoieMessageUtil(msg['texte'], msg['idUtil'], msg['idSalon'])['data']['Message']
    send(message['pseudo']+" : "+message['texte']+" à "+message['dateMessage'], room=msg['idSalon'])



#Attention, ne pas mettre l'affichage de tous les salons dans la connexion.
@socketio.on('connect')
def connexion():
    #Création d'évènement sur le socket s'effectuant au démarrage de la tchat room.
    @socketio.on('join')
    def on_join(data):
        username = data['data']['username']
        room = data['data']['roomId']
        join_room(room)
        send(username + " est entré dans le salon à l'id : "+str(room), room = room)

    # PAS BON, à voir si je peux l'envoyer sur chaque utilisateur et non pour tout le monde
    """@socketio.on('login')
    def test_login(data):
        if CSalon.listeMessageSalon(data['idSalon'])['data']['success'] == False:
            send("Aucun message n'a été envoyé", broadcast=True)
        else :
            listeMessage = CSalon.listeMessageSalon(data['idSalon'])['data']['Message']
            print(listeMessage)
            for message in listeMessage:
                send(message['pseudo']+" : "+message['message']+" à "+message['dateMessage'], broadcast=True)
"""


@app.route('/', methods=['GET'])
def home():
    return jsonify(accueil = "Connected")

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
#@app.route('/messageEnvoie', methods=['POST'])
#def envoie():
 #   return CMessage.envoieMessageUtil(request)

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