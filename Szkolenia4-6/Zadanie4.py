#co tu robi tak łatwe zadanie ;p

choice = int(input("Choose the day of the week by choosing a number from 1 do 7: "))

#jak się zabezpieczyć jakby user wpisał string? Kojarzę coś takiego jak "Try:", a jakoś inaczej?

if choice == 1:
    print("Monday")
elif choice == 2:
    print("Tuesday")
elif choice == 3:
    print("Wednesday")
elif choice == 4:
    print("Thursday")
elif choice == 5:
    print("Friday")
elif choice == 6:
    print("Saturday")
elif choice == 7:
    print("Sunday")
elif choice < 0 or choice > 7:
    print("There is no such a day.")
else:
    print("Something went wrong.")