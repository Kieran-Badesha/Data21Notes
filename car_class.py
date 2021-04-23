class Car:
    def __init__(self, car_name, car_type, car_age, max_speed, current_speed):
        self.car_name = car_name
        self.car_type = car_type
        self.car_age = car_age
        self.max_speed = max_speed
        self.__current_speed = current_speed

    def __repr__(self):
        car_info = f"Name: {self.car_name+',': <20} Type: {self.car_type+',': <15} First Built: {self.car_age+',': <12}\
Max Speed: {self.max_speed: <7} Current Speed: {self.__current_speed}"
        return car_info

    def change_speed(self, amount: int):
        new_speed = self.__current_speed + amount
        if new_speed >= self.max_speed:
            self.__current_speed = self.max_speed
        elif new_speed <= 0:
            self.__current_speed = 0
        else:
            self.__current_speed = new_speed


car1 = Car("Ferrari F40", "Sports", "1987", 202, 0)
car2 = Car("Benz Velo", "Old Timey", "1894", 12, 0)
car3 = Car("Aston Martin DB4", "GT", "1959", 152, 0)
car4 = Car("McLaren F1", "Sports", "1993", 221, 0)

car1.change_speed(50)
car1.change_speed(-25)

print(car1)
print(car2)
print(car3)
print(car4)


