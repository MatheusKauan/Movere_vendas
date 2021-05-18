import datetime
from Controller import Consultar_vendas as consultar_vendas #import da função consultar vendas
from Controller import Excluir_vendas as excluir_venda #import da função excluir vendas
from Controller import Consultar_maiorVenda as mostrar_maiorVenda #import da função consultar maior venda
from Controller import Inserir_venda as add_Vendas #import da função inserir vendas

#loop retornavel ao menu
while True:

    print('-----Sistema de Vendas-----')
    print()
    print('Selecione uma das opções')
    print('1- Inserir')
    print('2- Consultar')
    print('3- Excluir')
    print('4- Venda de maior valor')

    opcao = int(input('Opção: '))

    #opção 1 que faz a inserção da venda no banco de dados usando a função inserir vendas
    if opcao == 1:
        nome = input('Digite o nome: ')
        valor = float(input('Valor da venda = '))
        data = str(input('Data da venda AAAA-MM-DD: '))
        add_Vendas.inserir(nome,valor,data)

    #opção 2 que faz a consulta das vendas no banco de dados usando a função Consultar_vendas
    if opcao == 2:
        pesquisa = consultar_vendas.consulta('vendas')
        for x in pesquisa:
            print("id: {0} - Nome: {1} - Valor da venda: {2} - Data da Venda: {3}".format(x[0],x[1],x[2],x[3]))

    #opção 3 que faz a exclusão da venda escolhida no banco de dados usando a função Excluir_vendas
    if opcao == 3:
        id = int(input('Digite o id da coluna que quer excluir: '))
        excluir_venda.excluir(id)
    #opção 4 que busca no banco de dados a venda de maior valor usando a função consulta_maiorValor
    if opcao == 4:
        maiorValor = mostrar_maiorVenda.consulta_maiorValor('vendas')
        print('Maior venda: id: {0} - Nome: {1} - Valor da venda: {2} - Data da Venda: {3} '
              .format(maiorValor[0],maiorValor[1],maiorValor[2],maiorValor[3]))

    #input que pergunta ao usuario se ele deseja continuar ou encerrar o programa
    op=int(input('Deseja continuar '
              '\n0- Sim\n'
              '1- Não\n'))

    if op == 0:
        # caso o usuario escolha 0 ele cai no continue e o programa volta para o menu
        continue

    if op == 1:
        print('O programa foi finalizado')
        break