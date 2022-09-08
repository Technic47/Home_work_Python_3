# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

from Functions import rand_list, sum_of_elements

n = int(input('Enter length of array: '))

numbers = rand_list(n, -10, 10)

summ = sum_of_elements(numbers, 1, 2)

numbers_odd = [numbers[i] for i in range(1, len(numbers), 2)]
print('Элементы на нечётных позициях: {}'.format(numbers_odd))
print('Сумма элементов на нечётных позициях: {}'.format(summ))
