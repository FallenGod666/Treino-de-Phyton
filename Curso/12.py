# leia um angulo qualquer e de o seno cosseno e tangente desse angulo

import math

n = int(input('Digite um algulo para saber o sen o cons e a tangente: '))

c = math.cos(math.radians(n))
s = math.sin(math.radians(n))
t = math.tan(math.radians(n))

print(f'\n Sen {s:.2f}\n Cos {c:.2f}\n Tang {t:.2f}')
