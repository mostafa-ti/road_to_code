'''
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

Pizza Prices

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Extra Costs

Add pepperoni for small pizza: +$2

Add pepperoni for medium or large pizza: +$3

Add extra cheese for any size pizza: +$1

Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.
'''
# todo: work out how much they need to pay based on their size choice.

# todo: work out how much to add to their bill based on their pepperoni choice.

# todo: work out their final amount based on whether if they want extra cheese.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size.lower() == "l":
    bill = 25
elif size.lower() == "m":
    bill = 20
else:
    bill = 15
print(bill)