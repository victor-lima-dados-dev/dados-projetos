v = float(input('Qual é o valor do produto? R$'))
d = float(input('Qual o valor do desconto?  '))
de: float = d/100
vd: float = v*de
vf: float = v - vd
print('O produto que custava R${}, na promoção com desconto de {:.1f}% vai custar R${}'.format(v, d, vf))


