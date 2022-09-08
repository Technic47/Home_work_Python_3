# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

from Functions import fibonacci_pos, fibonacci_neg

n = int(input('Enter your number: '))

fib_pos = fibonacci_pos(n)  # положительная ветвь
fib_neg = fibonacci_neg(n)  # отрицательная ветвь

fib_numbers = fib_neg + fib_pos
print(fib_numbers)
