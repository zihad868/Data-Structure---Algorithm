def binary_search(arr, left, right, taget):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == taget:
            return mid
        elif arr[mid] < taget:
            return binary_search(arr, mid + 1, right, taget)
        else:
            return binary_search(arr, left, right - 1, taget)


numbers = [1, 8, 12, 15, 20, 25, 100, 200, 250]

result = binary_search(numbers, 0, len(numbers) - 1, 100)

print(result)

