from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Apostadores(db.Model):
    id                  = db.Column(db.Integer, primary_key = True)
    nombreApostador     = db.Column(db.String(50))


class ApostadoresSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Apostadores
        load_instance = True

