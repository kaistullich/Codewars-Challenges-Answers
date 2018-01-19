def substring(string, substr):
    string_len = len(string)
    substr_len = len(substr)

    i = 0

    while i < string_len:
        if string[i] == substr[i]:
            print('MATCH: ' + string[i])
            break
        print(i)
        i += 1


if __name__ == '__main__':
    substring('abcd', 'c')