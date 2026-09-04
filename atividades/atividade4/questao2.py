velocidade = float(input("Digite a velocidade em Km/h: "))

velocidade_maxima = 80

if velocidade > velocidade_maxima:
    print("Você foi multado por excesso de velocidade.")
else:
    print("Velocidade dentro do limite permitido da via.")
