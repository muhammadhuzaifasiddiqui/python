def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Asad", age=45, party="muslim_ittehad")
print_kwargs(name="Asad")
print_kwargs(name="Asad", age=45, party="muslim_ittehad", opposition="BJP")

# def print_kwargs(name, party, age):
#     print("Name: ", name, " Party: ", party, " Age: ", age)

# print_kwargs(name="Asad", age=45, party="muslim_ittehad")
# print_kwargs(name="Asad")
# print_kwargs(name="Asad", age=45, party="muslim_ittehad", opposition="BJP")