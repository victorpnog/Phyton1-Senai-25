#Crie um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra “a”
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece na última vez

#leitura de dados
frase = input('Escreva uma frase: ')

#processamento de dados
print(f'\nEssa frase tem {frase.count('A')}' 
      f'\nO primeiro "a" aparece na posição {frase.find ('A') + 1 }'
      f'\nO último "a" aparece na posição {frase.rfind('A') + 1 }')