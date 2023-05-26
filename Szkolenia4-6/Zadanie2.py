#Are you lucky?

import random

print("Are you LUCKY today?\n")
number = int(input("What is your number?: "))

computer_number_1 = random.randint(0, 200)
computer_number_2 = random.randint(0, 50)
computer_number_3 = random.randint(0, 10)
computer_number_4 = random.randint(-100, 100)
computer_number_5 = random.randint(-50, 0)

computer = [computer_number_1, computer_number_2, computer_number_3, computer_number_4, computer_number_5]
computer_final = random.choice(computer)

sum = 0
sum += number | computer_final
print(sum)

# wiem, że w tym zadaniu chodziło o użycie pętli for, ale zacząłem realizować ten pomysł i już tak to zostawiłem

if sum == -100 or sum == 0 or sum == 100:
    print("You are LUCKY as fuck!")
elif sum == number:
    print("What the fuck.")
elif sum < 0:
    print("You are not UNLUCKY!")
elif sum > 0:
    print("All right")
else:
    print("Something went wrong.")


