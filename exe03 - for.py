# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd'

for i in range(100):
    nome = input('Digite seu nome: (é necessário mais de 3 caracteres):')
    idade = float(input('Digite sua idade (entre 0 e 150):'))
    salario = float(input('Digite seu salário (é necessário um valor maior que zero):'))
    sexo = input('Digite seu sexo(F ou M):')
    sexo = sexo.capitalize()
    estado_civil = input('Digite seu estado civil (S - solteiro, C - casado, V - viúvo, D - Divorciado):')
    estado_civil = estado_civil.capitalize()
    if len(nome) > 3 and 0 <= idade <= 150 and salario > 0 and sexo in ['F', 'M'] and estado_civil in ['S', 'C', 'V', 'D']:
        print('Obrigado pelas informações.')
        break
    else:
        print('Algum dado informado está errado, tente outra vez.')