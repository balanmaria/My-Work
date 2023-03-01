import hangman_words, hangman_art
import random

print(hangman_art.logo)
my_word=random.choice(hangman_words.word_list)
print(f"Psst, the solution is {my_word}")

my_list = ["_" for _ in range(len(my_word))]
print(f"{' '.join(my_list)}")

end_of_game=False

lives = 6

guessed_letters=[]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
    else:
        guessed_letters.append(guess)

        for i in range(0, len(my_word)):
            if guess == my_word[i]:
                my_list[i] = guess

        if guess not in my_word:
            lives-=1
            print(f"You guessed {guess}, that's not in the worf. You lose a life.")
            if lives == 0:
                end_of_game=True
                print("You lose")

    print(f"{' '.join(my_list)}")

    if "_" not in my_list:
        end_of_game=True
        print("You win!")
        break

    print(hangman_art.stages[lives])