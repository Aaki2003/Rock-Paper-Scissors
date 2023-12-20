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




x = int(input("Choose 1 for rock, 2 for paper, 3 for scissor\n"))
if x>0 and x<4:
  comp = random.randint(1,3)
  comp_list = [rock,paper,scissors]
  print("You chose")
  if x==1:
    print("rock")
    print(rock)
  elif x==2:
    print("paper")
    print(paper)
  else:
    print("scissors")
    print(scissors)

  print("Computer chose")
  if comp==1:
    print("rock")
    print(rock)
  elif comp==2:
    print("paper")
    print(paper)
  else:
    print("scissors")
    print(scissors)
  
  if x==comp:
    print("Draw! Play Again\n")
  elif x==1 and comp==3:
    print("You Won\n")
  elif x==2 and comp==1:
    print("You Won\n")
  elif x==3 and comp==2:
    print("You Won\n")
  else:
    print("Computer won\n")
else:
  print("Wrong input! Play again")
