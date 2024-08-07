from sistema_login import cadastrar_usuario, login
from utilidades import  ui_user

def main():

    while True:
        print(f"""
{'=' * 30}
{'BANK NEWSTER'.center(30)}
{"=" * 30}

[1] Criar uma Conta
[2] Logar em uma Conta
[3] Sair
{'-' * 30}
""")
        option = int(input("Escolha uma opção: "))

        if option == 1:
            cadastrar_usuario()
        
        elif option == 2:
            usuario = login()

            if usuario:
                ui_user(usuario)

        elif option == 3:
            print("Obrigado por usar nosso sistema")
            break

if __name__ == "__main__":
    main()