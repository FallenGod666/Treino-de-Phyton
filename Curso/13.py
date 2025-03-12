# leia quatro nomes e sorteie um aleatoriamente 
import random

nome = []

print('Digite 4 nomes')

for i in range (1, 5):
    n = input(f'Digite o {i}º Nome: ')
    nome.append(n)

escolha = random.choice(nome)
print(f'\n O nome sorteado foi {escolha}')