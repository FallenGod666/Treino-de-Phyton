#leia quatro nomes e printa em ordem aleatoria 

import random

nomes = []

print('Digite 4 nomes')
print()

for i in range(1, 5):
    nome = input(f'Digite o {i}º nome: ')
    nomes.append(nome)

random.shuffle(nomes)

print(nomes)
