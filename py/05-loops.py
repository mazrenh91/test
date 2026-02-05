# loops - for loops

# for i in range(5):              # 0, 1, 2, 3, 4
#     print(i)

# for i in range(1, 6):            # 1, 2, 3, 4, 5
#     print(i)

# for i in range(0, 10, 2):       # 0, 2, 4, 6, 8
#     print(i)

#loops - while loops

# count = 0
# while count < 5:
#     print(count)
#     count += 1

# loops - loop control statement

# for i in range(10):
#     if i == 3:
#         continue        # skip this iteration
#     if i == 7:
#         break           # exit the loop
    # print(i)

# loops - loop control statement

# for i in range(2):
#     for j in range(3):
#         print(f"{i}, {j}")

# multiplication table generator

# number = int(input("enter number to multiply: "))
# for i in range(1, 13):
#     print(f"{i} * {number} = {i * number}")



# prime number program

# for i in range(3, 100):
#     if i == 20:
#         break
#     elif i % 2 == 0:
#         continue
#     elif i % 3 == 0:
#         continue
#     print(i)

# another example for prime

limit = 20

for num in range(3, limit+1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
