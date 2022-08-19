velocidade = float(input('\033[1;32mInforme a velocidade do carro:\033[m'))

if velocidade > 80:
    percentualExcedido = (velocidade - 80) * 100 / 80
    multa = percentualExcedido * 7.00
    print(f'A velocidade foi \033[1;32;30m{velocidade}\033[m km/h '
          f'\n A multa de\033[1;32;30m 7.00\033[m por km/h a cima'
          f'\n O total a pagar vai ser \033[1;32;30m{multa}\033[m reais')
else:
    print('\033[1;35mFique Tranquilo, você não precisa pagar multa !\033[m')
