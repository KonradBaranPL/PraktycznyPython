### 🔴 Ćwiczenie # Napisz program, który anonimizuje dane statystyczne w tekstach poprzez zastąpienie wszelkich liczb iksami.

text = input("Podaj tekst: ")

for t in text:
	if t.isnumeric():
		new_text = text.replace(t, "X")

print(new_text)
