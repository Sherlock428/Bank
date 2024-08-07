from usuario import Usuario
from transferencia import historico_transferencia, transferir, cadastrar_chave
import os

def sacar(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'SAQUE'.center(30)}
{'=' * 30}
""")
    try:
        saque = float(input("Qual valor deseja sacar: "))

        if saque <= user.credito:
            user.credito -= saque
            print(f"Você sacou cerca de {saque:.2f} de sua conta, seu saldo atual é de {user.credito:.2f}")

        else:
            print("Você não tem o valor suficiente para realizar o saque")
    except (ValueError, TypeError):
        print("Digite um valor válido")
        
    input("[Enter] -> Retornar ao Menu")


def depositar(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'DEPOSITAR'.center(30)}
{'=' * 30}
""")
    try:
        deposit = float(input("Qual valor deseja depositar: "))

        if deposit > 0:
            user.credito += deposit
            print(f"Você depositou R${deposit:.2f} em sua conta, seu saldo atual é de {user.credito:.2f}")
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")

def area_transferencia(user):
    os.system('cls')
    print(f"""
{'=' * 30}
{'Area PIX'.center(30)}
{'=' *30}

[1] Transferencia
[2] Historico de Transferencia
[3] Cadastrar Chave
""")
    try:
        opcao = int(input("Selecione: "))

        if opcao == 1:
            transferir(user)
            
        elif opcao == 2:
            historico_transferencia(user)

        elif opcao == 3:
            cadastrar_chave(user)
    
    except (ValueError, TypeError):
        print("ERROR:")

    input("[Enter] -> Retornar ao Menu")

def ui_user(user):

    ver_saldo = False
    mostrar_saldo = "_____"
    while True:

        if not user:
            print("Usuario não Encontrado")
            input("[Enter] -> Retonar ao Menu")
            return

        
        print(f"""
{'=' * 30}
{'BANCO NEWSTER'.center(30)}
{'=' * 30}
{f'Saldo: R${mostrar_saldo}'}
{'-' * 30}

[1] Mostrar Saldo
[2] Sacar
[3] Deposistar
[4] Area Transferencias

[0] Sair
""")
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                if ver_saldo == True:
                    mostrar_saldo = "_____"
                    ver_saldo = False
                
                elif ver_saldo == False:
                    mostrar_saldo = f'{user.credito:.2f}'
                    ver_saldo = True
            elif opcao == 2:
                sacar(user)
            elif opcao == 3:
                depositar(user)
            elif opcao == 4:
                area_transferencia(user)
            elif opcao == 0:
                break
        
        except (ValueError, TypeError):
            print("Digite um valor válido: ")