nome = input('Digite seu nome: ')

if nome == '':
    print('[ERRO] Dados em branco.')
else: 
    print('Seu nome é', nome)

    print('Seu nome invertido é', nome[::-1])

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não possui espaços')

    print('Seu nome tem', len(nome), 'caracteres')

    print('A primeira letra do seu nome é', nome[0:1])

    print('A última letra do seu nome é', nome[-1])
