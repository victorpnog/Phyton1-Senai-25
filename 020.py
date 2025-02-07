#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

idade = int(input('Digite sua idade: '))

if idade >= 16 and idade <= 69:
    peso = float(input('Digte seu peso: '))
    if peso >= 50:
        alcool = input('Você ingeriu álcool nas últimas 12 horas? Escreva SIM ou NÃO: ').lower().strip()[0]
        if alcool == 'n':
            print('Não pode doar')
        else:
            sono = input('Você dormiu 6h nas últimas 24h? Escreva SIM ou NÃO: ').lower().strip()[0]
            #continuar daqui!
    else:
        print('Não pode doar')
else:
    print('Não pode doar')