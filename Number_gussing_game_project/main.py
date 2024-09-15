# importing the random module
import random
# importing logo from art
from art import logo

# creating a function which can tell about the distance of guess from the number
def check_the_guess_deviation(guess,num):
    if guess < 1 or guess >100:
        print("Guess is out of range")
        return False
    if guess == num:
       print("Correct Guess\nYou won")
       return True
    if guess > num:
        if abs(guess-num)<10:
           print("High But You are close.\n")
           return False
        else:
            print("Too High\n")
            return False
    if guess < num:
        if abs(guess-num)<10:
           print("Low But You are close.\n")
           return False
        else:
            print("Too Low\n")
            return False
    return False

# Ensuring the correct integer input for the guess
def get_valid_input_for_guess():
   guess = None
   while True:
    try:
      guess = int(input("Make a Guess.\n"))
      return guess
    except ValueError:
      print("********YOUR ",guess,"NOT A VALID INTEGER********")

# function to perfrom the game
def Guess_the_num():
  yes_no = 'yes'
  # Creating a loop to run the game again and again until player quits it.  
  while yes_no == 'yes':
    print(logo)
    num = random.randint(1, 101)
    print(num)
    level = input('''
    Chose your lever
        1. Hard/hard --> 10 attempts
        2. Easy/easy --> 5 attempts
    ''').lower()
   # If player chooses the Hard level attempts = 5
    if level == 'hard':
        # Run a loop to ensure the all attempt untill the user win or lose
        for i in range(1, 6):
            guess = get_valid_input_for_guess()
            if check_the_guess_deviation(guess, num):
                break
            else:
                print("You have only", 5 - i, "attempts left.")
    # If player chooses the Easy level attemps = 10
    if level == 'easy':
        for i in range(1, 11):
            guess = int(input("Make a Guess.\n"))
            if check_the_guess_deviation(guess):
                break
            else:
                print("You have only", 10 - i, "attempts left.")
    # Taking response from user to play again or not
    yes_no = input("Type 'yes' to play again and Type any thing to exit\n")

Guess_the_num()
