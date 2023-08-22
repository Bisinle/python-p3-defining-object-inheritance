from vehicle import Vehicle


class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"


car = Car(23, 334455)
print(car.wheel_number)
print(car.go())  # prints the one it inherited from the superClass
