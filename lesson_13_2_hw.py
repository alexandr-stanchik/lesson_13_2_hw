# Hometask_13_4
# Напишите функцию, которая создает список случайных
# элементов. На фход функция принимает кол-во элементов,
# минимальное и максимальное значение
from random import randint


def rand_nums(count, min_item, max_item):
    return [randint(min_item, max_item) for i in range(count)]


print(rand_nums(int(input('count elements: ')), int(input('min value: ')), int(input('max value: '))))


# exam_2_5
# cakes = {'наполеон': [['масло', 'мука', 'сахар'], 50, 1000],
#          'медовик': [['масло', 'мука', 'сметанный крем'], 100, 1000],
#          'киевский': [['масло', 'мука', 'шоколадный крем'], 150, 1000]}
# cake = input('Какой торт вы бы хотели приобрести? ').lower()
# descr = input('Что бы вы хотели уточнить? ').lower()
#
# if descr == 'описание':
#     print(f'Торт {cake} состоит из {cakes[cake][0]}')
# elif descr == 'цена':
#     print(f'Торт {cake} стоит {cakes[cake][1]} рублей')
# elif descr == 'количество':
#     print(f'Торт {cake} осталось {cakes[cake][2]} грамм')
#
# weight = int(input('Сколько торта Вам положить? '))
# print(f'К оплате {cakes[cake][1] * weight / 100}')
# print(f'торта {cake} осталось {cakes[cake][-1] - weight} грамм')

def answer(cake_1, descr_1):
    if descr_1 == 'описание':
        print(f'Торт {cake_1} состоит из {cakes[cake_1][0]}')
    elif descr_1 == 'цена':
        print(f'Торт {cake_1} стоит {cakes[cake_1][1]} рублей')
    elif descr_1 == 'количество':
        print(f'Торт {cake_1} осталось {cakes[cake_1][2]} грамм')


cakes = {'наполеон': [['масло', 'мука', 'сахар'], 50, 1000],
         'медовик': [['масло', 'мука', 'сметанный крем'], 100, 1000],
         'киевский': [['масло', 'мука', 'шоколадный крем'], 150, 1000]}
cake = input('Какой торт вы бы хотели приобрести? ').lower()
descr = input('Что бы вы хотели уточнить? ').lower()

answer(cake, descr)

weight = int(input('Сколько торта Вам положить? '))
print(f'К оплате {cakes[cake][1] * weight / 100}')
print(f'торта {cake} осталось {cakes[cake][-1] - weight} грамм')


# Hometask_13_6
# Напишите функцию, вычисляющую значение
# факториала числа N. Используйте рекурсию
def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x


print(fact(int(input())))


# 13.11
# Напишите декоратор к функции деления, который меняет
# местами делимое и делител
def decor(func):
    def other(n1, n2):
        return func(n2, n1)

    return other


@decor
def div(n1, n2):
    return n1 / n2


print(div(int(input('делитель: ')), int(input('делимое: '))))
