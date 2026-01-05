import json


class Funcionario:
    """Classe base que representa um funcionário genérico da empresa.

    Contém os atributos e comportamentos comuns a todos os tipos
    de funcionários, como nome, salário base e serialização em JSON.
    """
    def __init__(self, nome: str, salario_base: float) -> None:
        """Inicializa um novo funcionário.

        Args:
            nome (str): Nome do funcionário.
            salario_base (float): Valor do salário base do funcionário.
        """
        self.nome = nome
        self.salario_base = salario_base
        self.criar_funcionario()

    def calcular_salario(self):
        ...

    def __repr__(self) -> str:
        return f'{self.nome} ({self.__class__.__name__})'
    
    def criar_funcionario(self):
        """Salva as informações do funcionário em formato JSON.

        O registro é adicionado (append) ao arquivo 'funcionarios.json'.
        """
        with open('funcionarios.json', 'a') as arquivo:
            json.dump(self.to_dict(), arquivo)

    def to_dict(self):
        """Converte o funcionário em um dicionário pronto para 
        serialização JSON.

        Returns:
            dict: Dicionário contendo nome, salário base e cargo do 
            funcionário.
        """
        return {
            "nome": self.nome,
            "salario_base": self.salario_base,
            "cargo": self.__class__.__name__
        }


class Desenvolvedor(Funcionario):
    """Representa um desenvolvedor.

    O salário é calculado com um acréscimo de 20% sobre o salário base.
    """
    def calcular_salario(self):
        return self.salario_base * 1.20


class Gerente(Funcionario):
    """Representa um gerente.

    O salário é calculado adicionando R$ 2.000 ao salário base.
    """
    def calcular_salario(self):
        return self.salario_base + 2000


class Estagiario(Funcionario):
    """Representa um estagiário.

    O salário é calculado como 80% do salário base.
    """
    def calcular_salario(self):
        return self.salario_base * 0.80
    

if __name__ == '__main__':
    func1 = Desenvolvedor('Daniel', 2000)