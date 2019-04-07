# Zadania_maturalne
Zawiera zadania ze zbioru zadań maturalnych - informatyka
##link do zbioru zadań: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/Matura_Zbiór_zadań_Informatyka.pdf
## Jeżeli zadanie jest z matury link powinien być zamieszczony przed opisem zadania

# Zadanie 59 - zbiór zadań
W programie wywoływane jest 3 zadanie, aby to zmeinić należy zmienić wywołanie funkcji na funkcję z innego zadania
# Wzorce wywołań:
### Zad1 - uwaga 1 zadanie długo się przetwarza
    iterator = 0
    numbs = read_file()
    for numb in numbs:
     if to_primals(numb):
            iterator += 1
    print(iterator)
### Zad2
    iterator = 0
    numbs = read_file()
    for numb in numbs:
        if pali_sum(numb):
            iterator += 1
    print(iterator)
### Zad3
    numbs = read_file()  
    count_power(numbs)
## Początek
na początku należy wczytać liczby z plki "liczby.txt", robimy to przy pomocy funkcji - read_file()
## 1) 
Zadanie pierwsze każe nam znaleźć liczby, które posiadają jedynie 3 różne czynniki pierwsze, do tego posłuży nam funkcja "to_primals"
## 2)
Przy wykonywaniu zadania drugie należy skorzystać z funkcji "rev" - odwraca liczbę oraz "pali_sum"-sprawdza czy suma liczby i jej odwrotności jest palindromem
## 3) 
Szukamy mocy liczby n czyli który element ciągu jesteśmy w stanie maksmalnie policzyć z zdanej anm liczby wg wzoru:
n1 = w(n)
n2 = w(n1)
itd...
gdzie w(n) - iloczyn cyfr liczby
Do wykonania tego zadania wykorzystywane są funkcje: multiplier- mnoży cyfry liczby, to_digits - zamienia liczbę w listę cyfr, 
count_power - liczy moc liczby oraz szuka najmniejszej i największej liczby o mocy 1
# Zadanie 65 - zbiór zadań
Wywoływane są wszystkie zadania po kolei:
```
    counters, dividers = read_file() #czyta plik
    reduced(counters,dividers) #sprawdza czy ułamek jest w fromie skróconej oraz wypisuje liczbę ułamków
    reduce(counters,dividers) #skraca ułamek i sumuje liczniki
    summary(counters, dividers) #sumuje wszystklie ułamki
```
## Początek
Jak w większości zadań maturalnych wczytujemy tutaj zawartość pliku z danymi. w tym wypadku korzystam z dwóch list, jedna z nich
przechowuje moje liczniki (counters) a druga mianowniki (denominators)
## 1)
Musimy znaleźć ułamka o najmniejszej wartości, w tym celu dzielę po prostu licznik przez mianownik i porównuję otrzymane wyniki
## 2)
Mamy podać liczbę ułamków zapisanych w postaci nieskracalnej (np 3/5), w tym celu piszemy funkcję ```nwd()```, która liczy nasz największy wspólny dzielnik dla licznika i mianownika, jeśli jest on równy 1 wtedy mamy do czynienia z ułamkiem nieskracalnym
```
        if nwd(counters[x], denominators[x]) == 1:
            iterator+=1
```
## 3) 
Musimy podać sumę wszystkich liczników skróconych ułamków, w dość prosty sposób stosujemy tutaj funkcję reduce:
```
score = 0
    for x in range(1, len(counters)):
        highest_dividor = nwd(counters[x], denominators[x])
        score += counters[x]/highest_dividor
    print(score)
```
## 4)
W tym zadaniu mamy zsumować wszystkie
