n = int(input("INGRESA UN NUMERO: "))


suma_pares = 0
suma_impares = 0


for i in range(1, n + 1):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i


print(f"\nSUMA DE PARES: {suma_pares}")
print(f"SUMA DE IMPARES: {suma_impares}")