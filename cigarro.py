    nome = input('qual o seu nome? ')
    cpd = int(input('quantos cigarros você fuma por dia? '))
    ano = int(input('há quantos anos você fuma? '))
     
    minutos = (cpd * 365 * ano) * 10
    dias = (minutos/60) / 24
     
    print('Sr(a) {}, você perdeu {:.0f} dias de vida'.format(nome, dias)
