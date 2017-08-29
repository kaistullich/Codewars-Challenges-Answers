import math


def get_middle(s):
    """
    For any given string grab the middle character. If the length of the word is ODD,
    grab the middle character. If the length of the word is EVEN grab the 2 middle
    characters.

    :param s: word [str]
    :return: middle character(s) [str]
    """

    wordLength = len(s)
    # create list with 1 character at a time
    splitWord = list(s)
    # if its an even word
    if wordLength % 2 == 0:
        evenChars = ''
        # the left character in the middle
        leftIndex = int((wordLength / 2) - 1)
        # the right character in the middle
        rightIndex = int(((wordLength / 2) + 1) - 1)
        # add both characters to new string
        evenChars += (splitWord[leftIndex])
        evenChars += splitWord[rightIndex]
        return evenChars
    # if its an odd word
    else:
        # grab middle character
        oddIndex = int(math.ceil(wordLength / 2) - 1)
        return splitWord[oddIndex]

if __name__ == '__main__':
    get_middle('test')
