import random

MAX_VALUE = 100
MIN_VALUE = 50
SIDE_ZERO = 0
SIDE_ONE = 1

total_coins = random.randint(MIN_VALUE, MAX_VALUE)
print(f'Всего монет: {total_coins}')
count_one = 0

for coin in range(total_coins):
    coin = random.randint(SIDE_ZERO, SIDE_ONE)
    if coin == 1:
        count_one += 1

if total_coins - count_one < count_one:
    print(f'Нужно перевернуть монет: {total_coins - count_one}')
else:
    print(f'Нужно перевернуть монет: {count_one}')
