#TODO:Calculate the distance of two points A = (3, 2), B = (- 1, -1) and print result to the console as shown below.
import math
x1=3
y1=2
x2=-1
y2=-1
distance=math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

print(f"The distance between points A and B: {distance}")

a1 = 3
a2 = 2
b1 = -1
b2 = -1
distance = ((b1 - a1) ** 2 + (b2 - a2) ** 2)**(1/2)
print(f'The distance between points A and B: {distance}')