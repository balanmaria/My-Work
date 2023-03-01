import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice in [0, 1, 2]:
    print(game_images[user_choice])
    random_number=random.randint(0,2)
    print("Computer chose: \n")
    print(game_images[random_number])
    if user_choice == random_number:
        print("Draw")
    elif user_choice == 0:
        if random_number == 2:
            print("You won!")
        else:
            print("You lost!")
    elif user_choice ==1:
        if random_number == 0:
            print("You won!")
        else:
            print("You lost!")
    else:
        if random_number == 1:
            print("You won")
        else:
            print("You lost!")
else:
    print("Game Over!")