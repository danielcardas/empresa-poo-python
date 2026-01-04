from departamento import Departamento
import json


class Empresa:
    def __init__(self, nome: str, departamentos: list | None = None) -> None:
        self.nome = nome
        self.departamentos = departamentos or []

    def to_dict(self):
        return {
            "nome": self.nome,
            "departamentos": [departamento.to_dict()
                              for departamento in self.departamentos]
        }

    def salvar_json(self):
        dados = self.to_dict()
        with open('empresas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def adicionar_departamento(self, departamento):
        self.departamentos.append(departamento)
        print(f'O Departamento {departamento} foi criado!')

    def folha_geral(self):
        valor_total = 0
        for departamento in self.departamentos:
            departamento.folha_pagamento()
            valor_total += departamento.total_folha()
        print(f'== Total geral da empresa: R${valor_total:.2f}')


if __name__ == '__main__':
    empresa1 = Empresa('Beta')
    departamento1 = Departamento('Administração')
    departamento2 = Departamento('Desenvolvimento')
    empresa1.adicionar_departamento(departamento1)
    empresa1.adicionar_departamento(departamento2)
    print(empresa1.to_dict())
    print(empresa1.salvar_json())