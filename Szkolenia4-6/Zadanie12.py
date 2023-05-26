# alfabet = ["a", "b", "c", "d", "e", "f"]
print(ord('A'))

for i in range(65, 91):
    print(chr(i))

for i in range(90, 64, -1):
    print(chr(i))


import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)