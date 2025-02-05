#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

#entrada de dados
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))
n4 = float(input('Digite a nota 4: '))
n5 = float(input('Digite a nota 5: '))
n6 = float(input('Digite a nota 6: '))

#calculo
media_final = (n1+n2+n3+n4+n5+n6) / 6

#retorno dos dados/media
print(f'A média final é: {media_final:.2f}')
