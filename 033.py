#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500
'''
conta = 0
for numero in range (501):
    resultado = numero % 4 == 0
    if resultado == True:
        print(f'{numero} é multiplo de 1 a 500')
        conta = conta + numero
    else:
        0

print(f'\nA soma é: {conta}')
'''

soma = 0
for x in range (501):
    if x % 4 == 0:
        soma = soma + x
print(f'\nA soma dos múltiplos de 4 é: {soma}')