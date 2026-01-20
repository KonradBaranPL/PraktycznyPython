### 🔴 Ćwiczenie

# Rozwiń program z poprzedniego ćwiczenia tak, aby znajdować wszystkie pliki pasujące do podanego przez użytkownika wzorca i zmienić ich rozszerzenie na .bak.
# Na ten moment dalej jedynie wyświetl, jaką zmianę byś dokonał(a) - realną zmianą nazwy pliku zajmiemy się w kolejnych lekcjach.

import glob

NEW_EXTENSION = ".bak"

files = glob.glob(input("Podaj nazwę pliku: "))

for file in files:

    if "." in file:
        filename_parts = file.rsplit(".", maxsplit=1)
        name = filename_parts[0]
        extension = filename_parts[1]
    else:
        name = file

    print(f"{file} -> {name}{NEW_EXTENSION}")