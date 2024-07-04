#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
#Faça um programa que gere a série até que o valor seja maior que 500.

termo = int(input('Digite o número de termos para a série de Fibonacci:'))
num1 = 1
num0 = 1

for i in range(termo):
    print(num1)
    num2 = num1
    num1+=num0
    num0 = num2
    if num1>500:
        break

print('O próximo valor ultrapassa o limite de segurança estabelecido pelo sistema.')