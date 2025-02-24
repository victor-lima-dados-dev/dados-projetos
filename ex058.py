from random import randint

comp = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Quqal é o seu palpite? "))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print("Mais... Tente mais um vez.")
        elif jogador > comp:
            print("Menos... Tente mais uma vez.")
print("Acertou com {} palpites".format(palpites))
