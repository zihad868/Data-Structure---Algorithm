def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


def verify(index):
    if index is not None:
        print("Target fount at index", index)
    else:
        print("Target not found")


numbers = [1, 8, 12, 15, 20, 25, 100, 200, 250]

result = binary_search(numbers, 100)
verify(result)
