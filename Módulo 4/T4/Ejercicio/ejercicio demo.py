lista = [3, 5, 2.0, -2.5, -1, 99, 8.765, 0.0]

print("Suma:", sum(lista))
print("Número:", len(lista))
print("Mínimo:", min(lista))
print("Máximo:", max(lista))

for f in lista:
    if f < 0:
        print("Negativo:", f)