"Vehicle Rental System"
from abc import ABC,abstractmethod


class Vehicle(ABC):
    def __init__(self, name, rental_rate ):
        self.name = name
        self.rental_rate = rental_rate
    @abstractmethod
    def calculate_rental(self):
        pass


class Car(Vehicle):
    def __init__(self, name, rental_rate, insurance_cost):
        super().__init__(name, rental_rate)
        self.insurance_cost = insurance_cost

    def calculate_rental(self,days):
        total = (self.rental_rate * days) + self.insurance_cost
        return total


class Bike(Vehicle):
    def __init__(self, name, rental_rate):
        super().__init__(name, rental_rate)


    def calculate_rental(self, days):
        total = self.rental_rate * days
        return total

# === RentalSystem to demonstrate usage ===
def main():
    # Create a Car and a Bike
    car = Car("Toyota Camry", rental_rate=70, insurance_cost=50)
    bike = Bike("Mountain Bike", rental_rate=20)

    # Number of days to rent
    days = 3

    # Calculate rental prices
    print("=== Rental Summary ===")
    print(f"Car: {car.name}, Days: {days}, Total: ${car.calculate_rental(days)}")
    print(f"Bike: {bike.name}, Days: {days}, Total: ${bike.calculate_rental(days)}")


# Run the example
if __name__ == "__main__":
    main()


