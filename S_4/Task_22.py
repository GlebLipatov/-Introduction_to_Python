import random

def creator_set(length: int):
    new_set = set()
    MAX_VALUE = 9
    for i in range(length):
        new_set.add(random.randint(0, MAX_VALUE))
    return new_set

set_1 = creator_set(int(input('Размер первого множества: ')))
set_2 = creator_set(int(input('Размер второго множества: ')))
set_3 = set().union(set_1, set_2)

print(set_1)
print(set_2)
print(set_3)
