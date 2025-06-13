# Asystent AI dla Testera Oprogramowania

Ten projekt to prosty graficzny interfejs użytkownika (GUI) zbudowany w Pythonie. Wykorzystuje model AI (Gemini) do analizy kodu i wsparcia testera oprogramowania.

## Wymagania

- Python 3.10 lub nowszy
- System Windows
- Połączenie z internetem

## Instalacja

1. Pobierz i rozpakuj projekt na dysk.
2. Otwórz terminal (cmd) i przejdź do folderu projektu.
3. Utwórz środowisko wirtualne:

   ```
   python -m venv venv
   call venv\Scripts\activate.bat
   pip install -r requirements.txt
   ```

## Uruchamianie

Można uruchomić na dwa sposoby:

- Kliknij dwukrotnie plik `start.bat`
- Albo ręcznie w terminalu:

   ```
   call venv\Scripts\activate.bat
   python app.py
   ```

## Wymagane biblioteki

Plik `requirements.txt` zawiera potrzebne biblioteki:

```
openai
google-generativeai
Pillow
```

## Co potrafi aplikacja

- Analiza kodu
- Wykrywanie błędów i naruszeń zasad SOLID
- Propozycje poprawek
- Generowanie testów jednostkowych
- Tworzenie przypadków testowych
- Edycja prompta systemowego
- Tryb jasny / ciemny
- Historia zapytań
- Odpowiadać na zapytania użytkownika
- Użytkownik może zmodyfikować ją dowolnie