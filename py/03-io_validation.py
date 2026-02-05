# name = input("Enter your name: ")
# height = float(input("Enter your height: "))    # Convert to float

# Input validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("Age must be positive!")
#     except ValueError:
#         print("Please enter a valid number!")

# # Output validation
# print(f"Hello, {name}!")
# print(f"You are {age} years old and {height} feet tall.")

while True:
    try:
        name = str(input("Enter your name: "))
        height = float(input("Enter your height in feet: "))
        if height < 0:
            print("You have input invalid data for height, please try again!")

        weight = float(input("Enter your weight in pound: "))
        if weight < 0:
            print("You have input invalid data for weight, please try again!")
        else:
            break

    except ValueError:
        print("Please enter a valid number!")
    
print("test")

# # 1. Create a simple calculator that takes two number and an operation from user.
# while True:
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         operation = input("Enter operation (+, -, *, /): ")
        
#         if operation == "+":
#             result = num1 + num2
#         elif operation == "-":
#             result = num1 - num2
#         elif operation == "*":
#             result = num1 * num2
#         elif operation == "/":
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 print("Cannot divide by zero!")
#                 continue
#         else:
#             print("Invalid operation!")
#             continue
            
#         print(f"Result: {result}")
#         break
        
#     except ValueError:
#         print("Please enter valid numbers!")


# # 2. Create a simple quiz program with 3 questions.
# score = 0

# # # Question 1
# answer1 = input("What is the capital of France? ").lower()
# if answer1 == "paris":
#     print("Correct!")
#     score += 1
#     print(score)
# else:
#     print("Wrong! The answer is Paris.")

# # # Question 2
# answer2 = input("What is 5 + 3? ")
# if answer2 == "8":
#     print("Correct!")
#     score += 1
#     print(score)
# else:
#     print("Wrong! The answer is 8.")

# # # Question 3
# answer3 = input("What color do you get when you mix red and blue? ").lower()
# if answer3 == "purple":
#     print("Correct!")
#     score += 1
# else:
#     print("Wrong! The answer is purple.")

# # Final score
# print(f"\nYour final score: {score}/3")
# if score == 3:
#     print("Perfect score!")
# elif score >= 2:
#     print("Good job!")
# else:
#     print("Better luck next time!")