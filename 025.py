#Crie um programa para jogar JOKEMPO, usando a função random.randint
import random
import time

#leitura de dados
print('------------------------------------------------------')
jo = int(input('1.PEDRA\n2.PAPEL\n3.TESOURA\n\n ').strip()[0])

print('------------------------------------------------------')
time.sleep(1.5)
print('JÓ')
time.sleep(1.5)
print('KEM')
time.sleep(1.5)
print('PÔ!')
print('------------------------------------------------------')

#processamento:
pc = random.randint(1,3)
print(f'\nA escolha do computador foi: {pc}')
print('------------------------------------------------------')
time.sleep(1.5)

#processamento batalha:
if (jo == pc):
    print('\nEmpate!')
elif (jo == 1 and pc == 2) or (jo == 2 and pc) == 3 or (jo == 3 and pc == 1):
    print('\nComputador ganha!')
elif (jo == 1 and pc == 3) or (jo == 2 and pc) == 1 or (jo == 3 and pc == 2):
    print('\nJogador ganha!')
else:
    print('\nVocê deve ter jogado outro número além de 1/2/3... Sua mula!!')