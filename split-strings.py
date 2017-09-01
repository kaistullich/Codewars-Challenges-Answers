def solution(string):
    """
    Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters then it should replace the missing
    second character of the final pair with an underscore ('_').

    :param string: a odd or even character string [str]
    :return: a list of strings in a pair (2) [str]
    """

    splitStringList = list(string)

    # groupedList = []
    # counter = 0
    # temp = []
    # for letter in splitStringList:
    #     # print('letter: ' + str(letter))
    #     temp.append(letter)
    #     if counter == 1:
    #         groupedList.append(temp)
    #         temp = []
    #         counter = 0
    #     counter += 1
    # print(groupedList)

    tempStr = ''
    letterList = []
    counter = 0
    for letter in splitStringList:
        if len(splitStringList) % 2 == 0:
            tempStr += letter
            if len(tempStr) == 2:
                letterList.append(tempStr)
                tempStr = ''
        else:
            tempStr += letter
            if len(tempStr) == 2:
                letterList.append(tempStr)
                tempStr = ''
            if splitStringList[counter] == letter:
                tempStr += letter + '_'
            counter += 1
    print(letterList)


def test_solution():
    assert solution('Alexis') == ['Al', 'ex', 'is']
    assert solution('Jim') == ['Ji', 'm_']
