from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from datetime import timedelta

from vistaapostadores import VistaCrearApostador, VistaObtenerApostador, VistaSaludServicio

from modelo.modeloapostadores import db, Apostadores, ApostadoresSchema

user_schema = ApostadoresSchema()

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123456@192.168.1.12:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 
app.config['PROPAGATE_EXEPTIONS'] = True 

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)

api.add_resource(VistaCrearApostador,'/apostador')
api.add_resource(VistaObtenerApostador,'/apostador')
api.add_resource(VistaSaludServicio,'/')

