#TODO: The following list is given:
# project_ids = ['02134', '24253']
# Check if the following project id:
# project_id = '02135'
# is in the project_ids list. If not, add this project_id to the list and print this list to the console.

project_ids = ['02134', '24253']
project_id = '02135'

if project_id not in project_ids:
    project_ids.append(project_id)

print(project_ids)