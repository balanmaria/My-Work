#TODO: Write a program that finds all two-digit numbers divisible by 11 (use a for loop). Print the result to the console as comma-separated values as shown below.

my_list = ""
for i in range(10, 100):
    if i % 11 == 0:
        my_list += str(i)
        my_list += ","

print(my_list[:-1])


result = []
for i in range(10, 100):
    if i % 11 == 0:
        result.append(str(i))

print(result)
print(','.join(result))