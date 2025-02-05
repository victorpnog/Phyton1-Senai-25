#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

#leitura de dados
raio = float(input('Digite o raio da esfera: '))

#processamento de dados
volume = (4/3) * 3.1415 * raio**3
area = 4 * 3.1415 * raio**2

#retorno de dados
print(f'\nO volume da esfera é {volume:.2f}')
print(f'\nA área da esfera é {area:.2f}')