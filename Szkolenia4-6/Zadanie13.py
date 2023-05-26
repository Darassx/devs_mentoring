words = {}
#
# print("Dodajemy słowa do słownika wraz z definicjami")


while True:
    print("1. Dodaj słowo wraz z definicją")
    print("2. Znajdź definicję słowa")
    print("3. Usuń słowo wraz z definicją z słownika")
    print("4. Wczytaj wszystkie słowa ze słownika.")
    print("5. Zakończ program")

    choice = int(input("Wybierz opcję z Menu: "))
    if choice == 1:
        word = input("Wpisz słowo, które chcesz dodać do słownika: ")
        definition = input("Podaj definicję słowa: ")
        words[word] = definition
    elif choice == 2:
        word_to_find = input("Wybierz słowo, dla którego chcesz odszukać definicję: ")
        if word_to_find not in words:
            print("Takie słowo nie istnieje w słowniku.")
        else:
            print(words.get(word_to_find))
    elif choice == 3:
        word_to_delete = input("Wybierz słowo, które chcesz usunąć ze słownika: ")
        if word_to_delete not in words:
            print("Takie słowo nie istnieje w słowniku.")
        else:
            del words[word_to_delete]
    elif choice == 4:
        print("Oto wszystkie słowa z naszego słownika:\n")
        for key, value in words.items():
            print(key, value)
    else:
        print("Koniec programu")
        break

