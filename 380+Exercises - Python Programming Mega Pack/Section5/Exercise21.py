#TODO: An infinite geometric sequence is given with the following formula:
# Calculate the sum of this sequence. Print the result to the console as shown below.

a1 = 1
a2 = 1/2
q = a2/a1
S = a1 / (1-q)
print(f'The sum of the sequence: {S}')