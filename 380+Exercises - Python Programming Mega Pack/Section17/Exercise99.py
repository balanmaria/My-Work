#TODO: The following list of hashtags is given:
# hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
# Check if all objects in the list are of str type. If so, print True, otherwise print False. Use the break statement in your solution.

hashtags = ['holiday', 'sport', 'fit', None, 'fashion']
result = True

for item in hashtags:
    if type(item) != str:
        result = False
        break
print(result)

#METODA II

result = True

for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = False
        break

print(result)