import funcionario
import json


class Departamento:
    """Representa um departamento dentro de uma empresa.

    Cada departamento possui um nome e uma lista de funcionários associados.
    É responsável por calcular a folha de pagamento e gerar relatórios
    financeiros relacionados aos seus colaboradores
    """
    def __init__(self, nome: str, funcionarios: list | None = None) -> None:
        """Inicializa um novo departamento.

        Args:
            nome (str): Nome do departamento
            funcionarios (list | None): Lista de funcionários pertencentes ao
            departamento
        """
        self.nome = nome
        self.funcionarios = funcionarios or []
        self.criar_departamento()

    def __repr__(self) -> str:
        return self.nome
    
    def to_dict(self):
        """Converte o departamento e seus funcionários em um dicionário.

        Returns:
            dict: Dicionário contendo o nome do departamento e a lista 
            de funcionários.
        """
        return {
            "nome": self.nome,
            "funcionarios": [funcionario.to_dict()
                             for funcionario in self.funcionarios]
        }

    def criar_departamento(self):
        """Salva os dados do departamento no arquivo 'departamentos.json'.

        Observação:
            Este método adiciona (append) o departamento no arquivo JSON.
            Caso o arquivo não exista, ele será criado automaticamente.
        """
        with open('departamentos.json', 'a') as arquivo:
            json.dump(self.to_dict(), arquivo)

    def adicionar_funcionario(self, funcionario: funcionario.Funcionario):
        """Adiciona um novo funcionário ao departamento.

        Args:
            funcionario (Funcionario): Instância da classe Funcionario 
            a ser adicionada.
        """
        self.funcionarios.append(funcionario)
        print(f'{funcionario.nome} incluido no Departamento {self.nome}')

    def folha_pagamento(self):
        """Exibe a folha de pagamento detalhada do departamento.

        Mostra o salário de cada funcionário e o total geral do departamento.
        """
        print(f'-- Folha de Pagamentos Departamento {self.nome} --')
        for i in self.funcionarios:
            print(f'Funcionario: {i} | '
                  f'Salário: R${i.calcular_salario():.2f}')
        print(f'Total do Departamento: R${self.total_folha():.2f}')

    def total_folha(self):
        """Calcula o valor total da folha de pagamento do departamento.

        Returns:
            float: Soma dos salários de todos os funcionários do departamento.
        """
        valor_total = 0
        for i in self.funcionarios:
            valor_total += i.calcular_salario()
        return valor_total
    

# if __name__ == '__main__':
#     funcionario1 = funcionario.Funcionario('Daniel', 500)
#     funcionario2 = funcionario.Funcionario('Joana', 600)
#     departamento1 = Departamento('Administração')
#     departamento1.adicionar_funcionario(funcionario1)
#     departamento1.adicionar_funcionario(funcionario2)
#     print(departamento1.to_dict())