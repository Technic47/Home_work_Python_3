# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

from Functions import rand_list, sum_pairs

n = int(input('Enter length of array: '))

numbers = rand_list(n, 0, 9)

mult = sum_pairs(numbers)

print('Произведения диаметральных пар элементов: {}'.format(mult))