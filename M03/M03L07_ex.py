### 🔴 Ćwiczenie

# Napisz program, który wczytuje listę wydatków z pliku expenses.txt (plik zawiera same wielkości wydatków jako liczby), a następnie wyświetla ich sumę.


# $ C:\PYTHON\PP\M03\expenses.txt

FILE = r"C:\PYTHON\PP\M03\expenses.txt"

with open(FILE) as stream:
    content = stream.read()

expenses = content.split()
print(expenses)

sum_expenses = 0

for e in expenses:
    sum_expenses += float(e)

print(sum_expenses)