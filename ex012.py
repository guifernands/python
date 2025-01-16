hora = input('Digite que horas são: ')

if hora is int:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 19:
        print('Boa tarde!')
    elif hora_int <= 23 and hora_int > 1:
        print('Boa noite!')
    else:
        print('[ERRO] Digite as horas corretamente.')
else: 
    print('[ERRO] Digite um número inteiro.')