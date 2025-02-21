lista = []

print('LISTA DE COMPRAS')
while True:
    comando = input('Selecione uma das opções [I]nserir [A]pagar [L]istar [P]arar: ').strip()

    if comando in ('I', 'i'):
        lista.append(input('Digite: '))

    elif comando in ('A', 'a'):
        if not lista:
            print('[ERRO] A lista está vazia.')
            continue

        try:
            indice = int(input('Digite o índice do item que deseja apagar: ').strip())
            if 0 <= indice and indice < len(lista):
                del lista[indice]

            else:
                print('[ERRO] Digite um índice válido.')

        except ValueError:
            print("[ERRO] Digite um número válido.")
        
    elif comando in ('L', 'l'):
        for indice, item in enumerate(lista):
            print(indice, item) 

    elif comando in ('P', 'p'):
        break

    else:
        print('[ERRO] Digite um caracter válido.')
        continue
