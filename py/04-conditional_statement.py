# conditional statement if-else / if-elif-else
# exercise 1

# age = 35

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# exercise 2

# score = 85

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Your grade is: {grade}")

# conditional statement and-or
# example 1

# user_age = 35
# has_license = True
# if user_age >= 18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")

# example 2

# day = "Saturday"

# if day =="Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")

# conditional statement nested condition
# example 1

# weather = "sunny"
# temperature = 75

# if weather == "sunny":
#     if temperature > 70:
#         print("It's sunny and warm.")
#     else:
#         print("It's sunny but cool.")

# exercise - BMI

weight = float(input("enter your weight in kg."))
height = float(input("enter your height in cm."))
bmi = weight / (height/100)**2


if bmi >= 30:
    print(f"your bmi is {bmi:.3f} - obesity")
elif bmi >= 29.9:
    print(f"your bmi is {bmi:.3f} - overweight")
elif bmi >=24.9:
    print(f"your bmi is {bmi:.3f} - normal weight")
else:
    print(f"your bmi is {bmi:.3f} - underweight")