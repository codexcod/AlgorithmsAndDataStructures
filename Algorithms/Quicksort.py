
def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1

    return left


def quickSort(arr, left, right):
    if left >= right:
        return

    pivot = arr[(left + right) // 2]

    index = partition(arr, left, right, pivot)
    quickSort(arr, left, index - 1)
    quickSort(arr, index, right)


array = [2, 8, 0, 6, 2, 7]
quickSort(array, 0, len(array) - 1)
print(array)
