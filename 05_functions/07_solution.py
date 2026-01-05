def summ_all(*args):
    print(args)
    for item in args:
        print(item*2)
    return sum(args *2)

print(summ_all(1, 2))
# print(summ_all(1,2, 3, 4, 5 ))
# print(summ_all(1, 2, 3, 4, 5, 6, 7, 8))