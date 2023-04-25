import Input

def pow(number: int, power: int, result = 1):
    if power == 0:
        return result
    return pow(number, power - 1, result * number)

print(pow(Input.input_from_user('Введите число, которое нужно возвести в степень: '),
          Input.input_from_user('Введите степень в которую будем возводить: ')))