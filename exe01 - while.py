# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

for _ in range(100):
    nota = float(input('Informe uma nota entre 0 e 10:'))
    if 0 <= nota <= 10:
        print('Obrigado pela avaliação.')
        break
    else:
        print('Nota inválida, tente novamente.')