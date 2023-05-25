d = (1, [2, 4], 'tekst', 3+5j)

#ostatni element
print(d[-1])

#pierwszy i drugi element
print(d[:2])

#czy "abc" jest elementem krotki?
if "abc" in d:
    print('"abc" is in the tuple.')
else:
    print('"abc" is not in the tuple.')