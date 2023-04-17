import random

length = int(input('Сколько элементов будет в списке: '))
numbers = []
count = 0

print(length)

for number in range(0, length):
    numbers.append(random.randint(0, 10))

print(numbers)

some_number = int(input('Какое число найти и посчитать: '))

for number in numbers:
    if number == some_number:
        count += 1

print(count)