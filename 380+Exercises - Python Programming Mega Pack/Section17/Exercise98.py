#TODO: Write a program that compares two lists and returns True if the lists contain at least one of the same element. Otherwise, it will return False.
# Use break statement in the solution and print result to the console.
# Lists:
# list1 = [1, 2, 0]
# list2 = [4, 5, 6, 1]

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]

for item in list1:
    if item in list2:
        print("True")
        break
    print("False")

#METODA II

list1 = [1, 2, 0]
list2 = [4, 5, 6, 1]
result = False

for item1 in list1:
    if item1 in list2:
        result = True
        break

print(result)