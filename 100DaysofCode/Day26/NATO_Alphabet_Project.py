import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO: Create a dictioary

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO: Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    answer=input("Enter a word: ").upper()

    try:
        output_list=[phonetic_dict[letter] for letter in answer]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()