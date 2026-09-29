class Animal():
    def __init__(self, nome: str, idade: int, nivel_fome: int = 50):
        self._nome = nome
        self._idade = 0
        self._nivel_fome = 0
        self._nivel_fome = nivel_fome


    @property
    def nome(self) -> str:
        return self._nome
    @property
    def idade(self) -> str:
        return self._idade
    @idade.setter
    def idade(self, valor: int):
        if valor <0:
            print("Erro idade invalida.")
        else:
            self._idade = valor


    @property
    def nivel_fome(self) -> int:
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, valor: int):
        if valor < 0:
            self._nivel_fome = 0
        elif valor > 100:
            self._nivel_fome = 100
        else:
            self._nivel_fome = valor

    def alimentar(self, porcao: int):
        if porcao <= 0:
            print("Erro porcao invalido.")
        else:
            self._nivel_fome -= porcao

    def emitir_som(self):
        print(f"{self.nome} faz um som generico.")

    def exibir_resumo(self):
        print(f"nome: {self.nome} | Idade: {self.idade} anos | Nivel de fome: {self.nivel_fome}")





