'''var_verdade = True
var_falso = False

# usar dois " == " atribui comparação aos items adjacentes
# comparacoes: !=   >   <   >=  <=
# comparacoes: and  or

if var_verdade == True: # IF EM INGLES SIGNIFICA "SE"
    print('var_verdade é Verdadeiro')

else: # ELSE EM INGLES SIGNIFICA "SE NÃO"
    print('Não deu Certo.')

## EXERCICIO NA ETAPA ABAIXO '''

print('Ficha de Cadastro do Exercito:\n1 = Idade \n2 = Peso \n3 = Altura')

idade = input('Qual a sua idade?')
peso = input('Qual o seu peso?')
altura = input('Qual a sua Altura?')

if (idade >= '18') and (peso >= '60') and (altura >= '1.70'):
    print('Você foi Aprovado para o Exercito!')

elif (idade < '18') or (peso < '60') or (altura < '1.70'):
   print('Você não atende os requisitos minimos para entrar no Exercito.')