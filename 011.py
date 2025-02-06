#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome

#leitura de dados
nome = input('Escreva seu nome completo:')
maiusculo = nome.upper()
minusculo = nome.lower()
contagem = len(nome.strip()) - 1 #aqui o len conta o tamanho da string, o strip tira o espaços. coloca -1 pq ele começa contando do numero 0

espaco = nome.find(' ') + 1 #ele procura o primeiro espaço pois o aspas está em vazio, soma mais um pois se não corta 1 antes dop espaço
primeiro_nome = nome[0:espaco] #mostra a 1a posição que é zero até o espaço

print(f'Nome em maiúsculo: {maiusculo}')
print(f'Nome em minúsculo: {minusculo}')
print(f'Contagem de letras {contagem}')
print(f'{primeiro_nome}')
