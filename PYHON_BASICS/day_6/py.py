
student = {
    "name": "Santhu",
    "age": 17,
    "marks": 85
}

print(student)


print(student["name"])
print(student["age"])
print(student["marks"])

student = {
    "name": "Santhu",
    "age": 17,
    "marks": 85
}

for key in student:
    print(key)

student = {
    "name": "Santhu",
    "age": 17,
    "course": "CSE",
    "marks": 85
}

print("Student Information")
print("-------------------")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])
