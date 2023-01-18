class Car:
    def __init__(self, the_model, the_year, the_color, penalties=0):  # конструктор
        # атрибуты
        self.model = the_model
        self.year = the_year
        self.color = the_color
        self.penalties = penalties
    # метод

    def drive(self, city):
        print(f'{self.model} {city}')

    def change_color(self, new_color):
        self.color = new_color


bmv_car = Car('BMV X7', 2020, 'Red')
print(bmv_car)
print(f'{bmv_car.color}')

nissan_car = Car(the_model=2021, the_color='blue', the_year='nissan skyline', penalties=1000)
print(f'{nissan_car.color}')

nissan_car.drive('Osh')
# nissan_car.color = 'yellow'

