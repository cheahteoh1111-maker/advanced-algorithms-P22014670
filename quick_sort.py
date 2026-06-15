def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller = []
    greater = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            greater.append(arr[i])

    return quick_sort(smaller) + [pivot] + quick_sort(greater)


numbers = [214, 12, 46, 57, 31, 8]

print("Original List:", numbers)
print("Sorted List:", quick_sort(numbers))