User_Weight = float(input("Enter your weight in kg:"))
User_Height = float(input("Enter your height in m:"))

BMI = round(User_Weight/(User_Height**2),1)

print("Your BMI is : ",BMI)

if BMI < 18.5:
    print("Underwright")
elif 18.5 <= BMI <= 24.9:
    print("Normal weight")
elif 25.0 <= BMI <= 29.9:
    print("Overweight")
elif 30.0 < BMI:
    print("Obese")

