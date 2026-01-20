### 🔴 Ćwiczenie
# Rozwiń program z poprzedniego ćwiczenia tak, aby faktycznie zmieniał nazwę pliku.

import glob
import os

NEW_EXTENSION = ".bak"

files = glob.glob(input("Podaj nazwę pliku: "))

for file in files:

    if "." in file:
        filename_parts = file.rsplit(".", maxsplit=1)
        name = filename_parts[0]
        extension = filename_parts[1]
    else:
        name = file
        extension = ""

    changed_filename = name + NEW_EXTENSION

    os.rename(file, changed_filename)

    print(f"{file} -> {name}{NEW_EXTENSION}")