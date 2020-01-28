import sys


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints or len(ints) == 0:
        return None, None

    min = sys.maxsize
    max = -sys.maxsize - 1

    for i in ints:
        if i > max:
            max = i

        if i < min:
            min = i

    return min, max


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    assert_equals(
        (None, None),
        get_min_max([])
    )

    assert_equals(
        (None, None),
        get_min_max(None)
    )

    assert_equals(
        (0, 9),
        get_min_max([9, 3, 1, 2, 0, 5, 4, 6, 7, 8])
    )

    assert_equals(
        (-9, 0),
        get_min_max([-9, -3, -1, -2, 0, -5, -4, -6, -7, -8])
    )

    assert_equals(
        (5, 5),
        get_min_max([5, 5, 5, 5, 5])
    )

    assert_equals(
        (0, 0),
        get_min_max([0])
    )



