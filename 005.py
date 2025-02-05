#Escreva um programa que converta real para o Franco Congolês

#Leia o valor em real
real = float(input('Digite a quantidade em reais para serem convertidos em FC: '))

#processamento do dado / conversão
franco_congoles = real * 495.75602

#saida de dados
print(f'R$ {real:.2f} vale hoje CDF {franco_congoles:.2f}')