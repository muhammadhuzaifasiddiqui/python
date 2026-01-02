while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1<=number<=10:
        print("Thank you!")
        break
    elif number<1:
        print("Too low")
    else:
        print("Too high")