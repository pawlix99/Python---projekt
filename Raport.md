## Raport projektu z Języków Symbolicznych

 
### "Warcaby"

Paweł Sikora/n
Nr. Albumu: 130580

### Założenia projektowe

Założeniem projektu było stworzenie gry strategicznej w Okręty.
Gra została wykonana w języku programowania Python.
Sposób działania i zachowania gry jest stworzony według zaleceń prowadzącego 
i udostepnionych przez niego materiałów.

### Przebieg

Program został napisany przy pomocy biblioteki Pygame. Pygame okazał się 
funkcjonalny w pisaniu gry, wiele problemów zostało poruszone w poradnikach,
dokumentacji i na forach internetowych.
Cały program podzielony jest na cztery pliki. Plik START.py
odpowiedzialny jest za poprawne uruchomienie gry, plik MyException.py zawiera jedynie klasę wyjątków. 
W pliku Interfejs.py umieściłem kod odpowiedzialny za widoczne aspekty gry,
w tym klasę Window zawierającą metodę wirtualną, klasę AlienShip, odpowiadającą za drugiego gracza – komputer,
dziedziczącą po klasie Ship i korzystające z metody wirtualnej getPositionInField.
Używam tu również wyjątków, przy funkcji odpowiadającej za rysowanie statków,
wyrażenia lambda do ustalania rozmiaru rysowanego statku jak i list comprehensions do tworzenia pól gry. 
W pliku Gra.py mieści się cała logika gry.
Wykorzystuję tu również bibliotekę Random w celu losowego ustalania pozycji statków komputera
i losowych strzałów na nasze okręty.
Spotkamy się z główną klasą Battle, dziedziczącą po klasie Window.
W tej części programu korzystam z wyrażeń lambda w celu operacji na polach wokół statku,
a za pomocą list comprehensions obsługuję tablicę celnych i spudłowanych strzałów.
Głównym problemem było obmyślenie prawidłowego zachowania po celnym strzale komputera (superInstynkt)
jak i odpowiednie przechowywanie wszystkich danych, np.takich jak oddane strzały.
