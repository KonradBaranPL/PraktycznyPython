### 🔴 Ćwiczenie
# Popraw kod z M03L09 tak, aby wczytać wydatki do listy, a następnie wylicz sumę i średnią wydatków, a także jakiej kwoty był najmniejszy i największy wydatek. Użyj wbudowanych funkcji sum, min oraz max.

# $ C:\PYTHON\PP\M03\expenses_ex.txt

FILE = r"C:\PYTHON\PP\M03\expenses_ex.txt"

with open(FILE, encoding="utf-8") as stream:
    content = stream.read()

expenses_lines = content.split("\n")

summary_expenses = 0

expenses_list = []
for line in expenses_lines:
    tokens = line.split()
    if tokens: # sprawdzenie czy lista nie jest pusta
        expense = float(tokens[0])
        expenses_list.append(expense)

total = sum(expenses_list)
maximum = max(expenses_list)
average = total / len(expenses_list)

print(total)
print(maximum)
print(average)