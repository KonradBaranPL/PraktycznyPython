### 🔴 Ćwiczenie

# Bazując na rozwiązaniu poprzedniego ćwiczenia, zmodyfikuj program tak, że jeżeli użytkownik poda kilka znaków, wówczas wyświetl błąd, że użytkownik powinien podać tylko jeden znak. W przeciwnym przypadku program powinien działać tak samo jak do tej pory.


char = input("Podaj jeden dowolny znak: ")
if len(char) == 1:
	if char.isalpha():
		print("To jest litera")
	else:
		print("To nie jest litera")
else:
	print("Podałeś za dużo znaków lub nie podałeś żadnego znaku")