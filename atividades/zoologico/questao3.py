
class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.nome = nome
        self.idade = 0
        self.nivel_fome = 0

        self.idade = idade
        self.nivel_fome = nivel_fome



@property
def nome(self):
    return self.__nome



@property
def idade(self):
    return self.__idade


@idade.setter
def idade(self, valor):
    if valor < 0:
        print("Erro: Idade inválida")
    else:
        self.__idade = valor



@property
def nivel_fome(self):
    return self.__nivel_fome


@nivel_fome.setter
def nivel_fome(self, valor):
    if valor < 0:
        self.__nivel_fome = 0
    elif valor > 100:
        self.__nivel_fome = 100
    else:
        self.__nivel_fome = valor

def alimentar(self, porcao):
    if porcao <= 0:
        print("Erro: Porção inválida")
        return
    self.nivel_fome = self.nivel_fome - porcao


def emitir_som(self):
    print(f"{self.nome} faz um som genérico.")


def exibir_resumo(self):
    print(f"Nome: {self.nome}")
    print(f"Idade: {self.idade} anos")
    print(f"Nível de fome: {self.nivel_fome}")


class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh

    @property
    def velocidade_kmh(self):
        return self.__velocidade_kmh

    def correr(self):
        print(f"{self.nome} correu a {self.velocidade_kmh} km/h!")
        self.nivel_fome = self.nivel_fome + 20

    # Polimorfismo
    def emitir_som(self):
        print(f"{self.nome} ruge alto!")

    # Polimorfismo
    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade de corrida: {self.velocidade_kmh} km/h")


class Ave(Animal):
    def __init__(self, nome, idade, nivel_fome, envergadura_asas):
        super().__init__(nome, idade, nivel_fome)
        self.__envergadura_asas = envergadura_asas

    @property
    def envergadura_asas(self):
        return self.__envergadura_asas

    def voar(self):
        if self.nivel_fome <= 80:
            print(f"{self.nome} voou com suas asas de {self.envergadura_asas}cm!")
            self.nivel_fome = self.nivel_fome + 15
        else:
            print(f"Voo negado: {self.nome} está faminto demais para voar!")


    def emitir_som(self):
        print(f"{self.nome} canta um som melodioso!")


    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das asas: {self.envergadura_asas}cm")


