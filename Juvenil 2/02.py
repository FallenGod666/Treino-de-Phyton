idades = []
maior18 = 0
menor5 = 0

for i in range (1, 6):
    idade = int(input(f'Digite a {i} idade: '))
    idades.append(idade)

    if idade > 18:
        maior18 += 1

    if idade < 5:
        menor5 += 1

    
media_idades = sum(idades) / len(idades)
maior_idade = max(idades)

print()
print(f'A média de idades é: {media_idades}')
print(f'Maiores de 18 são: {maior18}')
print(f'Menores de 5 são: {menor5}')
print(f'A maior idade dentre todas é: {maior_idade}')
