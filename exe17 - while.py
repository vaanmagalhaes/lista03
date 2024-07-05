# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num1 = int(input('Digite o número a ser fatorado:'))
resultado = 1
contador = 1

while contador <= num1:
    resultado *= contador
    contador += 1

print(resultado)