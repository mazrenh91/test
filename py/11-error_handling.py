# # basic exception handling
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result: {result}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# # # ----------------------------------------------------------------- # # #

# # using else and finally
# try:
#     file = open("data.txt", "r")
# except FileNotFoundError:
#     print("File not found!")
# else:
#     # executes if no exception occured
#     content = file.read()
#     print("File read successfully")
# finally:
#     # always executes
#     if "file" in locals() and not file.closed:
#         file.close()
#         print("Cleanup completed")

# # # ----------------------------------------------------------------- # # #

# raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(10)
except ValueError as ve:
    print(f"Validation Error: {ve}")