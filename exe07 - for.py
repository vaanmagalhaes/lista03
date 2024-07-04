#Faça um programa que leia 5 números e informe o maior número.

maior_numero = float('-inf')
for i in range(5):
    numero = float(input('Digite um número:'))
    if numero > maior_numero:
        maior_numero = numero
        
print('O maior número informado foi:', maior_numero)