#TODO:Find the roots of the quadratic equation: pow(x,2) + 5*x+4=0
# Print the result to the console as shown below.
import math

a=1
b=5
c=4

root1 = (-b + math.sqrt(pow(b,2) - 4*a*c))/2*a
root2 = (-b - math.sqrt(pow(b,2) - 4*a*c))/2*a

print(f"x1 = {root1}")
print(f"x2 = {root2}")

a = 1
b = 5
c = 4
delta = b ** 2 - 4 * a * c
delta_sqrt = delta ** (1/2)
x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)
print(f'x1 = {x1}')
print(f'x2 = {x2}')