def binary_search(numbers, target):
    """
    Search for a target number in a sorted list using Binary Search.
    If the target is found, return its index.
    If the target is not found, return -1.
    """

    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2

        if numbers[middle] == target:
            return middle
        elif target > numbers[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return -1


def main():
    numbers = [8, 12, 31, 46, 57, 214]
    target = 31

    print("Binary Search")
    print("List:", numbers)
    print("Target:", target)

    result = binary_search(numbers, target)

    if result != -1:
        print("Found at index", result)
    else:
        print("Target not found")


if __name__ == "__main__":
    main()