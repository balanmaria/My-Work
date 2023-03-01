#TODO: From the following text:
# string = 'PKV-89415-PLN'
# extract the code containing the first three and last three characters. Print the result to the console.

string = 'PKV-89415-PLN'
print(f"{string[0:3]}{string[-3:]}")

string = 'PKV-89415-PLN'
code = string[:3] + string[-3:]
print(code)