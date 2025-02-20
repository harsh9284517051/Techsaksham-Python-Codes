w, h = float(input("Enter weight: ")), float(input("Enter height: "))

if w == 0 or h == 0:
    print("Error: Weight and height must be greater than 0.")
else:
    bmi = round(w / h**2, 2)
    status = ("Underweight" if bmi <= 18.5 else "Normal Weight" if bmi < 25 else "Slightly Overweight" if bmi < 30 else "Obese" if bmi < 35 else "Clinically Obese")
    print(f"BMI: {bmi}, Status: {status}")