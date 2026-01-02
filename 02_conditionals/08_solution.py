password = "Secure3P@ss"
password_length = len(password)

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "strong"

print(f"The password strength is: {strength}.") 