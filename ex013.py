nome = input('Qual seu nome? ')
nome_tamanho = len(nome)

if nome_tamanho <= 5:
    print('Seu nome é curto')
elif nome_tamanho <= 7:
    print('Seu nome é médio')
elif nome_tamanho <= 9:
    print('Seu nome é grande')
