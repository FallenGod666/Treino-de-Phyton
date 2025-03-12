import random
num_sorteado = random.randint(1, 10)

print('O Computador sorteou um número entre 1 e 10.')
print('Você tem 4 tentativas para acertar qual número é esse.')

tentativas = 4

for tentativa in range(1, tentativas + 1):
    chute = int(input(f'Tentativa {tentativa}, qual o seu chute?: '))

    if chute == num_sorteado:
        print(f'Você acertou na {tentativa} tentativa!')
        break
    elif chute < num_sorteado:
        print('Dica: O número é maior...')
    else:
        print('Dica: O número é menor...')

else:
    print(f'Perdeu, o número sorteado foi {num_sorteado}')