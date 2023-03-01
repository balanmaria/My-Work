#TODO: The following text is given:
# text = 'Python programming'
# Standardize the text (replace uppercase letters with lowercase). Then create a list of unique characters in the text. Remove the space from this list and sort from a to z. After all print the list to the console.

text = 'Python programming'
text = text.lower()
unique_characters = []
for i in text:
    if i not in unique_characters and i !=" ":
        unique_characters.append(i)

print(f"{[i for i in sorted(unique_characters)]}")


text = 'Python programming'
text = text.lower()
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters)