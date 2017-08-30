import re


def to_camel_case(text):
    """
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized.

    :param text: a word [str]
    :return: camel case of the word [str]
    """

    striped = re.split('-+|_+', text)

    if not text:
        return ''
    elif text[0].isupper():
        return ''.join(striped)
    else:
        camelWord = striped[0]
        for word in striped[1::]:
            if word.islower():
                word = word.title()
                camelWord += word
            else:
                camelWord += word
        return camelWord


if __name__ == '__main__':
    # returns "theStealthWarrior"
    to_camel_case("the-stealth-warrior")

    # returns "TheStealthWarrior"
    to_camel_case("The_Stealth_Warrior")

    # returns ''
    to_camel_case('')

    # returns ABC
    to_camel_case('A-B-C')

    # returns ThePippiWasHungry
    x = to_camel_case('The-pippi-was_Hungry')
    print(x)
