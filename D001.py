#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário
#Saída esperada: A posição do objeto no tempo x é de y (m)

#entrada dos dados
velocidade_inicial = float(input('Informe a velocidade inicial em metros por segundos: '))
velocidade_final = float(input('Informe a velocidade final em metros por segundos: '))
tempo_incial = float(input('Informe o tempo inicial em segundos: '))
tempo_final = float(input('Informe o tempo final segundos: '))

#processamento de dados
delta_velocidade = velocidade_final - velocidade_inicial
delta_tempo = tempo_final - tempo_incial
aceleracao = delta_velocidade/delta_tempo

#saída do valor da aceleração
print(f'\nA aceleração é: {aceleracao} m/s^2')

#processamento da velocidade
velocidade = velocidade_inicial + aceleracao * delta_tempo

#formula final da posição do Movimento Retilíneo Uniformemente Variado (MRUV)
formula_posicao = 0 + velocidade_inicial * delta_tempo + ((aceleracao * delta_tempo **2)/2)

'''
#saída da velocidade inicial / aceleração / da posição do móvel /
print(f'\nA velocidade inicial foi {velocidade_inicial}m/s \nAceleração de {aceleracao}m/s^2 \n\nPortanto, a posição de um móvel após os dados é de: {formula_posicao}m')
'''
print(f'\nA posição do objeto no tempo {delta_tempo}s é de {formula_posicao}m')