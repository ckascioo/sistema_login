from os import system
from getpass import getpass
import stdiomask
from time import sleep

# MENU
def intro():
    print('Bem-vindo a este sistema')
    print('Escolha uma opção:')
    print('[1] - Fazer login')
    print('[2] - Cadastrar novo usuário')
    opcao = input('Digite uma opção: ')
    if not opcao:
        print('Opção invalida')
        sleep(2)
        return None
    return int(opcao)

# Login
def login():
    user_login = input('Digite seu usuário: ')
    user_senha = stdiomask.getpass(prompt='Digite sua senha: ', mask='*')
    return(user_login, user_senha)

# Usuarios
def db_usuarios(user_login, user_senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='UTF-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip() # Corrigido
                usuarios.append(linha.split())
        # Login, senha = login()
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if nome == user_login and user_senha == password:
                    return True
    except FileNotFoundError:
        return False

def voltar():
    input('Precione qualquer tecla para voltar...')

while True:
    system('cls')
    opcao = intro()

    if opcao == 2:
        # Cadastro
        user_login, user_senha = login()
        if user_login == user_senha:
            print('Sua senha deve ser diferente de login.')
            senha = getpass('Digite sua senha: ')
        user = db_usuarios(user_login, user_senha)
        if user == True:
            print('Usuário já existe!')
            voltar()
        else:
            with open('usuarios.txt', 'a+', encoding='utf-8', newline='') as arquivo:
                arquivo.writelines(f'{user_login} {user_senha}\n')
            print(f'O usuário {user_login} foi cadastrado!')
            voltar()

    elif opcao == 1:
        # Fazer Login
        user_login, user_senha = login()
        user = db_usuarios(user_login, user_senha)
        if user == True:
            print(f'Login com usuário {user_login} realizado com sucesso!')
            voltar()
        else:
            print('Nome de usuário ou senha invalidos')
            voltar()
    else:
        input('Precione enter para finalizar...')
        print('Finalizando sistema')
        sleep(2)
        break