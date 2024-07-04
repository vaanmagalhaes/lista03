#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.

termo = int(input('Digite o número de termos para a série de Fibonacci:'))
num1 = 1
num0 = 1
contador = 0

while contador <= termo:
    print(num1)
    num2 = num1
    num1+=num0
    num0 = num2
    contador = contador+1
