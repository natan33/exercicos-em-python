num = int(input('Informe um numero: '))

if num % 2 == 0:
    print('\033[7;32;30mNumero Par\033[m')
else:
    print('\033[0;30;41mNumero Impar\033[m')