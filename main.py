import pandas as pd

df_cars = pd.read_csv("cars.csv", dtype={"id": str})


class Car:
    def __init__(self, car_id):
        self.car_id = car_id
        car_data = df_cars.loc[df_cars["id"] == self.car_id]
        if car_data.empty:
            raise ValueError(f"Car with ID {car_id} not found!")

        self.make = car_data["make"].squeeze()
        self.model = car_data["model"].squeeze()
        self.year = car_data["year"].squeeze()
        self.available_status = car_data["available"].squeeze()

    def available(self):
        return self.available_status == "yes"

    def book(self):
        df_cars.loc[df_cars["id"] == self.car_id, "available"] = "no"
        df_cars.to_csv("cars.csv", index=False)
        self.available_status = "no"

class RentalTicket:
    def __init__(self, customer_name, car_obj):
        self.customer_name = customer_name
        self.car_obj = car_obj

    def generate(self):
        ticket = f"""
        ---- RENTAL CONFIRMATION ----
        Customer: {self.customer_name}
        Car: {self.car_obj.make} {self.car_obj.model} ({self.car_obj.year})
        Car ID: {self.car_obj.car_id}
        Thank you for renting with us!
        -----------------------------------
        """
        return ticket

def main():
    print("Available cars:")
    print(df_cars)

    customer_name = input("Enter your name: ")

    car_id = input("Enter the ID of the car you want to rent: ")

    car = Car(car_id)

    if car.available():
        print(f"{car.make} {car.model} is available. Booking now...")

        car.book()

        ticket = RentalTicket(customer_name, car)
        print(ticket.generate())

    else:
        print("Sorry, this car is NOT available.")


if __name__ == "__main__":
    main()