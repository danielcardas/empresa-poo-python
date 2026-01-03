class Empresa:
    def __init__(self, nome: str, departamentos: list | None = None) -> None:
        self.nome = nome
        self.departamentos = departamentos or []
    
    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)
        print(f'O Departamento {departamento} foi criado!')

    def folha_geral(self):
        valor_total = 0
        for departamento in self.departamentos:
            departamento.folha_pagamento()
            valor_total += departamento.total_folha()
        print(f'== Total geral da empresa: R${valor_total:.2f}')