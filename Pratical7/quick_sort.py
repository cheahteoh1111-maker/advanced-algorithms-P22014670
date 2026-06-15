def quick_sort(numbers):
    """
    Sort a list of numbers using the Quick Sort algorithm.
    Quick Sort also uses the divide and conquer method.
    """

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]

    smaller_numbers = []
    greater_numbers = []

    for number in numbers[:-1]:
        if number <= pivot:
            smaller_numbers.append(number)
        else:
            greater_numbers.append(number)

    return quick_sort(smaller_numbers) + [pivot] + quick_sort(greater_numbers)


def main():
    numbers = [214, 12, 46, 57, 31, 8]

    print("Quick Sort")
    print("Original List:", numbers)

    sorted_numbers = quick_sort(numbers)

    print("Sorted List:", sorted_numbers)


if __name__ == "__main__":
    main()