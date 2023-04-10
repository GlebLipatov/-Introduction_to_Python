def sum_digits(number):
    result = 0;
    while number > 0:
        result += number % 10
        number //= 10
    return result


def lucky_ticket(first_number, second_number):
    if sum_digits(first_number) == sum_digits(second_number):
        print('yes')
    else:
        print('no')


ticket_number_1 = 385916
ticket_number_2 = 123456

lucky_ticket(ticket_number_1 // 1000, ticket_number_1 % 1000)
lucky_ticket(ticket_number_2 // 1000, ticket_number_2 % 1000)
