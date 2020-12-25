import pyodbc
import datetime
import json

from flask import jsonify


def connexionBdd():
    try:
        server = 'DESKTOP-CJC5BPT\SQLEXPRESS'
        database = 'chat'
        username = 'sa'
        password = 'tennis'

        cnxn = pyodbc.connect(  'Driver={SQL Server};'
                                'Server='+server+';'
                                'Database='+database+';'    
                                'UID='+username+';'
                                'PWD='+password)
        print("Vous êtes connecté")

        return cnxn
    except:
        print("Impossible de se connecter à la base de données")


def ajouterUtilisateur(nomUtilisateur):
    try:
        co = connexionBdd().cursor()
        strSql = "INSERT INTO Utilisateur(pseudo) VALUES(?)"

        if not testPseudo(nomUtilisateur):

            co.execute(strSql, nomUtilisateur)
            co.commit()
            return jsonify({'data':{'Utilisateur':{'success': True, 'message': "Compte créé"}}})

        else:
            print("Le pseudo existe déjà")
            return jsonify({'data':{'Utilisateur':{'success':False, 'message':'Le pseudo existe déjà'}}})

    except:
        print("Erreur lors de l'execution de la requête ajoutUtil")


#Utilisateur

def testPseudo(pseudo):
    try:
        co = connexionBdd().cursor()
        strSql = "SELECT pseudo FROM Utilisateur WHERE pseudo = '"+pseudo+"'"

        co.execute(strSql)
        raw = co.fetchall()

        if len(raw) == 1:
            print("L'utilisateur existe déjà")
            return True
        else:
            print("L'utilisateur n'existe pas")
            return False
    except:
        print("Erreur sql")


def connexion(pseudo):
    co = connexionBdd().cursor()
    strSql = "SELECT id, pseudo FROM Utilisateur WHERE pseudo = '" + pseudo + "'"

    if testPseudo(pseudo):
        co.execute(strSql)
        raw = co.fetchone()
        print(type(raw))
        return jsonify({'data':{'Utilisateur':{'success':True, 'id':raw[0], 'pseudo':raw[1]}}})

    else:
        return jsonify({'data':{'Utilisateur':{'success':False, 'message':"Le pseudo n'existe pas"}}})

#Message

def addMessage(texte, idUtil, idSalon):
    try:
        co = connexionBdd()
        strSql = "INSERT INTO Message(texte, dateMessage, idUtil, idSalon) VALUES(?,CONVERT(datetime, ?, 121),?,?)"
        date = datetime.datetime.now()
        print(date)
        info = (texte, date, idUtil, idSalon)
        co.execute(strSql, info)

        co.commit()
        co.close()
        cnx = connexionBdd().cursor()

        strSql = "SELECT pseudo FROM Utilisateur WHERE id = "+str(idUtil)

        cnx.execute(strSql)

        raw = cnx.fetchone()

        print(raw[0])
        print("message envoyé")

        return json.loads(json.dumps({'data':{'sucess': True,'Message':{'texte': texte, 'dateMessage': str(date), 'pseudo': raw[0]}}}))

    except:
        return False
addMessage("test", 1, 1)
#Serveur

def creationSalon(nomSalon, idUtil):
    try:

        if not verifSalon(nomSalon):

            co = connexionBdd()

            strSql = "INSERT INTO Salon(nomSalon, idUtil) VALUES(?,?)"

            info = (nomSalon, idUtil)
            co.execute(strSql, info)
            co.commit()
            co.close()

            idSalon = recupSalonByName(nomSalon)[0]

            ajoutUtilSalon(idUtil, idSalon)

            print("Salon Créé")
            return jsonify({'data':{'Salon':{'success':True, 'message':"Salon créé"}}})
                #json.loads(json.dumps({'success':True, 'message':"Salon Créé"}))
        else:
            return jsonify({'data':{'Salon':{'success':False, 'message':"Le salon existe déjà"}}})
                #json.loads(json.dumps({'success':False, 'message':"Le salon existe déjà"}))
    except:
        print("erreur sql")

def ajoutUtilSalon(idUtil, idSalon):
    try:
        co = connexionBdd()
        strSql = "INSERT INTO Salon_Util(idUtil, idSalon) VALUES(?,?)"
        info = (idUtil, idSalon)
        co.execute(strSql, info)
        print(strSql)

        co.commit()
        co.close()

        print("Ajout de l'utilisateur au serveur nouvellement créé")

    except:
        print("Erreur sql")

