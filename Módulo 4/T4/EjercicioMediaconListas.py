
s = 0
c = 0
x = input("Dame la lista de números: ")

l = x.split()
ln = []
for e in l:
    ln.append(float(e)) #Añadirlo a nueva lista, formada por números

lns = ln
print("Suma:", sum(ln))
lon = len(lns)
print("Media:", sum(ln)/lon)


lns.sort()
print(lns)

if lon % 2 == 1: #Es impar
    print ("Mediana:", lns[lon//2])
else:
    temp = (lns[lon//2] + lns[lon//2 + 1]) / 2
    print ("Mediana:", temp)




