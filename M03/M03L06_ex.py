expenses = [12.99, 100, 149.99, 1990]

for expense in expenses:
    print(f"{expense} zł")

print(sum(expenses))


# inna wersja:
expenses = [12.99, 100, 149.99, 1990]

total = 0
for expense in expenses:
    total += expense  # to samo co: total = total + expense
    print(f"{expense} zł")

print(total)