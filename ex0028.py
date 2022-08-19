from random import randint
compAleatorio = randint(0,5)
print('JOGO DE ADVINHA')
usuario = int(input('Informe um numero \n entre 0 e 5: '))

if usuario == compAleatorio:
    print('Você advinhou o numero')
else:
    print('Numero incorreto \n tente de novo')













