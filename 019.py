#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

#leitura de dados
numero = float(input('Digite um número:'))

#processamento
if numero >= 0 and numero <= 10:
    print('O número está entre 0 e 10')
elif numero > 10 and numero <= 20:
    print('O número está entre 10 e 20')
else:
    print('O número não está nos conjuntos')
