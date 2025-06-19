# Asystent AI dla Testera Oprogramowania
Autor: Jakub Szaraj
E-mail: kubasz2231@gmail.com
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

## Zrzuty ekranu działania aplikacji

![1](images\1.png)
![2](images\2.png)
![3](images\3.png)
![4](images\4.png)
![5](images\5.png)
![6](images\6.png)
![7](images\7.png)  
![8](images\8.png)
![9](images\9.png)
![10](images\10.png)
![11](images\11.png)
![12](images\12.png)
![13](images\13.png)
![14](images\14.png)