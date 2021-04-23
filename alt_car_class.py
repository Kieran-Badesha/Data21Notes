# Define the class name
class Car:
    # Define the class objects
    def __init__(self, car_make, car_model, year_made, doors, power, max_speed, current_speed):
        self.car_make = car_make
        self.car_model = car_model
        self.year_made = year_made
        self.doors = doors
        self.power = power
        self.max_speed = max_speed
        self.__current_speed = current_speed

    # Define how to represent your objects as a string
    def __repr__(self):
        car_info = f'Make: {self.car_make+",": <10} Model: {self.car_model+",": <8} First Built: \
{self.year_made + ",": <8} Doors: {self.doors + ",": <6} Horsepower: {self.power + "bhp,": <12} Max Speed: \
{self.max_speed+"Mph, ": <8} Current Speed: {self.__current_speed+"Mph"} '
        return car_info

    # Define parameters for speed and how speed will change
    def change_speed(self, amount: int):
        new_speed = float(self.__current_speed) + amount
        if new_speed >= float(self.max_speed):
            (self.__current_speed) = float(self.max_speed)
        elif new_speed <= 0:
            (self.__current_speed) = 0
        else:
            (self.__current_speed) = new_speed

    def get_current_speed(self):
        return self.__current_speed

car1 = Car("Ferrari", "F40", "1987", "2", "478", "202", "0")
car2 = Car("Benz", "Velo", "1894", "0", "1.5", '12', '0')

print(car1)
print(car2)