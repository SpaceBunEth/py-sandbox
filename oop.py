class Car:
    def __init__(self, input_model, mileage):
        self.model = input_model
        self.mileage = mileage
    def vroom(self, distance):
        self.mileage += distance
    def __str__(self):
        output = f"Hello, I am a {self.model} and I have traveled {self.mileage} miles"
        return output

my_car = Car("doodooCar",99)
print(my_car)