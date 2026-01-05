"""Script principal do sistema de gestão empresarial.

Cria instâncias de funcionários, departamentos e empresas,
demonstra o uso das classes e gera o arquivo JSON com os dados completos.
"""
from empresa import Empresa
import funcionario
import departamento


if __name__ == '__main__':
    
    empresa1 = Empresa('Betasoft')

    # Criação dos funcionários
    funcionario1 = funcionario.Desenvolvedor('Daniel', 2000)
    funcionario2 = funcionario.Gerente('Cleber', 8000)
    funcionario3 = funcionario.Estagiario('João', 1600)

    # Criação dos departamentos
    desenvolvedor = departamento.Departamento('Desenvolvedor')
    administracao = departamento.Departamento('Administração')

    # Associação de funcionários aos departamentos
    desenvolvedor.adicionar_funcionario(funcionario1)
    desenvolvedor.adicionar_funcionario(funcionario2)
    administracao.adicionar_funcionario(funcionario3)
    
    # Associação de departamentos à empresa
    empresa1.adicionar_departamento(desenvolvedor)
    empresa1.adicionar_departamento(administracao)

    empresa1.folha_geral()
    empresa1.salvar_json()
