# Hier wird der BMI berechnet
# kg / cm²
print("Gib Deine Eckdaten ein und erfahre Deinen BMI...\n")

height = int(input("Wie groß bist Du in cm? "))
weight = int(input("Wie viel wiegst du in kg? "))

bmi = float(10000*(weight / (height*height)))

print("")
print ("Dein BMI beträgt", round(bmi, 2))
print("")
print("unter 18,5 → Untergewicht,")
print("18,5–24,9 → Normalgewicht,")
print("25–29,9 → Übergewicht,")
print("ab 30 → Adipositas")
print("")

if bmi<=float(18.5):
    print("Du bist untergewichtig!")
elif float(18.5)<bmi<=float(24.99):
    print("Du bist normalgewichtig!")
elif float(25)<bmi<=float(29.99):
    print("Du bist übergewichtig!")
else:
    print("Du bist adipös, Specki!")

print("")