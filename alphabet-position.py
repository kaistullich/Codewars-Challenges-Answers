"""

Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it. a being 1, b being 2, etc. As an example:
"""

import string
import re


def alphabet_position(text):
    alph = list(enumerate(string.ascii_lowercase))
    splitText = re.split('\W+', text.lower())

    countingString = ''

    for word in splitText:
        for letter in word:
            for number, alphLetter in alph:
                if letter == alphLetter:
                    countingString += str(number + 1) + ' '

    strippedCountingStr = countingString.strip()

    return strippedCountingStr

if __name__ == '__main__':
    alphabet_position("The sunset sets at twelve o' clock.")
