#TODO: Using the while loop, calculate how many years you have to wait for the return on the investment described below to at least double your money (we only take into account full periods).
# Description:
# n - number of periods (in years)
# pv - present value
# r - interest rate (annual)
# fv - future value
# Investment parameters:
# pv = 1000
# r = 0.04
# Print result to the console as shown below.

pv = 1000
r = 0.04

fv = pv
n=0
while fv < 2*pv:
   fv += r * fv
   n+=1

print(f"Future value: {fv:.2f} USD. Number of periods: {n} years")

#METODA II

n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)

while fv <= 2000:
    fv = fv * (1 + r)
    n += 1
print(f'Future value: {fv:.2f} USD. Number of periods: {n} years')