import string
from collections import Counter


def is_pangram(s):
    """
    A pangram is a sentence that contains every single letter of the alphabet at least once. For example,
    the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters
    A-Z at least once (case is irrelevant).

    Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
    Ignore numbers and punctuation.

    :param s: The string to check for pangram
    :return: True or False
    """
    stripped = ''.join([i.lower() for i in s if i.isalpha()])

    c = Counter(stripped)
    if c.most_common(1)[0][1] > 1:
        if sorted(c) == list(string.ascii_lowercase):
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    print(is_pangram('abcdefghijklmopqrstuvwxyz'))
