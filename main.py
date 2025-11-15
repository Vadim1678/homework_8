class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Car:
    def __init__(self, car_id ,model, year, price):
        self.car_id = car_id
        self.model = model
        self.year = year
        self.price = price

class Rental:
    def __init__(self, rental_id, user, car, rental_price):
        self.user = user
        self.car = car
        self.rental_id = rental_id
        self.rental_price = rental_price

    def generate_confirmation(self):
        print(f"Створення підтвердження оренди №{self.rental_id}.")
        print(f"Користувач: {self.user.first_name} {self.user.last_name}")
        print(f"Автомобіль: {self.car.model} {self.car.year}")
        print(f"Ціна оренди: {self.rental_price} грн")

    def end_rental(self):
        print(f"Завершення оренди №{self.rental_id}.")

class CarRentalSystem:
    def __init__(self, cars):
        self.cars = cars

    def view_available_cars(self):
        print("Доступні авто:")
        for car in self.cars:
            print(f"{car.car_id}. {car.model} {car.year} — {car.price} грн")

    def book_car(self, user, car):
        print(f"{user.first_name} бронює {car.model}")
        return Rental(1, user, car, car.price)




user1 = User("Vadim", "Derish")
car1 = Car(1, "Renault", 2020, 5000)
car2 = Car(2, "Toyota", 2019, 3000)

system = CarRentalSystem([car1, car2])

system.view_available_cars()
rental = system.book_car(user1, car1)

rental.generate_confirmation()
rental.end_rental()