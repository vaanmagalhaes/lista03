# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

for i in range(100):
    nota = float(input('Digite uma nota entre 0 e 10:'))
    if 0 <= nota <= 10:
        print('Obrigada pela avaliação!')
        break
    else:
        print('Valor inválido, tente novamente.')