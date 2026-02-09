# # functions with parameters
# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Alice")

# # functions with return values
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result)   # 8

# # default parameters
# def greet_with_title(name, title="Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_title("Smith"))            # Hello, Mr. Smith! - if blank, will take Mr.
# print(greet_with_title("Johnson", "Dr."))     # Hello, Dr. Johnson!

# # # ----------------------------------------------------------------- # # #

# # *args - variable number of arguments
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3,4, 5))  # 15

# # *kwargs - keyword arguments
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name = "Alice", age = 30, city = "New York")

# # combining *args and **kwargs
# def flexible_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# flexible_function(1, 2, 3, name = "Alice", age = 25)

# # # ----------------------------------------------------------------- # # #

# # lambda functions (anonymous functions)
# square = lambda x: x**2
# print(square(5))  # 25

# add = lambda x, y: x + y
# print(add(3, 4))  # 7

# # # ----------------------------------------------------------------- # # #

# # exercise
# # write a function that checks if a number is prime
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):   # optimize by checking up to square root of num
#         if num % i == 0:
#             return False
#     return True
# print(is_prime(3))  # True

# # # ----------------------------------------------------------------- # # #

# build a temperature converter function. (celciuns to fahrenheit)
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celsius_to_fahrenheit(25))  # 77.0