def rejoindreSalon(idUtil, nomSalon):
    try:
        if verifSalon(nomSalon):
            idSalon = recupSalonByName(nomSalon)[0]
            print(idSalon)
            if not verifUserInSalon(idUtil, idSalon):
                ajoutUtilSalon(idUtil, idSalon)

                return json.loads(json.dumps({'data':{'Salon':{'success': True, 'message': "Utilisateur ajouté" }}}))
            else:
                print("L'utilisateur est déjà dans le salon")
                return json.loads(json.dumps({'data':{'Salon':{'success': False, 'message':"L'utilisateur est déjà dans le salon"}}}))
                    #jsonify({'error': "L'utilisateur est déjà dans le salon"})
        else:
            print("Le salon n'existe pas")
            return json.loads(json.dumps({'data':{'Salon':{'success': False, 'message': "Le salon n'existe pas"}}}))
                #jsonify({'error': "Le salon n'existe pas"})
    except:
        print("erreur sql")

def verifSalon(nomSalon):
    try:
        co = connexionBdd().cursor()
        strSql = "SELECT nomSalon, idUtil FROM Salon WHERE nomSalon = '"+nomSalon+"'"

        co.execute(strSql)
        raw = co.fetchall()

        if len(raw) == 1:
            print("Le salon existe")
            return True
        else:
            print("Le salon n'existe pas")
            return False

    except:
        print("erreur sql")



def recupSalonByName(nomSalon):
    try:
        co = connexionBdd().cursor()
        strSql = "SELECT id, nomSalon, idUtil FROM Salon WHERE nomSalon = '"+nomSalon+"'"

        co.execute(strSql)
        print("execution")
        raw = co.fetchone()

        return raw

    except:
        print("Erreur sql")

def verifUserInSalon(idUtil, idSalon):
    try:
        co = connexionBdd().cursor()
        strSql = "SELECT * FROM Salon_Util WHERE idUtil = "+str(idUtil)+" and idSalon = "+str(idSalon)+""
        print(strSql)
        co.execute(strSql)
        raw = co.fetchall()
        print(len(raw))
        if len(raw) == 1:
            print("Il est dans le salon")
            return True
        else:
            print("Il n'est pas dans le salon")
            return False

    except:
        print("Erreur sql")

def listerSalonParUtil(idUtil):
    try:
        co = connexionBdd().cursor()
        strSql = "SELECT idSalon, nomSalon, Salon.idUtil FROM Salon, Salon_Util WHERE Salon_Util.idSalon=Salon.id and Salon_Util.idUtil="+str(idUtil)+""
        listJson = []
        co.execute(strSql)
        raw = co.fetchall()
        print(raw)
        if len(raw) >= 1:
            for row in raw:
                listJson.append({'idServeur':row[0], 'nomServeur':row[1], 'createurSalon':row[2]})

            json.dumps(listJson)
            jsonFinal = json.dumps({"Salon":(listJson)})

            result = json.loads(jsonFinal)

            print(result)

            return result
        else:
            #print(json.loads(json.dumps({'Salon': False, 'message':"Vous n'avez rejoint aucun serveur"})))
            return json.loads(json.dumps({'Salon': False, 'message':"Vous n'avez rejoint aucun serveur"}))
    except:
        print("Erreur")

def listeMessageSalon(idSalon):
    try:
        co = connexionBdd().cursor()
        listMessage = []
        strSql = "SELECT Message.id, texte, dateMessage, pseudo FROM Utilisateur, Message WHERE Utilisateur.id = Message.idUtil and idSalon = "+str(idSalon)+""
        co.execute(strSql)
        raw = co.fetchall()
        print(len(raw))

        if len(raw) >= 1:
            for row in raw:
                listMessage.append({'id':row[0],'message':row[1], 'dateMessage':str(row[2]), 'pseudo':row[3]})

            json.dumps(listMessage)

            jsonFinal = json.dumps({'data':{'success':True,'Message':(listMessage)}})
            result = json.loads(jsonFinal)

            return result
        else:
            return json.loads(json.dumps({'data':{'success': False, 'message' : "Aucun message"}}))
    except:
       print("Erreur")