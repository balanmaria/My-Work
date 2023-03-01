alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art

def caesar(star_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in star_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_postion=position + shift_amount
            end_text += alphabet[new_postion]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    caesar(text, shift, direction)
    answer=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if answer == "no":
        should_continue=False
        print("Goodbye!")