from peewee import *

db = SqliteDatabase('Usuarios.db')

class BaseModel(Model):
    
    class Meta:
        database = db

class Usuario(BaseModel):
    nome = CharField()
    email = CharField(unique=True)
    cpf  = CharField(unique=True)
    credito = DecimalField(default=0)
    senha = CharField()
    

class Chaves(BaseModel):
    email = CharField(unique=True, null=True)
    cpf = CharField(unique=True, null=True)
    numero_telefone = CharField(unique=True, null=True)
    chave_aleatoria = CharField(unique=True, null=True)
    usuario = ForeignKeyField(Usuario, backref='chaves')

class Transacao(BaseModel):
    descricao = TextField(null=True)
    chave = CharField()
    remetente = ForeignKeyField(Usuario, backref='Usuario')
    valor = DecimalField()
    destinatario = ForeignKeyField(Usuario, backref='User')
    # historico = ForeignKeyField(Usuario, backref='histo')

def conectar_banco():
    db.connect()
    db.create_tables([Usuario, Chaves, Transacao])