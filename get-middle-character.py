def get_middle(s):
    wordLength = len(s)

    if wordLength % 2 == 0:
        print('Its an even word')
    else:
        print('odd length word')

if __name__ == '__main__':
    get_middle('test')