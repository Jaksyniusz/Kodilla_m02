# Kodilla_m02
2nd module tasks

### Zadanie 2.1
Ćwiczenie

Stwórz własną listę, która zawiera różne typy danych. Zobacz czy przyjmie je bez żadnego problemu. Następnie przejdź po liście z użyciem pętli for i wydrukuj kolejne elementy. Jeśli masz jakieś wątpliwości, napisz na czacie swojej edycji bootcampa, tam z pewnością znajdzie się ktoś, kto pomoże.


### Zadanie 2.2.1
Ćwiczenie

Jeśli ciekawi Cię jakie funkcje/metody dostępne są dla obiektu typu tekst, możesz to sprawdzić wbudowaną funkcją dir. Poniższe wywołanie wypisze je wszystkie:
<pre>
greetings = "cześć, poskramiaczu lwów"
print(dir(greetings))
</pre>


### Zadanie 2.2.2
Ćwiczenie

Sprawdź dostępne metody dla listy z wykorzystaniem funkcji dir. Stwórz obiekt listy, np. tak:<br>
<pre>my_list = list()</pre><br>
A następnie wywołaj funkcję dir na obiekcie my_list.<br>
Porównaj to ze spisem dostępnym w dokumentacji o listach. Całkiem spory zasób opcji, co?<br>


