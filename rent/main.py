import validate as v
from abc import ABC
from datetime import datetime


class User(ABC):
    def __init__(self, name, email, role):
        self.name = v.validate_username(name)
        self.email = v.validate_email(email)
        self.role = role


class Customer(User):
    def __init__(self, name, email, phone, role="customer"):
        super().__init__(name, email, role)
        self.phone = v.validate_phone(phone)


class Admin(User):
    def __init__(self, name, email, admin_id, role="admin"):
        super().__init__(name, email, role)
        self.admin_id = admin_id


class Car:
    def __init__(self, maker, model, plate_number, color, price, available=True):
        self.maker = maker
        self.model = model
        self.plate_number = plate_number
        self.color = color
        self.price = price
        self.available = available

    def __str__(self):
        return f"{self.maker} {self.model} ({self.plate_number}) - {self.color} - ${self.price} - {'Available' if self.available else 'Rented'}"


class RentCar:
    def __init__(self, customer, car, borrow_date, return_date):
        self.customer = customer
        self.car = car
        self.borrow_date = borrow_date
        self.return_date = return_date


class System:
    def __init__(self):
        self.cars = []
        self.rents = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)

    def show_available_cars(self):
        return [car for car in self.cars if car.available]

    def rent_car(self, customer: Customer, car: Car, borrow_date, return_date):
        if car.available:
            rent = RentCar(customer, car, borrow_date, return_date)
            self.rents.append(rent)
            car.available = False
            return rent
        return None

    def return_car(self, rent: RentCar):
        if rent in self.rents:
            rent.car.available = True
            self.rents.remove(rent)