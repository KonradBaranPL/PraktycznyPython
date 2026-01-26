### 🔴 Ćwiczenie
# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo. 
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?


# "ile razy pojawia się słowo Ile ile W w w tym tekście"
comment = input("Wpisz swój komentarz: ").lower()

comment_words = comment.split()

counter = {}

for word in comment_words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1


for word in counter:
    print(f"{word} - {counter.get(word, 0)}")


# WZORCOWE ROZWIĄZANIE:

import sys

INTERPUNCTION = "..,;:?!…—–-()[]„”\"'«»/\\%*#@&^_=+|~`"

if len(sys.argv) != 2:
    sys.exit(1)

text = sys.argv[1]

text = text.lower()

for i in INTERPUNCTION:
    text = text.replace(i, " ")

word = text.split()

for word in comment_words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1


# zupełnie inne wyświetlenie wyniku niż u mnie - BARDZO WAŻNE !!!
for word, occurrancies in counter.items():
    print(f"{occurrancies:3} {word}")
