#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
registro = 0

while registro < 5:
    numero = float(input('Informe um número:'))
    soma+= numero
    registro+=1
    
media = soma/5

print('A soma dos números informados é:', soma, '. E a média desses números é:', media)
