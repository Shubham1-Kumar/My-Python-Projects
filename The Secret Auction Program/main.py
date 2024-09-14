from art import logo
print(logo)
# creating an empty dictionary to store the biding details
Auction_detail ={}
# Creating a function to find the Maximum bid and bidder
def Winner_of_the_Auction():
    max_bid = 0
    mext_bid = 0
    winner = ""
    for i in Auction_detail:
        next_bid = int(Auction_detail[i])
        if next_bid > max_bid:
            max_bid = next_bid
            winner =i
    print(f"The winner is {winner} with a bid ${max_bid}")

Response_for_a_bid = 'yes'
while Response_for_a_bid.lower() == 'yes':
    # Taking input for the name
    name = input("What is your name :- ?")

   # Ensuring the name and bid is correct/valid
    try:
        int(name)
        print("The NAME CAN'T BE AN INTEGER\nPLEASE ENTER A VALID NAME(OTHER THAN ANY KIND OF NUMBER\n)")
    except ValueError:
        # Solving the ValueError for bid # bid should be an integer
        try:
            bid= int(input("what's your bid :- "))
            # Adding details to the dictionary
            Auction_detail[name] = bid
        except ValueError:
            print("Please enter a valid response for BID.\n This BID can not be accepted")

    # Taking further response for any left bid
    Response_for_a_bid = input("Are there any other bidders? Type 'yes' or 'no'\n")

Winner_of_the_Auction()