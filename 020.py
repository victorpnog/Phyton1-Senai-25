#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

idade = int(input('Digite sua idade: '))

if idade >= 16 and idade <= 69:
    peso = float(input('\nDigte seu peso: '))
    if peso >= 50:
        alcool = input('\nVocê ingeriu álcool nas últimas 12 horas? Escreva SIM ou NÃO: ').lower().strip()[0]
        if alcool == 'n':
            sono = input('\nVocê dormiu 6h ou mais nas últimas 24h? Escreva SIM ou NÃO: ').lower().strip()[0]
            if sono == 's':
                documento = input('\nVocê está com seus documentos em mãos? Escreva SIM ou NÃO: ').lower().strip()[0]
                if documento == 's':
                    print ('\nParabéns, você atendeu todos os 5 requisitos para doação!')
                else:
                    print('\nNão pode doar porque não está com os documentos!')
            else:
                print('\nNão pode doar pelo sono!')
        else:
            print('\nNão pode doar pelo álcool!')
    else:
        print('\nNão pode doar pelo peso!')
else:
    print('\nNão pode doar pela idade!')