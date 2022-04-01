def recursiveBinarySearch(arr, value, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == value:
        return mid

    elif arr[mid] < value:
        return recursiveBinarySearch(arr, value, mid + 1, end)

    else:
        return recursiveBinarySearch(arr, value, start, mid - 1)


nums = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(recursiveBinarySearch(nums, 4, 0, len(nums)-1))


def iterativeBinarySearch(arr, value, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return mid

        elif arr[mid] < value:
            start = mid + 1

        else:
            end = mid - 1
    return None


print(recursiveBinarySearch(nums, 4, 0, len(nums)-1))
