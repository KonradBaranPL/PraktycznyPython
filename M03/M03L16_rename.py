### 🔴 Ćwiczenie

# Rozwiń program z M03L12 tak, aby program najpierw wyświetlił jakie nastąpią zmiany plików, następnie poprosił użytkownika o potwierdzenie i dopiero potem dokonał zmiany nazw.
# W tym celu potrzebujesz listę zmian. Każda zmiana będzie dwuelementową listą zawierającą starą i nową nazwę pliku. Będziesz mieć do czynienie z listą list.
#######################################

import glob
import os

FILE_EXTENSION = ".bak"

pattern = input("Podaj pattern nazwy plików: ") # M03\*.txt
filenames = glob.glob(pattern)

list_of_changes = []

for filename in filenames:
    if "." in filename:
        tokens = filename.rsplit(".", maxsplit=1)
        name = tokens[0]
        extension = tokens[1]
    else:
        name = filename
        extension = ""

    new_filename = name + FILE_EXTENSION

    print(filename, "->", new_filename)
    list_of_changes.append((filename, new_filename))
    print(list_of_changes)


    # os.rename(filename, new_filename)