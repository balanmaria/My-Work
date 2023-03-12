#TODO: The following list of numbers is given:
# items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
# Write a program that removes odd numbers and returns the remaining ones. Print the result to the console.

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
new_val = []

for i in items:
    if i % 2 == 0:
        new_val.append(i)

print(new_val)

result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)