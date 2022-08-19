num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

if num1 > num2:
    print(f'\033[32m{num1}\033[m é Maior que \33[30m{num2}\033[m')
elif num1 < num2:
    print(f'{num2} é Maior que {num1}')
else:
    print('Não existe valor maior, os dois são iguais')