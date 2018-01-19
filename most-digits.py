def find_longest(arr):
    for num in arr:
        temp = num
        print(f'Temp: {temp}')
        print(f'Num: {num}')
        if num > temp:
            print('larger')

def test_find_longest():
    assert find_longest([1, 10, 100]) == 100


if __name__ == '__main__':
    find_longest([1, 10, 100])