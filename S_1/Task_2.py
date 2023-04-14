def sum_digits(number):
    result = 0;

    while number > 0:
        result += number % 10
        number //= 10
    return result


number_1 = 123
number_2 = 100

print(sum_digits(number_1))
print(sum_digits(number_2))
