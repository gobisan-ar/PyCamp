class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


sample_car = Car()
new_car = Car(make="BNW")
my_car = Car(make="Jaguar", model="XE")
print(my_car.make)
