import validate as v
from abc import ABC
from datetime import datetime


def admin_only(func):
    def wrapper(self, user, *args, **kwargs):
        if not isinstance(user, Admin):
            raise v.ValidationError("Only admin can perform this action")
        return func(self, user, *args, **kwargs)
    return wrapper


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
        return f"{self.maker} {self.model} ({self.plate_number}) - {self.color} - ${self.price}/day - {'Available' if self.available else 'Rented'}"


class RentCar:
    def __init__(self, customer, car, borrow_date, return_date):
        self.customer = customer
        self.car = car
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        days = (self.return_date - self.borrow_date).days
        days = days if days > 0 else 1
        return days * self.car.price


class System:
    def __init__(self):
        self.cars = []
        self.rents = []

    @admin_only
    def add_car(self, user: Admin, car: Car):
        self.cars.append(car)

    def show_cars(self):
        return [str(car) for car in self.cars]

    def rent_car(self, customer: Customer, car: Car, borrow_date, return_date):
        if not isinstance(customer, Customer):
            raise v.ValidationError("Only customers can rent a car")

        if car.available:
            rent = RentCar(customer, car, borrow_date, return_date)
            self.rents.append(rent)
            car.available = False
            return rent
        return None

    def cancel_rent(self, customer: Customer, rent: RentCar):
        if rent.customer != customer:
            raise v.ValidationError("You can only cancel your own rent")
        if rent in self.rents:
            rent.car.available = True
            self.rents.remove(rent)

    def update_rent_dates(self, customer: Customer, rent: RentCar, new_borrow_date, new_return_date):
        if rent.customer != customer:
            raise v.ValidationError("You can only update your own rent")
        rent.borrow_date = new_borrow_date
        rent.return_date = new_return_date
        rent.cost = rent.calculate_cost()
        return rent