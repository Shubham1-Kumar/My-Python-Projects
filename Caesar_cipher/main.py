# importing logo from art module
from art import logo
# printing the logo
print(logo)

# create list of alphabet, numbers and symbols
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',' ']

# function to encode and decode according to response
def caesar(original_text, shift_amount, encode_or_decode):

    # initialize and empty string to stor the output
    output_text = ""

    # creating a loop to go through each character of the input text
    for letter in original_text:
        # make shift negative or in opposite direction multiplying by -1
        if encode_or_decode == "decode":
            shift_amount *= -1

         # check the list of the letter
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
            continue
        elif letter in numbers:
            shifted_position = numbers.index(letter) + shift_amount
            shifted_position %= len(numbers)
            output_text += numbers[shifted_position]
            continue
        elif letter in symbols:
            shifted_position = symbols.index(letter) + shift_amount
            shifted_position %= len(symbols)
            output_text += symbols[shifted_position]
            continue
        # if the letter is not in any list add it as it is
        else:
            output_text += letter
    # print the output
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Create a var to store response for continuation also initialize it with 'yes' to run the code at least once
yes_or_no = 'yes'

# run the loop for yes
while yes_or_no == 'yes':

  # to fetch error and resolve it
  try:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = str(input("Type your message:\n").lower())
    shift = int(input("Enter Shift:\n"))
    if direction == 'encode' or direction == 'decode':
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    else:
        print("Please check and correct your response for 'encode' or 'decode' :")
    yes_or_no = input("Enter Yes to continue and No to stop \t").lower()
    if yes_or_no !='yes' and yes_or_no != 'no':
        print("Enter a valid response:\n")
  #  Escape the execution and prints the message int it ValueError and continues the program
  except ValueError:
      print("Enter a integer for the Shift\n")

