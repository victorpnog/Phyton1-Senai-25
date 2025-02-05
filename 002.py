#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

#leitura de dados
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade_nasc = input('Digite a Cidade de Nascimento: ')

#retorno de dados
print(f'\nSeu nome é: {nome}, tem {idade} anos e nasceu em {cidade_nasc}')