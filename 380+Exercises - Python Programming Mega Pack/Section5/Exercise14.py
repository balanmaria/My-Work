#TODO:The arithmetic sequence is given with the following formula:an = 10 + 4n
# Calculate the sum of the first ten elements of this sequence. Print the result to the console as shown below.

sum = 0

for i in range(1,11):
    sum += (10 + 4*i)

print(f"The sum of the first 10 elements in a sequence: {sum:.1f}")

a1 = 14
a10 = 50
n = 10
s10 = ((a1 + a10) / 2) * n
print(f'The sum of the first 10 elements in a sequence: {s10}')