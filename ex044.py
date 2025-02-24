print('{:=^40}'.format('Loja do Victor'))
preco = float(input('Preço das compras em R$: '))
print('''Formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Tenha um bom dia!')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Tenha um bom dia!')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    parcela = total / parcelas
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))

