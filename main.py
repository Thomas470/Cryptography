letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
't', 'u', 'v', 'w', 'x', 'y', 'z']

chave = input("Insira qual será a chave (letra): ")
chave.lower()

mensagem = input("Digite a mensagem: ")
mensagem.lower()

def Criptografa():
    global textoFinal
    textoFinal = ''
    for caracetere in mensagem:
        if caracetere == ' ' or caracetere == ',' or caracetere == "(" or caracetere == ")" or caracetere == ":":
            indiceSimbolo = mensagem.index(caracetere)  # Tratamento de símbolos
            m = indiceSimbolo
            textoFinal = textoFinal + mensagem[m]
        else:
            cifraDeCesar = letras[letras.index(chave):] + letras[:letras.index(chave)]  # Cifra
            if caracetere in letras:
                   caracetere = cifraDeCesar[letras.index(caracetere)]  # Realizando a Criptografia
                   textoFinal = textoFinal + caracetere
            else:
                textoFinal = textoFinal + caracetere  # Caso os caracteres não sejam compatíveis com as letras básicas do alfabeto
                print("Caractere incompatível com as letras básicas do alfabeto.")
                exit()
    print("A mensagem criptografada é:", textoFinal)

def Descriptografa():
    global textoFinal
    textoFinal = ''
    for caracetere in mensagem:
        if caracetere == ' ' or caracetere == ',' or caracetere == "(" or caracetere == ")" or caracetere == ":":
            indiceSimbolo = mensagem.index(caracetere)  # Tratamento de símbolos
            m = indiceSimbolo
            textoFinal = textoFinal + mensagem[m]
        else:
            cifraDeCesar = letras[letras.index(chave):] + letras[:letras.index(chave)]  # Cifra
            if caracetere in letras:
                   caracetere = letras[cifraDeCesar.index(caracetere)]  # Realizando a Descriptografia
                   textoFinal = textoFinal + caracetere
            else:
                textoFinal = textoFinal + caracetere   # Caso os caracteres não sejam compatíveis com as letras básicas do alfabeto
                print("Caractere incompatível com as letras básicas do alfabeto.")
                exit()
    print("A mensagem criptografada é:", textoFinal)


modo = input("Digite C para criptografar uma mensagem ou D para descriptografar: ")
if modo == 'C':
    Criptografa()
else:
    Descriptografa()
