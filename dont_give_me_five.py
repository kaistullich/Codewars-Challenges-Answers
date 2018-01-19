def dont_give_me_five(start, end):
    """
    Don't give me five!
    In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

    Examples:
        1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
        4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12

    The result may contain fives. ;-)

    The start number will always be smaller than the end number. Both numbers can be also negative!
    """

    total = 0
    for num in range(start, end+1):
        if num == 5:
            print(f'The number was 5 : {num}')
            pass
        else:
            print(f'All numbers except 5 : {num}')
            print(f'the total BEFORE = {total}')
            total += 1
            print(f'the total AFTER = {total}\n')


if __name__ == '__main__':
    dont_give_me_five(1, 9)
    dont_give_me_five(4, 17)
