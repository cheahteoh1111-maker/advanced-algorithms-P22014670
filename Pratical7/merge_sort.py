def merge_sort(numbers):
    """
    Sort a list of numbers using the Merge Sort algorithm.
    Merge Sort uses the divide and conquer method.
    """

    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2

    left_part = numbers[:middle]
    right_part = numbers[middle:]

    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)

    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.
    """

    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def main():
    numbers = [214, 12, 46, 57, 31, 8]

    print("Merge Sort")
    print("Original List:", numbers)

    sorted_numbers = merge_sort(numbers)

    print("Sorted List:", sorted_numbers)


if __name__ == "__main__":
    main()