from art import logo
print(logo)
# Description
print('''
Valid Operations are
+
-
*
/
%
||--> it will subtract and make the result positive
1. Only valid decimal Numbers are allowed
2. Any invalid input will make repeat the step again and again
3. After the completion of any task you can choose
   1 'y' to continue with the result 
   2 'n' to a fresh start
   3 any other key input to exit
   4 Division by zero is not allowed
 ''')

# creating function to perform various operations
def add(n1, n2):
    return n1 + n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def subtract(n1,n2):
    return n1-n2
def remainder(n1,n2):
    return n1%n2
def mod(n1,n2):
    return abs(n1-n2)

# Storing the functions with the key symbols each symbol will trigger a operations
Operation = {'+':add,
              '-':subtract,
              '*':multiply,
              '/':divide,
              '%':divide,
              '||':mod
              }

# Creating a function which check the ValueError and runs until the user enter  a valid number
def get_valid_number(prompt):
    """Helper function to repeatedly ask for a valid Decimal input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number format. Please enter a valid decimal number.\n")

# Checks the entered key/operation is valid or not and takes the input until they enter the valid operation
def get_valid_key():
    key = input('''Pick an Operation from
    +
    -
    /
    *
    %
    ||\n
    ''')
    while True:
        if key in Operation:
            return key
        if key not in Operation:
            key = input("Please Enter a Valid operation + - / * || %  to continue\n")

# Calculator function which manages all the input output and operations
def calculator():
  flag = True
  n1 = None
  operation = None
  while flag:
      # Handling the errors
      try:
       if n1 is None:  # Only ask for the first number when n1 is None
          n1 = get_valid_number("Enter the first number:\n ")

       # taking a valid input for operation
       operation = get_valid_key()

       # taking valid input for n2
       n2 = get_valid_number("Enter the second number\n")

       # performing the operation and giving the result
       current_val = Operation[operation](n1,n2)
       print(f"{n1} {operation} {n2} = {current_val} ")

       # taking response for further process
       response = input('''
       1. Type 'y' to continue calculation using result
       2. Type 'n' for a fresh start
       3. Type any other key to exit\n''')
       # user can continue with n1 = result by the response 'y'
       if response == 'y':
           flag = True
           n1 = current_val
       # user can start with fresh values
       elif response == 'n':
           n1 = None
       else:
           flag = False

      # Handling the ZeroDivisionError
      except ZeroDivisionError:
           print("Error: Division by zero is not allowed.\n")

calculator()






