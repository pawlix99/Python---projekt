## Raport projektu z Języków Symbolicznych
Paweł Sikora Nr. albumu: 130580
 
### Temat projektu: 5. Warcaby

### Założenia projektowe

Założeniem projektu było stworzenie gry strategicznej w Warcaby.
Gra została napisana w języku programowania Python. 
Przy tworzeniu gry wykorzystane zostały zasady, gdzie mamy planszę 8x8, pionki mogą poruszać się tylko do przodu,
a damki poruszają się w obu kierunkach tylko o jedno pole.
Opierając się na założeniach stworzona plansza powstała, jako siatka przycisków 8x8.

### Przebieg

Do stworzenia gry wykorzystana została biblioteka tkinter, polecana przez prowadzącego.
Biblioteka ta okazała się łatwa w obsłudze, nie było większych problemów z używaniem jej,
a na wszystkie problemy można było znaleźć odpowiedzi w internecie.
Cały program zawarłem w jednym pliku.
Projekt oparłem na przyciskach, z których stworzona była siatka do planszy 8x8.
Pionki przedstawiłem w postaci napisów na przyciskach, które są aktualizowane podczas rozgrywki.
Do obsługi tych przycisków napisałem dość rozpudowaną metodę, która obsługuje wszystkie ruchy pionków oraz damek.
Spotkałem się tu ze sporymi trudnościami, musiałem wykonywać wiele testów i wciąż eliminować występujące błędy w wykonywanych ruchach.
Najwięcej problemów sprawiła mi część, polegająca na sprawdzaniu czy po wykonaniu bicia pionkiem możliwe jest kolejne bicie,
a następnie wykonanie tego bicia.
Analogicznie do pionków jeszcze więcej działań było potrzeba przy damkach, które mogą poruszać się w obydwu kierunkach.
Dodane zostały komunikaty pojawiające się w czasie rozgrywki informujące o złym ruchu jeśli wykonał go nie ten gracz, lub kiedy 
wciśnięte zostało nie dozwolone pole. Pojawia się również komunikat kiedy gracz nie zauważy,
że ma możliwość kolejnego bicia tym samym pionkiem.
O tym, do którego gracza należy obecny ruch informuje nas napis nad planszą.
Dodany został również przycisk Reset przywracający planszę do początkowego ustawienia.
Grę zawsze rozpoczyna gracz 1, z pionkami białymi (oznaczonymi jako B).
W grze mamy liczniki pionków graczy. Jeśli któryś z liczników spadnie do zera, to gra się kończy i otrzymujemy komunikat o zwycięstwie jednego z graczy.

Ponadto obok przycisku reset, dodałem przyciski test 4, test 5, test 6 oraz test 7 i 8,
które dają nam specjalne początkowe rozstawienia, potrzebne do wykonania testów.
