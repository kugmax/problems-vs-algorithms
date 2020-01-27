def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    if not input_list or len(input_list) <= 0:
        return []

    pointer_0 = 0
    pointer_2 = len(input_list) - 1
    i = 0

    while i <= pointer_2:
        v = input_list[i]

        if v == 0:
            input_list[i] = input_list[pointer_0]
            input_list[pointer_0] = 0
            pointer_0 += 1
            i += 1

        elif v == 2:
            input_list[i] = input_list[pointer_2]
            input_list[pointer_2] = 2
            pointer_2 -= 1
        else:
            i += 1

    return input_list


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    assert_equals(
        [],
        sort_012(None)
    )

    assert_equals(
        [],
        sort_012([])
    )

    assert_equals(
        [1],
        sort_012([1])
    )

    assert_equals(
        [0,0,0,0, 1,1],
        sort_012([0, 0, 0, 1, 1, 0])
    )

    assert_equals(
        [1,1, 2,2,2,2],
        sort_012([2, 2, 2, 1, 1, 2])
    )

    assert_equals(
        [0,0,0, 1,1,1, 2,2,2,2,2],
        sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    )

    assert_equals(
        [0,0,0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2],
        sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    )

    assert_equals(
        [0,0,0,0,0,0, 1,1,1,1,1,1, 2,2,2,2,2,2,2],
        sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    )