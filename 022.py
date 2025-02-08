#Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média, é insuficiente
# (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).

#leitura de dados
nota_1 = float(input('Escreva a 1a nota: '))
nota_2 = float(input('Escreva a 2a nota: '))
nota_3 = float(input('Escreva a 3a nota: '))
nota_4 = float(input('Escreva a 4a nota: '))
nota_5 = float(input('Escreva a 5a nota: '))

#processamento
media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5)/5

if media > 9:
    print(f'\nSua média foi {media}, EXCELENTE!')
elif media >= 7 and media <= 9:
    print(f'\nSua média foi {media}, BOA!')
elif media < 7 and media >= 6:
    print(f'\nSua média foi {media}, SUFICIENTE!')
else:
    media < 6
    print(f'\nSua média foi {media}, INSUFICIENTE!')

