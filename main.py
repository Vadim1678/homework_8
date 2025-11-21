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

class PlaylistService:
    def __init__(self):
        self.playlists = {
            "Chill / Relax": "https://music.youtube.com/watch?v=EGLoIaHwKfE&si=gedrEB5AP2nEOdyZ",
            "Energy/Party": "https://music.youtube.com/watch?v=r6FA4j-kGa4&si=TG1D-K19YLjOemM6",
            "Road Trip Classics": "https://music.youtube.com/watch?v=_G33r-isgco&si=q30iiJ8dBQEiQ5Pl",
            "Hip-Hop": "https://music.youtube.com/watch?v=rwYrEEka1mc&si=r35A_0eRqptbmYzp",
            "Lo-Fi": "https://music.youtube.com/watch?v=CLeZyIID9Bo&si=oRQiBTUcvfSSvBYs",
            "Pop Hits": "https://music.youtube.com/watch?v=jsfzwnOohlc&si=eBfp9I9MSlnGBYrf"
        }

    def get_playlist_link(self, mood):
        return self.playlists.get(mood, None)

class RentalTicket:
    def __init__(self, customer_name, car_obj, playlist_name=None, playlist_link=None):
        self.customer_name = customer_name
        self.car_obj = car_obj
        self.playlist_name = playlist_name
        self.playlist_link = playlist_link

    def generate(self):
        ticket = f"""
        ---- RENTAL CONFIRMATION ----
        Customer: {self.customer_name}
        Car: {self.car_obj.make} {self.car_obj.model} ({self.car_obj.year})
        Car ID: {self.car_obj.car_id}
        """

        if self.playlist_name:
            ticket += f"""
                Option: Ідеальний Плейлист ("{self.playlist_name}")
                Playlist Link: {self.playlist_link}
                """

        ticket += """
                Дякуємо за оренду
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

        playlist_service = PlaylistService()
        playlist_name = None
        playlist_link = None

        want_playlist = input("Бажаєте додати опцію 'Ідеальний Плейлист'? (yes/no): ")

        if want_playlist == "yes":
            print("Доступні варіанти:")
            for mood in playlist_service.playlists.keys():
                print(mood)

            music = input("Оберіть настрій або жанр: ")

            playlist_link = playlist_service.get_playlist_link(music)

            if playlist_link:
                playlist_name = music
                print("Плейлист додано!")
            else:
                print("Такого плейлисту не знайдено.")

        ticket = RentalTicket(customer_name, car, playlist_name, playlist_link)
        print(ticket.generate())

    else:
        print("Sorry, this car is NOT available.")

if __name__ == "__main__":
    main()