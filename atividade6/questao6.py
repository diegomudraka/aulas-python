numero_secreto = 14
tentativas = 0

palpite = int(input("Tente adivinhar o numero secreto: "))
tentativas += 1

while palpite != numero_secreto:
    palpite = int(input("Palpite: "))
    tentativas += 1
print("Parabens! Voce acertou o numero secreto em ", tentativas, "tentativas")
