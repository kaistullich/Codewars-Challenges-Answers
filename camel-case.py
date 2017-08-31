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

if __name__ == '__main__':
    # returns "theStealthWarrior"
    stealth = to_camel_case("the-stealth-warrior")
    print(stealth)

    # returns "TheStealthWarrior"
    stealth1 = to_camel_case("The_Stealth_Warrior")
    print(stealth1)

    # returns ''
    none = to_camel_case('')
    print(none)

    # returns ABC
    abc = to_camel_case('A-B-C')
    print(abc)

    # returns ThePippiWasHungry
    # FIXME: this is not camel casing correctly. Output should be = ThePippiWasHungry : Currently = ThepippiwasHungry
    pippi = to_camel_case('The-pippi-was_Hungry')
    print(pippi)
