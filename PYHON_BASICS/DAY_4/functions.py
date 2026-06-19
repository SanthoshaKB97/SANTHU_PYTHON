

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:")
print(fruits)
i#ndex
print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Slicing
print("\nFirst 2 Fruits:", fruits[:2])
print("Last 2 Fruits:", fruits[2:])

# Append
fruits.append("Grapes")
print("\nAfter Append:")
print(fruits)

# Insert
fruits.insert(1, "Pineapple")
print("\nAfter Insert:")
print(fruits)

# Remove
fruits.remove("Banana")
print("\nAfter Remove:")
print(fruits)

# Pop
removed_item = fruits.pop()
print("\nRemoved Item:", removed_item)
print(fruits)

# Length
print("\nTotal Fruits:", len(fruits))

# Check Item
if "Mango" in fruits:
    print("Mango is available")
else:
    print("Mango is not available")

# Sort
fruits.sort()
print("\nSorted List:")
print(fruits)

# Reverse
fruits.reverse()
print("\nReverse List:")
print(fruits)

# Loop
print("\nUsing For Loop:")
for fruit in fruits:
    print(fruit)

# User Input
num = int(input("\nHow many numbers do you want to add? "))

numbers = []

for i in range(num):
    value = int(input(f"Enter Number {i+1}: "))
    numbers.append(value)

print("\nYour Numbers:")
print(numbers)

print("Maximum Number:", max(numbers))
print("Minimum Number:", min(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
