import funcionario


class Departamento:
    def __init__(self, nome: str, funcionarios: list | None = None) -> None:
        self.nome = nome
        self.funcionarios = funcionarios or []

    def __repr__(self) -> str:
        return self.nome

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