#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez

#leitura de dados
frase = input('Escreva uma frase: ')
primeiro_a = frase.find ('a') + 1
ultimo_a = frase.rfind('a') + 1

#processamento de dados
print(f'\nEssa frase tem {frase.count('a')} "a"')
print(f'\nO primeiro "a" aparece na posição {primeiro_a}')
print(f'\nO último "a" aparece na posição {ultimo_a}')