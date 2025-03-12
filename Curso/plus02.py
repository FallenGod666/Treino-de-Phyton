n1 = int(input('Insira o 1º valor: '))
n2 = int(input('Insira o 2º valor: '))

s = n1 + n2
m = n1 * n2 
d = n1 / n2
di = n1 // n2
p = n1 ** n2
rd = n1 % n2

print()
print(f'A soma dos números é: {s} \n A multiplicação é: {m} \n A divisão é: {d:.2f} \n A divisão inteira é: {di} \n O valor 1 elevado a potencia do valor 2 é: {p:.2f}')
print(f'E o valor que ersta da divisão entrer eles é: {rd}')