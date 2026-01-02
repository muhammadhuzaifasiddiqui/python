items = ["apple", "banana", "orange", "apple", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print(f"Duplicate found: {item}")
    unique_items.add(item)    
else:
        print(unique_items)