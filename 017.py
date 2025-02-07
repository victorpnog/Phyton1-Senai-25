#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

#leitura de dados
letra = input('Escreva uma letra: ').strip()[0]

#processamento
if letra in 'AEIOU':
    print(f'A letra é vogal: {letra}')
else:
    print(f'A letra é consoante: {letra}')