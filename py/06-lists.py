# lists

# fruits = ["apple", "banana", "orange"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["hello", 42, 3.14, True]
# empty_list = []

# # Accessing Elements
# print(fruits[0])        # "apple"
# print(fruits[-1])       # "orange"
# print(numbers[1:4])     # [2, 3, 4]
# print(numbers[:3])      # [1, 2, 3]
# print(numbers[2:])      # [3, 4, 5]

# lists operation - CRUD

# fruits.append("grape")      # add to end
# fruits.insert(1, "kiwi")    # insert at index
# fruits.remove("banana")     # remove the value
# popped = fruits.pop()       # remove and return last
# fruits.sort()               # sort in place
# fruits.reverse()            # reverse in place

# print(fruits)

# list of operations

# len(fruits)                 # length
# "apple" in fruits           # check membership
# fruits + ["mango"]          # concatenation
# fruits * 2                  # repetition

# print(len(fruits))

groceries = ["1 apple", "2 carrots", "3 kailan"]

groceries.append("4 orange juice")
groceries.insert(0, "5 onions")
groceries.remove("1 apple")
groceries.pop()
groceries.sort()
groceries.reverse()

print(groceries)
print(max(groceries))
print(min(groceries))