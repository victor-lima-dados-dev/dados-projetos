# Lendo o peso e a altura da pessoa
peso = float(input('Digite o peso (em kg): '))
altura = float(input('Digite a altura (em metros): '))

# Calculando o IMC
imc = peso / (altura ** 2)

# Determinando o status de acordo com o IMC
if imc < 18.5:
    status = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    status = 'Peso Ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

# Mostrando o resultado
print('-=' * 20)
print('Resultado do IMC')
print('-=' * 20)
print(f'Seu IMC é: {imc:.2f}')
print(f'Status: {status}')
