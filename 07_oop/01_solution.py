class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        # self.total_car += 1
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(isinstance(my_tesla, ElectricCar))
# print(isinstance(my_tesla, Car))


# print(my_tesla.brand)
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "City"
# Car("Tata", "Nexon")

# print(my_car.model)


# print(Car.total_car)
# print(safari.fuel_type())

# print(my_car.general_description())
# print(Car.general_description())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.fuel_type())

# my_new_car = Car("Honda", "Civic")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())


class Battery:
    def battery_info(self):
        return "This is battery."

class Engine:
    def engine_info(self):
        return "This is engine."

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model 3")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())






















# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.brand + " !"
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"            

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla", "Model S", "100KWH")

# print(my_tesla.get_brand())
# print(my_tesla.full_name())

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Honda", "Civic")
# print(my_new_car.brand)
# print(my_new_car.model)


# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.brand + " !"

#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"

# my_car = Car("Toyota", "Corolla")
# print(my_car.full_name())


# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#         return "Electric Charge"

# my_tesla = ElectricCar("Tesla", "Model S", "100KWH")
# print(my_tesla.fuel_type())

# safari = Car("Tata", "Safari")
# safariThree = Car("Tata", "Nexon")
# print(safari.fuel_type())
# print(safari.total_car)
# test = Car("test", "test")
# print(test.total_car)
# print(Car.total_car)


# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())