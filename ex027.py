nome = str(input('Digite aqui o seu nome: ')) .strip() .upper()
n = nome.split()
print('O seu primeiro nome é: {}.'.format(n[0]))
print('O seu último nome é: {}.'.format(n[len(n)-1]))

