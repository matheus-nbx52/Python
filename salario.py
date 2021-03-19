salario = float(input('qual o salario do funcionario? '))
anos = int(input('há quantos anos o funcionario trabalha? '))

if salario <= 500.00:
    reajuste = (salario * 0.25) + salario

elif 500 < salario <= 1000.00:
    reajuste = (salario * 0.20) + salario

elif 1000 < salario <= 1500.00:
    reajuste = (salario * 0.15) + salario

elif 1500 < salario <= 2000.00:
    reajuste = (salario * 0.10) + salario

else:
    reajuste = salario

if 1 <= anos <= 3:
    bonus = 100.00 + reajuste
    print(f'o salario do funcionario sera de R${bonus:.2f}')

elif 4 <= anos <= 6:
    bonus = 200.00 + reajuste
    print(f'o salario do funcionario sera de R${bonus:.2f}')

elif 7 <= anos <= 10:
    bonus = 300.00 + reajuste
    print(f'o salario do funcionario sera de R${bonus:.2f}')

elif anos == 0:
    bonus = reajuste
    print(f'o salario do funcionario sera de R${bonus:.2f}')

else:
    bonus = 500.00 + reajuste
    print(f'o salario do funcionario sera de R${bonus:.2f}')
