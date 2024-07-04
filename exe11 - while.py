#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
soma = 0
print('os números no intervalo entre', num1, 'e', num2, 'são:')

while num1 < num2-1:
    num1 = num1 + 1
    print(num1)
    soma = soma + num1
    
print('A soma dos números no intervalo é:', soma)