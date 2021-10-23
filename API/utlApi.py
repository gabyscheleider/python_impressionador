import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')

cotacoes_dic = cotacoes.json()
print(cotacoes_dic)
