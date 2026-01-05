# username = "chaiaurcode"
# def func0():
#     username = "chai"
#     print(username)

# print(username)
# func0()

x = 99
# def func(y):
#     z = x + y
#     return z
# result = func(1)
# print(result)


# def func2():
#     global x
#     x=67

# func2()
# print(x)


# def func3():
#     x = 88
#     def func4():
#         print(x)
#     return func4
# myResult = func3()
# myResult()


def biryanicoder(num):
    def actual(x):
        return x**num
    return actual
square = biryanicoder(2)
cube = biryanicoder(3)
print(square(5))
print(cube(4))