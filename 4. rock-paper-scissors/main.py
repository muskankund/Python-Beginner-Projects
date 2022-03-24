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

computer_choice = random.randint(0,2)
yours_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

list1 = [rock,paper,scissors]
print(f"{list1[yours_choice]}\n")
print(f"Computer chose:\n{list1[computer_choice]}\n")

if(yours_choice>=3 or yours_choice<0):
  print("Invalid Choice!")
elif(yours_choice==0 and computer_choice==2)or(yours_choice>computer_choice):
  print("You Win!")
elif(yours_choice==2 and computer_choice==0)or(yours_choice<computer_choice):
  print("You Lose!")
elif(yours_choice==computer_choice):
  print("Draw!")