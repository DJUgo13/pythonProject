chu = float(input('введите температуру в Чуйской области :'))
osh = float(input('введите температуру в Ошской области :'))
tal = float(input('введите температуру в Таласской области :'))
nar = float(input('введите температуру в Нарынской области :'))
dja = float(input('введите температуру в Джалал-Абадской области :'))
isy = float(input('введите температуру в Иссык-Кульской области :'))
bat = float(input('ведите температуру в Баткенской области :'))

temp_Kr = round((chu + osh + tal + nar + dja + isy + bat) / 7, 1)

print(f'Средняя температура по кыргызстану {temp_Kr}')

