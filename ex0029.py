velocidade = float(input('\033[1;32mInforme a velocidade do carro:\033[m'))

if velocidade > 80:
    percentualExcedido = (velocidade - 80) * 100 / 80
    multa = percentualExcedido * 7.00
    print(f'A sua velocidade foi de \033[1;32;30m{velocidade}\033[m km/h '
          f'\n Com a multa de\033[1;32;30m 7.00\033[m por km/h a cima'
          f'\n Total de: \033[1;32;30m{multa}\033[m reais')
else:
    print('\033[1;35m Fique Tranquilo,Não consta multa no sistema !\033[m')
