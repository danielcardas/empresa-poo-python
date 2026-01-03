class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        ...

    def __repr__(self) -> str:
        return f'{self.nome} ({self.__class__.__name__})'


class Desenvolvedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.20


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base + 2000


class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 0.80