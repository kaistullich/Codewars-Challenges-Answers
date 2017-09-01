def subset(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        # variable for if string in other list
        yes = 0
        # variable for if string NOT in other list
        no = 0
        for i in list1:
            if i in list2:
                yes += 1
            else:
                no += 1
        if no > 0:
            return False
        return True


def test_subset():
    list1 = ['alex', 'bob', 'charles', 'david']
    list1_identical_reverse = ['david', 'charles', 'bob', 'alex']
    list2 = ['a', 'b', 'c']
    assert subset(list1, list1_identical_reverse) == True
    assert subset(list1, list2) == False
