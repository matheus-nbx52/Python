from random import randint

print(randint(1, 9))
coluna = []
matriz = []

linhas = int(input('Informe a quantidade de linhas: '))
colunas = int(input('Informe a quantidade de colunas: '))

i = 0
while i <= colunas:
    numero = randint(1, 9)
    coluna.append(numero)
    i += 1
    if i == colunas:
        matriz.append(coluna)
        coluna = []
        i = 0
        if len(matriz) == linhas:
            break

i = 0
print(f'impressão da matriz {linhas}x{colunas}:')
while i < linhas:
    print(matriz[i])
    i += 1