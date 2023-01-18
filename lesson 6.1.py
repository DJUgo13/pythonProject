# функции, аргументы: *args, **kwargs
# DRY - dont repeat yourself


# def len1(seq):
#     counter = 0
#     for i in seq:
#         counter += 1
#     return counter
#
# print(len1(input('word: ')))
# print(len('123'))


# def greet(name, surname='surname'): # name - обязательный позиционный параметр
#     print(f"name: {name}, surname: {surname} ")
#
#
# greet('Bogdan', 'shepshely')
# greet(name='Deril', surname='sharbek uulu') #keyword arguments(именованные аргументы)
# greet('Yuri', 'ronaldo')

# width = 5
# lenth = 7
# square_2 = width * lenth
# print(square_2)

# width = 7
# lenth = 15
# square_hall = width * lenth
# print(square_2)

# def get_area(width: int, length: int) -> int:
#     '''Принимает два значения ширина и длина
#     Возвращает площадь(целое)'''
#     return width * length
#
# print(help(get_area))
# print(get_area.__doc__)
#
# square_2 = get_area(5, 7)
# square_hall = get_area(15, 7)
# print(square_hall, square_2, sep='\n')

# def sum_numb(a, b=1, *args):
#     print(a, args)
#     return sum(args) / a * b
#
#
# print(sum_numb(17, 35))
#
# def menu(**kwargs):
#     return sum(kwargs.values())
#
#
# print(menu(a=1, b=2))

students = {
    'bogdan': 4,
    'marsel': 3,
    'alan': 5
}

def find_stud(name):
    if name in students:
        return True
    return False


def add(name: str, rate: int):
    if not find_stud(name):
        if rate in range(1, 6):
            students[name] = rate
        else:
            print('только от 1 до 5')
    else:
        print(f'{name} такое имя есть')

def edit(name, new_name):
    if find_stud(name):
        students[new_name] = students.pop(name)


def delete(name):
    if find_stud(name):
        del students[name]
    else:
        print('имя не найдено')


while True:
    print(students)
    command = input(f'1) add\n'
                    f'2) edit\n'
                    f'3) delete\n')
    if command == '1':
        add(name=input('новое имя: '), rate=int(input('оценка: ')))
    elif command == '2':
        edit(name=input('старое имя: '), new_name=input('новое имя: '))
    elif command == '3':
        delete(name=input('введите имя: '))
