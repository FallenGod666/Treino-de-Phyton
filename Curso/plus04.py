# Leia duas notas e calcule a média
notas = []

for i in range (1, 3):
    nota = float(input(f'Insra a {i}ª nota: '))
    notas.append(nota)
    
print(f'\n As duas notas somadas são {sum(notas)} \n A média do aluno é {sum(notas)/len(notas)}')
