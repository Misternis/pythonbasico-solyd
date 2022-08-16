'''Cria um programa que busque titulos de filmes e faça uma lista'''
import requests
import json

def checagemfilme(titulo):
    lista = []
    for i in range(1, 101):
        try:
            req = requests.get('http://www.omdbapi.com/?s='+titulo+'&apikey=6ae89f67&type=movie&page='+ str(i))
            resposta = json.loads(req.text)
            if resposta['Response'] == 'False':
                break
            else:
                for filme in resposta['Search']:
                    nomefilme = filme['Title']
                    ano = filme['Year']
                    string = nomefilme + ' (' + ano + ')'
                    lista.append(string)
        except:
            print('Erro na Requisição.')
            break
    return lista

sair = False
while not sair:
    op = input('Digite o Nome do Filme ou SAIR:')
    if op == 'SAIR' or op == 'sair':
        sair = True
    else:
        lista_de_filmes = checagemfilme(op)
        print('Estes são os Filmes Encontrados: ', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)