import random

diff=['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

print("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.")
user_choice=int(input())

print(diff[user_choice])

computer_choice=random.randint(0,2)

print("Computer Choice")

print(diff[computer_choice])

if user_choice==computer_choice:
    print("Game Tie Retry")
elif user_choice == 0 and computer_choice == 2:
    print("You Won")
elif user_choice == 1 and computer_choice == 0:
    print("You Won")
elif user_choice == 2 and computer_choice == 1:
    print("You Won")
else:
    print("You Lose")
