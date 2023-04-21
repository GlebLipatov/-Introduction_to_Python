import random

blueberry_bushes = dict()
sum_berrys = 0
top_bush = 0

for i in range(int(input('Кол-во кустов на грядке: '))):
    blueberry_bushes[i + 1] = random.randint(5, 15)

for bush in range(3 ,len(blueberry_bushes)):
    if blueberry_bushes[bush - 2] + blueberry_bushes[bush - 1] + blueberry_bushes[bush] > sum_berrys:
        sum_berrys = blueberry_bushes[bush - 2] + \
                     blueberry_bushes[bush - 1] + \
                     blueberry_bushes[bush]
        top_bush = bush - 1

print(blueberry_bushes)
print(top_bush)
