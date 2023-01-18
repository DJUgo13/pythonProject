# Структуры данных: списки, срезы, кортежи.
# list - список
# tuple - кортеж

# objects = (12,)
# objects += (2, 4, 5)
# objects = list(objects)
# objects.append(123)
# objects = tuple(objects)
# objects[0] = 23
# print(objects)
# print(type(objects))





# [start:stop:step]
# numbers = list(range(1, 6))
# numbers = [i*3 for i in range(1, 6) if i < 4]
# print(numbers)

# words = [False, 34.6, 55, 34.6, True, 3, 12, 5, 18]
# words = ['false', 'apple', 'book', 'true', 'geektech']
# new_copy = words.copy()
#
# print(new_copy is words)
# print(new_copy == words)
# print(id(new_copy), id(words))
#
# new_copy[0] = 555
#
# print(f'{words=}')
# print(f'{new_copy=}')



# words.reverse()
# words.sort()
# print(words)


"""удаление"""
# words[4] = words[4].replace('t', '')
# words.remove(34.6)
# deleted = words.pop(-1)
# print(deleted)
# del words[1:5]
# words = [i for i in words if words.count(i) < 2]


"""изменение"""
# words[3], words[4] = words[4], words[3]
# words[2] = 'frontend'
# words[0] /= 2
# words[1:3] = [input('введите слово: ')]

"""добавление"""
# words.append(100)
# words.insert(4, 'geektech')
# words.extend(numbers)
# words += numbers





# print(type(words))
# print(type(numbers))
