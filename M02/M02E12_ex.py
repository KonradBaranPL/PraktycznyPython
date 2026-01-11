# Napisz program, który będzie dokonywał audytu bezpieczeństwa u klientów Niebezpiecznika - jesteś odpowiedzialny za moduł sprawdzający złożoność haseł i generujący raport z rekomendacjami.
#
# 1. Poproś użytkownika o hasło, a następnie sprawdź, czy spełnia ono reguły bezpieczeństwa.
# 2. Hasło powinno mieć minimum jedną małą literę, jedną wielką literę i jeden znak specjalny.
# 3. Hasło nie może zawierać spacji!  (wewnętrzny wymóg klienta wynikający z ograniczeń ich systemu teleinformatycznego)
# 4. Hasło musi mieć minimum 8 znaków.
# 5. Jeśli hasło jest niepoprawne, wyświetl raport w punktach co należy zmienić.


password = input("Podaj hasło: ")

has_small_letter = True
has_capital_letter = True
has_special_character = True
has_no_spaces = True
is_minimum_length = True

for char in password:
	if char.islower():




	elif char.isnumeric():
		char_type = "cyfra"
	elif char.isspace():
		char_type = "biały znak"
	else:
		char_type = "znak specjalny"
	print(f"{char} - {char_type}")