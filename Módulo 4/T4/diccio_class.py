#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "recorrer diccionarios" del Módulo 4

dicc1 = {
    "Naranjas": {"cantidad": 25, "proveedor" : "p1"},
    "Manzanas": {"cantidad": 1, "proveedor": "p2"},
    "Fresas": {"cantidad": 240, "proveedor": "p3"},
    "Kiwis": {"cantidad": 15.33333, "proveedor": "p1"},
    "Plátanos": {"cantidad": 5.5, "proveedor": "p2"},   
}

dicc2 = {
    "Naranjas": None,
    "Manzanas": 55,
    "Fresas": 0.0,
    "Kiwis": "tres bandejas",
    "Plátanos": 5.5,
}

frutas = dicc1

# { "p1" : 25 }
pesos_subtotal = {}

for fruta in frutas.keys():  # si no indico nada, es como keys()
    # MODIFICAR para que cumpla lo que se pide:
    print("Cantidad de:", fruta, "es", frutas[fruta]['cantidad'])
    prov = frutas[fruta]['proveedor']
    if prov in pesos_subtotal:
        pesos_subtotal[prov] = pesos_subtotal[prov] + frutas[fruta]['cantidad']
    else:
        pesos_subtotal[prov] = frutas[fruta]['cantidad']

for prov in pesos_subtotal.keys():  # si no indico nada, es como keys()
      print("La cantidad del proveedor:", prov, "es", pesos_subtotal[prov])

# print()


# # Alternativa: recorrer los items (tuplas clave-valor)

# for fruta, cantidad in frutas.items():
#     # MODIFICAR para que cumpla lo que se pide:
#     if cantidad > 0:
#         print("La cantidad de:", fruta, "es", cantidad)

# print()


# # Alternativa 2, no recomendable para este caso: sacar los elementos con popitem()
# # No es recomendable simplemente por eficiencia, tenemos que hacer primero una copia
# # porque no sabemos si luego haría falta la lista original de nuevo (probable...)

# copia_frutas = dict(frutas)  # copia
# # copia_frutas = frutas.copy()  # alternativa (mejor) para copia
# while len(copia_frutas) > 0:
#     fruta, cantidad = copia_frutas.popitem()
#     # MODIFICAR para que cumpla lo que se pide:
#     if cantidad > 0:
#         print("La cantidad de:", fruta, "es", cantidad)