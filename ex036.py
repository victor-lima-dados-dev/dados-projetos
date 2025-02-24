vcasa = float(input('Qual o valor da casa: '))
sl = float(input('Qual o seu salário: '))
anos = int(input('Em quantos anos você pretende pagar: '))
prestação = vcasa / (anos*12)
mínimo = sl * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(vcasa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')



