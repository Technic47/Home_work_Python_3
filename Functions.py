from random import randint


def rand_list(n, min, max, type_numb=int, after_dot=2):
    """
    Функция для создания одномерного списка
    с псевдослучайным заполнениемю
    :param n: - длина списка
    :param min: - минимальное число
    :param max: - максимальное число
    :param type_numb: - аргумент для выбора способа генерации
    :return: - заполненный список
    """
    if type_numb == int:
        numbers = [randint(0, 9) for i in range(n)]
    elif type_numb == float:
        accuracy = 10 ** after_dot
        numbers = [(randint((min * accuracy), (max * accuracy)) / accuracy) for i in range(n)]
    print('Изначальный массив: {}'.format(numbers))
    return numbers


def sum_of_elements(numbers, start=0, step=1):
    """
    Функция для вычисления суммы списка чисел
    с заданием стартового значения и шага.
    :param numbers: - список чисел
    :param start: - позиция начала
    :param step: - шаг суммирования
    :return: - значение суммы
    """
    summ = 0
    for i in range(start, len(numbers), step):
        summ += numbers[i]
    return summ


def sum_pairs(numbers):
    """
    Функция для вычисления сумм
    диаметрально парных элементов списка
    :param numbers: - список чисел
    :return: - список с суммами
    """
    mult = []
    if len(numbers) % 2 == 0:
        length = len(numbers) // 2
    else:
        length = len(numbers) // 2 + 1
    for i in range(length):
        mult.append(numbers[i] * numbers[-(i + 1)])
    return mult


def ost_min_max_diff(numbers):
    """
    Функция находит дробную часть от каждого число из списка
    :param numbers: - список чисел
    :return: - список дробных частей
    """
    ost_numb = []
    for i in range(len(numbers)):
        ost = round(numbers[i] * 100)
        hundreds = ost // 100
        ost -= (hundreds * 100)
        ost_numb.append(ost)
    return ost_numb


def dec_to_bin(n):
    """
    Функция для перевода числа из десятичной
    в двоичную систему исчеслений
    :param n: - число для перевода
    :return: - число в BIN
    """
    c = 1
    number = 0
    while n != 0:
        b = n % 2
        n //= 2
        c *= 10
        number = number + b * c
    return number // 10


def dec_to_bin_recursion(n, number):
    """
    Функция для перевода числа из десятичной
    в двоичную систему исчеслений используя рекурсию.
    Нужен внешний массив для заполнения
    и последующая обработка для красивого вывода
    :param n: - число для перевода
    :return: - число в BIN
    """
    if n == 0:
        return
    dec_to_bin_recursion(n // 2, number)
    number.append(n % 2)
    return number


def fibonacci_pos(n):
    """
    Функция для вычисления чисел Фибоначчи до предела n
    :param n: - предел количества чисел
    :return: - список чисел Фибоначчи
    """
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def fibonacci_neg(n):
    """
    Функция для вычисления негаативных чисел Фибоначчи до предела n
    :param n: - предел количества чисел
    :return: - список негаативных чисел Фибоначчи
    """
    neg_fib = [-1, 1]
    for i in range(n-2):
        neg_fib.insert(0, (neg_fib[1] - neg_fib[0]))
    return neg_fib