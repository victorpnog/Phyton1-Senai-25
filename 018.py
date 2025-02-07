#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).

#leitura de dados
idade = int(input('Digite sua idade: '))

#processamento de dados
if idade >= 18:
    print('Você é maior de idade! Bora tomar uma!')
else:
    print('Você é menor de idade!')