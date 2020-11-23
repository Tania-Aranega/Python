#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def min_temp_spread_from_csv_file(filename, enc="utf-8"):
    """Devuelve d, min, máx, que son el valor número del día, su temperatura mínima, y su temperatura máxima, 
    para el día que tenga la menor diferencia (más-mín), de entre los contenidos en el ficero."""
    COL_TEMP_MAX = 1 #columna 2
    COL_TEMP_MIN = 2 #columna 3
    COL_DIA = 0 #Columna 1
    try:
        dif_ganadora = 999
        day = 0
        mx = 0
        mn = 0
        with open(filename, "r") as f_read:
            f_read.readline() #Descartar la cabecera
            for line in f_read:
                line = line.strip()
                l = line.split(",")
                mx = float(l[COL_TEMP_MAX])
                mn = float(l[COL_TEMP_MIN])
                dif_actual = mx - mn
                if dif_actual < dif_ganadora:
                    dif_ganadora = dif_actual
                    day_gan = int(l[COL_DIA])
                    mx_gan = mx
                    mn_gan = mn
                    # print(f"Nuevo candidato: {day_gan}, {mx_gan}, {mn_gan}")

    except FileNotFoundError:
        print(f"ERROR. El archivo '{filename} no existe.")
    return day_gan, mx_gan, mn_gan 




flashcard_filename ="weather.csv"
dy, mn, mx = min_temp_spread_from_csv_file(flashcard_filename)

print(f"El resultado final es : día  {dy}, máxima de {mx} ºF, mínima de {mn} ºF, diferencia de {mx - mn} ºF")
