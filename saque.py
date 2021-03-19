saque = float(input())

while True:
    quantidade = saque//200
    resto = saque % 200
    saque
    print(resto)
    print(f'{quantidade:.0f}')

    if resto <= 200:
        resto = saque % 100
        print(resto)

    if resto <= 100:
        resto = saque % 50
        print(resto)
        break
