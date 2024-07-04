#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

num = 0

while num < 50:
    num+=1
    if num%2!=0:
        print(num, 'é um número ímpar')