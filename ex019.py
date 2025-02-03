chave = 'gladiador'
palavra = ['*'] * len(chave)
t = 0

while True:

    if '*' in palavra:
        t+=1
        tentativa = input('Digite uma letra: ').lower() # Letra que o usuário quer chutar

        if len(tentativa) > 1:
            print('[ERRO] Digite apenas uma letra.')
            continue
        
        if tentativa in chave:
            for i, letra in enumerate(chave): # Substitui o caractere na posição correta
                if letra == tentativa:
                    palavra[i] = tentativa
        else:
            print('Letra não encontrada.')

        print(''.join(palavra)) # Mostra o progresso da palavra

    else:
        print('PARABÉNS!! Você acertou a palavra depois de',t ,'tentativas!')
        break