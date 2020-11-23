#!/usr/bin/env python3
# -*- coding: utf-8 -*-

diccionario = {
    "a": "n",
    "b": "o",
    "c": "p",
    "d": "q",
    "e": "r",
    "f": "s",
    "g": "t",
    "h": "u",
    "i": "v",
    "j": "w",
    "k": "x",
    "l": "y",
    "m": "z",
}


def print_rot13(frase):
    """Recibe una cadena como argumento para codificar ese mensaje, la
       convierte a mensaje encriptado e imprime en pantalla la nueva cadena
       encriptada
    """
    frase_encriptada = ""

    for i in frase.casefold():
        if i in diccionario or i in diccionario.values():
            if i in diccionario.keys():
                frase_encriptada = frase_encriptada + diccionario[i]
            else:
                frase_encriptada = frase_encriptada + \
                    list(diccionario.keys())[
                        list(diccionario.values()).index(i)]
        else:
            frase_encriptada += i
    print(frase_encriptada)

