from main import *
a1 = Admin("ramin", "ramin@gmail.com", 1)
c1 = Customer("ali", "ali@gmail.com", "0912345678")
c2 = Customer("mohsen", "mohsen@gmail.com", "09123345678")

car1 = Car("BMW", "X6", "11a22", "black", 100)
car2 = Car("BENZ", "c200", "22b33", "white", 120)

system = System()
system.add_car(a1, car1)
system.add_car(a1, car2)

print(system.show_available_cars())

rent1 = RentCar(c1, car1, datetime(2025, 8, 23), datetime(2025, 8, 26))
system.add_rent(rent1)
print(rent1.calculate_cost())
print(system.show_available_cars())

system.update_rent_dates(c1, rent1, datetime(2025, 8, 24), datetime(2025, 8, 28))
print(rent1.calculate_cost())

system.cancel_rent(c1, rent1)
print(system.show_available_cars())