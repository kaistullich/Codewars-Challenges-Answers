def descending_order(num):
    """
    Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

    Examples:
        Input: 21445 Output: 54421

        Input: 145263 Output: 654321

        Input: 1254859723 Output: 9875543221
    """
    return int(''.join(sorted(str(num))[::-1]))


if __name__ == '__main__':
    descending_order(15)
    descending_order(123456789)
    print(descending_order(1201))
