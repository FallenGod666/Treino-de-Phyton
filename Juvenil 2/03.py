idades = []
H_idades = []
M_maior20 = 0
h = 0
m = 0

for i in range(1, 6):
    sexo = input(f'Qual o seu sexo? H para Homem e M para Mulher: ').strip().upper()

    if sexo == "H":
        h += 1
        idade = int(input(f'Qual sua idade?: '))
        idades.append(idade)
        H_idades.append(idade)
    else:
        m += 1
        idade = int(input(f'Qual sua idade?: '))
        idades.append(idade)
        if idade > 20:
            M_maior20 += 1

media_idades = sum(idades) / len(idades)
media_idades_H = sum(H_idades) / len(H_idades)

print()
print(f'Foram cadastrados {h} Homens e {m} Mulheres')
print(f'A média de idade do grupo é {media_idades}')
print(f'A média da idade dos homens é {media_idades_H}')
print(f'A quantidadde de mulheres maior de 20 anos é de {M_maior20}')
  
