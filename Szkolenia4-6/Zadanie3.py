numbers = []

for number in range(10):
    choice = int(input("What is your choice?: "))
    numbers.append(choice)

print("\nThese are even numbers: ")
for number in numbers:
    if number % 2 == 0:
        print(number, end=" ")

print("\n\nAnd these ones are odd: ")
for number in numbers:
    if number % 2 == 1:
        print(number, end=" ")

#Pewnie dałoby się tu stworzyć funkcję hmmmm ?