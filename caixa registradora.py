print('Bem-vindo ao mercado X')
total = 0
while True:
    produto = input('insira o codigo do produto: ')

    if produto == '501':
        quantidade = int(input('quantidade: '))
        total = total + 7.95 * quantidade
        print(f'{quantidade}x Arroz Tio João 1kg R$ 7.95')

    elif produto == '502':
        quantidade = int(input('quantidade: '))
        total = total + 4.65 * quantidade
        print(f'{quantidade}x Feijão Kicaldo 1kg R$ 4.65')

    elif produto == '503':
        quantidade = int(input('quantidade: '))
        total = total + 2.98 * quantidade
        print(f'{quantidade}x Aguardente Velho Barreiro 910 ml R$ 2.98')

    elif produto == '504':
        quantidade = int(input('quantidade: '))
        total = total + 9.85 * quantidade
        print(f'{quantidade}x Fio Dental Reach Essencial Menta 100m R$ 9.85')

    elif produto == '505':
        quantidade = int(input('quantidade: '))
        total = total + 29.90 * quantidade
        print(f'{quantidade}x Fralda Huggies G Turma da Mônica Tripla Proteção Mega - 48 Unidades R$ 29.90')

    elif produto == '506':
        quantidade = int(input('quantidade: '))
        total = total + 5.95 * quantidade
        print(f'{quantidade}x Bebida à Base de Soja Sabor Maçã Ades 1 Litro R$ 5.95')

    elif produto == '0':
        break

    else:
        print('codigo do produto invalido, insira novamente')

print(f'valor total da compra: R${total:.2f}')