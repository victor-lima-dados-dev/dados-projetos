nome = str(input('Digite uma frase: ')) .strip() .upper()
print('A letra A aparece {} vezes na frase.'.format(nome.count('A')))
print('A primeira letra A apareceu na posisão: {}.'.format(nome.find('A')+1))
print('A última letra A apareceu na posisão: {}.'.format(nome.rfind('A')+1))
