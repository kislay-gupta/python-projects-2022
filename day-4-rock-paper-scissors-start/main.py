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

import random
user_move = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#user move

if user_move == 0:
    print(rock)
elif user_move == 1:
    print(paper)
elif user_move == 2:
    print(scissors)
else:
    print("please enter a valid option")

#ai move
print("computer chose:")
ai_random = random.randint(0, 2)

if ai_random == 0:
    print(rock)
elif ai_random == 1:
    print(paper)
else:
    print(scissors)


if user_move == 0 and ai_random == 2:
    print("you won")
elif ai_random == 0 and user_move == 2:
    print("you lose")
elif ai_random > user_move:
    print("you lose")
elif user_move > ai_random:
    print("you won")
elif user_move == ai_random:
    print("It's a draw")
elif ai_random == 0 and user_move == 2:
    print("you lose")