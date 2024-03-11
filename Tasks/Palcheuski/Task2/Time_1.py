while True:
    x = input("Введите время в формате чч:мм\n")

    while x[2] != ':' or not len(x) == 5 or not (x[:2]+x[3:]).isdigit() or not 0 <= int(x[:2]) < 24 or not 0 <= int(x[3:]) < 60:
        x = input("Неверный ввод, попробуйте еще раз, требуется ввести в формате чч:мм\n")

    hh_n = {0: 'первого', 1: 'второго', 2: 'третьего', 3: 'четвертого', 4: 'пятого', 5: 'шестого', 6: 'седьмого', 7: 'восьмого', 8: 'девятого', 9: 'десятого', 10: 'одиннадцатого', 11: 'двенадцатого',
            12: 'первого', 13: 'второго', 14: 'третьего', 15: 'четвертого', 16: 'пятого', 17: 'шестого', 18: 'седьмого', 19: 'восьмого', 20: 'девятого', 21: 'десятого', 22: 'одиннадцатого', 23: 'двенадцатого'}

    hh_00 = {0: 'Двенадцать часов ночи', 1: 'Час ночи', 2: 'Два часа ночи', 3: 'Три часа ночи', 4: 'Четыре часа ночи', 5: 'Пять часов утра',
                6: 'Шесть часов утра', 7: 'Семь часов утра', 8: 'Восемь часов утра', 9: 'Девять часов утра', 10: 'Десять часов утра', 11: 'Одиннадцать дня ровно',
                12: 'Двенадцать дня ровно', 13: 'Час дня', 14: 'Два часа дня', 15: 'Три часа дня', 16: 'Четыре часа', 17: 'Пять часов',
                18: 'Шесть часов вечера', 19: 'Семь вечера', 20: 'Восемь вечера', 21: 'Девять вечера', 22: 'Десять вечера', 23: 'Одиннадцать вечера ровно'}

    hh_1_29 = {1: 'Одна минута', 2: 'Две минуты', 3: 'Три минуты', 4: 'Четыре минуты', 5: 'Пять минут', 6: 'Шесть минуты', 7: 'Семь минут',
                  8: 'Восемь минут', 9: 'Девять минут', 10: 'Десять минут', 11: 'Одиннадцать минут', 12: 'Двенадцать минут ', 13: 'Тринадцать минут',
                  14: 'Четырнадцать минут', 15: 'Пятнадцать минут ', 16: 'Шестнадцать минут', 17: 'Семнадцать минут', 18: 'Восемнадцать минут',
                  19: 'Девятнадцать минут', 20: 'Двадцать минут', 21: 'Двадцать одна минута', 22: 'Двадцать две минуты', 23: 'Двадцать три минуты',
                  24: 'Двадцать четыре минуты', 25: 'Двадцать пять минут', 26: 'Двадцать шесть минут', 27: 'Двадцать семь минут', 28: 'Двадцать восемь',
                  29: 'Двадцать девять минут'}

    hh_31_45 = {31: 'Традцать одна минута', 32: 'Тридцать две минуты', 33: 'Тридцать три минуты', 34: 'Тридцать четыре минуты', 35: 'Тридцать пять минут', 36: 'Тридцать шесть минут',
                37: 'Тридцать семь минут', 38: 'Тридцать восемь минут', 39: 'Тридцать девять минут', 40: 'Сорок минут', 41: 'Сорок одна минута', 42: 'Сорок две минуты', 43: 'Сорок три минуты', 44: 'Сорок четыре минуты'}

    hh_45_59 = {45: 'Без пятнадцати минут', 46: 'Без четырнадцати минут', 47: 'Без тринадцати минут', 48: 'Без двенадцати минут', 49: 'Без одиннадцати минут', 50: 'Без десяти минут ',
                51: 'Без девяти минут', 52: 'Без восьми минут', 53: 'Без семи минут', 54: 'Без шести минут', 55: 'Без пяти минут', 56: 'Без четырех минут', 57: 'Без трех минут',
                58: 'Без двух минут', 59: 'Без одной минуты'}

    mm_hh = {0: 'час', 1: 'два', 2: 'три', 3: 'четыре', 4: 'пять', 5: 'шесть', 6: 'семь', 7: 'восемь', 8: 'девять', 9: 'десять', 10: 'одиннадцать', 11: 'двенадцать', 12: 'час',
             13: 'два', 14: 'три', 15: 'четыре', 16: 'пять', 17: 'шесть', 18: 'семь', 19: 'восемь', 20: 'девять', 21: 'десять', 22: 'одиннадцать', 23: 'двенадцать'}

    if int(x[3:]) == 0:
        print(x + ' - ' + hh_00[int(x[:2])])

    if int(x[3:]) == 30:
        print(x + ' - ' + 'Половина ' + hh_n[int(x[:2])])

    if 0 < int(x[3:]) < 30:
        print(x + ' - ' + hh_1_29[int(x[3:])] + ' ' + hh_n[int(x[:2])])

    if 30 < int(x[3:]) < 45:
        print(x + ' - ' + hh_31_45[int(x[3:])] + ' ' + hh_n[int(x[:2])])

    if int(x[3:]) >= 45:
        print(x + ' - ' + hh_45_59[int(x[3:])] + ' ' + mm_hh[int(x[:2])])
