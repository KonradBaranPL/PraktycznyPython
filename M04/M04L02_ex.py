### 🔴 Ćwiczenie
# Napisz program, który otwiera wskazany przez użytkownika plik (wskazany jako argument linii poleceń, a nie przez input()) i zlicza ile jest w nim znaków, słów i linii.

# $ python C:\PYTHON\PP\M04\M04L02_ex.py example.txt
# $ python C:\PYTHON\PP\M04\M04L02_ex.py another.txt

import sys

INTERPUNCTION = "..,;:?!…—–-()[]„”\"'«»/\\%*#@&^_=+|~`"

file = sys.argv[1]

with open(file, encoding="utf-8") as stream:
    text = stream.read()

words = text.split()
count_words = len(words)

characters = text.replace("\n", "")
characters = text.strip()
for i in INTERPUNCTION:
    if i in characters:
        characters = characters.replace(i,"")
count_characters = len(characters)

print(f"plik zawiera {count_words} słów, {count_characters} liter")


# ROZWIĄZANIE:
# chodziło o to żeby zliczyć znaki, a więc równiez spacje, a same litery, więc to dużo prostsze

import sys

file = sys.argv[1]

with open(file, encoding="utf-8") as stream:
    text = stream.read()

lines = text.split("\n")

lines_counter = len(lines)
words_counter = len(text.split())
characters_counter = len(text)