a = [3, 1, 5, 7, 9, 2, 6]

#wywołujemy element na indeksie nr 3, jest na pozycji 4, bo liczymy od 0
print(a[3])

#wywołujemy elementy pomijając pierwszy ("zerowy") i do 4 wyłącznie (tzn indeks nr 3 = "7" jest ostatni)
print(a[1:4])

#analogicznie, od indeksu nr 3 do samego końca lecimy
print(a[3:])

#wywołujemy 3 ostatnie elementy od końca
print(a[-3:])

#trzy pierwsze elementy
print(a[:3])

#wywołujemy od indeksu 3 do przedostatniego
print(a[3:-1])

#wywołujemy co drugi element
print(a[::2])

#?tu nie jestem na 100% pewien
#wywołujemy elementy od indeksu 5 do 2, a to "-1" oznacza, że cofamy się o 1
print(a[5:2:-1])

#suma tych elementów ;d
print(sum(a))

#srawdzamy czy "8" jest w naszej liście - nie ma czyli "False"
print(8 in a)

#pytamy czy "4" jest nieobecna w naszej liście, a to prawda, bo jej tam nie ma, więc "True"
print(4 not in a)