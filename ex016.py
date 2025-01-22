# Calculadora com while

while True:
# Primeiro número
    entrada_num = input('Digite o primeiro número: ')
    num1 = (entrada_num.isnumeric())
    sinal = ''
    passe = False

# Sinal
    if num1 is True:
        entrada_sinal = input('Escolha o sinal: \n [ad] para adição. \n [sub] para subtração. \n [div] para divisão. \n [mod] para módulo (resto da divisão). \n').lower()
        sinal = (entrada_sinal.isalpha())

        if sinal is True:
            
            if entrada_sinal == 'ad':
                sinal = '+'
                passe = True

            elif entrada_sinal == 'sub':
                sinal = '-'
                passe = True

            elif entrada_sinal == 'div':
                sinal = '/'
                passe = True

            elif entrada_sinal == 'mod':
                sinal = '%'
                passe = True

            else:
                print('[ERRO] Digite corretamente.')

        else: 
            print('[ERRO] Digite corretamente.')

    else:
        print('[ERRO] Digite um número.')

# Segundo número

    if passe is True:
        entrada_num2 = input('Digite o segundo número: ')
        num2 = (entrada_num2.isnumeric())

        if num2 is True:
            
            if sinal == '+':
                res = int(entrada_num) + int(entrada_num2)
                print(entrada_num, '+', entrada_num2, '=', res)

            elif sinal == '-':
                res = int(entrada_num) - int(entrada_num2)
                print(entrada_num, '-', entrada_num2, '=', res)

            elif sinal == '/':
                res = int(entrada_num) / int(entrada_num2)
                print(entrada_num, '/', entrada_num2, '=', res)

            elif sinal == '%':
                res = int(entrada_num) % int(entrada_num2)
                print(entrada_num, '%', entrada_num2, '=', res)

        else:
            print('[ERRO] Digite um número.')

# Sair
    sair = input('Sair? [S]im ').lower().startswith('s')
    if sair is True:
        break