### Zadanie 2.2.3
Przykład użycia /*the rest w kodzie


### Zadanie 2.3.1
Ćwiczenie

Zdefiniuj listę kierunków świata, która zawiera północ i południe. Dodaj brakujący zachód, wykorzystując operator plus. Następnie dodaj też wschód, korzystając z metody append. Wydrukuj na koniec listę.


### Zadanie 2.3.2
Ćwiczenie

Zdefiniuj ponownie listę 4 kierunków świata — północ, południe, wschód i zachód. Następnie usuń północ i południe, żeby zostawić tylko 2 kierunki. Do usuwania posłuż się komendą del. Wydrukuj listę 2 elementów, które zostały. Następnie usuń zachód komendą remove. Teraz został Ci tylko wschód (“Na wschód, tam musi być jakaś cywilizacja”). Wydrukuj także tą, jednoelementową listę.


### Zadanie 2.3.3
Ćwiczenie

Stwórz listę z liczbami: 3, 6, 17, 4, 0, -20, 20, 100. Następnie posortuj ją. Możesz wykorzystać wbudowaną metodę sort, albo wbudowaną funkcję sorted. Wynik wyświetl na ekranie.


### Zadanie 2.3.4
Ćwiczenie

W zbiorze dni tygodnia brakuje jednego!<br>
{'pon', 'wto', 'sro', 'pia', 'sob', 'nie'}.<br>
Uzupełnij go metodą update.


### Zadanie 2.3.5
Ćwiczenie

<pre>
salads = {
    "owocowa": ["ananas", "truskawka", "jagody"],
    "moja_buraczana": ["buraki", "ser kozi", "rukola"],
    "mamina": ["groszek", "kukurydza", "majonez", "ziemniaki"]
}
</pre>
Posłuży nam to jako temat przewodni motywów modyfikacji kolekcji.<br>
Zdefiniuj sobie powyższy słownik, a następnie wyświetl składniki wybranej sałatki, np. owocowej, jeśli planujesz deser, albo buraczanej, jeśli przechodzisz na wegetariańską stronę mocy.


### Zadanie 2.3.6
Zadanie: ludzie listy piszą

Stwórz nowy plik na Twoim komputerze, w którym umieścisz wszystkie zadania. Zadbaj o to, by uporządkować kod, rozdzielając go liniami z komentarzami. Pamiętasz jak to zrobić?

Zadanie 1<br>
Mamy zadaną listę z imionami: John, Michael, Terry, Eric, Graham. Zamodeluj to w Pythonie, czyli stwórz listę o nazwie name_list. Zbuduj także słownik (name_dictionary), w którym dla każdego imienia przypisz liczbę znaków, które na nie przypadają. Np. „John” to 4 znaki.<br>

Zadanie 2<br>
Masz listę liczb [1, 2, 3, 5, 6, 11, 12, 18, 19, 21].<br>
Stwórz nową listę i ją wydrukuj. Nowa lista powinna zawierać tylko liczby pierwsze z poprzedniej listy.<br>

Zadanie 3<br>
Oto lista dni tygodnia: ['pon','śro','pią','sob'].<br>
Brakuje tu kilku. Uzupełnij i wydrukuj całość. Ciekawe co będzie trudniejsze – dojście, których dni brakuje, czy użycie odpowiedniej funkcji.<br>

Zadanie 4<br>
Oto sekwencja kroków do zrobienia herbaty.<br>
<pre>
    włącz czajnik
    znajdź opakowanie herbaty
    zalej herbatę
    nalej wody do czajnika
    wyjmij kubek
    włóż herbatę do kubka
</pre>
Kosmita nie wie jak, się robi herbatę... Stwórz sekwencję zgodnie z kolejnością nieposortowaną. Następnie poprzestawiaj elementy sekwencji tak, żeby kosmita mógł zrobić sobie herbatę.


### Zadanie 2.4.1
Ćwiczenie

Stwórz w kodzie iterator z listą jak w przykładzie i wywołaj go 5 razy (o 1 raz za dużo w stosunku do wielkości listy). Co się wtedy stanie?<br>
Iterator z natury jest „leniwy”, czyli wywołuje swoje operacje dopiero, gdy go o to poprosisz. Jest to zaleta, bo dzięki temu możemy bezpiecznie przetwarzać duże ilości danych (długie listy) – nie trzeba ich od samego początku ładować do pamięci, a dane pobierane są „na żądanie”. Niedługo poznasz też generatory, które zostały zbudowane z tą samą myślą techniczną.


### Zadanie 2.4.2
Ćwiczenie

Stwórz słownik z nazwami krajów (klucze) i ich stolic (wartości) dla wszystkich sąsiadów Polski. Następnie przejdź przez słownik i wydrukuj wszystkie pary klucz-stolica.


### Zadanie 2.5.1
Ćwiczenie

Poeksperymentuj z różnymi wyrażeniami wstawianymi zamiast number * number. Pokaż szefowi swoje umiejętności, spróbuj dodawać liczby, odejmować, przeprowadzić na nich bardziej skomplikowane działania w nawiasach. Od tego zależy Twoja przyszłość w tej firmie.


### Zadanie 2.5.2
Ćwiczenie

Zakoduj listę składaną, która tworzy nową listę z liczbami długość słów (obliczysz je funkcją len). Oto lista do przerobienia: ['Arystoteles','Platon','Sokrates'].


### Zadanie 2.5.3
Zadanie: listy składane

Umieść dwa zadania w jednym pliku. Oczywiście jak zawsze za zadanie tworzymy nowy folder, a w nim plik main.py. Oto one:<br>
Zadanie 1<br>
Użyj listy składanej, aby stworzyć listę sześcianów (potęgi trzeciej) liczb z zakresu od 1 do 10. Następnie użyj pętli for in, aby zwrócić w konsoli liczby niepodzielne przez 2.<br>
Zadanie 2<br>
Dana jest lista: [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]. Zadeklaruj ją w Pythonie, a następnie użyj slicingu, by otrzymać listę, która zawiera tylko zera z tej kolekcji. Potem użyj tej samej techniki do zwrócenia listy, która zawiera wszystkie inne liczby tylko nie zera z tej kolekcji.<br>
Możesz wykonać to w kilku krokach (stworzenie kilku list pośrednich), jak i w jednym.


### Zadanie 2.6
BONUS. Samodzielne ćwiczenia dla orłów

Na koniec mamy jeszcze coś specjalnego – jeśli chcesz ugruntować swoją wiedzę, sprawdzić się i trochę poszperać w internecie, zapraszamy do zrobienia tych ćwiczeń!<br>
Na ćwiczenia ponownie stwórz nowy plik i podeślij go mentorowi, kiedy skończysz.<br>
Powodzenia.<br>

Ćwiczenie 1

Oto dane, które musisz przekleić do swojego pliku.<br>
<pre>
exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []
best_student = ("",0)
</pre>
Zidentyfikuj najlepszych i najgorszych uczniów<br>
Uczniowie klasy 1A pisali niedawno egzamin z języka angielskiego. Wyniki każdego z uczniów zostały umieszczone w słowniku przypisanym do zmiennej exam_points. Pomóż nauczycielowi w przygotowaniu listy uczniów, którzy:<br>
Nie zdali egzaminu. Są to wszyscy uczniowie z oceną niedostateczny. Przypisz ich do zmiennej failed_students Zdali egzamin śpiewająco! Są to wszyscy uczniowie z oceną 'bardzo dobry'. Przypisz ich do zmiennej top_students Nauczyciel chciałby też znać imię najlepszego ucznia oraz liczbę punktów, jaką uzyskał podczas egzaminu. Zapisz tę informację w postaci krotki, której pierwszą wartością będzie imię ucznia, a drugą wartością będzie liczba punktów. Przypisz tę krotkę do zmiennej best_student.<br>
Skala ocen z egzaminu:<br>
0 - 45 niedostateczny 46 - 60 dopuszczający 61 - 75 dostateczny 76 - 90 dobry 91 - 100 bardzo dobry<br>

Ćwiczenie 2

Na potrzebę tego zadania musisz utworzyć drugi plik i przekleić do niego poniższy kod:<br>
<pre>
names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}
</pre>
Stwórz słownik imion Do zmiennej names została przypisana lista imion męskich.<br>
Stwórz słownik, którego kluczami będą pierwsze litery imion w liście names, a wartościami będą wszystkie imiona, które zaczynają się na daną literę.<br>
Słownik przypisz do zmiennej name_dict.<br>
Na przykład:<br>
name_dict['P'] powinien zwracać imiona: Paweł, Piotr<br>
Podpowiedź Miej na uwadze, że imiona w słowniku nie powinny się powtarzać!<br>

Ćwiczenie 3

Kod do przekopiowania:<br>
<pre>
num = 30
fibonacci = []
</pre>
Stwórz listę zawierającą kolejne elementy ciągu Fibonacciego<br>
Ciąg Fibonacciego to sekwencja, w której każda kolejna liczba jest sumą dwóch poprzednich liczb.<br>
Na przykład:<br>
1,1,2,3,5,8,13... Napisz program, który zwraca listę kolejnych 30 elementów ciągu Fibonacciego.<br>
Listę zawierającą kolejne elementy ciągu przypisz do zmiennej fibonacci<br>

Ćwiczenie 4

Kolejny kod do przekopiowania do nowego pliku:<br>
<pre>
a = 1
b = -2
c = -5

def equation(a,b,c):
  pass
</pre>
Zadanie: Program do rozwiązywania równania kwadratowego Stwórz funkcję equation, która jako argumenty bierze zmienne a, b, c będące współczynnikami równania kwadratowego, a następnie oblicza rozwiązania tegoż równania.<br>
Podpowiedź W pierwszej kolejności, funkcja main na podstawie zadanych argumentów powinna obliczać wyróżnik równania kwadratowego - czyli znaną wszystkim ze szkoły średniej deltę.<br>
Następnie w zależności od tego, czy delta jest większa, równa lub mniejsza od 0 - funkcja powinna zwracać odpowiednio:<br>
Jeśli delta > 0: dwa rozwiązania x1 oraz x2. Niech funkcja zwraca je jako krotkę.<br>
Jeśli delta = 0: jedno rozwiązanie x0. Niech funkcja zwraca wtedy tylko tę zmienną.<br>
Jeśli delta < 0: brak rozwiązań. Niech funkcja zwraca wtedy tekst "Brak rozwiązań".