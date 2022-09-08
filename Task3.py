# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и
# минимальным значением дробной части элементов.


from Functions import rand_list, ost_min_max_diff


n = int(input('Enter length of array: '))

numbers = rand_list(n, 0, 10, float)

ost_numb = ost_min_max_diff(numbers)

diff = max(ost_numb) - min(ost_numb)
print('Min ost = {0};\nMax ost = {1};\nDifference = {2}.' \
      .format(min(ost_numb), max(ost_numb), diff))