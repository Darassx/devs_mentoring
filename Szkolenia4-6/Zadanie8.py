#BMI

waga = float(input("Ile ważysz?: "))
wzrost = float(input("Wzrost?: "))

BMI = waga / (wzrost * 2) * 100
BMI = float(BMI).__round__(1)

if BMI < 18.5:
    print("niedowaga")
elif 18.5 <= BMI < 24:
    print("waga normalna")
elif 24 <= BMI < 26.5:
    print("lekka nadwaga")
elif 26.5 <= BMI < 30:
    print("nadwaga")
elif 30 <= BMI < 35:
    print("nadwaga i otyłość I stopnia")
elif 35 <= BMI < 40:
    print("nadwaga i otyłość II stopnia")
elif BMI >= 40:
    print("nadwaga i otyłość III stopnia")
else:
    print("coś poszło nie tak")

print(f"Twoje BMI to {BMI}")

