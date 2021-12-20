import pymongo
from pymongo import cursor


class Mongodb:
    def __init__(self):

        conn_str = "mongodb+srv://QQSM:qqsm@qqsm.8zhje.mongodb.net/qqms?retryWrites=true&w=majority"
        client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

        try:
            print("     ")
            #print("     able to connect to the server.")
        except Exception:
            print("     Unable to connect to the server.")

        db = client.get_database('qqsm')
        collection = db.participantes
        self.collection = collection

    def insertar_participante(self, participante):
        nombre = participante.nombre
        cedula = participante.cedula
        bolsa = participante.bolsa
        respuesta = participante.numero_respuesta
        item = {
            'nombre': nombre,
            'cedula': cedula,
            'bolsa': bolsa,
            'respuesta': respuesta
        }
        cursor = self.collection.find_one({'cedula': cedula})
        if cursor == None:
            self.collection.insert_one(item)
            print('     ¡Muy bien! \n')
        else:
            print('     Lo siento pero tú ya participaste \n')
            exit()
    
    def modificar_participante(self, participante):
        nombre = participante.nombre
        cedula = participante.cedula
        bolsa = participante.bolsa
        respuesta = participante.numero_respuesta
        cursor = self.collection.update_one({'cedula':cedula}, {"$set": {'bolsa':bolsa, 'respuesta':respuesta}})
    
    def Obtener_participante(self, participante):
        cursor = self.collection.find_one({'cedula': participante.cedula})
        print(cursor)
        print('     \n')

     

                
