distancia = float(input('\033[0;34mInforme a distancia percorrida na viajem\nEm Km:\033[m'))

if distancia <= 200:
    precoPassagem = distancia * 0.50
    print(f'km percorridos  \033[1;30m{distancia}\033[m  km \n O valor da passagem é: \033[1;30m{precoPassagem:.2f}\033[m  reais')
elif distancia > 200:
    precoPassagem = distancia * 0.45
    print(f'km percorridos \033[4;30m{distancia}\033[m\n  O valor da Passagem é:  \033[4;30m{precoPassagem:.2f}\033[m reais')

