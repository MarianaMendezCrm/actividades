n = int(input("INGRES UN NUMERO: "))


for i in range(1, n + 1):
    espacios = ' ' * (n - i)
    estrellas = '*' * (2 * i - 1)
    print(espacios + estrellas)