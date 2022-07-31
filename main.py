from random import choice
from unidecode import unidecode
from os import path

# Dicionário de palavras (normal e sem acentos)
with open(path.dirname(__file__) + "\\dicionario.txt", "rt", encoding="utf-8") as arquivo:
    dicionario = [palavra.upper() for palavra in arquivo.read().splitlines()]
    dicionario_filtrado = [unidecode(palavra) for palavra in dicionario]
    palavra = choice(dicionario_filtrado)

for tentativa in range(6):
    # Entrada do palpite, verificando sua validade
    while True:
        palpite = unidecode(input(">> ").upper())
        if len(palpite) == 5 and palpite in dicionario_filtrado:
            break
        print("\nPalavra inválida.\n")
    palpite_acentuado = dicionario[dicionario_filtrado.index(palpite)]

    # Contador de letras amarelas do palpite
    contador = {letra: palavra.count(letra) for letra in palpite}
    for letra_palpite, letra_palavra in zip(palpite, palavra):
        if letra_palpite == letra_palavra:
            contador[letra_palpite] -= 1

    # Imprime as letras de acordo com seus acertos
    for index in range(5):
        if palpite[index] == palavra[index]:
            print(f"\033[1;42m\033[1;30m {palpite_acentuado[index]} \033[0;0m ", end="")
        elif contador[palpite[index]] > 0:
            print(f"\033[1;43m\033[1;30m {palpite_acentuado[index]} \033[0;0m ", end="")
            contador[palpite[index]] -= 1
        else:
            print(f"\033[1;100m\033[1;30m {palpite_acentuado[index]} \033[0;0m ", end="")
    print()

    # Verificar vitória ou o fim da partida
    if palpite == palavra:
        print("\nPalavra Correta.")
        break
    elif tentativa == 5:
        print(f"\nVocê perdeu. A palavra era {dicionario[dicionario_filtrado.index(palavra)]}")
