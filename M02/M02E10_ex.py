### 🔴 Ćwiczenie
# Napisz program, który prosi użytkownika o hasło, a następnie dla każdego znaku wyświetla jakiego typu jest to znak (litera vs cyfra vs biały znak vs znak specjalny).


# password = input("Podaj hasło: ")
#
# for char in password:
# 	if char.isalpha():
# 		print(f"{char} - litera")
# 	elif char.isnumeric():
# 		print(f"{char} - cyfra")
# 	elif char.isspace():
# 		print(f"{char} - biały znak")
# 	else:
# 		print(f"{char} - znak specjalny")


# Wzorcowe rozwiązanie bez duplikacji kodu:

password = input("Podaj hasło: ")

for char in password:
	if char.isalpha():
		char_type = "litera"
	elif char.isnumeric():
		char_type = "cyfra"
	elif char.isspace():
		char_type = "biały znak"
	else:
		char_type = "znak specjalny"
	print(f"{char} - {char_type}")