while 1:
    a = input('Введи слово : ').lower()
    if a == 'exit':
        print('exit....')
        break
    elif a == 'выход':
        print('exit....')
    else:
        gla = 'aeyuoiыауеияюоёэ'
        sog = 'qzwsxdcrvtgbhnjmklpйцфвкнгшщзхпрлджчсмтб'
        b = 0
        c = 0
        print(f'слово: {a}')
        print('Всего символов: ', len(a))
        for i in a:
            if i in gla:
                b += 1
        print('гласных :', int(b))
        for e in a:
            if e in sog:
                c += 1
        print('Согласный:', int(c))
        srg = round(b / len(a) * 100, 2)
        srs = round(c / len(a) * 100, 2)
        print(f'Гласные/Согласные: {srg}% / {srs}%')
