km_distance = int(input("Enter the distance to travel in kilometers: "))

transport_mode = "metro"

if km_distance < 3:
    transport_mode = "walk"
elif km_distance >= 3 | km_distance < 16:
    transport_mode = "bike"
elif km_distance > 16:
    transport_mode = "car"
else:
    transport_mode = "unknown"

print(f"For a distance of {km_distance} km, you should: {transport_mode}.")