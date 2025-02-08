#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente
# (1 é segunda-feira, 2 é terça-feira, etc.).

#leitura de dados
dia = int(input('Digite o dia da semana: '))

#processamento de dados
if dia == 1:
    print('Segunda')
elif dia == 2:
    print('Terça')
elif dia == 3:
    print('Quarta')
elif dia == 4:
    print('Quinta')
elif dia == 5:
    print('Sexta')
elif dia == 6:
    print('Sábado')
elif dia == 7:
    print('Domingo')
else:
    print('Número não válido!')