### 🔴 Ćwiczenie # Popraw kod z M03L12 tak, aby wykorzystać unpacking.
# Podpowiedź: w Twoim programie wykorzystujesz metodę `split()`, aby podzielić nazwę pliku na dwie części: nazwę i rozszerzenie. Przypisz te dwie informacje do dwóch osobnych zmiennych w JEDNEJ linii.

import glob

NEW_EXTENSION = ".bak"

files = glob.glob(input("Podaj nazwę pliku: "))

for file in files:

    if "." in file:
        filename_parts = file.rsplit(".", maxsplit=1)
        name, extension = filename_parts
    else:
        name = file

    print(f"{file} -> {name}{NEW_EXTENSION}")