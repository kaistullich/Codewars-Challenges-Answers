def namelist(names):
    """
    Given: an array containing hashes of names

    Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

    :param names: list of dict
    :return: string
    """
    if not names:
        return ''
    else:
        counter = 0

        newList = list()

        for name in names:
            if counter != len(names) - 2 and counter != len(names) - 1:
                newList.append(name['name'] + ', ')
                counter += 1
            elif counter == len(names) - 1:
                newList.append(name['name'])
            else:
                newList.append(name['name'] + ' & ')
                counter += 1

        namesString = ''.join(newList)

        return namesString


if __name__ == '__main__':
    namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
    namelist([])
