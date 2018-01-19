def friend(f):
    """
    Make a program that filters a list of strings and returns a list with only your friends name in it.

    If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!

    Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

    :param f:
    :return:
    """
    lowered = [name.lower() for name in f]
    friends = ['jason', 'alex', 'bob']
    friendList = list()

    for name in lowered:
        if name in friends:
            friendList.append(name)
        elif len(name) == 4:
            friendList.append(name)

    return friendList


if __name__ == '__main__':
    print(friend(['Holdan', 'Bob','Jason', 'bigewh', 'fhre']))
    print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
