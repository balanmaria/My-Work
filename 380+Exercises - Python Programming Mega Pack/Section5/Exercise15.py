#TODO:The geometric sequence is given with the following formula: a(n) = 8* pow(2, n-1)
# Calculate the sum of the first six elements of this sequence. Print the result to the console as shown below.

sum =0

for i in range(1,7):
    sum += 8*pow(2,i-1)

print(f"The sum of the first {i} elements of the sequence is: {sum:.1f}")

a1 = 8
a2 = 8 * 2
n = 6
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
print(f'The sum of the first {n} elements of the sequence is: {s6}')