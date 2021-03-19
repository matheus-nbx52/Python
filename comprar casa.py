casa = float(input('qual o valor da casa?'))
salario = float(input('qual o seu salario?'))
anos = int(input('qual a quantidade de anos a pagar a casa?'))

prestacao = casa / (12 * anos)

if prestacao > salario * 0.30:
    print('emprestimo reprovado')
else:
    print('emprestimo aprovado')

