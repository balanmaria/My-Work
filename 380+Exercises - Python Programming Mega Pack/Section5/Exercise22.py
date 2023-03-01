#TODO: Calculate the standard deviation of the following set of data: 10, 11, 9.
# Print the result to the console as shown below.

import statistics

numbers = [10, 11, 9]
print(f"The standard deviation: {statistics.pstdev(numbers):.2f}")

x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3.0
var = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3.0
std = var**(1/2)
print(f'The standard deviation: {std:.2f}')