# Task 1 - Student Dictionary3

student = {
    "name": "Santhu",
    "age": 17,
    "course": "CSE",
    "marks": 85
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])


# Task 2 - Update Marks

student["marks"] = 95
print("Updated Marks:", student["marks"])


# Task 3 - Add New Key

student["city"] = "Bangalore"
print("City:", student["city"])


# Task 4 - Mobile Dictionary

mobile = {
    "brand": "Samsung",
    "model": "S25",
    "price": 80000,
    "storage": "256GB"
}

print("\nMobile Information")
print("Brand:", mobile["brand"])
print("Model:", mobile["model"])
print("Price:", mobile["price"])
print("Storage:", mobile["storage"])


# Task 5 - For Loop

marks = {
    "Maths": 85,
    "Python": 90,
    "Java": 80
}

print("\nSubject Marks")

for subject, mark in marks.items():
    print(subject, ":", mark)
