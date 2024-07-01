# Faça um programa que leia um nome de usuário e a
# sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input('Digite o usuário:')
senha = input('Digite a senha:')
usuario = usuario.capitalize()
senha = senha.capitalize()
while usuario == senha:
    print('Erro! O usuário não pode ser igual a senha, tente outra vez.')
    usuario = input('Digite o usuário:')
    senha = input('Digite a senha:')
    usuario = usuario.capitalize()
    senha = senha.capitalize()