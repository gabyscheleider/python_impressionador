""" Para pegar um texto de trás para frente: texto[índice] -> onde índice é negativo """
email = "gaby@exemplo.com"
nome = 'Gabriely Scheleider'
""" Resposta igual a X """
print(email[-10])

""" Para pegar o pedaço de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice] """

""" Pegar o texto inteiro menos a última letra (podendo escolher outras coisas) """
print(email[:-1])

""" Pegar o texto até a letra que eu defini em quantidade, nesse caso as 4 primeiras"""
print(email[:4])

""" Fazendo para ele pegar o final, ele não pega o texto das 4 primeiras letras, somente pega o final depois das 4"""
print(email[4:])

""" Para pegar um pedaço de texto por exemplo a partir das duas primeiras letras até as 6 primeiras letras """
print(nome[2:6])

""" Exercício fixação: Basta completar os prints da forma correta """
print("Tamanho do e-mail: " + str(len(email)) + " caracteres")
print("O primeiro caractere é: " + email[0])
print("O último caractere é: " + email[-1])
print("O servidor do email é: " + email[5:12])