n = int(input("Enter a number to get it's factorial value: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial(n)

# print(factorial(n))