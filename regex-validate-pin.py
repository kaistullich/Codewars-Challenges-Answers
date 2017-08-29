def validate_pin(pin):
    # check the length of pin
    length = len(pin)
    # validate if only 4 or 6 nums long
    if length == 4 or length == 6:
        # check if only a number
        if pin.isdigit():
            return True
    return False

if __name__ == '__main__':
    validate_pin("1234")
    validate_pin("12345")
    validate_pin("a234")