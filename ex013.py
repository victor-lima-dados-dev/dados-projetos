sl = float(input('Digite o valor do salário: '))
au = float(input('Qual o valor do aumento em porcento?  '))
a2: float = au/100
a3: float = sl * a2
au4: float  = sl + a3
print('O salário inicial é de R${} com o aumento de {}% o valor do salário final é de: R${} '.format(sl,au,au4))


