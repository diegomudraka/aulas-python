class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade > 0 and quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
            print(f"Venda aprovada: {quantidade} unidade(s) vendida(s).")
        else:
            print("Venda negada: Estoque insuficiente")

    def aplicar_desconto(self, percentual):
        if 0 < percentual <= 80:
            self.__preco = self.__preco * (1 - percentual / 100)
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print("----- Resumo do Produto -----")
        print(f"Nome: {self.__nome}")
        print(f"Preço atual: R$ {self.__preco:.2f}")
        print(f"Estoque atual: {self.__quantidade_estoque}")
        print("Dados internos reais (__dict__):")
        print(self.__dict__)
        print("------------------------------")


# ===================== TESTES =====================

meu_produto = Produto("Notebook Gamer", 5000.00, 10)

print("Estado inicial:")
meu_produto.exibir_resumo()

print("\nTeste 1: tentativa de adicionar estoque inválido (negativo)")
meu_produto.adicionar_estoque(-5)

print("\nTeste 2: adicionar estoque válido")
meu_produto.adicionar_estoque(5)

print("\nTeste 3: aplicar desconto inválido (acima de 80%)")
meu_produto.aplicar_desconto(90)

print("\nTeste 4: aplicar desconto válido")
meu_produto.aplicar_desconto(10)

print("\n1) Tentando forçar alteração direta dos atributos privados:")
meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100

print("\n2) Tentando realizar venda absurdamente maior que o estoque:")
meu_produto.realizar_venda(9999)

print("\n3) Exibindo resumo final (dados reais não devem ter sido afetados):")
meu_produto.exibir_resumo()
