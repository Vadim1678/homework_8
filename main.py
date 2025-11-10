class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def view_available_cars(self):
        for car in cars:
            print(f"{car.model} {car.year} {car.price}")
        pass

    def book_car(self, car):
        print(f"{self.first_name} бронює автомобіль {car.model}")

        pass

class Car:
    def __init__(self, car_id ,model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def view_available_cars(self):
        pass

class Rental:
    def __init__(self, rental_id, rental_price):
        self.rental_id = rental_id
        self.rental_price = rental_price

    def generate_confirmation(self):
        print(f"Створення підтвердження оренди №{self.rental_id}.")
        pass

    def end_rental(self):
        print(f"Завершення оренди №{self.rental_id}.")
        pass




user1 = User("Vadim", "Derish")
car1 = Car(1, "Renault", 2020, 5000)
car2 = Car(2, "Toyota", 2019, 3000)

cars = [car1, car2]

user1.view_available_cars()
user1.book_car(car1)

rental1 = Rental(1, 5000)
rental1.generate_confirmation()
rental1.end_rental()