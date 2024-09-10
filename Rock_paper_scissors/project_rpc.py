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

User_response = int(input("Enter 0 for rock 1 for paper and 2 for the scissors"))
import random
Computer_response = random.randint(0,2)

# Case for draw
if User_response == Computer_response :
    if User_response == 0:
        print(rock)
    elif User_response == 1:
        print(paper)
    else:
        print(scissors)
    print("Draw")

# Case in which player wins
if User_response == 0 and Computer_response == 1 or Computer_response== 2 :
    print("Your response:-")
    print(rock)
    if Computer_response == 1:
        print("Computer's response")
        print(paper)
    else:
        print("Computer's response")
        print(scissors)
    print("YOU WON!!!")

# Case in which computer wins
elif User_response == 1 or User_response == 2 and Computer_response == 0:
    if User_response == 1:
        print("Your response")
        print(paper)
    else:
        print("Your response")
        print(scissors)
    print("Computer's response")
    print(rock)
    print("You Loosed!!!")

# Case in which computer wins
elif User_response == 1 and Computer_response == 2 :
    print("Your response")
    print(paper)
    print("Computer's response")
    print(scissors)
    print("You Loosed!!!")

# Case in which player wins
elif User_response == 2 and Computer_response == 1:
    print("Your response")
    print(scissors)
    print("Computer's response")
    print(paper)
    print("YOU WON!!!")
else:
    print("Enter a Valid response")

