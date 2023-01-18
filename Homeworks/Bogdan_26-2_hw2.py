print('Просьба вводить числа иначе программа вас не поймет')
day = int(input('Введите свой день рождения:'))
month = int(input('Введите месяц своего рождения:'))

if 21 <= day <= 31 and month == 3 or 1 <= day <= 20 and month == 4:
    print('Вы Овен')
elif 21 <= day <= 30 and month == 4 or 1 <= day <= 21 and month == 5:
    print('Вы Телец')
elif 22 <= day <= 31 and month == 5 or 1 <= day <= 21 and month == 6:
    print('Вы Близнецы')
elif 22 <= day <= 30 and month == 6 or 1 <= day <= 22 and month == 7:
    print('Вы Рак')
elif 23 <= day <= 31 and month == 7 or 1 <= day <= 21 and month == 8:
    print('Вы Лев')
elif 22 <= day <= 31 and month == 8 or 1 <= day <= 23 and month == 9:
    print('Вы Дева')
elif 24 <= day <= 30 and month == 9 or 1 <= day <= 23 and month == 10:
    print('Вы Весы')
elif 24 <= day <= 31 and month == 10 or 1 <= day <= 22 and month == 11:
    print('Вы Скорпион')
elif 23 <= day <= 30 and month == 11 or 1 <= day <= 22 and month == 12:
    print('Вы Стрелец')
elif 23 <= day <= 31 and month == 12 or 20 >= day >= 1 == month:
    print('Вы Козерог')
elif 21 <= day <= 31 and month == 1 or 1 <= day <= 19 and month == 2:
    print('Вы Водолей')
elif 20 <= day <= 29 or not month == 2 or 1 <= day <= 20 and month == 3:
    print('Вы Рыбы')
else:
    print('Просьбы ввести свой день рождения а не что то еще')