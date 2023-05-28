osoby = {
    '91051200119': {'kolor oczu': 'niebieski', 'imie': 'Mariusz', 'nazwisko': 'Kowalski'},
    '93071400992': {'kolor oczu': 'zielony', 'imie': 'Jadwiga', 'nazwisko': 'Słoma'},
    '99121200881': {'kolor oczu': 'piwny', 'imie': 'Jakub', 'nazwisko': 'Kledzik'},
    '88010600776': {'kolor oczu': 'brązowy', 'imie': 'Tatiana', 'nazwisko': 'Krawczyk'},
    '95090800124': {'kolor oczu': 'niebieski', 'imie': 'Łukasz', 'nazwisko': 'Krawężnik'},
        }

for pesel in osoby:
    if pesel == '91051200119':
        osoby[pesel].update({'imię matki': 'Anna', 'wiek matki': 35})
    elif pesel == '93071400992':
        osoby[pesel].update({'imię matki': 'Magda', 'wiek matki': 39})



for key, value in osoby.items():
    print(key,value)