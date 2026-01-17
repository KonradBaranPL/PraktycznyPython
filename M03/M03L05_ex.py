### 🔴 Ćwiczenie

# 1. Rozwiń program z poprzedniego ćwiczenia tak, aby zapisać zanonimizowany tekst do nowego wyjściowego pliku. 
# 2. Poproś użytkownika zarówno o nazwę pliku wejściowego (tego, który mamy odczytać, np. plik.txt), jak i wyjściowego (tego, do którego mamy zapisać). 
# 3. Jeżeli użytkownik nie poda nazwy pliku wyjściowego, wówczas wypisz zanominimizowany tekst funkcją print.
# 4. Jeżeli plik wyjściowy już istnieje, to go nie nadpisuj. W tym celu trzeba wykorzystać funkcję open w inny sposób. Jak? Znajdź w dokumentacji tej funkcji!

# $ C:\PYTHON\PP\M03\numbers.txt

filename = input("Podaj nazwę pliku do odczytu: ")

output_filename = input("Podaj nazwę pliku do zapisu: ")

with open(filename, encoding="utf-8") as stream:
	content = stream.read()

new_text = ""

for t in content:
	if t.isdigit():
		new_text = new_text + "X"
	else:
		new_text = new_text + t

# print(new_text)

if output_filename: 
    with open(output_filename, "x") as writer:
        writer.write(new_text)
    print("Zapisano do pliku")
else:
	print(new_text)