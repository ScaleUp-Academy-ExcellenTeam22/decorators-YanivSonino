def type_check(correct_type):
    """
    Checks the type of function arguments.

    :param correct_type: The type to check.
    :return: The decorator.
    """
    def decorator(func):
        def inner(number):
            if type(number) is not correct_type:
                raise ValueError("The type is wrong")
            return func(number)
        return inner
    return decorator


@type_check(int)
def times2(num):
    return num*2


if __name__ == '__main__':
    print(times2(3))
    print(times2('3'))  # wrong
