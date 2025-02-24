nome = str(input('Digite o nome aqui: ')) .strip()
print('Iremos analisar o seu nome.')
print('O seu nome em maisculo é {}'.format(nome.upper()))
print('O seu nome em minusculo é {}'.format(nome.lower()))
print('A quantidade de números é igual á {}'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


