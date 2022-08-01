'''EXERCICIO: FAÇA UM PROGRAMA QUE LEIA A QUANTIDADE DE PESSOAS QUE SERÃO CONVIDADAS PARA UMA FESTA,
APÓS ISSO O PROGRAMA IRÁ PERGUNTAR O NOME DE TODAS AS PESSOAS CONVIDADAS, E GERAR UMA LISTA.
DEPOIS IMPRIMA TODOS OS NOMES DA LISTA.'''

print('Programa de Controle de Convidados para Festa')
print('_____________________________________________\n')

numero_convidados = input('Coloque aqui a quantidade de Convidados.')
lista_convidados = []

i = 1
while i <= int(numero_convidados):
    nome_convidado = input('Escreva o nome do convidado #'+ str(i) +': ')
    lista_convidados.append(nome_convidado)
    i = i + 1

print('\nSerão', numero_convidados, 'convidados para a Festa.')
print('\nLista de Convidados:')

for convidado in lista_convidados:
    print(convidado)