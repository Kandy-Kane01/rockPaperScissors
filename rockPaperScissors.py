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
#print relevant image for user or computer choice
game_images = [rock, paper, scissors]
#get user input and turn it into integer
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])
#get computers random choice
computer_choice = random.randint(0, 2)
print("Computer chose:")
#ensure the user choice isn't greater than 3, put it before it checks for game images, if the user types a number greater than the number of choices, it will print this message
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else:
#print out game images
  print(game_images[computer_choice])
#check who wins 
if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
  #check which number is greater
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
