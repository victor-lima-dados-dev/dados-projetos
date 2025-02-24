qkm = float(input('Quantidade de Km percorridos: '))
qdias = int(input('Quantidade de dias alugado:  '))
km = 0.15*qkm
vl = 60*qdias
vf = km+vl
print('O valor a ser pago é de: R${:.2f}'.format(vf))
