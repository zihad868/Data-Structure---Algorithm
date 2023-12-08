def linear_search(lst, target):
    for i in range(0, len(lst)):
        if lst[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target fount at index", index)
    else:
        print("Target not found")


numbers = [12, 45, 7, 50, 2, 100, 3, 87, 12]

result = linear_search(numbers, 1000)
verify(result)