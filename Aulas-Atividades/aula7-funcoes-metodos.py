'''ESCREVA UMA FUNÇÃO QUE RECEBE UM OBJETO DE COLEÇÃO E RETORNA O VALOR DO MAIOR NUMERO DENTRO,
E OUTRA FUNÇÃO QUE RETORNE O MENOR VALOR.

'''

def maior (colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor (colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(maior([1,2,20,35,7,9,0]))
print(menor([1,2,20,35,7,9,0]))