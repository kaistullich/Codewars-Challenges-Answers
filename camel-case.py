import re


def to_camel_case(text):
    """
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized.

    Examples:

        to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
        to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
        to_camel_case('') # returns ''
        to_camel_case('A-B-C') # returns ABC
        to_camel_case('The-pippi-was_Hungry') # returns ThePippiWasHungry

    :param text: a word [str]
    :return: camel case of the word [str]
    """

    striped = re.split('-+|_+', text)

    if not text:
        return ''
    elif text[0].isupper():
        return ''.join(striped)
    else:
        camelWordFirstWord = striped[0]
        for word in striped[1::]:
            if word.islower():
                word = word.title()
                camelWordFirstWord += word
            else:
                camelWordFirstWord += word
        return camelWordFirstWord


def test_to_camel_case():
    """
    install `pytest` library if not already installed:
        - pip install -U pytest

    For testing run `pytest <filename>.py`
    """
    assert to_camel_case('the-stealth-warrior') == 'theStealthWarrior'
    assert to_camel_case("The_Stealth_Warrior") == 'TheStealthWarrior'
    assert to_camel_case('') == ''
    assert to_camel_case('A-B-C') == 'Abc'
    assert to_camel_case('The-pippi-was_Hungry') == 'ThePippiWasHungry'
