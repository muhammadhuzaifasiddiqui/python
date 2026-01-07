def debug(func):
    def wrapper(*args, **kwargs):
        # 1. Convert args tuple to a clean string
        args_value = ', '.join(str(arg) for arg in args)
        
        # 2. Convert kwargs dict to a clean string
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        
        print(f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def process_items(items, options):
    print("Processing items...")

# --- THE COMPLEX CALL ---
# args is a List: ["a", "b"]
# kwargs is a Dictionary: {'verbose': True}
process_items(["apple", "banana"], options={"verbose": True})



# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
#         print(f"calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
#         return func(*args, **kwargs)
#     return wrapper

# @debug
# def hello():
#     print("hello")

# @debug
# def greet(name, type, greeting="Hello", greetingtwo="BHai"):
#     print(f"{greeting}, {type}, {name}, {greetingtwo}")

# hello()
# greet("chai", "Coffee", greeting="hanji, ", greetingtwo="Bhai Jaan")



# def debug(func):
#     def wrapper(*args, **kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
#         print(f"calling: {func.__name__} with args {args_value} and Kwargs {kwargs_value}")
#         return func(*args, **kwargs)
        
#     return wrapper

# @debug
# def hello():
#     print("Hello!")

# @debug
# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")

# hello()
# greet("Chai", greeting="hanji")