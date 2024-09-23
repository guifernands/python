x = input("Digite qualquer coisa: ")

print("O tipo primitivo desse valor é {}".format(type(x)))
print("O valor é um número? {}".format(x.isnumeric()))
print("O valor é alfabético? {}".format(x.isalpha()))
print("O valor é um espaço? {}".format(x.isspace()))
print("O valor é alfanumérico? {}".format(x.isalnum()))
