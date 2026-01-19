### 🔴 Ćwiczenie

# Rozwiń program z M03L07. Tym razem format pliku jest następujący: każda linia to jeden wydatek. Najpierw jest kwota wydatku, a po spacji jego opis. Opis może zawierać kolejne spacje. Plik może zawierać puste linie. Przykładowy plik to expenses-ex.txt
# W tym ćwiczeniu nie wystarczy, aby skorzystać ze .split(), dlatego że ono dzieli nie tylko na poszczególne linie, ale także po spacjach w każdej linii. Tutaj konieczne jest dzielenie tylko po znakach nowej linii. Jak to zrobić? Da się to zrobić używając .split(), ale trzeba przekazać pewien parametr. Doczytaj w dokumentacji jak dokładnie to zrobić.
# Mając już pojedynczą linię konieczne będzie dalsze jej podzielenie już po spacjach, tak aby dostać się do kwoty wydatku, która jest na początku każdej linii.


# $ C:\PYTHON\PP\M03\expenses_ex.txt

FILE = r"C:\PYTHON\PP\M03\expenses_ex.txt"

with open(FILE, encoding="utf-8") as stream:
    content = stream.read()

expenses_lines = content.split("\n")

summary_expenses = 0

for line in expenses_lines:
    if line:
        line_words = line.split()
        cost = line_words[0]
        summary_expenses += float(cost)

print(summary_expenses)

