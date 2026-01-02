age = 19
day = "Wednesday"

price = 12 if age >= 18 else 8
if day == "Wednesday":
    price -= 2
print(f"Ticket price: ${price}")