### 🔴 Ćwiczenie # Rozwiń program z poprzedniej lekcji tak, aby wyświetlał komunikat błędu, gdy użytkownik nie poda nazwy pliku. Wyświetl błąd także wtedy, gdy poda więcej niż jeden plik.

# $ python C:\PYTHON\PP\M04\M04L03_ex.py example.txt
# $ python C:\PYTHON\PP\M04\M04L03_ex.py another.txt

import sys


if len(sys.argv) != 2:
    sys.exit(1)

file = sys.argv[1]

with open(file, encoding="utf-8") as stream:
    text = stream.read()

lines = text.split("\n")

lines_counter = len(lines)
words_counter = len(text.split())
characters_counter = len(text)

print(lines_counter, words_counter, characters_counter, file)


# ROZWIĄZANIE: 

import sys


if len(sys.argv) == 1:
    print("Nie podałeś żadnego pliku")
    sys.exit(1)
elif len(sys.argv) > 2:
    print("Podałeś za dużo plików")
    sys.exit(2)