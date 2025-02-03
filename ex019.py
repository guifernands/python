chave = 'gladiador'
palavra = ['*'] * len(chave)

while True:
    tentativa = input('Digite uma letra: ').lower()

    if len(tentativa) > 1:
        print('[ERRO] Digite apenas uma letra.')
        continue
    
    if tentativa in chave:
        for i, letra in enumerate(chave): # Substitui o caractere na posição correta
            if letra in tentativa:
                palavra[i] = tentativa
    else:
        print('Letra não encontrada.')