n1 = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(n1))
print('Só tem espaços? ', n1.isspace())
print('É um número? ', n1.isnumeric())
print('É Alfanúmerico? ', n1.isalnum())
print('Está em maiúsculas? ', n1.isupper())
print('Está em minúcuslas? ', n1.islower())
print('Está capitalizada? ', n1.istitle())

n2 = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(n2))
print('Só tem espaços? {} , É um número? {}, É Alfanúmerico? {}'.format(n2.isspace(), n2.isnumeric(), n2.isalpha()))
