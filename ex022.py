inserir = ''
apagar = ''
listar = ''
lista = []

comando = input('LISTA DE COMPRAS \n Selecione uma das opções [I]nserir [A]pagar [L]istar: ').isupper()

if comando == 'I':
    lista.append(input('Digite: '))
    
print(lista)