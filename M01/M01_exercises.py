# L12 ZADANIE 1

def calculate_characters():
	text = input("Podaj jakiś tekst: ")
	text_length = len(text)
	return text_length

text_length = calculate_characters()
print(f"Tekst ma {text_length} znaków")
