#TODO: Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization and a 5-year investment period. Round the result to the nearest cent.
# Tip: Use compound capitalization of interest.
# Print the result to the console as shown below.

start = 1000

for _ in range(5):
    start += 0.03*start

print(f"The future value of the investment: {start:.2f} USD")