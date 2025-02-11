#Escreva um programa que verifique se uma palavra é um palíndromo.

#leitura de dados:
palavra = input('Digite a plavra: '.strip().lower())
pont = 0

for i in range(0, len(palavra)):
    if palavra[i] == palavra[-i -1]:
        pont = pont + 1

if pont == len(palavra):
    print('É um palindromo')
else:
    print('Não é')

'''
if palavra == palavra[::-1]
    print('É palíndromo')
else:
    print('Não é')
'''



if palavra == palavra[::-1]:
    print('É um palíndromo')