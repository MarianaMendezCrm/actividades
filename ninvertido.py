numero = int(input("INGRESA UN NUMERO ENTERO: "))


signo = -1 if numero < 0 else 1
numero = abs(numero)


numero_invertido = 0
while numero != 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10


numero_invertido *= signo


print(f"EL NUMERO INVERTIDO ES: {numero_invertido}")