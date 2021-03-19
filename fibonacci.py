numero = int(input('digite um numero inteiro'))
fb0 = 0
fb1 = 1
fbn = 0

while True:
    print(fbn, end=' ')
    fbn = fb0 + fb1
    fb1 = fb0
    fb0 = fbn
    if fbn > numero:
        print(fbn)
        break

