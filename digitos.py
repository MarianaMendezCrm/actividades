contador = 0
num = int(input("INGRESA UN NUMERO: "))
cadena_num = str(num)

for digito in cadena_num:
    contador = contador + 1
print("EL NUMERO ", num,"TIENE", contador,"DIGITOS")