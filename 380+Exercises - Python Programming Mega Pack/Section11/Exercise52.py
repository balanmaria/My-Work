#TODO: Tuples are immutable. The following tuple is given:
# members = (('Kate', 23), ('Tom', 19))
# Insert a tuple ('John', 26) between Kate and Tom as shown below. Print the result to the console.

members = (('Kate', 23), ('Tom', 19))
list = list(members)
list.insert(1,('John', 26))
new_tuple = tuple(list)

print(new_tuple)

members = (('Kate', 23), ('Tom', 19))
members = (members[0], ('John', 26), members[1])
print(members)