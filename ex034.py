sl = float(input('Qual o valor do salário do funcionario? R$'))
if sl >= 1250:
    a2 = 0.10
    a3 = sl * a2
    au4 = sl + a3
    print('O salário inicial é de R${} com o aumento de 10% o valor do salário final é de: R${}'.format(sl, au4))
else:
    a2 = 0.15
    a3 = sl * a2
    au4 = sl + a3
    print('O salário inicial é de R${} com o aumento de 15% o valor do salário final é de: R${}'.format(sl, au4))