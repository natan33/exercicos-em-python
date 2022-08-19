#Emprestimo bancario Para Casa
nome = str(input('Informe seu nome: '))
salario = float(input('Digite o seu Salario: '))
casa = float(input('Informe o valor da casa: '))
quantosAnosPG = float(input('Quantos anos deseja pagar? '))

#Calculo da Mensalidade
prestacaoMensal = (casa / quantosAnosPG) / 12

#Calculo da porcentagem da Salario
porcen_30_do_Sal = (salario * 30) / 100

#Condição para Aprovar ou Não
if prestacaoMensal > porcen_30_do_Sal:
    print('Empréstimo negado \n'
          'Mensalidade maior que 30% do salario\n'
          f'Mensalidade proposta: {prestacaoMensal}\n'
          f'Salário: {salario}\n'
          f'valor de 30% do Salario: {porcen_30_do_Sal} ')

elif prestacaoMensal <= porcen_30_do_Sal:
    print(f'\033[1;32mEmprestimo Aprovado\033[m\n'
          f'Valor da Mensalidade: \033[1;30m{prestacaoMensal:.2f}\033[1;32m reais')

