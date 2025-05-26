
import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissor
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

signs = [rock, paper, scissor]

game_ques = input("Rock, Paper or Scissor? ").lower()
computer_sign = random.choice(signs)

if game_ques == "rock":
    print(rock)
    print(computer_sign)
    if computer_sign == rock:
        print("It's a tie!")
    elif computer_sign == paper:
        print("You lose!")
    else:
        print("You win!")
elif game_ques == "paper":
    print(paper)
    print(computer_sign)
    if computer_sign == rock:
        print("You win!")
    elif computer_sign == paper:
        print("It's a tie!")
    else:
        print("You lose!")
elif game_ques == "scissor":
    print(scissor)
    print(computer_sign)
    if computer_sign == rock:
        print("You lose!")
    elif computer_sign == paper:
        print("You win!")
    else:
        print("It's a tie!")
else:
    print("Invalid!")
    