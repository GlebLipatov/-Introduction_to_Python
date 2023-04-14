import random

MAX_VALUE = 1000
first_number = random.randint(0, MAX_VALUE)
second_number = random.randint(0, MAX_VALUE)
has_answer = False

print(f'Сумма чисел ровна {first_number + second_number}')
print(f'Произведение чисел ровно {first_number * second_number}\n')

for i in range(1000):
    if (has_answer):
        break
    for j in range(1000):
        if i + j == first_number + second_number and i * j == first_number * second_number:
            print(f'Первое число: {i}, второе число: {j}.')
            has_answer = True
            break
