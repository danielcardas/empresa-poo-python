from departamento import Departamento
import json


class Empresa:
    """Representa uma empresa composta por múltiplos departamentos.

    A classe Empresa é responsável por centralizar e gerenciar
    os departamentos, calcular a folha de pagamento geral
    e realizar a persistência de dados em formato JSON.
    """
    def __init__(self, nome: str, departamentos: list | None = None) -> None:
        """Inicializa uma nova empresa.

        Args:
            nome (str): Nome da empresa.
            departamentos (list | None): Lista opcional de departamentos 
            associados à empresa.
        """
        self.nome = nome
        self.departamentos = departamentos or []

    def to_dict(self):
        """Converte a empresa em um dicionário contendo todos os 
        departamentos e seus funcionários.

        Returns:
            dict: Estrutura de dicionário representando a empresa completa.
        """
        return {
            "nome": self.nome,
            "departamentos": [departamento.to_dict()
                              for departamento in self.departamentos]
        }

    def salvar_json(self):
        """Salva as informações da empresa e seus departamentos
        em um arquivo JSON.

        O arquivo é salvo como 'empresas.json' na raiz do projeto.

        Returns:
            None
        """
        dados = self.to_dict()
        with open('empresas.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def adicionar_departamento(self, departamento):
        """Adiciona um novo departamento à empresa.

        Args:
            departamento (Departamento): Instância do departamento a 
            ser adicionada.
        """
        self.departamentos.append(departamento)
        print(f'O Departamento {departamento} foi criado!')

    def folha_geral(self):
        """Exibe a folha de pagamento consolidada da empresa.

        Percorre todos os departamentos, exibe suas folhas de pagamento
        e mostra o valor total geral da empresa.
        """
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