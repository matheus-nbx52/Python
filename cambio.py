real = float(input('valor em reais: '))
print('selecione a moeda a ser cpmprada digitando sua letra: ')
opcao = input('e - Euro, d - Dolar, m - Peso Mexicano, a - Peso Argentino, l - Libra')

if opcao == 'e':
    conversao = real * 0.31
    print(f'você comprou {conversao:.2f} Euros')

elif opcao == 'd':
    conversao = real * 0.42
    print(f'você comprou {conversao:.2f} Dolares')

elif opcao == 'm':
     conversao = real * 5.55
     print(f'você comprou {conversao:.2f} Peso Mexicano')

elif opcao == 'a':
    conversao = real * 2.84
    print(f'você comprou {conversao:.2f} Peso Argentino')

elif opcao == 'l':
    conversao = real * 0.26
    print(f'você comprou {conversao:.2f} Libras')

else:
    print('comando invalido')

