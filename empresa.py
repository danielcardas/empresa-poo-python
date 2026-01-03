from funcionario import Funcionario


class Empresa:
    def __init__(self, nome: str, funcionarios: list | None = None) -> None:
        self.nome = nome
        self.funcionarios = funcionarios or []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
        print(f'{funcionario.nome} registrado!')

    def folha_pagamento(self):
        print('-- Folha de Pagamentos --')
        for i in self.funcionarios:
            # Chamei apenas i em funcionário pois defini no repr de Funcionario
            print(f'Funcionario: {i} | '
                  f'Salário: R${i.calcular_salario():.2f}')

    def total_folha(self):
        valor_total = 0
        for i in self.funcionarios:
            valor_total += i.calcular_salario()
        return valor_total