#Faça um programa que peça dois números, base e expoente, calcule e
#mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.

base = int(input('Digite o número da base:'))
expoente = int(input('Digite o número do expoente:'))
resultado = 1
contador = 1

while contador <= expoente:
    resultado *= base
    contador+=1
    
print(base, 'elevado a', expoente, 'é igual a', resultado)