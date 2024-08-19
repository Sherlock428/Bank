from database import Usuario, Chaves
from peewee import DoesNotExist
import os


def cadastrar_usuario():
    try:
        os.system('cls')
        print(f"""
{'=' * 30}
{'CRIAR NOVO USUARIO'.center(30)}
{'=' * 30}
""")
        nome = input("Digite seu nome: ")
        cpf  = int(input("Digite seu cpf: "))
        email = input("Digite Seu Email: ")
        senha = input("Digite sua senha: ")

        while len(senha) < 6:
            senha = input("Digite uma senha com pelo menos 6 caracteres: ")
        
        confirmar_senha = input("Confirme sua senha: ")

        while senha != confirmar_senha:
            senha = input("Digite sua senha: ")
            confirmar_senha = input("Confirme sua senha: ")

        novo_usuario = Usuario.create(nome=nome, email=email, cpf=cpf, senha=senha)
        
        chaves = Chaves.create(usuario=novo_usuario)
        
        print(f"usuario cadastrado {novo_usuario} ")
    except Exception as e:
        print(f"ERROR: {e} ")

def login():
    os.system('cls')
    print(f"""
{'=' * 30}
{'LOGIN'.center(30)}
{'=' * 30}
""")
    try:
        cpf = int(input("Digite o seu cpf: "))
        senha = input("Digite sua senha: ")

        usuario = Usuario.get(Usuario.cpf == cpf, Usuario.senha == senha)

        if usuario:
            return usuario
    
    except DoesNotExist:
        print("Usuario Não encontrado")
        input("[Enter] -> Retornar ao Menu")
    except (ValueError, TypeError):
        print("ERROR: CPF deve ser apenas numeros")
        input("[Enter] -> Retornar ao Menu")

