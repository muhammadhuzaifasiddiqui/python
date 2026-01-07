import time

def timer(func):
    def wrapper(*args, **kwargs):
        # PRINTING THE CAPTURED DATA
        print(f"Inside wrapper - args: {args}, kwargs: {kwargs}")
        
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        print(f"{func.__name__} ran in {end-start} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

# CALLING WITH A KEYWORD ARGUMENT
example_function(n=3)





# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)








# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start =time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start} time.")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)