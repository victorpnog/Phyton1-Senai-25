#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

#leitura de dados
conta = 0
for x in range (1,11):
    soma = int(input('Escreva um número:'))
    if soma %2 == 0:
        print(f'O número é {soma}')
        conta = conta + soma
    else:
        0

print(f'A soma é: {conta}')