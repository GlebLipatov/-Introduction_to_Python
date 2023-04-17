import random

length = int(input('Сколько элементов будет в списке: '))
digits = []


print(length)

for number in range(0, length):
    digits.append(random.randint(-10, 10))

print(digits)

result = digits[0]
target_digit = int(input('Введите цифру от 0 до 10: '))
min_difference = target_digit - result


for digit in digits:
    current_difference = target_digit - digit
    if target_digit != digit and (min_difference.__abs__() > current_difference.__abs__()):
        result = digit
        min_difference = target_digit - result

print(result)