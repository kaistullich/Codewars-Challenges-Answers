def findSmallestInt(arr):
    """
    Given an array of integers your solution should find the smallest integer.

    For example:

    Given [34, 15, 88, 2] your solution will return 2
    Given [34, -345, -1, 100] your solution will return -345
    You can assume, for the purpose of this kata, that the supplied array will not be empty.

    :param arr: array of numbers
    :return: array with smallest number removed
    """
    smallest_int = min(arr)

    for num in arr:
        if num > smallest_int:
            smallest_int = num

    return smallest_int


if __name__ == '__main__':
    findSmallestInt([78, 56, 232, 12, 11, 43])
    findSmallestInt([34, -345, -1, 100])
