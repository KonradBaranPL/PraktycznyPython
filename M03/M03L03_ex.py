### 🔴 Ćwiczenie

# Rozwiń program z M02L11. Tamten program pytał użytkownika o tekst do zanonimizowania, czyli zastępował wszelkie występujące tam liczby iksami, np. 1234 -> XXXX. Tym razem zapytaj użytkownika o nazwę pliku (np. plik.txt) i wczytaj tekst właśnie z niego. Zanonimizuj go, a następnie wyświetl na ekranie.

# $ C:\PYTHON\PP\M03\numbers.txt
filename = input("Podaj nazwę pliku: ")

stream = open(filename, "r", encoding="utf8")
content = stream.read()
stream.close()

new_text = ""

for t in content:
	if t.isdigit():
		new_text = new_text + "X"
	else:
		new_text = new_text + t

print(new_text)