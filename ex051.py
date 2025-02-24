primeiro = int(input('Primeiro Numero: '))
razão = int(input('Razão: '))
décima = primeiro + (10 - 1) * razão
for c in range(primeiro, décima + razão, razão):
    print('{}'.format(c), end='→ ')
print('ACABOU')