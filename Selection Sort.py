def selection_sort(arr):
    for i in range(0, len(arr)-1):
        index_min = i
        for j in range(i+1, len(arr)):
            if arr[index_min] > arr[j]:
                index_min = j

        if index_min != i:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    return arr
sort = selection_sort([10, 5,100, 8, 2])

print(sort)