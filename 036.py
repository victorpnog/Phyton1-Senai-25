#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maior_peso = 0
menor_peso = 100000

for leitura in range (1,8):
    peso = float(input('Digite seu peso: '))
    print("_________________")
    if maior_peso < peso:
        maior_peso = peso
    else:
        0
    if menor_peso > peso:
        menor_peso = peso
    else:
        0

print (f' O maior peso é: {maior_peso} kgs'
       f'\n O menor peso é: {menor_peso} kgs')