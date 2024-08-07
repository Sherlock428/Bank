from usuario import Usuario
import os

usuarios_cadastrados = [Usuario(nome='teste', cpf=1, senha='123456', credito=10000, chaves=[], historico=[]), Usuario(nome='Y', cpf=2, senha='123456', credito=0, chaves=['2'], historico=[])]

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
        senha = input("Digite sua senha: ")

        while len(senha) < 6:
            senha = input("Digite uma senha com pelo menos 6 caracteres: ")
        
        confirmar_senha = input("Confirme sua senha: ")

        while senha != confirmar_senha:
            senha = input("Digite sua senha: ")
            confirmar_senha = input("Confirme sua senha: ")

        novo_usuario = Usuario(nome=nome, cpf=cpf, senha=senha, credito=0, chaves=[])
        usuarios_cadastrados.append(novo_usuario)
        print(f"usuarios cadastrados {usuarios_cadastrados}")
    except Exception as e:
        print(f"ERROR: {e} ")

def login():
    os.system('cls')
    print(f"""
{'=' * 30}
{'LOGIN'.center(30)}
{'=' * 30}
""")
    cpf = int(input("Digite o seu cpf: "))
    senha = input("Digite sua senha: ")

    for u in usuarios_cadastrados:
        if cpf == u.cpf and senha == u.senha:
            print(f"Usuario {u.nome}, encontrado!")
            return u

    
    print("Usuario Não encontrado")
    return None

