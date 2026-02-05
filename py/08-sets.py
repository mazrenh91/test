# # sets - sets operations

# fruits = {"apple", "banana", "orange"}
# numbers = {1, 2, 3, 4, 5}

# # set operations
# fruits.add("grape")     # add element
# fruits.remove("banana") # remove element (with error)
# fruits.discard("kiwi")  # remove if exists (no error)

# print(fruits)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))             # {1, 2, 3, 4, 5, 6}
# print(set1.intersection(set2))      # {3, 4}
# print(set1.difference(set2))        # {1, 2}
# print(set2.difference(set1))        # {5, 6}

grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95)
]

# find unique students using set
students = set()
for i in grades:
    students.add(i[0])      # grade[0] is the student name
print("Unique students:", students)

# find unique subjects using set
subjects = set()
for i in grades:
    subjects.add(i[1])      # grade[1] is the subject name
print("Unique subjects:", subjects)

# find Alice's grade
alice_grades = []
for i in grades:
    if i[0] == "Alice":
        alice_grades.append((i[1], i[2]))   # (subject, grade)
print("Alice's grades:", alice_grades)


