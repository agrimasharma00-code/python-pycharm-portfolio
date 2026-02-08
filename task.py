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
game_images =[rock,paper,scissors]
user_choice = int(input("What do you choose ? Type 0 for Rock , 1 for paper , 2 for scissors.. "))


if user_choice>=0 or user_choice<=2:
    print(f"User Chose : {game_images[user_choice]}")

computer_choice=random.randint(0,2)
print("Computer choice : ")
print(game_images[computer_choice])


if user_choice >=3 or user_choice<0:
    print("You input a invalid number..YOU LOSE!!")

elif user_choice ==0 and computer_choice==2:
    print("User Wins!!")

if user_choice ==2 and computer_choice==0:
    print("computer Wins!!")

elif computer_choice > user_choice:
    print("Computer Wins!!")

elif computer_choice < user_choice:
    print("User Wins!!")
elif computer_choice == user_choice:
    print("Its a Draw..")

else:
    print("You input a invalid number..")