#Uso do print e operações matemáticas

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