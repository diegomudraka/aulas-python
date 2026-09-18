class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):

        return self.__nome
    @property
    def preco(self):

        return self.__preco
    @property
    def quantidade_estoque(self):

        return self.__quantidade_estoque























