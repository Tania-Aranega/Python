x = 0
n = 0
suma = 0
cont = True

while cont == True: #Indica que el número es distinto de 0.
    x = input("Introduce menos y usa el 0 para indicar que no añades más números:")
    a = float(x)
    cont = bool(a)
    suma = suma + a
    n = n - 1

cont = False
print(f"La suma de los números añadidos es {suma}") 
promedio = suma / n
print(f"El promedio de los números añadidos es {promedio}")