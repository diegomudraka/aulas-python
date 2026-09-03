#Operadores
"""
 Atribuição
 = -> variavel = 10
 ! = Não, Not, Contrario...
 Sim -> !Sim = Não


 Comparação
 esperar uma resposta de true ou false
 != se for diferente retorna False
 idade = 18
 idade != 17 -> True
 idade != 18 -> False

 == -> se for diferente retorna True
 > -> se for maior retorna true
 < -> se for menor retorna false

 >= -> se for maior e igual retorna true
 <= -> se for menor e igual retorna false
 Para mais comparações

 and -> se todas as comparações forem true, retorna true
 idade = 18
 idade == 18 and idade > 18 -> True
 idade == 18 and idade < 18 -> False

 or -> se ao menos uma das comparações

"""
#Testes
idade = 18 #inteiro

#comparacao = idade != 17 #boleano
#print(comparacao)
#print(idade != 18) #false
#print(idade == 18) #true
#print(idade > 18) #false
#print(idade < 18) #true

#print(idade >= 18) #false
#print(idade <= 18) #true

#testes

idade = 18 #inteiro
pais_acompanham = true

print("Nossa balada, não aceita crianças, idosos e pais do convidado")
print("Você pode entrar em uma balada.")
#print((idade > 10) and (idade < 20) and (idade == 18))
print((idade >= 18) and(idade < 65) and (pais_acompanham != True))

