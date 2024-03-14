def time_input():
    hh_words = {
        0: "двенадцать ночи",
        1: "час",
        2: "два часа",
        3: "три часа",
        4: "четыре часа",
        5: "пять часов",
        6: "шесть часов",
        7: "семь часов",
        8: "восемь часов",
        9: "девять часов",
        10: "десять часов",
        11: "одиннадцать часов",
        12: "двенадцать часов",
        13: "тринадцать часов",
        14: "четырнадцать часов",
        15: "пятнадцать часов",
        16: "шестнадцать часов",
        17: "семнадцать часов",
        18: "восемнадцать часов",
        19: "девятнадцать часов",
        20: "двадцать часов",
        21: "двадцать один час",
        22: "двадцать два часа",
        23: "двадцать три часа"
    }

    hh_words_half = {
        0: "двенадцатого ночи",
        1: "первого",
        2: "второго",
        3: "третьего",
        4: "четвертого",
        5: "пятого",
        6: "шестого",
        7: "седьмого",
        8: "восьмого",
        9: "девятого",
        10: "десятого",
        11: "одиннадцатого",
        12: "двенадцатого",
        13: "тринадцатого",
        14: "четырнадцатого",
        15: "пятнадцатого",
        16: "шестнадцатого",
        17: "семнадцатого",
        18: "восемнадцатого",
        19: "девятнадцатого",
        20: "двадцатого",
        21: "двадцать первого",
        22: "двадцать второго",
        23: "двадцать третьего",
        24: "двенадцати ночи"
    }

    mm_words = {
        1: "одна минута",
        2: "две минуты",
        3: "три минуты",
        4: "четыре минуты",
        5: "пять минут",
        6: "шесть минут",
        7: "семь минут",
        8: "восемь минут",
        9: "девять минут",
        10: "десять минут",
        11: "одиннадцать минут",
        12: "двенадцать минут",
        13: "тринадцать минут",
        14: "четырнадцать минут",
        15: "пятнадцать минут",
        16: "шестнадцать минут",
        17: "семнадцать минут",
        18: "восемнадцать минут",
        19: "девятнадцать минут",
        20: "двадцать минут",
        21: "двадцать одна минута",
        22: "двадцать две минуты",
        23: "двадцать три минуты",
        24: "двадцать четыре минуты",
        25: "двадцать пять минут",
        26: "двадцать шесть минут",
        27: "двадцать семь минут",
        28: "двадцать восемь минут",
        29: "двадцать девять минут",
        30: "половина",
        31: "тридцать одна минута",
        32: "тридцать две минуты",
        33: "тридцать три минуты",
        34: "тридцать четыре минуты",
        35: "тридцать пять минут",
        36: "тридцать шесть минут",
        37: "тридцать семь минут",
        38: "тридцать восемь минут",
        39: "тридцать девять минут",
        40: "сорок минут",
        41: "сорок одна минута",
        42: "сорок две минуты",
        43: "сорок три минуты",
        44: "сорок четыре минуты",
        45: "пятнадцать минут",
        46: "четырнадцать минут",
        47: "тринадцать минут",
        48: "двенадцать минут",
        49: "одиннадцать минут",
        50: "десять минут",
        51: "девять минут",
        52: "восемь минут",
        53: "семь минут",
        54: "шесть минут",
        55: "пять минут",
        56: "четыре минуты",
        57: "три минуты",
        58: "две минуты",
        59: "одна минута"
    }

    mm_words_end = {
        1: "одной минуты",
        2: "двух минут",
        3: "трех минут",
        4: "четырех минут",
        5: "пяти минут",
        6: "шести минут",
        7: "семи минут",
        8: "восьми минут",
        9: "девяти минут",
        10: "десяти минут",
        11: "одиннадцати минут",
        12: "двенадцати минут",
        13: "тринадцати минут",
        14: "четырнадцати минут",
        15: "пятнадцати минут",
    }

    while True:
        user_input = input("Please input the time in the format hh:mm :")
        if user_input.lower() == 'quit':
            break

        user_time = user_input.split(":")

        if len(user_time) == 2 and user_time[0].isdigit() and user_time[1].isdigit():
            hh, mm = map(int, user_time)
            if 0 <= hh <= 23 and 0 <= mm <= 59:
                if mm == 0:
                    print(f"{hh_words[hh]} ровно.")
                elif mm < 30:
                    print(f"{mm_words[mm]} {hh_words_half[(hh + 1) % 24]} часа")
                elif mm == 30:
                    print(f"половина {hh_words_half[(hh + 1) % 24]}.")
                elif 30 < mm < 45:
                    print(f" {mm_words[mm]} {hh_words_half[hh + 1]}.")
                elif 45 <= mm < 60:
                    print(f" без {mm_words_end[60 - mm]} {hh_words[(hh + 1) % 24]}.")
 
            else:
                print("Вы ввели неверный формат времени. Используйте формат часы:минуты  диапазоне от 00:00 до 23:59.")
        else:
            print("Вы ввели неверный формат времени. Пожалуйста, введите время в формате hh:mm или напишите 'quit' чтобы выйти.")

time_input()


