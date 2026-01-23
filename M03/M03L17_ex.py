### 🔴 Ćwiczenie
# Wczytaj listę komentarzy z pliku comments.txt. Każdy komentarz to osobna linia. Zapisz komentarze w zmiennej, pod którą kryje się lista list. Każdy komentarz reprezentuj jako listę słów, a nie jako string.
# Następnie pozwól użytkownikowi wprowadzić słowo i wyświetl w ilu komentarzach pojawia się to słowo?
# Wielkość liter nie powinna mieć znaczenia.
# Pozbądź się znaków interpunkcji.

DATA_FILE = "comments.txt"

with open(DATA_FILE, encoding="utf-8") as stream:
    content = stream.read()

content = content.lower() # tak zrobiłem "lower" po swojemu

comments = content.split("\n")

list_of_comments = []
for comment in comments:
    comment = comment.lower() # tutaj było "lower" w rozwiązaniu
    comment_words = comment.split()
    list_of_comments.append(comment_words)

key_word = input("Jakiego słowa szukasz? ").lower()

counter = 0
for c in list_of_comments:
    if key_word in c:
        counter += 1

print(f"Słowo '{key_word}' pojawiło się w {counter} komentarzach")

# nie zaimplementowałem usuwania interpunkcji