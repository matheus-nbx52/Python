altura = int(input('qual a altura do reservatorio? '))
largura = int(input('qual a altura do largura? '))
comprimento = int(input('qual a altura do comprimento? '))
litros = int(input('quantos litros você consome por dia? '))

capacidade = altura * largura * comprimento * 1000
autonomia = capacidade/litros

print(f'a capacidade do reservatorio é de {capacidade} litros')
print(f'a autonomia do reservatorio é de {autonomia:.0f} dias')

if autonomia < 2:
    print('consumo esta elevado')

elif 2 <= autonomia <= 7:
    print('consumo esta moderado')

else:
    print('consumo esta elevado')


