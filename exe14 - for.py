#Faça um programa que peça 10 números inteiros, calcule e mostre
#a quantidade de números pares e a quantidade de números impares.

list=[]
par = 0
impar = 0

for i in range (0,10):
    list.append(int(input('Digite um número:')))
for i in list:
    if i%2==0:
        par = par+1
    elif i%2!=0:
        impar = impar+1
        
print('Dos números informados', par, 'são pares e', impar, 'são ímpares.')