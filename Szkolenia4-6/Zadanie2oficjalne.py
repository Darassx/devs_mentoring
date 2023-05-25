n = int(input("How many numbers you wanna give?: "))
sum = 0

for i in range(n):
    number = int(input("What is the number nr {}: ".format(i)))
    if number < 0:
        print("We don't wanna the negative ones.")
        continue

    sum += number

print(sum)