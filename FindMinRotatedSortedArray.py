def findMin(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        midPoint = left + (right - left) // 2
        if arr[midPoint] > arr[right]:
            left = midPoint + 1

        else:
            right = midPoint

    return left


print(findMin([7, 8, 9, 10, 11,-2, -1, 0, 1, 2, 3, 4, 5, 6]))
