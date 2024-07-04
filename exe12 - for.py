#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50

num1 = int(input('Escolha um número de 1 a 10 para ver sua tabuada:'))
while num1<1 or num1>10:
    print('Digite um número válido.')
    num1 = int(input('Escolha um número de 1 a 10 para ver sua tabuada:'))

num2 = 10

for i in range (num2+1):
    mult = num1*i
    print(num1, 'x', i, '=', mult)