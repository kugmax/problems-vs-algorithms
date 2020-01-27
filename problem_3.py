def sort(input_list):
    if len(input_list) <= 1:
        return input_list

    middle = len(input_list) // 2

    return merge(sort(input_list[:middle]),
                 sort(input_list[middle:]))


def merge(left, right):
    result = []

    i = 0
    j = 0
    for k in range(len(left) + len(right)):
        if i >= len(left):
            result.extend(right[j:])
            break

        if j >= len(right):
            result.extend(left[i:])
            break

        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list or len(input_list) <= 0:
        return None, None

    sorted = sort(input_list)

    result_1 = 0
    result_2 = 0
    is_increment_1 = True
    for v in sorted:
        if is_increment_1:
            result_1 *= 10
            result_1 += v
        else:
            result_2 *= 10
            result_2 += v

        is_increment_1 = not is_increment_1

    return result_1, result_2


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


if __name__ == "__main__":
    assert_equals((None, None), rearrange_digits([]))
    assert_equals((None, None), rearrange_digits(None))

    assert_equals((1, 0), rearrange_digits([1]))
    assert_equals((1, 1), rearrange_digits([1, 1]))
    assert_equals((11, 1), rearrange_digits([1, 1, 1]))
    assert_equals((91, 2), rearrange_digits([1, 2, 9]))
    assert_equals((92, 91), rearrange_digits([1, 2, 9, 9]))
    assert_equals((531, 42), rearrange_digits([1, 2, 3, 4, 5]))
    assert_equals((964, 852), rearrange_digits([4, 6, 2, 5, 9, 8]))
