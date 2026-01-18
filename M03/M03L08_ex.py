### 🔴 Ćwiczenie

# Napisz program, który ocenia jak bardzo "naukowo" brzmi dany tekst. W tym celu policz jak często w tym zdaniu pojawiają się liczby. Wyświetl jaki procent wszystkich "słów" to właśnie liczby.
# Postaraj się, aby program nie zwracał uwagi na interpunkcję. To znaczy, że w zdaniu "Numer 1234." drugie słowo to "1234.". Potraktuj je jako liczbę, pomimo że zawiera kropkę.
# To oznacza, że zdefiniujesz stałą zawierającą kilka znaków interpunkcyjnych.
# Samodzielnie znajdź metodę do określania, czy dany string jest liczbą.

# INTERPUNCTION = "..,;:?!…—–-()[]„”\"'«»/\\%*#@&^_=+|~`"
INTERPUNCTION = ".,%"

text = input("Wpisz tekst: ")




for i in INTERPUNCTION:
    if i in text:
        text = text.replace(i,"")


words = text.split()
print(words)

words_count = len(words)
print(words_count)

numbers_count = 0
for w in words:
    if w.isdigit:
        numbers_count += 1

print(numbers_count)


print(text)


# for t in text:
#     if t in INTERPUNCTION:
#         new_text = text.replace(t, " ")
#     else:
#         new_text = text
# print(new_text)

# Przykładowy tekst do testowania: 
# Stopa bezrobocia w Polsce w 2020 roku wyniosła 3,2%, w 2021 roku spadła do 2,9%, a w 2022 roku wzrosła do 4,1%. Wzrost bezrobocia odnotowano w każdym z ostatnich trzech lat.