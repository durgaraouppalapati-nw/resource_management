def my_func():
    return 3


def test_my_func(snapshot):
    return_value = my_func()

    snapshot.assert_match(return_value, 'gpg_response')


def add_two_numbers(number1, number2):
    return number1 + number2


def test_add_two_positive_numbers(snapshot):
    number1 = 1
    number2 = 2

    return_value = add_two_numbers(number1, number2)

    snapshot.assert_match(return_value, 'jpg_response')


def test_add_two_negative_numbers(snapshot):
    number1 = -1
    number2 = -2

    return_value = add_two_numbers(number1, number2)

    snapshot.assert_match(return_value, 'jpg_response')


def test_add_two_float_numbers(snapshot):
    number1 = 1.0
    number2 = 2.0

    return_value = add_two_numbers(number1, number2)

    snapshot.assert_match(return_value, 'jpg_response')
