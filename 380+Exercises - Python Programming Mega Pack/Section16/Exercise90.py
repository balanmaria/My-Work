#TODO: The following text is given:
# text = 'Python is a very popular programming language'
# Write a program which extracts exactly the first four words as a list. Standardize each word, i.e. replace uppercase letters with lowercase. Present the result in a list and print to the console as shown below.

text = 'Python is a very popular programming language'

print(text.lower().split()[:4])

#METODA II

words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)