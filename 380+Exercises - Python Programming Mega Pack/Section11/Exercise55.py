#TODO: The following tuple is given (name, age):
# info = (('Monica', 19), ('Tom', 21), ('John', 18))
# Sort this tuple:
# -ascending by age
# -descending by age
# And print the result to the console as shown below.

info = (('Monica', 19), ('Tom', 21), ('John', 18))

print(f"Ascending: {tuple(sorted(info))}\nDescending: {tuple(sorted(info,reverse=True))}")

info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Ascending: {asc}')
print(f'Descending: {desc}')