import json


class Funcionario:
    def __init__(self, nome: str, salario_base: float) -> None:
        self.nome = nome
        self.salario_base = salario_base
        self.criar_funcionario()

    def calcular_salario(self):
        ...

    def __repr__(self) -> str:
        return f'{self.nome} ({self.__class__.__name__})'
    
    def criar_funcionario(self):
        with open('funcionarios.json', 'w') as arquivo:
            json.dump(self.to_dict(), arquivo)

    def to_dict(self):
        return {
            "nome": self.nome,
            "salario_base": self.salario_base,
            "cargo": self.__class__.__name__
        }


class Desenvolvedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.20


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base + 2000


class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 0.80
    

if __name__ == '__main__':
    func1 = Desenvolvedor('Daniel', 2000)
    func1.criar_funcionario()