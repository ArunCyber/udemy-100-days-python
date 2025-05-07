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

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

signs = [rock, paper, scissors]

game_ques = input("Stone, Paper or Scissors?").lower()


if game_ques == "stone"
    computer_sign = random.choice(signs)
    if computer_sign == "stone"