#Uso do print e operações matemáticas
'''
print('Bem vindo ao Senai')
print(2+6)
print(100-12)
print(100/4)
print(2 ** 2)

#variaveis
idade = 18
print(idade + 3)

#print formatado
nome = 'Victor Nogueira'
idade = 23
print(f'Seu nome é {nome}, e sua idade é {idade}')

#input = leitura de informações
idade = input('Digite a sua idade: ')
print(f'Sua idade é {idade}')


#tipos de dados

lanche = int(input('\n\nDigite o valor do lanche: R$ '))
suco = int(input('Digite o valor do suco: R$ '))
valor_total_lanche = lanche + suco
print(f'\nO valor da refeição foi: R${valor_total_lanche}')


#String
nome = 'Luis Eulalio'


#Fatiamento
print(nome[0])
print(nome[1:5])
print(nome[1:5:2])

#Análise
print(len(nome)) #aqui vai contar tudo
print(nome.count('l')) #aqui vai contar a quantidade dessa letra
print(nome.find('l')) #aqui vai mostrar a posição que está a letra que colocar entre aspas

#Transformação
nome = input('Nome: ').strip() #aqui vai tirar todos os espaços
print(nome)
print(nome.upper())
print(nome.lower())
print(nome.replace('L','P'))


#Condicionais

#1
altura = float(input('Altura: '))

if altura > 1.5:
    print('Pode andar no brinquedo')
else:
    print('Quem sabe o ano que vem!')

#2
altura = float(input('Altura: '))

if altura > 2:
    print('Cuidado! Vai bater a cabeça')
elif altura < 1.5:
    print('Quem sabe ano que vem!')
else:
    print('Pode andar no brinquedo')
'''

#Estruturas de repetição

# for simples

for x in range (0,10):
    print(x)

for x in range (10, 0, -1):
    print (x)

soma = 0
for x in range (0,10):
    numero = int(input('Digite um numero: '))
    soma = soma + numero
print(soma)