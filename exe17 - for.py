# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num1 = int(input('Digite o número a ser fatorado:'))
resultado = 1
for i in range(1, num1+1):
    resultado *= i

print(resultado)