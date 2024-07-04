#Faça um programa que peça 10 números inteiros, calcule e mostre
#a quantidade de números pares e a quantidade de números impares.

list=[]
par = 0
impar = 0
contador = 0
i = 0

while contador <10:
    list.append(int(input('Digite um número:')))
    contador = contador+1
    if list[i]%2==0:
        par = par+1
    else:
        impar = impar+1
    i = i+1
        
print('Dos números informados', par, 'são pares e', impar, 'são ímpares.')