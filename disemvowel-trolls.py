"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""


def disemvowel(string):
    vowels = 'aeiouAEIOU'
    newString = ''
    for letter in string:
        if letter.isalpha() and letter in vowels:
            continue
        else:
            newString += letter

    return newString


if __name__ == '__main__':
    disemvowel('This website is for losers LOL!')