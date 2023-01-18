class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number


class Animal:
    def __init__(self, name, age):
        self.__name = name
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            raise ValueError('sf')
        self.__age = age
        self.__was_born()

    def info(self):
        return f'{self.__name}, {self.__age}, {self.get_birth()}'

    def get_age(self):
        return self.__age

    def set_name(self, value):
        if isinstance(value, int) and value >= 0:
            self.__age = value
        else:
            raise ValueError('sf')

    def get_birth(self):
        return 2023 - self.__age

    def __was_born(self):
        print(f'{self.__name}')


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    def info(self):
        return super(Dog, self).info() + f'{self.__commands}'


animal = Animal('Jojo', 17)
print(animal.info())

cat = Cat('Jo', 12)
print(cat.info())

dog = Dog('jo', 12, 'sit, bark')
print('')
