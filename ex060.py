# 1 Método
"""from math import factorial
num = int(input('Digite aqui um número para calcular o seu fatorial: '))
f = factorial(num)
print('O fatorial de  {}! é {}'.format(num, f))"""

# 2 Método
n = int(input("Digite um número para calcular o seu fatorial: "))
c = n
f = 1
print("Calculando {}!".format(n), end=" ")
while c > 0:
    print("{}".format(c), end=" ")
    print("x" if c > 1 else "=", end=" ")
    f *= c
    c -= 1
print("{}".format(f))
