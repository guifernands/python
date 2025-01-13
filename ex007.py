valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1 > valor2:
    print(valor1, 'é maior que', valor2)
elif valor2 > valor1:
    print(valor2, 'é maior que', valor1)
else:
    print('[ERRO] Números iguais ou letras.')