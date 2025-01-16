entrada = input('Digite um número: ')

if entrada.isdigit():
    entr_int = int(entrada)
    par_impar = entr_int % 2 == 0
    par_impar_texto = 'ímpar'
else:
    print('[ERRO] Digite um número inteiro.')

if par_impar:
    par_impar_texto = 'par'

print('O número digitado é', par_impar_texto)