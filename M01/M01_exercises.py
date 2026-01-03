# L12 ZADANIE 1

# def calculate_characters():
# 	text = input("Podaj jakiś tekst: ")
# 	text_length = len(text)
# 	return text_length
#
# text_length = calculate_characters()
# print(f"Tekst ma {text_length} znaków")


# L13 ZADANIE - PROJEKT


text = input("Wpisz tekst artykułu: ")

words = len(text.split())
characters = len(text)

avg_word_length = characters / words
print(avg_word_length)
print(text.upper())