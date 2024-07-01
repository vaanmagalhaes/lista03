# Faça um programa que leia um nome de usuário e a
# sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

for i in range (100):
    usuario = input('Digite seu usuário:')
    senha = input('Digite sua senha:')
    usuario = usuario.capitalize()
    senha = senha.capitalize()
    if usuario != senha:
        print('Login aceito.')
        break
    else:
        print('Erro. A senha não pode ser igual ao usuário, tente outra vez.')