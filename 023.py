#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

#leitura de dados
frase = input('Escreva uma frase: ').lower().strip()[0]

#processamento
if frase in 'aeiou':
    print('\nComeça com vogal!')
else:
    print('\nComeça com consoante!')
