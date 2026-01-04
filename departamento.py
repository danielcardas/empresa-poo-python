import funcionario
import json


class Departamento:
    def __init__(self, nome: str, funcionarios: list | None = None) -> None:
        self.nome = nome
        self.funcionarios = funcionarios or []
        self.criar_departamento()

    def __repr__(self) -> str:
        return self.nome
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "funcionarios": [funcionario.to_dict()
                             for funcionario in self.funcionarios]
        }

    def criar_departamento(self):
        with open('departamentos.json', 'a') as arquivo:
            json.dump(self.to_dict(), arquivo)

    def adicionar_funcionario(self, funcionario: funcionario.Funcionario):
        self.funcionarios.append(funcionario)
        print(f'{funcionario.nome} incluido no Departamento {self.nome}')

    def folha_pagamento(self):
        print(f'-- Folha de Pagamentos Departamento {self.nome} --')
        for i in self.funcionarios:
            # Chamei apenas i em funcionário pois defini no repr de Funcionario
            print(f'Funcionario: {i} | '
                  f'Salário: R${i.calcular_salario():.2f}')
        print(f'Total do Departamento: R${self.total_folha():.2f}')

    def total_folha(self):
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