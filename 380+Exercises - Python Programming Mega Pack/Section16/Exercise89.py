#TODO: The following list is given:
# items = [1, 5, 3, 2, 2, 4, 2, 4]
# Write a program that removes duplicates from the list (the order must be kept) and print the list to the console.

items = [1, 5, 3, 2, 2, 4, 2, 4]

dict = {}

for i in items:
    dict[i] = items.count(i)

my_list = []
for key in dict.keys():
    my_list.append(key)
print(my_list)

#PART II

for item in items:
    if not item in result:
        result.append(item)

print(result)