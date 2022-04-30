def do_it_twice(func):
    """
    Make function executes twice.
    :param func: The functopn to decorate
    :return: decorator.
    """
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return inner


@do_it_twice
def add_numbers(x, y):
    print("add number executed")
    return x + y


if __name__ == '__main__':
    add_numbers(5, 3)
