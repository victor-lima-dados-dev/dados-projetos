from datetime import date
atual = date.today().year
nasc = int(input('informe sua data de nascimento: '))
idade = atual - nasc
if 0 < idade <= 9:
    print('Você é MIRIM')
elif 10 < idade <= 14:
    print('Você é INFANTIL')
elif 15 < idade <= 19:
    print('Você é JUNIOR')
elif 20< idade <= 25:
    print('Você é SÊNIOR')
elif idade < 25:
    print('Você é MASTER')
