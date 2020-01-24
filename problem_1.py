import math

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number <= 1:
        return number

    def devide(acc):
        # acc = round(acc)
        # acc = math.floor(number)
        pow2 = math.floor(acc * acc)

        print(number, acc, pow2)
        if pow2 == number:
            return int(acc)
        elif pow2 < number:
            return devide((number + acc) / 2)
        else:
            return devide(acc / 2)

    print(number, " start")
    result = devide(number / 2)
    print(int(result))
    return result


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    assert_equals(0, sqrt(0))
    assert_equals(1, sqrt(1))
    assert_equals(-9, sqrt(-9))

    assert_equals(3, sqrt(9))
    assert_equals(4, sqrt(16))
    assert_equals(5, sqrt(27))