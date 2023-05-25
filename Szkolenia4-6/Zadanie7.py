number = int(input("What is your number?: "))

if number >= 0:
    print(number)
elif number < 0:
    print(number.__abs__())


