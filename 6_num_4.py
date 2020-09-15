class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


acura = SportCar(210, 'Red', 'acura', False)
opel = TownCar(95, 'Pink', 'opel', True)
bmw = WorkCar(35, 'Black', 'bmw', False)
ford = PoliceCar(180, 'White', 'Ford', True)
print(bmw.turn_left())
print(f'When {opel.turn_right()}, then {acura.stop()}')
print(f'{bmw.go()} with speed exactly {bmw.show_speed()}')
print(f'{bmw.name} is {bmw.color}')
print(f'Is {acura.name} a police car? {acura.is_police}')
print(f'Is {ford.name}  a police car? {ford.is_police}')
print(acura.show_speed())
print(opel.show_speed())
print(ford.show_speed())



