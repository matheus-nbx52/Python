import py
caixa = {}
informacoes = {}
opcao = ('selecione uma opção :'
      '1-Adicionar produto '
      '2-Remover produto '
      '3-Pesquisar Valor do Produto ' 
      '4-Editar Produto '
      '5-Sair '
      '')

while True:
    print(100*'=')
    print(opcao)
    select = input()
    if select == '1':
        nome = input('insira o nome do produto: ')
        if nome not in caixa:
            unidade = int(input('insira a quantidade: '))
            preco = float(input('insira o preço: '))
            informacoes['quantidade'] = unidade
            informacoes['preço'] = preco
            caixa[nome] = informacoes
            informacoes = {}

        else:
            print('o nome do produto já foi registrado ')
            print('use a opção editar para alterar algo ')

    elif select == '2':
        nome = input('qual o nome do produto que você deseja remover? ')
        if nome in caixa:
            print(f'removendo...{nome}, {caixa[nome]}')
            del caixa[nome]
            print('produto removido')
        else:
            print('produto inexistente')

    elif select == '3':
        print('pesquisando preço de produto')
        nome = input('insira o nome do produto: ')
        if nome in caixa:
            print(f'o preço do(a) {nome} esta por {caixa[nome]["preço"]:.2f}')
        else:
            print('produto inexistente')

    elif select == '4':
        print('editando produto...')
        nome = input('insira o nome do produto que você quer editar: ')
        if nome in caixa:
            unidade = int(input(f'insira uma nova quantidade para {nome}: '))
            del caixa[nome]['quantidade']
            preco = float(input('insira um novo preço: '))
            del caixa[nome]['preço']
            informacoes['quantidade'] = unidade
            informacoes['preço'] = preco
            caixa[nome] = informacoes
            informacoes = {}
        else:
            print('produto inexistente')

    elif select == '5':
        print('encerrando programa...')
        break

    else:
        print('comando invalido')

