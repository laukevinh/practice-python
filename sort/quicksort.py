def quick_sort(array):
    """Wrapper for actual quick sort"""
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, low, high):
    """Quick sort uses O(log n) space. To achieve this, pass the entire array.
    Don't use slices because it makes shallow copies.
    """
    if low < high:
        idx = partition(array, low, high)
        quick_sort_helper(array, low, idx - 1)
        quick_sort_helper(array, idx + 1, high)

def partition(array, low, high):
    j = low
    for i in range(low, high):
        if array[i] < array[high]:
            array[i], array[j] = array[j], array[i]
            j += 1
    array[j], array[high] = array[high], array[j]
    return j
