#TODO: The following dictionary is given:
# project_ids = {
#     '01': 'open',
#     '03': 'in progress',
#     '05': 'in progress',
#     '04': 'completed'
# }
# Extract a list of unique values (sorted alphabetically) from the project_ids dictionary and print it to the console.

project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

print(sorted(set(project_ids.values())))

result = list(set(project_ids.values()))
result.sort()
print(result)