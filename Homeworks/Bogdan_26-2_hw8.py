left = 1
right = 100
tries = 1
with open('results.txt', 'w', encoding='utf-8') as file:
    while True:
        current = (left + right) // 2
        is_right = input(f'Ваше число: {current}? (да, больше или меньше)')
        if is_right.lower() == 'да':
            print('Я его угадал!')
            break
        elif is_right == 'больше':
            left = current + 1
            tries += 1
        elif is_right == 'меньше':
            right = current - 1
            tries += 1
        else:
            print('вы ввели не понятный символ, введите больше или меньше или да ')
    user_number = str(current)
    tries = str(tries)
    file.write(f'ваше число: {user_number}')
    file.write(f'\nкол-во попыток: {tries}')

