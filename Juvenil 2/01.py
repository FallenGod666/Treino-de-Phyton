precos = []

for i in range (1, 6):
    preco = float(input(f'Digite o {i} preço $ '))
    precos.append(preco)


maior = max(precos)
menor = min(precos)

print(f'O maior valor digitaddo foi de {maior}')
print(f'O menor valor digitado foi {menor}')