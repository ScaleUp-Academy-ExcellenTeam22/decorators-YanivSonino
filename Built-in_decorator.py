import atexit


class NumberWithFunctions:
    """ A Number class with functions to use.

    :ivar num: The number to define.

    :param num: The number to build.

    """
    def __init__(self, num):
        self.num = num
        self.counter = 0

    @property
    def number(self):
        return self.num

    @staticmethod
    def how_to_use():
        print("Use This class if you need number calculations")

    def add_number(self, num_to_add):
        self.num += num_to_add

    def dec_number(self, num_to_dec):
        self.num -= num_to_dec

    def __str__(self):
        return ''.join("The number is: {}").format(self.num)


@atexit.register
def end_of_code():
    print("Thanks for using this code")


if __name__ == '__main__':
    num1 = NumberWithFunctions(1)
    NumberWithFunctions.how_to_use()
    num1.add_number(3)
    print(num1)
    num1.dec_number(2)
    print(num1)
    print(num1.number)
    num1.number = 3  # won't work because of the property decorator, need to add setter.
