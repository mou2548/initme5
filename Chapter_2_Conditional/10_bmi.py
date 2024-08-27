weight = int(input("Weight : "))
height = int(input("Height : "))
bmi = weight/((height/100)**2)
if bmi >= 30:
    result = "You're in the obese range."
elif bmi >= 25:
    result = "You're in the overweight range."
elif bmi >= 18.6:
    result = "You're in the healthy weight range."
else:
    result = "You're in the underweight range."
print(f"Your BMI is {bmi:.1f} {result}")