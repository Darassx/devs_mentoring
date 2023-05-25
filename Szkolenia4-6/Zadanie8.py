#BMI

waga = float(input("Ile ważysz?: "))
wzrost = float(input("Wzrost?: "))

BMI = waga / (wzrost * 2) * 100
BMI = float(BMI).__round__(1)

if BMI < 18.5:
    print("niedowaga")
elif BMI >= 18.5 and BMI < 24:
    print("waga normalna")
elif BMI >= 24 and BMI < 26.5:
    print("lekka nadwaga")
elif BMI >= 26.5 and BMI < 30:
    print("nadwaga")
elif BMI >= 30 and BMI < 35:
    print("nadwaga i otyłość I stopnia")
elif BMI >= 35 and BMI < 40:
    print("nadwaga i otyłość II stopnia")
elif BMI >= 40:
    print("nadwaga i otyłość III stopnia")
else:
    print("coś poszło nie tak")

print(f"Twoje BMI to {BMI}")

