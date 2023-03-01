import requests
from datetime import datetime
from configdata import graph_config, user_params, token, USERNAME, GRAPH_ID

USERNAME = USERNAME
TOKEN = token
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = GRAPH_ID

user_params = user_params

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = graph_config

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#today = datetime.now()
today = datetime(year = 2023, month=2, day=13)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}

response = requests.post(url = pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

new_pixel_data = {
    "quantity": "33"
}

# response = requests.put(url = update_endpoint,json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# response = requests.delete(url = delete_endpoint, headers=headers)
# print(response.text)