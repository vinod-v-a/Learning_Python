class Room:
    def __init__(self,room_type, price):
        self.room_type = room_type
        self._price = price

    def display_info(self):
        print(f"Room Type {self.room_type}, Price per night {self._price}")


class Customer:
    def __init__(self, name):
        self.name = name



class Reservation:
    def __init__(self, room, customer, nights):
        self.room = room
        self.customer = customer
        self.nights = nights

    def calculate_total(self):
        return self.room.get_price() * self.nights

    def display_reservation(self):
        print("Reservation Details:")
        self.customer.display_info()
        self.room.display_info()
        print(f"Number of Nights: {self.nights}")
        print(f"Total Cost: ${self.calculate_total()}")


room1 = Room("Deluxe Suite", 150)


customer1 = Customer("RAj", "RAj@email.com")

reservation1 = Reservation(room1, customer1, 3)


reservation1.display_reservation()