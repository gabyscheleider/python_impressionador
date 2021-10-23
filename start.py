""" Strings """
## Verificar se um texto está contido dentro do outro:
## Verificação IN é case sensitive

print('y' in 'Gabriely') #Lê-se 'y' está contido em 'Gabriely'? -> true

print('Y' in 'Gabriely') #Mas false se 'Y'

""" Variáveis """
qtde_vendas = 2323

print(qtde_vendas)

""" Pegando informações do usuário """
nome = input('Qual o seu nome?')

sobrenome = input('Qual o seu sobrenome?')

print(nome + ' ' + sobrenome)

""" Variáveis e tipos de variáveis """
faturamento = 1000.05
print (type(faturamento))

faturamento = 1000
print (type(faturamento))

faturamento = 1
print (type(faturamento))

faturamento = '1'
print (type(faturamento))

""" Misturando tipos de variáveis """
faturamento = 12334.23
print('O faturamento da loja foi' + faturamento) # -> errado por que faturamento não é uma string
print('O faturamento da loja foi ' + str(faturamento) + ' reais') # -> errado por que faturamento não é uma string

""" Format """
faturamento = 1000
custo = 123
lucro = faturamento - custo
print('O faturamento da loja foi {}. O custo da loja foi {}. Assim, o lucro foi de {}'.format(faturamento,custo,lucro))

''' Comparações em python - A diferente '''
# Quando vc não quiser fazer nada na sua condição você pode usar o 'pass'

email_user = 'gaby@gmail.com'

if not '@' in email_user:
    print('Email inválido')
else:
    pass