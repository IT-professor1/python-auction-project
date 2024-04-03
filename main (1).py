def main():
  item_price = 0.0
  user_bid = 0.0
  user_choice = ''
  item_name = ""
  email = ""


print("Let's list an item.")
item_name = input("Type the name of the item for auction: ")
item_price = float(input("What is the starting price?"))
print("The starting price is", item_price)
user_choice = input("Do you want to bid? (y/n)")

if user_choice.lower() == 'y':
  user_bid = float(input("How much would you like to bid?"))
  if user_bid < item_price:
    print("Your bid is too low. You must bid at least", item_price)
  else:
    print("Your bid of", user_bid,
          "has been accepted. Enter your email to pay within 24 hours.")
    email = input("Enter your email: ")
    print("Thank you.")
else:
  print("No bid placed.")
