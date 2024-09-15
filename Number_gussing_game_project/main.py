import random
from art import logo
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

def get_valid_input_for_guess():
   guess = None
   while True:
    try:
      guess = int(input("Make a Guess.\n"))
      return guess
    except ValueError:
      print("********YOUR ",guess,"NOT A VALID INTEGER********")


def Guess_the_num():
  yes_no = 'yes'
  while yes_no == 'yes':
    print(logo)
    num = random.randint(1, 101)
    print(num)
    level = input('''
    Chose your lever
        1. Hard/hard --> 10 attempts
        2. Easy/easy --> 5 attempts
    ''').lower()
    if level == 'hard':
        for i in range(1, 6):
            guess = get_valid_input_for_guess()
            if check_the_guess_deviation(guess, num):
                break
            else:
                print("You have only", 5 - i, "attempts left.")
    if level == 'easy':
        for i in range(1, 11):
            guess = int(input("Make a Guess.\n"))
            if check_the_guess_deviation(guess):
                break
            else:
                print("You have only", 10 - i, "attempts left.")
    yes_no = input("Type 'yes' to play again and Type any thing to exit\n")

Guess_the_num()