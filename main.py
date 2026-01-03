import empresa
import funcionario

if __name__ == '__main__':
    empresa1 = empresa.Empresa('Betasoft')
    funcionario1 = funcionario.Desenvolvedor('Daniel', 2000)
    funcionario2 = funcionario.Gerente('Cleber', 8000)
    funcionario3 = funcionario.Estagiario('João', 1600)

    empresa1.adicionar_funcionario(funcionario1)
    empresa1.adicionar_funcionario(funcionario2)
    empresa1.adicionar_funcionario(funcionario3)
    
    empresa1.folha_pagamento()
    print(f'Total da Folha: R${empresa1.total_folha():.2f}')
