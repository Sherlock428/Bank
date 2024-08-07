from usuario import  Transacao
from sistema_login import usuarios_cadastrados
import os

def transferir(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'TRANSFERIR PIX'.center(30)}
{'=' * 30}
""")
    try:
        chave = input("Digite a chave de quem vai receber: ")

        for u in usuarios_cadastrados:
            if chave in u.chaves:
                valor_t = float(input("Qual valor você deseja transferir: "))

                if user.credito >= valor_t:    
                    print(f"""
{f'Transferir R${valor_t:.2f} para:'}
Nome: {u.nome}
CPF: {u.cpf}
    """)
                    descricao = ''
                    print(f"[0] -> Retornar ao Menu\n"
                        f"[1] -> Adicionar Descrição\n"
                        f"[Enter] -> Continuar\n")
                    
                    cont = input("Descrição: ")

                    if cont == "0":
                        print("Transação Cancelada")
                        input("[Enter] -> Retornar ao Menu")
                        return
                    
                    elif cont == "1":
                        descricao = input("Adicione uma descrição: ")
                    
                    if cont is "":
                        descricao = "Sem Descrição"
                    
                    user.credito -= valor_t
                    u.credito += valor_t

                    print("Transfêrencia Concluida\n")

                    nova_transferencia = Transacao(descricao=descricao, chave=chave, valor=valor_t, destinatario=u, remetente=user)

                    user.historico.append(nova_transferencia)
                    u.historico.append(nova_transferencia)
                    os.system('cls')
                    print(nova_transferencia)
                    # input("[Enter] -> Retornar ao Menu")
                    return
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")
        input("[Enter] -> Retornar ao Menu")

    print("Chave não encontrada. Transação cancelada")
def historico_transferencia(user):
    print(f"""
{'=' * 30}
{'HISTORIOCO TRANSFERENCIA'.center(30)}
{'=' * 30}
""")
    for t in user.historico:
        print(f"{t}")
        print('-' * 30)
    
    input("[Enter] -> Retornar ao Menu")

def cadastrar_chave(user):
    print(f"""
{'=' * 30}
{'CADASTRAR CHAVE'.center(30)}
{'=' * 30}

[1] Chave CPF
[2] Chave Aleatoria
""")
    
    option = int(input("Selecione chave que deseja Cadastrar: "))

    if option == 1:
        cpf_chave = f'{user.cpf}'
        if cpf_chave not in user.chaves:
            user.chaves.append(cpf_chave)
            print("Chave Cadastrada")
            input("[Enter] -> Retornar ao Menu")

        else:
            print("Você já Cadastrou seu CPF")
            input("[Enter] -> Retornar ao Menu")

    
    elif option == 2:
        pass