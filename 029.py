#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

#leitura de dados
numero = int(input('Digite um número: '))

#processamento
for tabuada in range (1,11):
    resultado = tabuada * numero
    print(f'{numero} x {tabuada} = {resultado}')