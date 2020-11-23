lista = input("Dime una lista de palabras:")

clave = ""


for i in lista.split(): # Recorrer la lista
    if clave.lower().find(i.lower()) >= 0: # Si hay una palabra en la lista igual que la palabra clave
        print(i, "Esta repetida") # Se imprimen la palabra que se repite
    clave = clave + " " + i 
