palavra = input('Digite uma palavra: ')
palavra_tam = len(palavra)
indice = 0
palavra_nova = ''

while indice < palavra_tam:
    letra = palavra[indice]
    palavra_nova += letra
    caracter = '^'
    palavra_nova += caracter
    indice += 1

print(palavra_nova)