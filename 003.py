#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

#leitura de dados
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#processamento dos dados
nome_completo = nome + ' ' + sobrenome

#retorno de dados
print (f'\nSeu nome é: {nome_completo}')