""" Operações com strings """
""" str -> transforma número em string
in -> verifica se um texto está contido dentro do outro
operador + -> concatenar string
format e {} -> substitui valores
%s -> substitui textos
%d -> substitui números decimais

Vamos deixar uma cartilha para download """

faturamento = 1000
custo = 500
lucro = faturamento - custo

print('O faturamento foi de: ' + str(faturamento))

""" Para ser mais fácil: """
print('O faturamento foi de: {}. O custo foi de {} e o lucro de {}.'.format(faturamento,custo,lucro))

""" Eu posso usar o texto mais de uma vez """
print('O faturamento foi de: {}. O custo foi de {} e o lucro de {}. Lembrando o faturamento foi de {}'.format(faturamento,custo,lucro, faturamento))

""" Ou """

print('O faturamento foi de: {0}. O custo foi de {1} e o lucro de {2}. Lembrando o faturamento foi de {0}'.format(faturamento,custo,lucro))

""" Uso do %s e %d """
print('O faturamento foi de: %d' % faturamento)

print('O faturamento foi de: %d. O custo foi de %d e o lucro de %d' % (faturamento,custo, lucro))
""" Se fosse string seria %s """

""" Uso do in """
print('@' in 'gaby@exp.com')
print('@' in 'gaby#exp.com')