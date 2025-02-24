km = float(input('Qual a sua distância em Km: '))
if km <= 200:
    print('O valor da passagem é de R${:.2f}'.format(km * 0.50))
else:
    print('O valor da passagem é de: R${:.2f}'.format(km * 0.45))