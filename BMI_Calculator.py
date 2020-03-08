#BMI calculator
#JonStephen

hight=float(input("Enter your Hight im meters:"))
weight=float(input("Enter your Weight in kg:"))


bmi = weight/(hight**2)
print("Your BMI is: {0} and you are:".format(bmi), end='')

if(bmi<16):
    print("you are underweight")

elif(bmi>=16 and bmi<18.5):
    print("Healthy")

elif(bmi>=25 and bmi<30 ):
    print("You are overweight")

