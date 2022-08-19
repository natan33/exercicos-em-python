# sorteando Alunos
#modulo random escolhe valores aleatorios
import random
n1 = str(input('\033[7;35;37mprimeiro Aluno: '))
n2 = str(input('\033[4;30;34mSegundo Aluno: '))
n3 = str(input('\033[1;30;31mTerceiro Aluno:'))
n4 = str(input('\033[2;32;35mQuarto Aluno: '))

lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f' o Aluno escolhido foi: \033[37m{escolhido}\033[m')