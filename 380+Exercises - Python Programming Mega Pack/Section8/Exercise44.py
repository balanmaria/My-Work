#TODO: From the given url:
# url = (
#   "https://e-smartdata.teachable.com/p/"
#   "sciezka-data-scientist-machine-learning-engineer"
#   )
#   extract the slug after the last character '/'. Then replace all dashes with spaces and print the result to the console as shown below.

url = (
    "https://e-smartdata.teachable.com/p/"
    "sciezka-data-scientist-machine-learning-engineer"
)

print(url.split("/")[-1].replace("-"," "))

name = url.split('/')[-1]
name = name.replace('-', ' ')
print(name)