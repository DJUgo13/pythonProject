class Figure:
    unit = 'mm'

    def __init__(self):
        self.__calculate_perimetr()
        self.calculate_area()

    def get_perimetr(self):
        return self.__perimetr

    def set_perimetr(self, perimetr):
        self.__perimetr = perimetr

    def calculate_area(self):
        pass

    def __calculate_perimetr(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, __side_length):
        self.__side_length = __side_length
        self.calculate_area()
        self.perimetr = self.__calculate_perimetr()

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def __calculate_perimetr(self):
        return self.__side_length * 4

    def info(self):
        print(
            f'Square side length: {self.__side_length}{self.unit} Perimetr: {self.__calculate_perimetr()}{self.unit} Area: {self.calculate_area()}{self.unit}')


class Rectangle(Figure):
    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def calculate_area(self):
        return self.__length * self.__width

    def __calculate_perimetr(self):
        return (self.__length + self.__width) * 2

    def info(self):
        print(
            f'Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit} Perimetr: {self.__calculate_perimetr()}{self.unit} Area: {self.calculate_area()}{self.unit}')


square_1 = Square(2)
square_2 = Square(5)

rec1 = Rectangle(12, 4)
rec2 = Rectangle(4, 8)
rec3 = Rectangle(10, 2)

all_result = [square_1, square_2, rec2, rec3, rec1]
for i in all_result:
    i.info()
