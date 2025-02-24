nt1 = float(input('Digite a sua primeira nota: '))
nt2 = float(input('Digite a sua segunda nota: '))
media = (nt1+nt2)/2
if media < 5.0:
    print('Não foi dessa vez, você foi Reprovado')
elif 7.0 > media >= 5.0:
    print('Você fara a recuperação')
elif media >= 7.0:
    print('Parabéns, você foi Aprovado')

