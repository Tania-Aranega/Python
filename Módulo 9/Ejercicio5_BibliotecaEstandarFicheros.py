
# def palabra_larga (filename):
#     """Devuelve la palabra más larga de un fichero"""
#     longitud_inicial = 0
#     p_larga = ""
#     with open(filename, 'r') as f_read:
#         for linea in f_read:
#             for palabra in linea.split():
#                 if len(palabra) > longitud_inicial:
#                     longitud_inicial = len(palabra)
#                     p_larga = palabra
#     return p_larga

# filename = "Módulo 9/prueba-palabras.txt"
# print (palabra_larga(filename))

# #-------------------------------------------
# def numero_lineas (filename):
#     """ Cuenta el número de líneas de un fichero """
#     lineas = 0
#     with open(filename, 'r') as f_read:
#         for linea in f_read:
#             lineas+=1
#         return lineas


# filename = "Módulo 9/prueba-palabras.txt"
# print (numero_lineas(filename))

# #-------------------------------------------

# def potencia (base=2):
#     """Calcula las potencias de 2 hasta 50)"""
#     exponente = 0
#     while exponente < 50:
#         yield base**exponente
#         exponente+=1


# it = list(potencia())

# with open('Módulo 9/potencias.txt', 'w') as f_write:
#     for i in it:
#         f_write.writelines(str(i) + "\n")


# #--------------------------------------


# def potencia (base=2):
#     """Calcula las potencias de 2 hasta 50)"""
#     exponente = 0
#     while exponente < 50:
#         yield base**exponente
#         exponente+=1


# with open('Módulo 9/potencias.txt', 'w') as f_write:
#     for i in potencia():
#         f_write.write(str(i) + "\n")

#--------------------------------------

import datetime
import sys

def tiempo_transcurrido(day, month, year):
    today = datetime.date.today()
    print(today)
    past = datetime.date(year, month, day)
    diferencia = abs(today - past)
    print("Han pasado", diferencia.days * 24, horas)


year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])
print (sys.argv)

tiempo_transcurrido(day, month, year)
