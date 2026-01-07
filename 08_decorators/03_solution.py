import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(1.5)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 3))
print(long_running_function(4, 3))




# import time

# def cache(func):
#     cache_value = {}
#     def wrapper(*args):
#         # --- THE CRASH HAPPENS ON THIS LINE ---
#         if args in cache_value:
#             return cache_value[args]
        
#         result = func(*args)
#         cache_value[args] = result
#         return result
#     return wrapper

# @cache
# def sum_list(*numbers):
#     time.sleep(2)
#     return sum(numbers)

# # Passing a LIST as an argument
# print(sum_list(1, 2, 3))





# import time

# def cache(func):
#     cache_value = {}
#     # print(cache_value)
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         else:
#             result = func(*args)
#             cache_value[args] = result
#             return result
#     return wrapper

# @cache
# def long_running_function(a, b):
#     time.sleep(2)
#     return a + b

# print(long_running_function(2, 3))
# print(long_running_function(4, 3))