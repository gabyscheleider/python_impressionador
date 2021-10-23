""" Condições em Python """
""" IF condição: """
"""     O que realizar """
######################################
meta = 50000
qt_vendida = float(input('Valor vendido: '))
vendas = qt_vendida - meta

""" 
if qt_vendida > meta:
    print('Batemos a meta de venda, a quantidade vendida foi de {} e a meta era {}. Foram vendidos {} produtos a mais que a meta'.format(qt_vendida,meta,vendas))
else:
    print('A meta não foi batida, faltaram {} produtos. Vendemos somente {} e a meta era de {}'.format(vendas,qt_vendida,meta)) """
######################################

if qt_vendida <= meta:
    bonus = 0.02 * qt_vendida
elif qt_vendida > (meta *2):
    bonus = 0.2 * qt_vendida
else:
    bonus = 0.05 * qt_vendida

print('O bonus dele foi de: {}'.format(bonus))

''' Verificar se o input está preenchido '''
faturamento = float(input('Qual foi o faturamento da loja?'))
custo = float(input('Qual o custo de produção esse mês?'))

if faturamento and custo:
    lucro = faturamento - custo
    print('O lucro foi de: {}'.format(lucro))
else:
    print('Fatura e Custo precisam ser preenchidos para que o calculo seja realizado')

