name = "Manohar"
height_feet = 5.7
height_inches = (int(height_feet) * 12) + (height_feet - int(height_feet)) * 10
height_m = height_feet * 0.3048
height_cm = height_m * 100
weight_kg = 77
bmi = weight_kg / float(height_m ** 2)
bmi = round(bmi, 1)
print(bmi)

if bmi > 25:
    print(name + ' is over weight')
elif bmi < 18.5:
    print(name + ' is under weight')
else:
    print(name + ' is medium weight')
