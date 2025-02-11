#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500
conta = 0
for numero in range (1,501):
    resultado = numero % 4 == 0
    if resultado == True:
        print(f'{numero} é multiplo de 1 a 500')
        conta = conta + numero
    else:
        0

print(f'\nA soma é: {conta}')