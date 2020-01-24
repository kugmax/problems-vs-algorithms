def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number == 0 or number == 1:
        return number, 0

    if number < 0:
        return -1, 0

    result = number / 2
    accuracy = 0.0001
    error = 1
    steps = 0

    while error > accuracy:
        steps += 1
        result = (result + number / result) / 2
        error = abs(number - result ** 2)

    return int(result), steps


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    assert_equals((0, 0), sqrt(0))
    assert_equals((1, 0), sqrt(1))
    assert_equals((-1, 0), sqrt(-9))

    assert_equals((1, 3), sqrt(2))
    assert_equals((3, 3), sqrt(9))

    assert_equals((4, 4), sqrt(16))

    assert_equals((5, 5), sqrt(27))
    assert_equals((6, 5), sqrt(36))
    assert_equals((7, 5), sqrt(49))
    assert_equals((8, 5), sqrt(64))

    assert_equals((9, 6), sqrt(81))
    assert_equals((10, 6), sqrt(100))
    assert_equals((11, 6), sqrt(121))
    assert_equals((12, 6), sqrt(144))
    assert_equals((13, 6), sqrt(169))
    assert_equals((14, 6), sqrt(196))
    assert_equals((15, 6), sqrt(225))

    assert_equals((16, 7), sqrt(256))
    assert_equals((16, 7), sqrt(257))