### 🔴 Ćwiczenie

# Rozwiń program z poprzedniego ćwiczenia tak, aby użytkownik mógł podać kilka słów (rozdzielając je spacją). Program powinien zliczyć ile jest komentarzy, w których występuje którekolwiek z podanych słów.

# Na przykład:
# jest -> 3
# jest tego -> 4
# jest pliku -> 4

FILE_TO_OPEN = r"M03\comments.txt"
PUNCTUATION_MARK = ",.!?;:()[]{}\"'“”%<>@#*&$=/\\|^~"

with open(FILE_TO_OPEN, encoding="utf-8") as stream:
    content = stream.read()

comments_str = content.split("\n")

single_comments_lofl = []
for comment in comments_str:
    comment = comment.lower()
    for mark in PUNCTUATION_MARK:
        comment = comment.replace(mark, "")
    comment_words = comment.split()
    if comment_words: # dzięki temu nie dodam pustych list
        single_comments_lofl.append(comment_words)


searched_words = input("Podaj szukane słowo: ").lower().split()
for word in searched_words:
    print(word, end=" ")

word_counter = 0
for comment in single_comments_lofl:
    if any(word in comment for word in searched_words):
        word_counter += 1

if not searched_words:
    print("Nie podałeś żadnych słów do wyszukania")
else:
    if word_counter == 0:
        print("Żaden komentarz nie zawiera podanych słów")
    elif word_counter == 1:
        print("1 komentarz zawiera przynajmniej jedno z podanych słów")
    else:
        print(word_counter, "komentarzy zawiera przynajmniej jedno z podanych słów")


# ### TA CZĘŚĆ JEST CGPT:
# if word_counter == 0:
#     print(f"Słowo '{searched_word}' nie występuje w żadnym komentarzu 😢")
# elif word_counter == 1:
#     print(f"Słowo '{searched_word}' występuje w 1 komentarzu ✅")
# else:
#     print(f"Słowo '{searched_word}' występuje w {word_counter} komentarzach ✅")

