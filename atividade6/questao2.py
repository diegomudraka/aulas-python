senha_correta = "123456"

senha_digitada = input("Digite sua senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta Tente novamente")
    senha_digitada = input("Digite sua senha: ")
print("Acesso permitido")


