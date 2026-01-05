import math

# def circleStates(radius):
#     print("Hello")
#     return math.pi*radius**2

# result = circleStates(5)
# print(circleStates(5))
# print(result)

def circle_stats(radius):
    area = math.pi*radius**2
    circum = 2*math.pi*radius
    return area, circum

a, c = circle_stats(5)
print("Area:", f"{a:.2f}")
print("cCircumference:", f"{c:.2f}")
print(f"The Area: {a:.2f} and Circumference is: {c:.2f}")

# def add_with_print(a, b):
#     answer = a + b
#     return answer

# x = add_with_print(3, 5)
# print(x + 7)

# def add_with_print(a, b):
#     answer = a + b
#     print(answer)

# y = add_with_print(3, 5)
# print(y + 7)