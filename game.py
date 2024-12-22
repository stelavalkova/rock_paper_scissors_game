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
print("Wellcome in ROCK,PAPER,SCISSORS game!")
my_decision = input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for scissors : \n")


# if int(my_decision) >= 3 or int(my_decision) < 0:
#     print("You type in invalid number.Try again")
if my_decision == "0":
     print("You choose a Rock!")
     print(rock)
elif my_decision == "1":
         print("You choose a Paper!")
         print(paper)
elif my_decision == "2":
         print("You choose a Scissors!")
         print(scissors)
else:
    print("You type in invalid number.Try again!")

optional_list = ["0","1","2"]
computer_choice = random.choice(optional_list)
# print(f"computer choice {computer_choice} ")


if computer_choice== "0":
   print(f"My choice is Rock! {rock}")
elif computer_choice  == "1":
   print(f"My choice is Paper! {paper}")
elif computer_choice == "2":
    print(f"My choice is Scissors! {scissors}")




if computer_choice == "0" and my_decision == "0":
    print("Draw")

elif computer_choice == "0" and my_decision == "1":
    print("You are Winner!")
elif computer_choice == "0" and my_decision == "2":
    print("You Loose!")
elif computer_choice == "1" and my_decision == "0":
    print("You Loose!")
elif computer_choice == "1" and my_decision == "1":
    print("Draw")
elif computer_choice == "1" and my_decision == "2":
    print("You are Winner!")
elif computer_choice == "2" and my_decision == "0":
    print("You are Winner!")
elif computer_choice == "2" and my_decision == "1":
    print("You Loose!")
elif computer_choice == "2" and my_decision == "2":
    print("Draw")

