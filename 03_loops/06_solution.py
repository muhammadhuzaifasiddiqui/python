number = int(input("Enter a number to find its factorial: "))
original_number = number  # Store the original number for final output
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial value of", original_number, "is = ", factorial)