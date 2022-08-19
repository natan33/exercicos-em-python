numero = int(input("Digiet um numero: "))
print('''Escolha uma das bases para conversão
[1] para bínario
[2] para octal
[3] para hexadecimal''')
opcao = int(input('Opção: '))
if opcao == 1:
    print(f'{numero} convertido para BINARIO é igual a \033[4;30m{bin(numero)[2:]}\033[m')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a \033[4;30m{oct(numero)[2:]}\033[m')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a \033[4;30m{hex(numero)[2:]}\033[m ')