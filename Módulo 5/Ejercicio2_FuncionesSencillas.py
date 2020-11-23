import math

def calcular_circunferencia(r):
    area = math.pi * (r**2)
    return area
 
print(calcular_circunferencia(5))



x = ['hola', 'tania', 'hasta luego']

def devol_palabra_larga(l):
    max = ""
    for palabra in l:
        if len(palabra) > len(max):
            max = palabra
    return max

print(devol_palabra_larga(x))




def devol_longitud(l):
    s = 0
    for i in l:
        s = s + len(i)
    return s

print(devol_longitud(['Hola', 'Mundo']))      
