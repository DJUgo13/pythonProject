ten = list(range(1, 11))
print(ten)

evens = list(filter(lambda x: x % 2 == 0, ten))
print(evens)

print(list(map(lambda x: x * x, evens)))


def find_ind(spisok=ten):
    while 1:
        try:
            index_user = int(input('Введите индекс или число 356 чтобы выйти:'))
            if index_user == 356:
                print('exit....')
                break
            else:
                print(spisok[index_user])
        except:
            print('только цифры от 0 до 9')


print(find_ind())
