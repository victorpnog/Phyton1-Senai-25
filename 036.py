#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

maior_peso = None
menor_peso = None

#leitura de dados
for i in range(1, 8):
    peso = float(input(f'Digite o peso da {i}ª pessoa (kg): '))

    #processamento
    if maior_peso is None or menor_peso is None:
        maior_peso = menor_peso = peso
    else:
        # Atualiza o maior peso
        if peso > maior_peso:
            maior_peso = peso
        # Atualiza o menor peso
        if peso < menor_peso:
            menor_peso = peso

#impressão
print("\nResumo dos pesos:")
print(f"Maior peso registrado: {maior_peso:.2f} kg")
print(f"Menor peso registrado: {menor_peso:.2f} kg")