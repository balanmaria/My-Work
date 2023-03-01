#TODO:Calculate the geometric mean of the following numbers: 4, 3, 4.5, 5 and print result to the console as shown below.
import math

numbers = [4, 3, 4.5, 5]

prod = 1
for i in numbers:
    prod *= i

print(f"Geometric average of the given numbers: {pow(prod,1/len(numbers)):.2f}")

x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = (x1 * x2 * x3 * x4)**(1/4)
print(f'Geometric average of the given numbers: {geo:.2f}')