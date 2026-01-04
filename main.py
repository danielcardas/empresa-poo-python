from empresa import Empresa
import funcionario
import departamento

if __name__ == '__main__':
    empresa1 = Empresa('Betasoft')
    funcionario1 = funcionario.Desenvolvedor('Daniel', 2000)
    funcionario2 = funcionario.Gerente('Cleber', 8000)
    funcionario3 = funcionario.Estagiario('João', 1600)

    desenvolvedor = departamento.Departamento('Desenvolvedor')
    administracao = departamento.Departamento('Administração')

    desenvolvedor.adicionar_funcionario(funcionario1)
    desenvolvedor.adicionar_funcionario(funcionario2)
    administracao.adicionar_funcionario(funcionario3)
    
    empresa1.adicionar_departamento(desenvolvedor)
    empresa1.adicionar_departamento(administracao)

    empresa1.folha_geral()
    empresa1.salvar_json()
