#Escreva um programa que leia o
#Nome, idade e sexo de 4 pessoas. No final mostre:
#a média de idade do grupo
#Qual é o homem mais velho
#Quantas mulheres têm menos de 20 anos

media = 0
maior_homem = 0
nome2 = ' '
mulher_20 = 0
for cadastro in range (1,5):
    nome = input('\n\nDigite seu nome: '.strip())
    idade = int(input('Digte sua idade: '.strip()))
    sexo = (input('Digite "F" para feminino, "M" para masculino: ').upper().strip())

    print ("_________________")
    media = media + idade
    if maior_homem < idade and sexo == 'M':
        maior_homem = idade
        nome2 = nome
    else:
        0

    if sexo == 'F' and idade < 20:
        mulher_20 = mulher_20 + 1
    else:
        0

media = media / 4
print(f' Média de idade do grupo: {media}'
      f'\n Maior idade entre os homens: {nome2} , com {maior_homem} anos '
      f'\n Quantidade de mulheres com menos de 20: {mulher_20}')
