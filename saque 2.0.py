saque = int(input('informe o valor do saque: '))
cont = 0
print('você recebeu: ')

if saque >= 200:
    while saque >= 200:
        saque -= 200
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 200', end=' , ')
    cont = 0

if 200 > saque >= 100:
    while saque >= 100:
        saque -= 100
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 100', end=' , ')
    cont = 0

if 100 > saque >= 50:
    while saque >= 50:
        saque -= 50
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 50', end=' , ')
    cont = 0

if 50 > saque >= 20:
    while saque >= 20:
        saque -= 20
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 20', end=' , ')
    cont = 0

if 20 > saque >= 10:
    while saque >= 10:
        saque -= 10
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 10', end=' , ')
    cont = 0

if 10 > saque >= 5:
    while saque >= 5:
        saque -= 5
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 5', end=' , ')
    cont = 0

if 5 > saque >= 2:
    while saque >= 2:
        saque -= 2
        cont += 1

if cont != 0:
    print(f'{cont} nota(s) de 2', end=' , ')
    cont = 0

if 2 > saque >= 1:
    while saque >= 1:
        saque -= 1
        cont += 1

if cont != 0:
    print(f'{cont} nota de 1', end=' , ')

