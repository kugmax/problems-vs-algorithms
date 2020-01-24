def is_array_sorted(arr, start, end):
    return arr[start] <= arr[end]


def is_target_in_array(target, arr, start, end):
    return start <= end and arr[start] <= target <= arr[end]


def is_in_left(arr, start, middle, end, target):
    is_left_sorted = is_array_sorted(arr, start, middle-1)

    if is_left_sorted:
        return is_target_in_array(target, arr, start, middle-1)
    else:
        return is_target_in_array(target, arr, middle + 1, end)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not number or not input_list or len(input_list) == 0:
        return -1

    start = 0
    end = len(input_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if input_list[middle] == number:
            return middle

        if is_in_left(input_list, start, middle, end, number):
            end = middle - 1
        else:
            start = middle + 1

    return -1


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    assert_equals(-1, rotated_array_search(None, None))
    assert_equals(-1, rotated_array_search([6], None))
    assert_equals(-1, rotated_array_search([], 6))
    assert_equals(-1, rotated_array_search([7], 6))
    assert_equals(-1, rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))

    assert_equals(4, rotated_array_search([1, 2, 3, 4, 6, 7, 8, 9, 10], 6))

    assert_equals(0, rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
    assert_equals(5, rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
    assert_equals(2, rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
    assert_equals(3, rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))
    assert_equals(5, rotated_array_search([6, 7, 8, 0, 2, 4, 5], 4))
    assert_equals(6, rotated_array_search([6, 7, 8, 0, 2, 4, 5], 5))

    assert_equals(2, rotated_array_search([5, 6, 7], 7))
    assert_equals(1, rotated_array_search([6, 7], 7))
    assert_equals(0, rotated_array_search([7, 6], 7))
    assert_equals(0, rotated_array_search([6], 6))
