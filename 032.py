#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

#leitura de dados
print('---------------------------')
print('Descubra se é par ou ímpar!')
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

#processamento
for numero in range (numero1, numero2+1):
    resultado = numero % 2 == 0
    if resultado == True:
        print(f'{numero} é Par')
    else:
        print(f'{numero} é Ímpar')