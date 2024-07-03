#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
#e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
#ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacao_a = 80000
taxa_anualA = 3/100
populacao_b = 200000
taxa_anualB = 1.5/100
anos = 0

for i in range (1000):
    if populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_anualA
        populacao_b += populacao_b * taxa_anualB
        anos += 1
    elif populacao_a >= populacao_b:
        break

print('Serão necessários', anos, 'anos para que a população do país A ultrapasse ou iguale a população do país B!')