#Crie um programa para jogar JOKEMPO, usando a função random.randint
import random

#leitura de dados
jo = int(input('Digite: "1" para PEDRA / "2" para PAPEL / "3" para TESOURA: ').strip()[0])

#processamento:
pc = random.randint(1,3)
print(f'\nA escolha do computador foi: {pc}')

#processamento batalha:
if jo == pc:
    print('\nEmpate!')
elif jo == 1 and pc == 2 or jo == 2 and pc == 3 or jo == 3 and pc == 1:
    print('\nComputador ganha!')
elif jo == 1 and pc == 3 or jo == 2 and pc == 1 or jo == 3 and pc == 2:
    print('\nJogador ganha!')
else:
    print('\nVocê deve ter jogado outro número além de 1/2/3... Sua mula!!')