# Pomóż zespołowi Stanford AI Lab przeanalizować zbiór danych składający się z 50 tys. recenzji filmów, dzięki czemu będą mogli automatycznie określać sentyment nowych komentarzy i wypowiedzi w internecie. W szczególności zależy im, aby zidentyfikować te najbardziej pozytywne i negatywne wypowiedzi wśród milionów neutralnych komentarzy - dzięki temu będą mogli udostępnić te najbardziej pozytywne, a w przypadku tych najbardziej negatywnych będą mogli zareagować i odpowiedzieć zanim taki komentarz dotrze do szerszego grona.

# 1. Wszystkie pliki znajdują się w katalogu M03/data/aclImdb/train. W podkatalogu "pos" znajdują się pozytywne komentarze, tzn. minimum 7/10. W podkatalogu "neg" znajdują się negatywne komentarze, czyli te 6/10, 5/10 i niżej. Każda recenzja to osobny plik.
# 2. W recenzjach znajdują się fragmenty HTML - "<br />" oznaczający znak końca linii. Takie fragmenty zastąp spacją.
# 3. Wczytaj wszystkie pozytywne i negatywne recenzje do dwóch osobnych zmiennych. Będzie łatwiej, jeśli każdą recenzję będziesz reprezentować nie jako string, tylko jako listę słów. Tak więc każda z tych dwóch osobnych zmiennych będzie listą list.
# 4. Następnie poproś użytkownika, aby wpisał komentarz, którego sentyment chce wyliczyć. Podziel ten komentarz na słowa.
# 5. Sentyment poszczególnych słów w tym komentarzu liczymy wg wzoru (positive-negative)/all_, gdzie positive to liczba pozytywnych recenzji, w których pojawiło się to słowo. Negative to liczba negatywnych recenzji, w których pojawiło się to słowo. Natomiast all_ to liczba wszystkich recenzji, w których pojawiło się to słowo. Na przykład, jeśli dane słowo pojawia się w 5 pozytywnych i 5 negatywnych recenzjach, to jego sentyment wynosi (5-5)/10 = 0.0. Jeśli dane słowo pojawia się w 9 pozytywnych i 1 negatywnej recenzji, to jego sentyment wynosi (9-1)/10 = +0.8. Jeśli dane słowo pojawia się w 90 pozytywnych i 10 negatywnych recenzjach, to jego sentyment wynosi (90-10)/100 = +0.8, tak samo jak wcześniej. Tak więc liczba zawsze jest z zakresu od -1.0 do +1.0. 
# 6. Sentyment całego tego komentarza to średnia arytmetyczna sentymentu wszystkich słów. Tak więc wystarczy zsumować sentyment poszczególnych słów i następnie taką sumę podzielić przez liczbę słów. W ten sposób sentyment całego komentarza też będzie z zakresu od -1.0 do +1.0.
# 7. Cały komentarz uznajemy za pozytywny, gdy jego sentyment jest > 0, a negatywny gdy jest < 0.
###############################################################################################################
import glob


PATH_POSITIVE_REVIEWS = r"C:\PYTHON\PP\M03\data\aclImdb\train\pos\*.txt"

PATH_NEGATIVE_REVIEWS = r"C:\PYTHON\PP\M03\data\aclImdb\train\neg\*.txt"

HTML_ELEMENT = "<br />"


files_positive = glob.glob(PATH_POSITIVE_REVIEWS)
files_negative = glob.glob(PATH_NEGATIVE_REVIEWS)

all_positive_reviews = []

all_negative_reviews = []

for file in files_positive:
    with open(file, encoding="utf-8") as stream:
        content = stream.read()

        content = content.replace(HTML_ELEMENT, " ")

        review = content.split()

        all_positive_reviews.append(review)


for file in files_negative:
    with open(file, encoding="utf-8") as stream:
        content = stream.read()

        content = content.replace(HTML_ELEMENT, " ")

        review = content.split()

        all_negative_reviews.append(review)


user_comment = input("Wpisz swój komentarz: ")