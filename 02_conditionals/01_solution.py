age = int(input("Enter your age: "))

if age < 14:
    print("child")
elif age<20:
    print("teenager")
elif age<60:
    print("adult")
else:
    print("senior")