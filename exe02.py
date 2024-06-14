#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

def login():
    """Campo de login"""
    usuario = input('Digite o usuário:')
    senha = input('Digite a senha')
    while senha == usuario:
        print('Não é permitido a senha ser igual ao usuário.')
        senha = input('Digite a senha')
    print('Cadastro realizado com sucesso.')

login()
