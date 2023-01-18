import random
from decouple import config

your_money = config('MY_MONEY')


def start_game():
    global your_money
    while True:
        if input('хотите ли вы сыграть еще, если да пишите yes, если нет no: ') == 'no':
            print(f'Ваши деньги: {your_money}')
            break
        elif input('хотите ли вы сыграть еще, если да пишите yes, если нет no: ') == 'yes':
            your_num = input('Введите число от 1 до 30: ')
            rand_num = random.randint(1, 31)
            rate = input(f'введите кол-во ставки 1 до {your_money}')
            if your_num == rand_num:
                your_money = your_money + 2 * rate
            else:
                your_money = your_money - rate


start_game()




