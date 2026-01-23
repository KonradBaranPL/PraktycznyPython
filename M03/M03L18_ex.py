### 🔴 Ćwiczenie

# Rozwiń program z poprzedniego ćwiczenia tak, aby użytkownik mógł podać kilka słów (rozdzielając je spacją). Program powinien zliczyć ile jest komentarzy, w których występuje którekolwiek z podanych słów.

# Na przykład:
# jest -> 3
# jest tego -> 4
# jest pliku -> 4


DATA_FILE = "comments.txt"

INTERPUNCTION = "..,;:?!…—–-()[]„”\"'«»/\\%*#@&^_=+|~`"


with open(DATA_FILE, encoding="utf-8") as stream:
    content = stream.read()

comments = content.split("\n")

list_of_comments = []
for comment in comments:
    comment = comment.lower()
    for i in INTERPUNCTION:
        if i in comment:
            comment = comment.replace(i,"")
    comment_words = comment.split()
    list_of_comments.append(comment_words)

keywords = input("Jakiego słowa szukasz? ").lower()

keywords_list = keywords.split()

counter = 0
for c in list_of_comments:
    for keyword in keywords_list:
        if keyword in c:
            counter += 1
            break

print(f"Przynajmniej jedno z podanych słów: '{keywords}', pojawiło się w {counter} komentarzach")