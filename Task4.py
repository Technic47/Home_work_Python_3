# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.

from Functions import dec_to_bin, dec_to_bin_recursion

n = int(input('Enter DEC number: '))

print('{} - Your number in BIN (simple iterations);'.format(dec_to_bin(n)))

number = []
number = dec_to_bin_recursion(n, number)
result = int(''.join(map(str, number)))
print('{} - Your number in BIN (recursion);'.format(result))

print('{} - Your number in BIN (build in function);'.format(bin(n)[2:]))
