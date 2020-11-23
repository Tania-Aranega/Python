#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def read_flashcard_file(filename, enc="utf-8"):
    """Devuelve un diccionario clave-valor en el que las claves son las preguntas, y
    los valores las respuestas, tal como se han leído de un fichero .csv"""
    question_dict = {}
    with open(filename) as f:
      for line in f:
        l = line.split(",")
        l[1] = l[1].strip()
        question_dict[l[0]] = l[1]
    return question_dict


  

    # COMPLETAR... !
    # return question_dict

# Nombre del fichero que se usará
# flashcard_filename = "flashcards_capitales_latin-1.csv"  # alternativa!
flashcard_filename = "flashcards_capitales_latin-1.csv"  # default value
read_flashcard_file(flashcard_filename)

# # Leer el fichero en cuestión
print("Flash card file to use:", flashcard_filename)
question_dict = read_flashcard_file(flashcard_filename)
questions = list(question_dict.keys())


# Escribir las instrucciones de juego
print("Welcome to the flashcard quizzer.")
print("At any time, type 'quit' to quit.")
print()


while True:
    question = random.choice(questions)
    print("Question: " + question)

    answer = question_dict[question]

    user_input = input("Your guess: ")
    user_input = user_input.upper()
    if user_input == "QUIT":
        print("Thanks for playing! Goodbye.")
        break
    elif user_input == answer:
        print("Correct!!! 🏆")
    else:
        print("Sorry, the answer was: " + answer)