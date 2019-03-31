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
############################################################################
na początku należy wczytać liczby z plki "liczby.txt", robimy to przy pomocy funkcji - read_file()
# 1) Zadanie pierwsze każe nam znaleźć liczby, które posiadają jedynie 3 różne czynniki pierwsze, do tego posłuży nam funkcja "to_primals"
# 2)Przy wykonywaniu zadania drugie należy skorzystać z funkcji "rev" - odwraca liczbę oraz "pali_sum"-sprawdza czy suma liczby i jej odwrotności jest palindromem
# 3) Szukamy mocy liczby n czyli który element ciągu jesteśmy w stanie maksmalnie policzyć z zdanej anm liczby wg wzoru:
n1 = w(n)
n2 = w(n1)
itd...
gdzie w(n) - iloczyn cyfr liczby
Do wykonania tego zadania wykorzystywane są funkcje: multiplier- mnoży cyfry liczby, to_digits - zamienia liczbę w listę cyfr, 
count_power - liczy moc liczby oraz szuka najmniejszej i największej liczby o mocy 1
