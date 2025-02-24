nu1 = int(input("Digite um número inteiro: "))
nu2 = int(input("Digite outro número inteiro: "))
if nu1 > nu2:
    print("O número {} é maior que {}.".format(nu1, nu2))
elif nu2 > nu1:
    print("O número {} é maior que {}.".format(nu2, nu1))
else:
    print("Os números {} e {} são iguais.".format(nu1, nu2))
