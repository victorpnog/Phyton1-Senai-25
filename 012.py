#Crie um programa que leia um nome, e mostre o primeiro e o último nome

#leitura de dados
nome = input('Escreva seu nome:')

#Processamento
espaco_esquerda = nome.find(' ')
espaco_direira = nome.rfind(' ') + 1

#impressão de dados
print(f'Primeiro nome: {nome[0:espaco_esquerda]}')
print(f'Último nome: {nome[espaco_direira:]}')

