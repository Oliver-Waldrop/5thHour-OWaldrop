#Name: Oliver Waldrop
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
height = int(input("Enter your height (in total inches: "))
weight = int(input("Enter your weight (in pounds): "))

bmi = (weight / (height ** 2)) *703
print (bmi)
if bmi >= 25:
    if bmi <= 29.9:
        print ("You are overweight")
    elif bmi >= 30:
        print ("You are obese")
if bmi >= 18.5:
    if bmi <= 24.9:
        print ("You are normal weight")
else:
        print ("You are underweight")