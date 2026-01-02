number = int(input("Enter a number to check if it is prime: "))
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")