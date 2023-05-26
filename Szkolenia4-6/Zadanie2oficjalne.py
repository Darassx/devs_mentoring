n = int(input("How many numbers you wanna give?: "))
total_sum = 0

for i in range(n):
    number = int(input(f"What is the number nr {i}: "))
    if number < 0:
        print("We don't wanna the negative ones.")
        continue

    total_sum += number

print(total_sum)
