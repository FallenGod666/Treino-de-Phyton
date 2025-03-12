pesos = []
alturas = []
media_altura_gurpo = 0
mais90kg = 0
menos50kg_menos160 = 0
mais190_mais100kg = 0

for i in range(1, 6):
    peso = int(input(f'Insira o {i}º peso: '))
    pesos.append(peso)
    altura = float(input(f'Insira a {i}ª altura: '))
    alturas.append(altura)

    if peso > 90:
        mais90kg += 1
    
    if peso < 50 and altura < 1.6:
        menos50kg_menos160 += 1

    if peso > 100 and altura > 1.9:
        mais190_mais100kg += 1
    
media_altura_gurpo = sum(alturas) / len(alturas)

print()
print(f'A média de altura do grupo é de {media_altura_gurpo}M')
print(f'A quantidade de pessoas que pesam mais de 90KG são {mais90kg}')
print(f'A quandtidade de pessoas que pesam menos de 50KG e medem menos de 1.6M é: {menos50kg_menos160}')
print(f'A quantidade de pessoas que pesam mais de 100KG e medem mais de 1.9M é: {mais190_mais100kg}')
