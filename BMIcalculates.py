weight = float( input("Type your weight in kg: "))
height = float( input("Type your height in Meters: "))

bmi = weight / (height ** 2)

print("your BMI is: ",round(bmi,2))

if (bmi <= 18.5):
    classification = "Underweight"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "Normal weight"
elif (bmi > 24.5 and bmi<= 29.9):
    classification = "overweight"
else:
    classificaion = "obesity"
    
print("The Classification of your BMI is:" , classification)
