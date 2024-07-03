#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.

#entrada
populacao_a = float(input('Informe a população inicial do país A:'))
taxa_anualA = float(input('Informe a taxa de crescimento anual do país A (%):'))
populacao_b = float(input('Informe a população inicial do país B:'))
taxa_anualB = float(input('Informe a taxa de crescimento anual do país B (%):'))

while populacao_a == 0 or taxa_anualA == 0 or populacao_b == 0 or taxa_anualB == 0:
    print('Informe um valor válido.')
    populacao_a = float(input('Informe a população inicial do país A:'))
    taxa_anualA = float(input('Informe a taxa de crescimento anual do país A (%):'))
    populacao_b = float(input('Informe a população inicial do país B:'))
    taxa_anualB = float(input('Informe a taxa de crescimento anual do país B (%):'))
    
#processamento
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_anualA
    populacao_b += populacao_b * taxa_anualB
    anos += 1
    
print('Serão necessários', anos, 'anos para que a população do país A ultrapasse ou iguale a população do país B.')