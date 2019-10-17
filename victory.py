# (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
# Написать или улучшить программу Викторина из предыдущего дз
# (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
# Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy')
#  предлагаю для тренировки пока использовать строку
# Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
# Пример использования sample:
# import random
# numbers = [1, 2, 3, 4, 5]
# # 2 - количество случайных элементов
# result = random.sample(numbers, 2)
# print(result) # [5, 1]
#
# После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
# пользователь вводит дату в формате 'dd.mm.yyyy'
# Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде:
# третье января 2009 года, склонением можно пренебречь
#
# В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
import random


famous_people_data = {
                'Mikhailo Lomonosov': '19.11.1711',
                'Vladimir Lenin': '22.04.1870',
                'Ivan Pavlov': '26.09.1849',
                'Ivan Sechenov': '13.08.1829',
                'Piotr Anokhin': '26.01.1898',
                'Zigmund Freud': '06.05.1856',
                'Zoya Kosmodemyanskaya': '13.09.1923',
                'Sergey Korolev': '12.01.1907',
                'Evgeniy Shvartz': '21.10.1896',
                'Iisus Christos': '01.01.0001',
}

month_names = [
    '',
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
]

day_names = [
    '',
    'первого',
    'второго',
    'третьего',
    'четвертого',
    'пятого',
    'шестого',
    'седьмого',
    'восьмого',
    'девятого',
    'десятого',
    'одиннадцатого',
    'двенадцатого',
    'тринадцатого',
    'четырнадцатого',
    'пятнадцатого',
    'шестнадцатого',
    'семнадцатого',
    'восемнадцатого',
    'девятнадцатого',
    'двадцатого',
    'двадцать первого',
    'двадцать второго',
    'двадцать третьего',
    'двадцать четвертого',
    'двадцать пятого',
    'двадцать шестого',
    'двадцать седьмого',
    'двадцать восьмого',
    'двадцать деватого',
    'тридцатого',
    'тридцать первого',
]

next_round = 'y'

while next_round == 'y':

    hit = 0
    lose = 0

    random_five_famous_names = random.sample(famous_people_data.keys(), 5)

    print(random_five_famous_names)

    for name in random_five_famous_names:

        # проверка корректности ввода
        correct_input = False

        while not correct_input:
            answer = input(f'Введите дату рождения для {name} в формате dd.mm.yyyy: ')

            if len(answer) == 10:
                if '.' in answer:
                    if answer.count('.') == 2:
                        datas = answer.split('.')
                        if len(datas[0]) == len(datas[1]) == 2 and len(datas[2]) == 4:
                            if datas[0].isdigit() and datas[1].isdigit() and datas[2].isdigit():
                                correct_input = True
                            else:
                                print('Введены НЕ числа')
                        else:
                            print(f'Неверная длина чисел даты рождения!')
                    else:
                        print(f'В дате должно быть ровно две разделительные точки!')
                else:
                    print(f'Дата должна быть разделена точками!!!')
            else:
                print(f'Неверный формат даты рождения! {name} недоволен!!!')

        if answer == famous_people_data[name]:
            hit += 1
            print('Верно!)')
        else:
            lose += 1
            true_datas = famous_people_data[name].split('.')
            print(
                f'Вы ошиблись... {name} родился {day_names[int(true_datas[0])]} {month_names[int(true_datas[1])]} {int(true_datas[2])} года')

        # if len(answer) == 10:
        #     if '.' in answer:
        #         if answer.count('.') == 2:
        #             datas = answer.split('.')
        #             if len(datas[0]) == len(datas[1]) == 2 and len(datas[2]) == 4:
        #                 if datas[0].isdigit() and datas[0].isdigit() and datas[0].isdigit():
        #                     if answer == famous_people_data[name]:
        #                         hit += 1
        #                     else:
        #                         lose += 1
        #                         true_datas = famous_people_data[name].split('.')
        #                         print(f'Вы ошиблись... {name} родился {day_names[int(true_datas[0])]} {month_names[int(true_datas[1])]} {int(true_datas[2])} года')
        #                 else:
        #                     print('Введены НЕ числа')
        #             else:
        #                 print(f'Неверная длина чисел даты рождения!')
        #         else:
        #             print(f'В дате должно быть ровно две разделительные точки!')
        #     else:
        #         print(f'Дата должна быть разделена точками!!!')
        # else:
        #     print(f'Неверный формат даты рождения! {name} недоволен!!!')

    hit_percent = (100 * hit // (hit + lose))
    lose_percent = (100 * lose // (hit + lose))
    print(f'Верно угадано: {hit} ({hit_percent}%), ошибок: {lose} ({lose_percent}%)!\n')

    if hit_percent == 100:
        print('100% верных ответов! Генильно! Да вы знаток!!! С вами мой ИИ тягаться не может, до свидания!')
        next_round = 'n'
    else:
        next_round = input('Хотите продолжить? [y/n]: ')
        print()

# Программа доработана так, что в случае 100% верных ответов продолжать не предлагается
# Комментарии по годам не стал делать, т.к. они хорошо видны в словаре
