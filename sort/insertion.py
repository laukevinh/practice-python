def insertion_sort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    return array
