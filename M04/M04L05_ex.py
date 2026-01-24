### 🔴 Ćwiczenie # Rozwiń program z poprzedniej lekcji tak, aby wyniki wyświetlić w tabeli. Użyj string interpolation. Dodaj nagłówek tabeli.

# $ python C:\PYTHON\PP\M04\M04L04_ex.py example.txt another.txt

import sys

files = sys.argv[1:]

if not files:
    print("Nie podałeś żadnego pliku")
    sys.argv(1)

for file in files:    
    with open(file, encoding="utf-8") as stream:
        text = stream.read()

    lines = text.split("\n")

    lines_counter = len(lines)
    words_counter = len(text.split())
    characters_counter = len(text)

    print(lines_counter, words_counter, characters_counter, file)