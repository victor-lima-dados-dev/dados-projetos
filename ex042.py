print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

# Verificando se é possível formar um triângulo
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo!')
    # Verificando o tipo de triângulo
    if a == b == c:
        print('O triângulo formado é EQUILÁTERO: todos os lados iguais.')
    elif a != b != c != a:
        print('O triângulo formado é ESCALENO: todos os lados diferentes.')
    else:
        print('O triângulo formado é ISÓSCELES: dois lados iguais, um diferente.')
else:
    print('Não é possível formar um triângulo com esses segmentos.')
