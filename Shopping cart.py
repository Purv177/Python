item = input(" what item would you like to buy?: ")
price = float(input(" What is the price of the item?: "))
quantity = int(input(" How much would you like to buy?: "))

total = price* quantity

print(f" You have bought {quantity} x {item}'s" )
print(f" Your total bill is ₹{total}")
