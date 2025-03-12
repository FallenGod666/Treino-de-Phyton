numeros = []

for i in range (1, 100):
    print('Digite vários números para fazer a somatória entre eles e quando digitar 1111, a contagem será encerrada!')
    numero = int(input(f'Digite o {i}º número: '))
    
    if numero == 1111:
        total = sum(numeros)
        print()
        print('Cálculo encerrado!')
        print()
        print(f'Os Valor da somatória é: {total}.')
        break

    else:
        numeros.append(numero)

