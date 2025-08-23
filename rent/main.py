import validate as v
from abc import ABC
from datetime import datetime


class User(ABC):
    def __init__(self, name, email):
        self.name = v.validate_username(name)
        self.emai = v.validate_email(email)


class Customer(User):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = v.validate_phone(phone)


class Admin(User):
    def __init__(self, name, email, id):
        super().__init__(name, email)
        self.id = id


class Car:
    def __init__(self, maker, model, plate_number, color, available=True):
        self.maker = maker
        self.model = model
        self.plate = plate_number
        self.color = color


class RentCar:
    def __init__(self, customer, car, Barrow, return_date):
        self.customer = customer
        self.car = car
        self.barrow = Barrow
        self.return_date = return_date


class System:
    def __init__(self):
        self.rents = []

    def add_rent(self, rent: RentCar):
        self.rents.append(rent)

    def remove_rent(self, rent: RentCar):
        self.rents.remove(rent)
