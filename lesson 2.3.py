class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    def drive(self):
        print('123')

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f'{self.model} {self.year}'


class FuelCar(Car):
    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def __str__(self):
        return super().__str__() + f' {self.fuel_bank}'

    def drive(self):
        print('123')


class ElectCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    def drive(self):
        print('123')

    def __str__(self):
        return super().__str__() + f' {self.battery}'


class HybridCar(FuelCar, ElectCar):
    def __init__(self, model, year, fuel_bank, battery):
        FuelCar.__init__(self, model, year, fuel_bank)
        ElectCar.__init__(self, model, year, battery)


nissan = FuelCar('Nissan Skyline', 2020, 30)
print(nissan)

tesla = ElectCar('Tesla Model X', 2020, 80000)
print(tesla)

toyota = HybridCar('Toyota Prius', 2019, 45, 9000)
print(toyota)
toyota.drive()
print(HybridCar.mro())
