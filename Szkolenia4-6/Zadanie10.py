import random

dolny_przedzial = int(input("Podaj dolny przedział liczb do naszej maszyny losującej: "))
gorny_przedzial = int(input("Podaj górny przedział: "))

komputer = random.randint(dolny_przedzial,gorny_przedzial)

wynik = gorny_przedzial - dolny_przedzial

wybor = int(input("Podaj swój wybór liczby z przedziału jaki wybrałeś: "))
licznik = 0

if wybor < dolny_przedzial or wybor > gorny_przedzial:
    print("Wybrałeś zły numer. Koniec gry.")

while wynik <= 0:
    print(f"Wybrałeś liczbę: {wybor}")
    print(f"Komputer wylosował liczbę: {komputer}")
    if wybor == komputer:
        print("WYGRAŁEŚ!")
        print(f"Zdobyłeś {wynik} punktów.")
        break
    else:
        print("Niestety, niepoprawny strzał.")
        wynik += -1