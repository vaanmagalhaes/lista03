#Faça um programa que receba dois números inteiros
#e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
print('os números no intervalo entre', num1, 'e', num2, 'são:')

for i in range (num1+1, num2):
    print(i)