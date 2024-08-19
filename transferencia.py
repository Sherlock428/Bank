from database import Chaves, Transacao, Usuario
from decimal import Decimal, InvalidOperation
import os
import random



def transferir(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'TRANSFERIR PIX'.center(30)}
{'=' * 30}
""")
    try:
        chave = input("Digite a chave de quem vai receber: ")

        usuario_receptor = Chaves.select(Chaves, Usuario).join(Usuario).where(
            (Chaves.email == chave) | (Chaves.chave_aleatoria == chave) | (Chaves.cpf == chave) | (Chaves.numero_telefone == chave)).first()
        
        if usuario_receptor:
            usuario = usuario_receptor.usuario
            valor_t = Decimal(input("Qual valor você deseja transferir: "))

            if user.credito >= valor_t:    
                    print(f"""
{f'Transferir R${valor_t:.2f} para:'}
Nome: {usuario.nome}
CPF: {usuario.cpf}
    """)
            descricao = ''
            print(f"[0] -> Retornar ao Menu\n"
                        f"[1] -> Adicionar Descrição\n"
                        f"[Enter] -> Continuar\n")
    
            cont = input("Continuar: ")

            if cont == "0":
                    print("Transação Cancelada")
                    input("[Enter] -> Retornar ao Menu")
                    return
                    
            elif cont == "1":
                descricao = input("Adicione uma descrição: ")
                    
            if cont == "":
                descricao = "Sem Descrição"
                    
                user.credito -= valor_t
                usuario.credito += valor_t
                usuario.save()

                print("Transfêrencia Concluida\n")

                nova_transferencia = Transacao.create(descricao=descricao, chave=chave, remetente=user, valor=valor_t, destinatario=usuario)

                os.system('cls')
                print(f"""{'=' * 30}
{'Comprovante Trasação'.center(30)}
{'=' * 30}

Valor: R${nova_transferencia.valor:.2f}
{'-' * 30}
Para: {nova_transferencia.destinatario.nome}
Chave: {nova_transferencia.chave}

Descrição: {nova_transferencia.descricao}
Remetente: {nova_transferencia.remetente.nome}""")
                    # input("[Enter] -> Retornar ao Menu")
                return
        else:
            print("ERROR: Chave não encontrada")
    except (ValueError, TypeError, InvalidOperation):
        print("ERROR: Digite um valor válido")
        

   

def historico_transferencia(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'HISTORIOCO TRANSFERENCIA'.center(30)}
{'=' * 30}
""")
    historico = Transacao.select().where(Transacao.remetente == user)

    if not historico:
        print("Nenhum Transferencia realizada")

    for t in historico:
        try:
            print(f"""
{'=' * 30}
{'COMPROVANTE DE TRANSFERENCIA'.center(30)}
{'=' * 30}

Valor: R${t.valor:.2f}
{'-' * 30}
Para: {t.destinatario.nome}
Chave: {t.chave}

Descrição: {t.descricao}
Remetente: {t.remetente.nome}""")

            print('-' * 30)
    
        except Usuario.DoesNotExist as e:
            print(f"ERRO: {e}")



def cadastrar_chave(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'CADASTRAR CHAVE'.center(30)}
{'=' * 30}

[1] Chave CPF
[2] Chave Aleatoria
[3] Chave Email
[4] Chave Telefone
[5] Minhas Chaves
""")
    
    
    
    chaves = Chaves.select().where(Chaves.usuario == user).first()
    option = int(input("Selecione chave que deseja Cadastrar: "))

    
    if option == 1:
        cpf_chave = f'{user.cpf}'
        chaves_cpf = Chaves.get_or_none((Chaves.cpf == cpf_chave) & (Chaves.usuario == user))
        if chaves_cpf:
            print("Você já Cadastrou seu CPF")
            
        else:
            chaves.cpf = cpf_chave
            chaves.save()
            print("Chave Cadastrada")

    
    elif option == 2:
        chave = chave_aleatoria()
        chaves.chave_aleatoria = chave
        chaves.save()
        print(f"Chave Aleatoria Gerada: {chave}")

    
    elif option == 3:
        email_existe = Chaves.get_or_none((Chaves.email == user.email) & (Chaves.usuario == user))

        if not email_existe:
            chaves.email = user.email
            chaves.save()
            print("Seu Email foi Cadastrado como Chave:")
        
        else:
            print("Email já Cadastrado")
    
    elif option == 4:
        numero_cadastrado = Chaves.get_or_none((Chaves.numero_telefone == Chaves.numero_telefone) & (Chaves.usuario == user))

        if not numero_cadastrado:
                try:
                    numero_telefone = int(input("Digite seu número de telefone: "))
                
                except (ValueError, TypeError):
                    print("ERROR: Digite um valor válido")
                chaves.numero_telefone = numero_telefone
                chaves.save()
                print("Seu Número foi Cadastrado como Chave")

        else:
                print("Número já Cadastrado")

    elif option == 5:

        if chaves:
            
            if chaves.cpf:
                print(f"CPF: {chaves.cpf}")
            if chaves.cpf:
                print(f"EMAIL: {chaves.email}")
            if chaves.cpf:
                print(f"NÚMERO DE TELEFONE: {chaves.numero_telefone}")
            if chaves.cpf:
                print(f"CHAVE ALEATÓRIA: {chaves.chave_aleatoria}\n")

        else:
            print("Nenhuma Chave Encontrada")


def chave_aleatoria():
    conjunto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                "0","1","2","3","4","5","6","7","8","9",
                "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    
    chave = []

    for c in range(11):
        letra_random = random.choice(conjunto)
        chave.append(letra_random)

    chave_formatada = ''.join(chave)

    return chave_formatada