### 🔴 Ćwiczenie

# Napisz program, który pyta o nazwę pliku, a następnie zmienia jego rozszerzenie na ".bak".
# Na ten moment wystarczy, że wyświetlisz nową nazwę pliku. Realną zmianą nazwy pliku zajmiemy się w kolejnych lekcjach.
# W tym celu podzielisz nazwę pliku na "właściwą" nazwę pliku oraz rozszerzenie.
# Uwaga! Program powinien działać także dla plików, które nie mają rozszerzenia, a także dla takich, które mają w nazwie więcej niż jedną kropkę! Na przykład:
#
#   NAZWA PLIKU      -> WŁAŚCIWA NAZWA     ROZSZERZENIE
#   plik.txt         -> plik               txt
#   wiele.kropek.txt -> wiele.kropek       txt
#   bez_rozszerzenia -> bez_rozszerzenia   (pusty string)
#
# Metoda .split() zaczyna dzielenie od lewej strony. W tym przypadku konieczne jest dzielenie od prawej strony - znajdź odpowiednią do tego metodę.

NEW_EXTENSION = ".bak"

origin_filename = input("Podaj nazwę pliku: ")

if "." in origin_filename:
    filename_parts = origin_filename.rsplit(".", maxsplit=1)
    name = filename_parts[0]
    extension = filename_parts[1]
else:
    name = origin_filename

print(f"Nowa nazwa pliku: {name}{NEW_EXTENSION}")