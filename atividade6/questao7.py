orcamento = 500

while orcamento > 0:
    gasto = int(input("Gasto: "))
    orcamento  -= gasto
    print("Saldo restante: ", orcamento)
print("Atenção: Voce ficou sem saldo ou estourou seu orcamento!")