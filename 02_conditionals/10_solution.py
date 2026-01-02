pet = input("Enter your pet name: ").strip().lower()
pet_age = int(input("Enter your pet age in years: "))
pet_food = ""

if pet == "dog" and pet_age < 2:
    pet_food = "Puppy food"
elif pet == "dog" and pet_age >= 2:
    pet_food = "Senior dog food"
elif pet == "cat" and pet_age < 2:
    pet_food = "Kitten food"
elif pet == "cat" and pet_age >= 2:
    pet_food = "Senior cat food"
else:
    pet_food = "Adult pet food"

print(f"For your {pet} aged {pet_age} years, we recommend: {pet_food}.")