import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

# # Level 1
# import random
# if nr_numbers <= len(numbers) and nr_symbols <= len(symbols) and nr_letters <= len(letters):
#  selected_letters = letters[random.randint(0,25)]
#  for l in range(0,nr_letters-1):
#     selected_letters += letters[random.randint(0,25)]
#  # print(selected_letters)
#  selected_symbol = symbols[random.randint(0,8)]
#  for s in range(0,nr_symbols-1):
#     selected_symbol += symbols[random.randint(0,8)]
#  # print(selected_symbol)
#  selected_number = numbers[random.randint(0,9)]
#  for n in range(0,nr_numbers-1):
#     selected_number += str(numbers[random.randint(0,9)])
#  # print(selected_number)
#  password_l1 = selected_letters+selected_number+selected_symbol
#  print("The final password is :- " + password_l1 )
# else:
#     print("range is exceeded")
# print(password_list)

# level 2

for l in range(0,nr_letters):
    letter_to_be_add = letters[random.randint(0,len(letters)-1)]
    password_list.append(letter_to_be_add)
for s in range(0,nr_symbols):
    symbol_to_be_add = symbols[random.randint(0,len(symbols)-1)]
    password_list.append(symbol_to_be_add)
for n in range(0,nr_numbers):
    number_to_be_add = numbers[random.randint(0,len(numbers)-1)]
    password_list.append(number_to_be_add)
print(password_list)
final_password = ""
for p in password_list:
    final_password += p

print(final_password)




