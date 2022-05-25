def print_surprise_decorator(func):
    """
    Print surprise instead of the original print of the function
    :param func: The function to decorate
    :return: decorator
    """
    def inner(*args):
        print("surprise")
    return inner


@print_surprise_decorator
def print_hello():
    print("Hello")


if __name__ == '__main__':
    print_hello()
