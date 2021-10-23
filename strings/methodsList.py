""" Métodos de String """
""" Não decore os métodos, os que você for mais usando com o tempo você vai decorar o que precisar.

Mas a dica é: use essa lista para consulta e busque entender como os métodos funcionam e suas aplicações, para poder consultar e usar quando precisar. """

# Métodos Embutidos no Python que funcionam em string:
    Sinal de Mais (+) -> Serve para concatenar strings
    str() -> transforma o valor em string
    in e not -> Servem para fazer verificações em string
    len() -> Calcula o tamanho do texto (quantidade de caracteres)

# Métodos Específicos de String:
    capitalize() -> Coloca a 1ª letra Maiúscula
    
    casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)
    
    count() -> Quantidade de vezes que um valor aparece na string
    
    endswith() -> Verifica se o texto termina com um valor específico e dá como resposta True ou False
    
    find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado
    
    format() -> Formata uma string de acordo com os valores passados. Já usamos bastante ao longo do programa.
    
    isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função.
    
    isalpha() -> Verifica se um texto é todo feito de letras.
    
    isnumeric() -> Verifica se um texto é todo feito por números.
    
    replace() -> Substitui um texto por um outro texto em uma string.
    
    split() -> Separa uma string de acordo com um delimitador em vários textos diferentes.
    
    splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto
    
    startswith() -> Verifica se a string começa com determinado texto
    
    strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final
    
    title() -> Coloca a 1ª letra de cada palavra em maiúscula
    
    upper() -> Coloca o texto todo em letra maiúscula
