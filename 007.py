#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#leitura de dados
numero = int(input('Escreva um número: '))

#processamento o dado
dobro = numero * 2
triplo = numero  * 3
raiz_quadrada = numero ** (0.5)

#retorno dos dados na tela
print(f'\nO dobro de {numero} é: {dobro}'
      f'\nO triplo de {numero} é: {triplo}'
      f'\nA raiz quadrada de {numero} é: {raiz_quadrada:.2f}')

#orientada a objeto:
f'''
print(f'\nO dobro de {numero} é: {numero * 2}'
      f'\nO triplo de {numero} é: {numero * 3 }'
      f'\nA raiz quadrada do {numero} é: {numero ** (0.5)}')
'''