def recursive_binary_search(arr, target):
    if len(arr) == 0:
        return None
    else:
        mid = len(arr) // 2

        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                return recursive_binary_search(arr[mid + 1:], target)
            else:
                return recursive_binary_search(arr[: mid], target)


numbers = [1, 8, 12, 15, 20, 25, 100, 200, 250]

result = recursive_binary_search(numbers, 100)

print(result)
