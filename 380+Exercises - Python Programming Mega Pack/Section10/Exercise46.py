#TODO: The following text is given:
# text = 'Programming in python.'
# Follow the next steps:
# -Change all letters to lowercase.
# -Delete spaces and period.
# -Create a set consisting of all letters in the text and assign to letters variable
# -Using the appropriate method for sets, remove all vowels from letters set:
# vowels = {'a', 'e', 'i', 'o', 'u'}
# -Print the number of items in the letters set as shown below.

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower().strip().replace(".","").strip()
# text = text.lower()
# text = text.replace(' ', '')
# text = text.replace('.', '')

letter = set(text)
cons = letter.difference(vowels)

print(f'Number of items: {len(cons)}')