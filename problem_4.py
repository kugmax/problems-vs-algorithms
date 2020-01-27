def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    if not input_list or len(input_list) <= 0:
        return []

    bucket_0 = []
    bucket_1 = []
    bucket_2 = []

    for v in input_list:
        if v == 0:
            bucket_0.append(v)
        elif v == 1:
            bucket_1.append(v)
        else:
            bucket_2.append(v)

    # TODO: this is also traversing!!!
    return bucket_0 + bucket_1 + bucket_2


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
        [0, 0, 0, 0, 1, 1],
        sort_012([0, 0, 0, 1, 1, 0])
    )

    assert_equals(
        [1, 1, 2, 2, 2, 2],
        sort_012([2, 2, 2, 1, 1, 2])
    )

    assert_equals(
        [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2],
        sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    )

    assert_equals(
        [0,0,0,0,0,0,0,0,0,0,0, 1,1,1,1,1,1, 2,2,2,2,2,2,2,2,2],
        sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    )

    assert_equals(
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
        sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    )