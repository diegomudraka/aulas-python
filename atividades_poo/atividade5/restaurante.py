
class item_pedido:
    def _init_(self, descricao: str, valor):
        self.descricao = descricao




class mesa:
    def _init_(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def listar_pedidos(self):
        try:
            for item in self.pedidos:
                print(item.descricao)
        except Exception as erro:
            print(f"Erro de digitação: {erro}")
        finally:
            print("Finalizando execução.")














