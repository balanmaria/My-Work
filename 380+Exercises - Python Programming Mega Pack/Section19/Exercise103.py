#TODO: Write a program that prints to the console the first ten prime numbers separated by a comma.
# Tip: Use a while loop with break statement.

def is_prime(number):
    is_prime = 1
    for i in range(2, number):
        if number % i ==0:
            is_prime = 0
            break
    return is_prime

number = 2
i=10
list = []
while i > 0:
    if is_prime(number) == 1:
        list.append(str(number))
        i -=1
    number +=1

print(','.join(list))

#SOLUTIA II

counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))