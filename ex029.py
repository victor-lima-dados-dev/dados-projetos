vl = float(input('Qual a velocidade atual do carro? '))
if vl > 80:
    multa = (vl - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança.')