# $ C:\PYTHON\PP\M03\numbers.txt

filename = input("Podaj nazwę pliku: ")

with open(filename, encoding="utf-8") as stream:
	content = stream.read()

new_text = ""

for t in content:
	if t.isdigit():
		new_text = new_text + "X"
	else:
		new_text = new_text + t

print(new_text)