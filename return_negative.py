def make_negative(num):
    """
    In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

    Example:
        make_negative(1);  # return -1
        make_negative(-5); # return -5
        make_negative(0);  # return 0
    Notes:

    The number can be negative already, in which case no change is required.
    Zero (0) can't be negative, see examples above.
    """
    if num != 0:
        print(f'number is not 0, its = {num}')
        # if number is already negative; return it
        if num < 0:
            print(f'Number is already negative = {num}')
            return num
        # number not 0 and not negative
        else:
            print(f'number is not 0 and not negative, its = {num}')
            try:
                num = num * -1
                print(f'after *-1 num  = {num}')
                return num
            except ValueError:
                raise
    # number is 0
    else:
        return num


if __name__ == '__main__':
    print(make_negative(42))
    print(make_negative(-9))
    # print(make_negative(0))
