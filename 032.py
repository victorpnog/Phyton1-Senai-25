#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

#leitura de dados
print('---------------------------')
print('Número pares entre dois números!')
inicio = int(input('\nDigite o primeiro número: '))
fim = int(input('Digite o segundo número: '))

#processamento
if inicio > fim:
    for x in range(fim, inicio +1):
        if x % 2 == 0:
            print(x)
else:
    for x in range (inicio, fim + 1):
        if x % 2 == 0:
            print(x)