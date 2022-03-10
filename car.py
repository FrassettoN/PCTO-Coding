class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back  an odometer!")


my_used_car = Car("subaru", "baracca", 1999)
print(my_used_car.get_descriptive_name())  # -> 1999 Subaru Baracca

my_used_car.update_odometer(23500)
my_used_car.read_odometer()  # -> This car has 23500 miles on it.

my_used_car.increment_odometer(100)
my_used_car.read_odometer()  # -> This car has 23600 miles on it.
