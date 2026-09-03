#Estrutura de dados

#If e Else -> Se e Senão
#Case sensitive -> E != e

idade = int(input("Digite sua idade: "))
#criando uma condição na execução do codigo
if idade >= 18:
    print("Você pode entrar nessa balada.")
    if idade > 65:
        print("Desculpa senhor, voce não pode entrar nessa balada.")
    else:
        print("Voce pode entrar na balada.")
elif  idade < 5: #Else + If -> elif
    print("Alem de não entrar, voce não pode andar sozinho.")

else:
    print("Voce não pode entrar, é menor de idade!")

nome = input("Digite seu nome: ")

if nome == "":
    print("Por favor digite um nome valido.")
else:
    print("Ola " + nome + "! Seja bem vindo a nossa balada!")

#else: #executa se a condição do if for false

#if idade <18:
    #print(("Você não pode entrar na balada."))


#if 1 == 1: #executa Se a resposta boleana for True
    #print("Verdadeiro")

#Elif
