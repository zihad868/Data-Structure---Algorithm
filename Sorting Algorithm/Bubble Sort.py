def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sort = bubble_sort([10, 15, 2, 5, 8, 0])
print(sort)
