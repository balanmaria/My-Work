#TODO: Write a program that checks if the given number is a prime number (use the break statement):
# number = 13
# Print one of the following to the console depends on the result:
# 13 - prime number
# 13 - not a prime number

number = 13

result = f"{number} - prime number"

for i in range(2,number):
    if number % i == 0:
        result = f"{number} - not prime number"
        break

print(result)

#METODA II

number = 13

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - not a prime number')
            break
    else:
        print(f'{number} - prime number')
else:
    print(f'{number} - not a prime number')
