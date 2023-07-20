from flask_restful import Resource
from flask import request
from datetime import datetime


from modelo.modeloapostadores import db, Apostadores, ApostadoresSchema

apostador_schema = ApostadoresSchema()
class VistaCrearApostador(Resource):

    def post(self):

        try:
            if len(request.json["nombre"].strip())==0:
                return "Code 400: Hay campos obligatorios vacíos (nombre del apostador)", 400
            apostador = Apostadores.query.filter( Apostadores.nombreApostador == request.json["nombre"]).first()

        except:
            return "Code Error: Hay campos que faltan o incorrectos en la peticion (nombre del apostador)",400

        if not apostador is None:
            return "Code 412: El apostador ya existe, no se puede crear", 412

      
        apostador_nuevo = Apostadores(nombreApostador=request.json["nombre"])
        db.session.add(apostador_nuevo)
        db.session.commit()

        return "Apostador creado!",201


class VistaObtenerApostador(Resource):
    
    def get(self):
        
        
        try: 
   
          
            #usuario = Apostadores.query.all()

            return [apostador_schema.dump(ca) for ca in Apostadores.query.all()]

        except Exception as e:
            return "Error en la petiion. {} ".format(e), 401




class VistaSaludServicio(Resource):
    
    def get(self):       
       
            return "Code 200: Pong", 200   
