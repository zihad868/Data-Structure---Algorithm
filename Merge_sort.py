def merge_sort(list):
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(l, r):
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    # Checking if any element was left
    result += l[i:]
    result += r[j:]
    return result


sorted_list = merge_sort([45, 15, 80, 45, 100])

print(sorted_list)

