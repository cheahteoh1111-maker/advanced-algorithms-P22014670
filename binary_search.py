def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [8, 12, 31, 46, 57, 214]
target = 31

result = binary_search(numbers, target)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")
