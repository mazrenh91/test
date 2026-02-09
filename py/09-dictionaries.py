# # dictionary

# student = {
#     "name": "Alice",
#     "age": 20,
#     "grade": "A",
#     "courses": ["Math", "Science", "English"]
# }

# # accessing and modifying
# print(student["name"])        # "Alice"
# print(student.get("age"))   # 20
# student["age"] = 21      # modifying value
# student["email"] = "alice@gmail.com"    # adding new key-value

# # dictionary methods
# keys = student.keys()          # get all keys
# values = student.values()      # get all values
# items = student.items()        # get all key-value pairs

# print(keys)
# print(values)
# print(items)

# # iterating through dictionaries
# for key in student:
#     print(f"{key}: {student[key]}")

# for key, value in student.items():
#     print(f"{key}: {value}")

# # nested dictionaries
# company = {
#     "employees": {
#         "john": {"age": 30, "department": "IT"},
#         "jane": {"age": 25, "department": "HR"}
#     },
#     "departments": ["IT", "HR", "Finance"]
# }

# print(company["employees"].items())  # prints all employees with their details
# print(company["employees"]) # prints the employees dictionary (same as above)
# print(company["departments"])

# Exercise: Student Records
# create a dictionary to store student records.
student_records = [
    {
    "student_id": 1,
    "name": "John",
    "age": 19,
    "major": "Computer Science",
    "grades": [85, 92, 78]
    },
    {
    "student_id": 2,
    "name": "Sarah",
    "age": 20,
    "major": "Biology",
    "grades": [90, 88, 95]
    }
]

# add new student record
student_records.append(
    {
    "student_id": 3,
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
    }
)

# update age for "John" to 20
for student in student_records:
    if student["name"] == "John":
        student["age"] = 20
        break

# loop through the dictionary and print each student's information in format Student ID: [id], Name: [name], Major: [major]
for student in student_records:
    print(f"Student ID: {student["student_id"]}, Name: {student["name"]}, Major: {student["major"]}")

