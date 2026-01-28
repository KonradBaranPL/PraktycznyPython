### 🔴 Ćwiczenie # Wejdź na stronę API Narodowego Banku Polskiego, pobierz stamtąd aktualne kursy walut (URL: http://api.nbp.pl/api/exchangerates/tables/a/), a następnie zapisz je do pliku kursy.json.

import requests
import sys

URL = "http://api.nbp.pl/api/exchangerates/tables/a/"
OUTPUT_FILENAME = "PP\M04\kursy2.json"

response = requests.get(URL)

if not response.ok:
    print("Błąd pobierania danych")
    sys.exit(1)
    
# text = str(response.text) # to moja wersja - nie trzeba konwertować na stringa
text = response.text

with open(OUTPUT_FILENAME, "w") as writer:
    writer.write(text)

print(f"Zapisano w pliku {OUTPUT_FILENAME}")