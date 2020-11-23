m = [[1,2],[3,4],[5,6]]
n = [[5,10,15,0],[0,0,20,0]]

# filas y columnas del resultado
a = len(m)  # filas de m
filas = a
d = len(n[0])  # columnas de n
columnas = d
b = len(m[0])  # columnas de m
c = len(n)  # filas de n
if b != c:
    print("Error, no calculable")
    exit(1)
# calcular r[0][0] le llamo x
x = 0
r=[]
for j in range(a):
    lista=[]
    for k in range(d):
         # Resultado para una celda dada
        for i in range(b):
            sumando = m[j][i] * n[i][k]
            x = x + sumando
        lista.append(x)
        x=0
    r.append(lista)
print(r)