def finding_missing_letter(chars):
    """

    #Find the missing letter

    Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

    You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
    The array will always contain letters in only one case.

    Example:

    ['a','b','c','d','f'] -> 'e'
    ['O','Q','R','S'] -> 'P'

    :param chars: list of characters
    :return: a string containing the missing character from the alphabet
    """
    return 0


def test_missing_letter():
    assert finding_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
    assert finding_missing_letter(['O','Q','R','S']) == 'p'
