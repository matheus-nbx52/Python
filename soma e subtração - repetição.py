numero = int(input('digite um numero inteiro'))
numero2 = int(input('digite um numero inteiro'))

if numero >= numero2:
    while True:
        numero -= numero2

        if numero2 > numero:
            resto = numero
            break

if numero2 > numero:
    resto = numero
    print(f'o resto da divisão de {numero} para {numero2} é {resto}')