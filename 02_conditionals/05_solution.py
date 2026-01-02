weather = input("Enter the weather condition (sunny, rainy, cloudy, snowy, foggy)").strip().lower()
activity = "Check the weather forecast."

if weather == "sunny":
    activity = "Go for a walk in the park."
elif weather == "rainy":
    activity = "Stay indoors and read a book."
elif weather == "snowy":
    activity = "Build a snowman."
elif weather == "cloudy":
    activity = "Visit a museum."
elif weather == "foggy":
    activity = "Drive carefully and enjoy the misty view."
else:
    activity = "Check the weather forecast again."

    print(activity)