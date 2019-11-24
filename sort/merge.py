def merge_sort(array):
    n = len(array)
    mid = n//2
    if n == 1:
        return array
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0
    while i < len(left):
        if j == len(right) or left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    return array
