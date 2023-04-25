import Input

def sum(first_number: int, sescond_number: int):
    if sescond_number == 0:
        return first_number
    return sum(first_number + 1, sescond_number - 1)

print(sum(Input.input_from_user('Введите первое слагаемое: '),
          Input.input_from_user('Введите второе слагаемое: ')))