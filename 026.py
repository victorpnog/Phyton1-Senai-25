#Crie um programa para analisar o IMC de uma pessoa,
# e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

#leitura de dados
peso = float(input('Digite seu peso: '))
altura = float (input('Digite sua altura: '))
sexo = int(input('Se você é Homem, tecle "1", se você é Mulher, tecle "2": '))

#processamento de dados
imc = peso/(altura**2)

#decisao
if sexo == 1:
    if imc >= 40:
        print('\nObeso')
    elif imc >= 35:
        print('\nObesidade grau I')
    elif imc >= 25:
        print('\nSobrepeso')
    elif imc >= 18:
        print('\nPeso Normal')
    elif imc < 18 and imc >= 0:
        print('\nAbaixo do peso')
    else:
        print('Tem algum erro no seu peso e/ou altura!')
elif sexo == 2:
    if imc >= 40:
        print('\nObesidade grau III')
    elif imc >= 35:
        print('\nObesidade grau II')
    elif imc >= 25:
        print('\nSobrepeso')
    elif imc >= 18.5:
        print('\nPeso Normal')
    elif imc >= 16:
        print('\nMagreza')
    elif imc <16 and imc >= 0:
        print('\nMagreza')
    else:
        print('Tem algum erro no seu peso e/ou altura!')

else:
    (print('Você não definiu corretamente se é homem ou mulher!'))