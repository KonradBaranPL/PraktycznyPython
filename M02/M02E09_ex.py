### 🔴 Ćwiczenie
# Napisz program, który prosi o jeden, pojedynczy znak, a następnie wyświetla, czy jest to liczba, litera, biały znak czy znak specjalny. # Białe znaki to spacja, tabulacja i nowa linia.

char = input("Podaj jeden dowolny znak: ")

if len(char) == 1:
	if char.isalpha():
		print("To jest litera")
	elif char.isnumeric():
		print("To jest cyfra")
	elif char.isspace():
		print("biały znak")
	else:
		print("znak specjalny")
else:
	print("Podałeś za dużo znaków")