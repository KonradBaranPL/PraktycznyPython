### 🔴 Ćwiczenie # Napisz program, który anonimizuje dane statystyczne w tekstach poprzez zastąpienie wszelkich liczb iksami.

text = input("Podaj tekst: ")

new_text = ""

for t in text:
	if t.isdigit():
		new_text = new_text + "X"
	else:
		new_text = new_text + t

print(new_text)
